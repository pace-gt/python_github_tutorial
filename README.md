#  python_github_tutorial

## Overview

This is a basic github repository to show a Github structure, docstrings, and test codes via pytest.


## Documentation

To be added in the future.


## Installation

This project's environment can be built using `miniforge`.
Alternative software for `miniforge`:
- You use can use `anaconda` or `miniconda`, which use the same `conda` command.
- You use can use `micromamba` or `mamba`,  supplimenting `micromamba` or `mamba` respectively for `conda` when using them.

The  python_github_tutorial package dependencies can be installed via conda, and this package tagged in conda via pip install:

Create and install conda package:

cd "<YOUR_FILE_PATH/python_github_tutorial>"

`cd python_github_tutorial`

Create the environment

`conda env create -f environment.yml`

Activate the environment the environment

`conda activate python_github_tutorial`

Install the developement enviroment

`pip install -e .`

Note: If you update the conda package, you may have to redo the pip install.  Without doing this, it may allow incompatable versions of the dependencies to be installed, etc.:


## Run the example

This is an example of the supplimentary functions in the utils directory (python_github_tutorial/utils) and the main function in the main_functions directory (python_github_tutorial/main_functions).

The example is located here 'examples_to_run/examples.py'. The instructions to run it are provided below:

`cd examples_to_run`

`python examples.py`

## Run the interactive example in Visual Studios Code (VScode)

This is the same example but running it as an interactive job (i.e., like a Jupyter notebook). The example is located here 'examples_to_run/interactive_examples.py'.

When using Visual Studios Code (VScode), the '# %%' above each section makes it a cell, which can be run individually by holding shift and pressing enter.


## Run the test cases (unit tests) using pytest

The python_github_tutorial software tests the installation using [pytest](https://docs.pytest.org/en/stable/).
The unit tests via ``pytest`` ensure that the code is build properly, running correctly and producing
accurate results.

To perform these tests (unit tests) for the python_github_tutorial package, please run the following commands
from the ``python_github_tutorial/tests`` directory:

Run all the tests:

`cd python_github_tutorial/tests`

`pytest -v`

Run individual test on 'test_math.py':

`cd python_github_tutorial/tests`

`pytest test_math.py`

Run individual test on 'test_main_functions.py':

`cd python_github_tutorial/tests`

`pytest test_main_functions.py`

## Build the documentation (docs)

Building these HTML files locally via sphinx, which will allow you to access them with your
local internet browsing application or HTML viewer (chrome, safari, VScode, etc.).
The HTML files will be located in the ``docs/_build/html`` directory after they are built.

The python_github_tutorial utilizes [sphinx](https://www.sphinx-doc.org/en/master/index.html) to construct the documentation.
The user can build the documentation locally by executing the following command from the ``docs`` directory:

`conda activate python_github_tutorial`

`cd python_github_tutorial/docs`

`make html`

You can find the docs `html` build here -> `docs/_build/html`.  When in the `docs/_build/html` directory, click on any `html` file and it will open the full docs.
