# Execute notebooks online

Please only execute the notebooks online on servers during the hands-on live tutorial if you are unable to manage a local installation. The MyBinder servers have limited resources, and the Google Colab servers offer limited execution time (approximately 2 hours).


## Google Colab

Google Colab by Google offers more computer resources available for the online execution of notebooks in the background compared to Binder. A major advantage is that both CPU and powerful GPUs are available, depending on the resources available on the Colab servers. However, the runtime is limited to approximately 2 hours, and at the beginning of the runtime, packages need to be installed (which happens automatically when executing the first cell, but it takes some time). Additionally, a Google account is required.

To execute the Jupyter Notebooks needed in the tutorial, please follow these steps:

To open a Notebook with Google Colab, please click one of the Google Colab badges in the table at the top of this page (and sign in with your Google account if you haven't already).

Select `Runtime` -> `Change runtime type` and choose `T4 GPU`. This will attempt to execute the tutorial on the GPU. It may happen that later on, you receive a message that the GPU is not available. In this case, in the free version, which is completely sufficient for the hands-on tutorial, the execution will be done only on the CPU, although execution on the GPU is much faster (the notebooks have been designed so that execution on the CPU should also work). Now, when you execute the first cell, the runtime begins (which can last approximately 2 hours). It is strongly recommended that you execute this cell at the beginning or just before starting the hands-on tutorial, as it installs important packages (for the execution of a cell: when a cell is selected, press shift+enter or click the run button (play button symbol)). The installation takes some time, and after that, you need to restart the runtime (which is also indicated to you). After restarting the tutorial, you must execute the first cell again. Then, you can also execute the other cells.

You need to perform each step for each Jupyter Notebook shortly before the start of the hands-on tutorial (recommended) or just before we switch to a new notebook. If you have multiple Google Colab notebooks open, you can close the ones you no longer need by selecting `Runtime` -> `Disconnect and delete runtime`. This is important because the number of concurrently running notebooks is limited.

If you have access to the `T4 GPU`, you can execute the second part of `Training_tutorial.ipynb`, where a large U-Net is trained on a large dataset. For this, a large GPU is required, and the `T4 GPU` is perfectly suitable for this task. 

# Binder

You can open this repository online using the BinderHub from `mybinder.org`, view the notebooks, and execute them. At` mybinder.org`, only execution on CPU is possible. It may take a while for the repository to load and become executable after clicking on the corresponding link for this repository. `Prediction_tutorial.ipynb` will open automatically. You can also open the `Training_tutorial.ipynb` notebook in MyBinder (button on the left sidebar) without completely reopening the repository in MyBinder. If there is too much traffic on MyBinder, execution may not be possible. The `Prediction_tutorial.ipynb` notebook, which demonstrates the prediction of Skyrmion U-Nets and allows for prediction on own Kerr images, works. In the `Training_tutorial.ipynb` notebook, cells can be executed, but training itself does not work because the resources provided by `mybinder.org` are insufficient for that purpose.

To open a notebook on `mybinder.org`, please click one of the Binder badges in the table at the top of this page.
