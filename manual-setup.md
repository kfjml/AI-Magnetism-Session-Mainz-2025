# Manual setup

Create a new environment with Python 3.11 and assign it a new environment name, for example, `skyrmion_unet`

```
conda create --name skyrmion_unet python=3.11
```

If the following installations does not work, one could attempt to install an environment with a different version number, e.g., changing `python=3.11` to `python=3.10`.

Activate this enviorment with the same name, in this case `skyrmion_unet`

```
conda activate skyrmion_unet
```

## Installing pip packages

First, you need to install `pip`. To do this, execute:

```
conda install pip
```

It's possible that `pip` is already installed for the environment, in which case you will receive a message confirming this.

Depending on which version you want to run the Skyrmion U-Net on the CPU or GPU of your machine where you're installing it, execute **only one** of the following commands. In case the installation fails, remove the double equal sign with the version number after the package name, e.g., `tensorflow>=2.18.0,<3` -> `tensorflow-cpu`. If issues persist, it is advisable to first remove only the version number from the package `tensorflow` or `tensorflow[and-cuda]`, and only proceed to remove other package version numbers if this does not work.

## Normal setup

Install the following pip packages, when you want to run the standard environment:

```
pip install notebook>=7.3.2,<8 numba>=0.61.0,<0.62 tensorflow>=2.16.2,<3 albumentations>=2.0.4,<3 matplotlib>=3.10.0,<4 pandas>=2.2.3,<3 chardet>=5.2.0,<6 ipympl>=0.9.6,<0.10 ipywidgets>=8.1.5,<9 opencv-python-headless>=4.11.0.86,<5 wget>=3.2,<4 pyyaml>=6.0.2,<7 pillow>=11.1.0,<12
```

## GPU with CUDA

Instead, if you want to run TensorFlow on the GPU and also install the necessary CUDA packages, use:

```
pip install notebook>=7.3.2,<8 numba>=0.61.0,<0.62 tensorflow[and-cuda]>=2.18.0,<3 albumentations>=2.0.4,<3 matplotlib>=3.10.0,<4 pandas>=2.2.3,<3 chardet>=5.2.0,<6 ipympl>=0.9.6,<0.10 ipywidgets>=8.1.5,<9 opencv-python-headless>=4.11.0.86,<5 wget>=3.2,<4 pyyaml>=6.0.2,<7 pillow>=11.1.0,<12
```
