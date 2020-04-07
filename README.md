# An open source crash course on parameter estimation of computational models using a Bayesian optimization approach

This repository contains an educational Jupyter notebook to learn how to construct inverse problems in computational engineering. The ready-to-use code of this educational material is maintained in [another GitHub repository](https://github.com/mbarzegary/BayesianFEM).

## Installation

This material is developed in Python 3.7 and depends on a couple of packages to work. The common first step in this sort of scenarios is creating a python virtual environment and activating it. This can be done in a wide range of methods using `venv`, `conda`, and `pipenv`. A simple approach with proper description for different platforms can be found [here](https://docs.python.org/3/tutorial/venv.html).

After activating the virtual environment, you should install iPython and Jupyter (if it is not previously installed by Anaconda or similar distributions). You can folllow the steps described [here](https://anbasile.github.io/posts/2017-06-25-jupyter-venv/) to do so. Then, you clone the repository and install the required packages:

`$ git clone https://github.com/mbarzegary/educational-bayesian.git`

`$ pip install -r requirements.txt`

After this, you can run Jupyter notebooks (by running `$ jupyter notebooks`) and navigate to HowToConstructInverseProblems.ipynb.
