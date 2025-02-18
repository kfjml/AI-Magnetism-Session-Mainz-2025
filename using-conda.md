# Using anaconda to install the packages for the repository
## 1 Install & start miniconda

Miniconda is a lightweight Python distribution that includes package management `conda`, simplifying the installation of Python packages. Install the newest version of Miniconda if you don't have it already (if you have Anaconda, you can also use that). Details can be found at:

[https://docs.anaconda.com/free/miniconda/](https://docs.anaconda.com/free/miniconda/)

[https://docs.anaconda.com/free/miniconda/miniconda-install/](https://docs.anaconda.com/free/miniconda/miniconda-install/)

Afterward, please start miniconda (or anaconda) from the command line (start miniconda/anaconda prompt on windows) and navigate to the directory of this repository (where the README.md is located).

## 2 Setup of the skyrmion U-Net environment 

For the hands-on tutorial, the standard environment (which may already support the GPU depending on the existing installation, but definitely works on the CPU) is completely sufficient. However, for higher performance and training larger Skyrmion U-Nets, it is recommended to install the GPU version. You can install both the CPU and GPU environments independently. First, the installation of the standard environment is explained. Below that, an environment is provided where the GPU should work.

## 2.1 Installation of the standard environment 

When you want to run the standard environment of the Skyrmion U-Net, execute the following command to create a conda environment `skyrmion_unet` with all necessary packages:

```
conda env create -f environment.yml
```

`environment.yml` is a YAML file where the environment, along with its packages and the specific versions recommended for use, is defined.

In the case that this installation **does not** work and returns an error (which may occur, for example, with Mac M1/M2 processors), please try the following command (**do not** execute if the previous environment installation succeeded):

```
conda env create -f conda_environment/environment_v2.yml
```

`environment_cpu_v2.yml` is also a YAML file, but in this case, the TensorFlow package version is not specified. It will automatically search for a suitable package version. It's possible that during the previous installation attempt, the `skyrmion_unet` environment was already created. In this case, before this new installation can proceed successfully, the environment must be deleted. This process is explained at the bottom of this page. If this second installation also **does not** work, try the following command (**do not** execute if either of the previous environment installation commands succeeded):

```
conda env create -f conda_environment/environment_v3.yml
```

`environment_cpu_v3.yml` is also a YAML file, but none of the various Python packages have a specified version. Suitable versions of the packages for the device will be automatically searched. Here, it might also be necessary to delete the environment again before this command works-

## 2.2 Installation of the GPU environment 

### Preliminary remarks for the GPU installation

If you intend to run the Skyrmion U-Net on a GPU, you need to install the NVIDIA GPU driver, the CUDA Toolkit, and the cuDNN SDK.  If you want to run the Skyrmion U-Net on a GPU and install the necessary CUDA packages, execute the following commands.  

For more information, please refer to [TensorFlow installation guide](https://www.tensorflow.org/install/pip), as the Skyrmion U-Net is based on TensorFlow.

### Installation of the GPU environment 

When you want to run the skyrmion U-Net on the GPU, run the following command which will create a conda environment `skyrmion_unet_gpu` for the GPU usage with all necessary packages

```
conda env create -f conda_environment/environment_gpu.yml
```

`environment_gpu.yml` is a YAML file where the environment, along with its packages and the specific versions recommended for use, is defined.

In the case that this installation **does not** work and returns an error (which may occur, for example, with Mac M1/M2 processors), please try the following command (**do not** execute if the previous environment installation succeeded):

```
conda env create -f conda_environment/environment_gpu_v2.yml
```

`environment_gpu_v2.yml` is also a YAML file, but in this case, the TensorFlow package version is not specified. It will automatically search for a suitable package version. It's possible that during the previous installation attempt, the `skyrmion_unet_gpu` environment was already created. In this case, before this new installation can proceed successfully, the environment must be deleted. This process is explained in Section 5. If this second installation also **does not** work, try the following command (**do not** execute if either of the previous environment installation commands succeeded):

```
conda env create -f conda_environment/environment_gpu_v3.yml
```

`environment_gpu_v3.yml` is also a YAML file, but none of the various Python packages have a specified version. Suitable versions of the packages for the device will be automatically searched. Here, it might also be necessary to delete the environment again before this command works, for details see Section 5.

## 3 Using the skyrmion U-Net

To activate the environment, you use the environment name of the environment  you installed. You activate the environment using the following command and the associated environment name, in the following command `skyrmion_unet`:

```
conda activate skyrmion_unet
```

Afterwards start a jupyter notebook with

```
jupyter notebook
```

This command will provide you with a localhost address, which you can then open in your web browser to access the Jupyter Notebook. Then you can try out the Jupyter notebooks for prediction (`Prediction_tutorial.ipynb`) and training (`Training_tutorial.ipynb`) in the main folder of the repository, and also create your own notebooks with own code for the Skyrmion U-Net. 

In these notebooks, please execute the cells sequentially from top to bottom (execution of a cell: when a cell is selected, press shift+enter or click the run button (play button symbol)). In the prediction notebook, you can interactively modify the outputs using the displayed GUI. If you want to change these cells with a GUI again after executing other cells, please execute these cells again.

The prediction notebook (`Prediction_tutorial.ipynb`) is designed to work completely with execution on a regular CPU. In the training notebook (`Training_tutorial.ipynb`), you can also execute on the CPU in the first part; it is designed to train a small U-Net, which can also be trained on the CPU. For the second part, a large U-Net is trained on a large dataset. A GPU is recommended for this, but the focus of the hands-on tutorial does absolutely not lie on this second part of the training notebook.

## 4 Deleting installed environments

If you no longer want to have the installed Skyrmion U-Net environments after the Hands-On tutorial, or if there were any issues during the installation process and you want to remove the environment to install the environment with the same name (the standard name `skyrmion_unet` is used for the standard environment, and `skyrmion_unet_gpu` is used for the GPU environment, in the YAML files) again with another YAML file, execute the following command along with the associated environment name, which is in the following command `skyrmion_unet`:

```
conda remove -n skyrmion_unet --all
```

During deletion, you will be prompted to confirm the removal of certain files and folders. Please press `y` here.