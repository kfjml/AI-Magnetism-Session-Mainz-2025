# Skyrmion U-Net workshop repository

| Description | Jupyter Notebook | Binder | Google Colab |
|---|---|---|---|
| Tutorial Prediction | Prediction_tutorial.ipynb | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/kfjml/AI-Magnetism-Session-Mainz-2025/HEAD?labpath=Prediction_tutorial.ipynb) |  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kfjml/AI-Magnetism-Session-Mainz-2025/blob/main/Prediction_tutorial.ipynb) | 
| Tutorial Training | Training_tutorial.ipynb | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/kfjml/AI-Magnetism-Session-Mainz-2025/HEAD?labpath=Training_tutorial.ipynb) |  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kfjml/AI-Magnetism-Session-Mainz-2025/blob/main/Training_tutorial.ipynb) | 
| Tutorial MDAI | MDAI_tutorial.ipynb | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/kfjml/AI-Magnetism-Session-Mainz-2025/HEAD?labpath=MDAI_tutorial.ipynb) |  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kfjml/AI-Magnetism-Session-Mainz-2025/blob/main/MDAI_tutorial.ipynb) | 
| Editor GUI  | Editor.ipynb | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/kfjml/AI-Magnetism-Session-Mainz-2025/HEAD?labpath=Editor.ipynb) |  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kfjml/AI-Magnetism-Session-Mainz-2025/blob/main/Editor.ipynb) | 

This repository is intended to help users get started with the Skyrmion U-Net through tutorials and to facilitate its use. For any questions regarding this repository, please contact Kilian Leutner at kileutne@students.uni-mainz.de.

## Getting Started on Your Own Device

If you have not yet downloaded this repository, you can do so in two ways. If you have `git` installed on your device, you can use the command:

```
git clone https://github.com/kfjml/AI-Magnetism-Session-Mainz-2025
```

If you do not have `git`, go to the main page of the GitHub repository, click the green `Code` button at the top of the page, and then select `Download ZIP`. After downloading, unzip the archive and open a command line. Navigate to the unzipped folder.

To run the project, we will install `pixi`, which is highly recommended because it ensures compatibility across multiple platforms. However, if you prefer to set up the environment and necessary packages using Anaconda, you can follow [these instructions](./using-conda.md). To install `pixi`, follow the instructions on [https://pixi.sh/latest/](https://pixi.sh/latest/). It is easy to install on Windows, Linux, and macOS via the command line. Once installed, open the command line (if it is not already open) and navigate to the downloaded repository folder (`AI-Magnetism-Session-Mainz-2025`). To install the default environment, which may already support the GPU depending on your system but will definitely work on the CPU, run:

```
pixi install
```

This installation process only affects the repository folder, and all required packages will be stored in a subfolder named `./pixi/`. After installation, start Jupyter Notebook by running:

```
pixi run jupyter notebook
```

This command will start Jupyter Notebook and output a localhost address, which you can open in your web browser to access Jupyter Notebook. Depending on your platform, the notebook may open automatically.

If you want to ensure that the environment runs on the GPU (if your device has a GPU), additional CUDA/cuDNN libraries will be installed by running:

```
pixi install --manifest-path gpu_pixi_environment/pixi.toml
```

## Getting Started in Online Notebooks

If you want to run the Jupyter Notebooks online, click on the badge of the respective Jupyter Notebook in the table at the top of the page to open it in **Google Colab** (this is the recommended option) or **MyBinder**. Please only use these online services during the hands-on live tutorial if you are unable to set up a local installation. This is because **MyBinder** has limited resources, and **Google Colab** allows you to run notebooks for only about 2 hours before disconnecting. For more details, check [here](./online-notebooks.md).

## Manual installation

For a manual installation in anaconda, see: [Manual setup](./manual-setup.md).

## Acknowledgements

The dataset included in this repository is extracted from the Zenodo repository (v2.0) by Winkler et al.: https://doi.org/10.5281/zenodo.10997175. The authors of this repository, which also includes the authors of the Zenodo repository, are Kilian Leutner, Thomas Brian Winkler, Isaac Labrie-Boulay, Alena Romanova, Hans Fangohr, Mathias Kläui, Raphael Gruber, Fabian Kammerbauer, Klaus Raab, Jakub Zazvorka, Elizabeth Martin Jefremovas, and Robert Frömter.
