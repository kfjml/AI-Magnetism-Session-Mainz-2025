import numpy as np
import pandas as pd
import wget
import zipfile
import os
import yaml

class MetaDataFile:
    allowed_attributes = ["filename","filetype"]
    def __init__(self,dictype):
        for ele in dictype:
            if ele in self.allowed_attributes or ele=="repository":
                setattr(self,ele,dictype[ele])
            
    def __repr__(self):
        return "Metadata("+",".join([ele+f"={getattr(self,ele)!r}" for ele in self.allowed_attributes if hasattr(self,ele)])+",repository_id="+self.repository.id+")"

    def __str__(self):
        return "Metadata("+",".join([ele+f"={getattr(self,ele)}" for ele in self.allowed_attributes if hasattr(self,ele)])+",repository_id="+self.repository.id+")"

class MetaData:
    allowed_attributes = ["key","type","column_name","legend"]
    def __init__(self,dictype):
        for ele in dictype:
            if ele in self.allowed_attributes or ele=="repository":
                setattr(self,ele,dictype[ele])
        self.metadatalist = None
            
    def __repr__(self):
        return "MetaData("+",".join([ele+f"={getattr(self,ele)!r}" for ele in self.allowed_attributes if hasattr(self,ele)])+",metadatalist=len("+f"{len(self.metadatalist)}),repository_id="+self.repository.id+")"

    def __str__(self):
        return "MetaData("+",".join([ele+f"={getattr(self,ele)}" for ele in self.allowed_attributes if hasattr(self,ele)])+",metadatalist=len("+f"{len(self.metadatalist)}),repository_id="+self.repository.id+")"
        
class Repository:
    allowed_attributes = ['id','name', 'source', 'description','data_table', 'measurement_method', 'measurement_method_class', 'date', 'version', 'tags', 'additional_metadata','data_url'] 
    def __init__(self,kwargs,repo_dir,metadata_dir):
        for key,value in kwargs.items():
            if key in self.allowed_attributes and key not in ["data_table","metadata_files"]:
                setattr(self,key,value)  

        self.repo_internal_name = "repo_id_"+self.id
        self.repo_dir = os.path.join(repo_dir,self.repo_internal_name)
        self.metadata_dir = metadata_dir
        if not os.path.exists(self.repo_dir):
            os.makedirs(self.repo_dir)
        
        if "data_table" in kwargs:
            self.data_table_fn = os.path.join(metadata_dir,kwargs["data_table"]["data_table"]) 
            self.delimiter = kwargs["data_table"].get("delimiter",",")
            keyl = [v["key"] for k,v in kwargs["data_table"]["columns"].items()]
            if len(keyl) != len(set(keyl)):
                raise InputError("Key's not unique")

            self.dataset = {v["key"]:MetaData({**v,"column_name":k,"repository":self}) for k,v in kwargs["data_table"]["columns"].items()}

            df = pd.read_csv(self.data_table_fn,delimiter=self.delimiter)
            for key,data in self.dataset.items():
                if data.type == "filename":
                    data.metadatalist = [os.path.join(self.repo_dir,ele) for ele in df[data.column_name].to_list()]
                elif data.type == "integer":
                    data.metadatalist = df[data.column_name].to_numpy().astype(np.int64)
                elif data.type == "float":
                    data.metadatalist = df[data.column_name].to_numpy().astype(np.float64)
                elif data.type == "string":
                    data.metadatalist = df[data.column_name].to_list()
                else:
                    data.metadatalist = df[data.column_name].to_list()

        if "additional_metadata" in kwargs:
            self.additional_metadata = [MetaDataFile({**v,"filename":k,"repository":self}) for k,v in kwargs["additional_metadata"].items()]
            
    def download(self):
        #f not os.path.exists(zenodo_folder):
        zipfn =  os.path.join(self.repo_dir,self.repo_internal_name+".zip")
        if not os.path.isfile(zipfn):
            wget.download(self.data_url,zipfn)
            
        with zipfile.ZipFile(zipfn,"r") as zip:
            if not all(os.path.exists(os.path.join(self.repo_dir,f)) for f in zip.namelist()):
                zip.extractall(self.repo_dir)                
            
    def __repr__(self):
        lab = [ele for ele in self.allowed_attributes if ele!="data_url"]+["data_table_fn","dataset","data_url"]  
        
        return "Repository("+",".join([key+f"={(getattr(self,key))!r}" for key in lab if hasattr(self,key)])+")"
    
    def __str__(self):
        lab = [ele for ele in self.allowed_attributes if ele!="data_url"]+["data_table_fn","dataset","data_url"]
        return "Repository("+",".join([key+f"={(getattr(self,key))}" for key in lab if hasattr(self,key)])+")"

class Repositories:
    @classmethod
    def import_from_yaml(cls,fnrepos,download_dir):
        with open(fnrepos,"r") as f:
            repo_dict = yaml.safe_load(f)
        json_repos = repo_dict["repositories"]
        return cls([Repository(repo,download_dir,os.path.dirname(fnrepos)) for i,repo in enumerate(json_repos)])
    
    def __init__(self,repository_list):
        self.repository_list = repository_list

    def filter_repositories(self,measurement_method=None,tags=None,measurement_method_class=None):
        return Repositories([ele for ele in self.repository_list if ((tags is None) or (len(set(ele.tags)&set(tags))>=1)) and ((measurement_method is None) or (measurement_method==ele.measurement_method)) and ((measurement_method_class is None) or (measurement_method_class==ele.measurement_method_class))])
        
    def download(self):
        for repo in self.repository_list:
            repo.download()

    def get_datasets_raw(self):
        return [ele.dataset for ele in self.repository_list]

    def get_datasets(self,l1):
        if len(l1)>0:
            dataset = {k:[ele.dataset[k] for ele in self.repository_list] for k in l1}
            datatable = {"repository_id": [int(ele.repository.id) for ele in dataset[l1[0]] for ele1 in ele.metadatalist]}
            for key in dataset:
                if len(dataset[key])>0:
                    datatable[dataset[key][0].key] = [ele1 for ele in dataset[key] for ele1 in ele.metadatalist]
            datatable = pd.DataFrame(datatable)
            return dataset,datatable
        return None

    def get_additional_metadatas(self):
        return [ele.additional_metadata for ele in self.repository_list]
        
    def __repr__(self):
        return f"Repositories({self.repository_list!r})"

    def __str__(self):
        return f"Repositories("+"; ".join([str(ele) for ele in self.repository_list])+")"

    def __len__(self):
        return len(self.repository_list)

    def __getitem__(self,ix):
        return self.repository_list[ix]