============
Installation
============

Install an editable version from the source (GitHub)
----------------------------------------------------

This project's environment can be built using ``miniforge``.
Alternative software for ``miniforge``:
- You use can use ``anaconda`` or ``miniconda``, which use the same ``conda`` command.
- You use can use ``micromamba`` or ``mamba``,  supplimenting ``micromamba`` or ``mamba`` respectively for ``conda`` when using them.

The  python_github_tutorial package dependencies can be installed via conda, and this package tagged in conda via pip install:

To perform the python_github_tutorial package build, please run the following commands
from the ``<YOUR_FILE_PATH>/python_github_tutorial`` directory.

::

    $ cd python_github_tutorial

    $ conda env create -f environment.yml

    $ conda activate python_github_tutorial

    $ pip install -e .


.. note::
    
    If you update the conda package, you may have to redo the pip install.  Without doing this, it may allow incompatable versions of the dependencies to be installed, etc.:


Run the Example
---------------

This is an example of the supplimentary functions in the utils directory (``<YOUR_FILE_PATH>/python_github_tutorial/python_github_tutorial/utils``) and the main function in the main_functions directory (``<YOUR_FILE_PATH>/python_github_tutorial/python_github_tutorial/main_functions``).
The example (``examples.py``) is located here ``<YOUR_FILE_PATH>/python_github_tutorial/examples_to_run``. The instructions to run it are provided below:

::
    
    $ cd examples_to_run

    $ python examples.py

Run the Interactive Example in Visual Studios Code (VScode)
-----------------------------------------------------------

This interactive example (``interactive_examples.py``) is located here ``<YOUR_FILE_PATH>/python_github_tutorial/examples_to_run``.

This is the same example but running it as an interactive job (i.e., like a Jupyter notebook). The example is located here 'examples_to_run/interactive_examples.py'.

When using Visual Studios Code (VScode), the '# %%' above each section makes it a cell, which can be run individually by holding shift and pressing enter.


Building the HTML documenation files (GitHub)
---------------------------------------------

Building these HTML files locally via sphinx, which will allow you to access them with your
local internet browsing application or HTML viewer (chrome, safari, VScode, etc.).

The python_github_tutorial utilizes `sphinx <https://www.sphinx-doc.org/en/master/index.html>`_ to construct the documentation. 

The user can build the documentation locally by executing the following command from the ``docs`` directory. 
To perform the documents (docs) build for the python_github_tutorial package, please run the following commands from the ``<YOUR_FILE_PATH>/python_github_tutorial/docs`` directory:

::
    
    $ conda activate python_github_tutorial
    
    $ cd docs

    $ make html


After the files are built, the HTML files will be located in the ``<YOUR_FILE_PATH>/python_github_tutorial/docs/_build/html`` directory after they are built.

You can find the docs `html` build here -> `docs/_build/html`.  When in the `docs/_build/html` directory, click on any `html` file and it will open the full docs.


Testing the software installation
----------------------------------

The python_github_tutorial software tests the installation using `pytest <https://docs.pytest.org/en/stable/>`_. 
The unit tests via ``pytest`` ensure that the code is build properly, running correctly and producing 
accurate results.  

To perform these tests (unit tests) for the python_github_tutorial package, please run the following commands
from the ``<YOUR_FILE_PATH>/python_github_tutorial/python_github_tutorial/tests`` directory:


Run all the tests:

::

    $ cd python_github_tutorial/tests

    $ pytest -v


Run individual test on 'test_math.py':

::

    $ cd python_github_tutorial/tests

    $ pytest test_math.py


Run individual test on 'test_main_functions.py':

::

    $ cd python_github_tutorial/tests

    $ pytest test_main_functions.py

Run individual test on 'test_docs_build.py':

::

    $ cd python_github_tutorial/tests

    $ pytest test_docs_build.py
