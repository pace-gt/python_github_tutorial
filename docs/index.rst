Python GitHub Tutorial
======================

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: http://opensource.org/licenses/MIT

This ``python_github_tutorial`` repository is an example of how to design
and structure a GitHub repository, 
and an example of how to structure and document Python code

This Github tutorial shows the following:

* Code structure in a GitHub repository.
* Setup and building GitHub documentation.
* Basic structure and docstrings for Python functions and classes.


Code structure in a GitHub repository
-------------------------------------

The Github repository is structured in a way that separates the main functions (``main_functions``),
helper functions (``utils``), and unit tests (``tests``) directories.  
In this case, the main directory is named ``main_functions``, but it can be named ``src`` 
or whatever the main function does. 
There can also be other directories as needed.  

This `medium article <https://medium.com/code-factory-berlin/github-repository-structure-best-practices-248e6effc405>`_ 
covers some of the other GitHub repository structuring best practices.


Setup and building GitHub documentation
---------------------------------------

This Github repository shows a simple example of how GitHub documentation is created via sphinx. 
This documentation can also be build locally via `sphinx <https://www.sphinx-doc.org/en/master/>`_  and the ``make html`` command in the ``docs`` 
directory, which builds the html files locally that can be viewed in your local 
This documentation can be build via `readthedocs <https://about.readthedocs.com/?ref=dotorg-homepage>`_ 
for everyone to find on the internet using the same files and structure. 
internet browsing application or html viewer (chrome, safari, VScode, etc.).


Basic structure and docstrings for Python functions and classes
---------------------------------------------------------------

This Github repository demonstrates how to write object-oriented Python code using classes and functions. 
In addition to the code structure itself, it is also an example of how to write Python docstrings. 
Python docstrings are the documentation for the classes and functions, which describe the 
input variables, attributes, methods, and outputs/output variables.


.. toctree::
	:caption: Overview
    	:maxdepth: 2
    
	overview/general_info

.. toctree::
	:caption: Getting Started
    	:maxdepth: 2
    
	getting_started/installation/installation
	getting_started/quick_start/quick_start_toc

.. toctree::
	:caption: Topic Guides
    	:maxdepth: 2

	topic_guides/data_structures
	topic_guides/specific_topic_guides

.. toctree::
	:caption: Reference
    	:maxdepth: 2

	reference/units
	reference/citing_python_github_tutorial


