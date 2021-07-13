# An open source crash course on parameter estimation of computational models using a Bayesian optimization approach

[![DOI](https://jose.theoj.org/papers/10.21105/jose.00089/status.svg)](https://doi.org/10.21105/jose.00089)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mbarzegary/educational-bayesian/HEAD)

This repository contains an educational Jupyter notebook to learn how to construct inverse problems in computational engineering. The ready-to-use code of this educational material is maintained in [another GitHub repository](https://github.com/mbarzegary/BayesianFEM).

## Publication

This material is used to publish a module in the Journal of Open Source Education. You can access the paper [here](https://doi.org/10.21105/jose.00089). The full citation data, in case you want to refer to it, is:

    @article{Barzegari2021,
    doi = {10.21105/jose.00089},
    url = {https://doi.org/10.21105/jose.00089},
    year = {2021},
    publisher = {The Open Journal},
    volume = {4},
    number = {40},
    pages = {89},
    author = {Mojtaba Barzegari and Liesbet Geris},
    title = {An open source crash course on parameter estimation of computational models using a Bayesian optimization approach},
    journal = {Journal of Open Source Education}
    }


## Installation

This material is developed in Python 3.7 and depends on a couple of packages to work. The easiest way to use the material is by clicking on the Binder badge above to run an interactive online session.

Alternatively, if you prefer to have a local version, you can install the prerequisites in your system and launch the notebook locally. The common first step in this sort of scenarios is creating a python virtual environment and activating it. This can be done in a wide range of methods using `venv`, `conda`, and `pipenv`. A simple approach with proper description for different platforms can be found [here](https://docs.python.org/3/tutorial/venv.html).

After activating the virtual environment, you should install iPython and Jupyter (if it is not already installed by Anaconda or similar distributions). You can follow the steps described [here](https://anbasile.github.io/posts/2017-06-25-jupyter-venv/) to do so. Then, you clone the repository and install the required packages:

`$ git clone https://github.com/mbarzegary/educational-bayesian.git`

`$ pip install -r requirements.txt`

After this, you can run Jupyter notebooks by running `$ jupyter notebooks`.

## Getting started

The learning material is provided as a single Jupyter notebook, in which all the steps of constructing an inverse problem is described in detail with accompanying Python codes. A very simple simulation code (in the context of an interpolation problem) is also provided and can be found in the repository. The code inside the notebook calls this external program at certain points to mimic the interaction of the parameter estimation routine and the main computational code that contains the unknown parameters.

After setting up the Jupyter notebook and installing the required packages, the user can navigate to the `src` folder and run the `CrashCourseOnParameterEstimation.ipynb` notebook. No further action is needed as the content of the notebook is self-explanatory and easy-to-follow.
