import os,sys,inspect,subprocess

from python_github_tutorial.tests.base_test import BaseTest

# set the directiories and required packages
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
grandparentdir = os.path.dirname(parentdir)
greatgrandparentdir = os.path.dirname(grandparentdir)
sys.path.insert(0,str(currentdir))
sys.path.insert(0,str(parentdir))
sys.path.insert(0,str(grandparentdir ))
sys.path.insert(0,str(greatgrandparentdir))

def find_directory(find_directory_name):
    """Find a directory full path by looking at the current directory and, a few directories backwards.

    This function finds a directory's full path looking at the current, parent, 
    grandparent, and greatgrandparent directories. 

    Parameters
    ----------
    find_directory_name: str
        The directory name that you want find the full path of.
    
    Returns
    -------
    full_directory_path: str
        The full path of the directory name you want to find (i.e., 'find_directory_name')
    """
    if not isinstance(find_directory_name, str):
        TypeError(f"ERROR: The 'find_directory_name' is a {type(find_directory_name)}, not a str.")

    if os.path.isdir(f"{currentdir}/{find_directory_name}") is True:
        full_directory_path = f"{currentdir}/{find_directory_name}"
    elif os.path.isdir(f"{parentdir}/{find_directory_name}") is True:
        full_directory_path = f"{parentdir}/{find_directory_name}"
    elif os.path.isdir(f"{grandparentdir}/{find_directory_name}") is True:
        full_directory_path = f"{grandparentdir}/{find_directory_name}"
    elif os.path.isdir(f"{greatgrandparentdir}/{find_directory_name}") is True:
        full_directory_path = f"{greatgrandparentdir}/{find_directory_name}"
    else:
        IndexError("ERROR: The 'docs' directory location not found.")

    return full_directory_path

class TestDocsBuild(BaseTest):

    # ******************************************
    # BUILD THE DOCS (START)
    # ******************************************

    # find the 'doc' directories relative path (needed for running pytest in various locations)
    search_for_directory = "docs"
    full_dir_path = find_directory(search_for_directory)
    
    build_docs_pipe = subprocess.Popen(
            f"cd {full_dir_path} && make html",
            shell=True, 
        )

    # check errors and wait
    build_docs_pipe.communicate()    

    # this is needed to capture any errors, as the subprocess alone will not.
    print(f"test_file.returncode = {build_docs_pipe.returncode}")
    if build_docs_pipe.returncode == 0:
        docs_build_passed_bool = True
    else:
        print("Test failed")
        docs_build_passed_bool = False

    print("***********************************")
    assert docs_build_passed_bool is True

    # ******************************************
    # BUILD THE DOCS (END)
    # ******************************************

    # ******************************************
    # Test the HTML file are built (START)
    # ******************************************

    def test_doc_search_html_built(self):
        # find the 'doc' directories relative path (needed for running pytest in various locations)
        search_for_directory = "docs"
        full_dir_path = find_directory(search_for_directory)
        
        build_docs_pipe = subprocess.Popen(
            f"cd {full_dir_path} && make html",
            shell=True, 
        )

        # add the 'docs' subfolder location and the filname 
        doc_sub_directory = "_build/html" 
        doc_filename = "search.html"

        doc_file_path = f"{full_dir_path}/{doc_sub_directory}"
        is_dir_bool = os.path.isdir(doc_file_path)
        is_file_bool = os.path.isfile(f"{doc_file_path}/{doc_filename}")

        assert is_dir_bool is True
        assert is_file_bool is True

    
    def test_doc_search_html_built(self):
        # find the 'doc' directories relative path (needed for running pytest in various locations)
        search_for_directory = "docs"
        full_dir_path = find_directory(search_for_directory)
        
        build_docs_pipe = subprocess.Popen(
            f"cd {full_dir_path} && make html",
            shell=True, 
        )

        # add the 'docs' subfolder location and the filname 
        doc_sub_directory = "_build/html" 
        doc_filename = "search.html"

        doc_file_path = f"{full_dir_path}/{doc_sub_directory}"
        is_dir_bool = os.path.isdir(doc_file_path)
        is_file_bool = os.path.isfile(f"{doc_file_path}/{doc_filename}")

        assert is_dir_bool is True
        assert is_file_bool is True
        

    def test_doc_file_installation_html_built(self):
        # find the 'doc' directories relative path (needed for running pytest in various locations)
        search_for_directory = "docs"
        full_dir_path = find_directory(search_for_directory)
        
        build_docs_pipe = subprocess.Popen(
            f"cd {full_dir_path} && make html",
            shell=True, 
        )

        # add the 'docs' subfolder location and the filname 
        doc_sub_directory = "_build/html/getting_started/installation" 
        doc_filename = "installation.html"

        doc_file_path = f"{full_dir_path}/{doc_sub_directory}"
        is_dir_bool = os.path.isdir(doc_file_path)
        is_file_bool = os.path.isfile(f"{doc_file_path}/{doc_filename}")

        assert is_dir_bool is True
        assert is_file_bool is True


    def test_doc_file_add_2_numbers_example_html_built(self):
        # find the 'doc' directories relative path (needed for running pytest in various locations)
        search_for_directory = "docs"
        full_dir_path = find_directory(search_for_directory)
        
        build_docs_pipe = subprocess.Popen(
            f"cd {full_dir_path} && make html",
            shell=True, 
        )

        # add the 'docs' subfolder location and the filname 
        doc_sub_directory = "_build/html/getting_started/quick_start" 
        doc_filename = "add_2_numbers_example.html"

        doc_file_path = f"{full_dir_path}/{doc_sub_directory}"
        is_dir_bool = os.path.isdir(doc_file_path)
        is_file_bool = os.path.isfile(f"{doc_file_path}/{doc_filename}")

        assert is_dir_bool is True
        assert is_file_bool is True


    def test_doc_file_math_function_class_example_html_built(self):
        # find the 'doc' directories relative path (needed for running pytest in various locations)
        search_for_directory = "docs"
        full_dir_path = find_directory(search_for_directory)
        
        build_docs_pipe = subprocess.Popen(
            f"cd {full_dir_path} && make html",
            shell=True, 
        )

        # add the 'docs' subfolder location and the filname 
        doc_sub_directory = "_build/html/getting_started/quick_start" 
        doc_filename = "math_function_class_example.html"

        doc_file_path = f"{full_dir_path}/{doc_sub_directory}"
        is_dir_bool = os.path.isdir(doc_file_path)
        is_file_bool = os.path.isfile(f"{doc_file_path}/{doc_filename}")

        assert is_dir_bool is True
        assert is_file_bool is True


    def test_doc_file_quick_start_toc_html_built(self):
        # find the 'doc' directories relative path (needed for running pytest in various locations)
        search_for_directory = "docs"
        full_dir_path = find_directory(search_for_directory)
        
        build_docs_pipe = subprocess.Popen(
            f"cd {full_dir_path} && make html",
            shell=True, 
        )

        # add the 'docs' subfolder location and the filname 
        doc_sub_directory = "_build/html/getting_started/quick_start" 
        doc_filename = "quick_start_toc.html"

        doc_file_path = f"{full_dir_path}/{doc_sub_directory}"
        is_dir_bool = os.path.isdir(doc_file_path)
        is_file_bool = os.path.isfile(f"{doc_file_path}/{doc_filename}")

        assert is_dir_bool is True
        assert is_file_bool is True


    def test_doc_file_tutorials_html_built(self):
        # find the 'doc' directories relative path (needed for running pytest in various locations)
        search_for_directory = "docs"
        full_dir_path = find_directory(search_for_directory)
        
        build_docs_pipe = subprocess.Popen(
            f"cd {full_dir_path} && make html",
            shell=True, 
        )

        # add the 'docs' subfolder location and the filname 
        doc_sub_directory = "_build/html/getting_started/quick_start" 
        doc_filename = "tutorials.html"

        doc_file_path = f"{full_dir_path}/{doc_sub_directory}"
        is_dir_bool = os.path.isdir(doc_file_path)
        is_file_bool = os.path.isfile(f"{doc_file_path}/{doc_filename}")

        assert is_dir_bool is True
        assert is_file_bool is True

    
    def test_doc_file_general_info_html_built(self):
        # find the 'doc' directories relative path (needed for running pytest in various locations)
        search_for_directory = "docs"
        full_dir_path = find_directory(search_for_directory)
        
        build_docs_pipe = subprocess.Popen(
            f"cd {full_dir_path} && make html",
            shell=True, 
        )

        # add the 'docs' subfolder location and the filname 
        doc_sub_directory = "_build/html/overview" 
        doc_filename = "general_info.html"

        doc_file_path = f"{full_dir_path}/{doc_sub_directory}"
        is_dir_bool = os.path.isdir(doc_file_path)
        is_file_bool = os.path.isfile(f"{doc_file_path}/{doc_filename}")

        assert is_dir_bool is True
        assert is_file_bool is True

    
    def test_doc_file_citing_python_github_tutorial_html_built(self):
        # find the 'doc' directories relative path (needed for running pytest in various locations)
        search_for_directory = "docs"
        full_dir_path = find_directory(search_for_directory)
        
        build_docs_pipe = subprocess.Popen(
            f"cd {full_dir_path} && make html",
            shell=True, 
        )

        # add the 'docs' subfolder location and the filname 
        doc_sub_directory = "_build/html/reference" 
        doc_filename = "citing_python_github_tutorial.html"

        doc_file_path = f"{full_dir_path}/{doc_sub_directory}"
        is_dir_bool = os.path.isdir(doc_file_path)
        is_file_bool = os.path.isfile(f"{doc_file_path}/{doc_filename}")

        assert is_dir_bool is True
        assert is_file_bool is True


    def test_doc_file_units_html_built(self):
        # find the 'doc' directories relative path (needed for running pytest in various locations)
        search_for_directory = "docs"
        full_dir_path = find_directory(search_for_directory)
        
        build_docs_pipe = subprocess.Popen(
            f"cd {full_dir_path} && make html",
            shell=True, 
        )

        # add the 'docs' subfolder location and the filname 
        doc_sub_directory = "_build/html/reference" 
        doc_filename = "units.html"

        doc_file_path = f"{full_dir_path}/{doc_sub_directory}"
        is_dir_bool = os.path.isdir(doc_file_path)
        is_file_bool = os.path.isfile(f"{doc_file_path}/{doc_filename}")

        assert is_dir_bool is True
        assert is_file_bool is True

    
    def test_doc_data_structures_html_built(self):
        # find the 'doc' directories relative path (needed for running pytest in various locations)
        search_for_directory = "docs"
        full_dir_path = find_directory(search_for_directory)
        
        build_docs_pipe = subprocess.Popen(
            f"cd {full_dir_path} && make html",
            shell=True, 
        )

        # add the 'docs' subfolder location and the filname 
        doc_sub_directory = "_build/html/topic_guides" 
        doc_filename = "data_structures.html"

        doc_file_path = f"{full_dir_path}/{doc_sub_directory}"
        is_dir_bool = os.path.isdir(doc_file_path)
        is_file_bool = os.path.isfile(f"{doc_file_path}/{doc_filename}")

        assert is_dir_bool is True
        assert is_file_bool is True


    def test_doc_specific_topic_guides_html_built(self):
        # find the 'doc' directories relative path (needed for running pytest in various locations)
        search_for_directory = "docs"
        full_dir_path = find_directory(search_for_directory)
        
        build_docs_pipe = subprocess.Popen(
            f"cd {full_dir_path} && make html",
            shell=True, 
        )

        # add the 'docs' subfolder location and the filname 
        doc_sub_directory = "_build/html/topic_guides" 
        doc_filename = "specific_topic_guides.html"

        doc_file_path = f"{full_dir_path}/{doc_sub_directory}"
        is_dir_bool = os.path.isdir(doc_file_path)
        is_file_bool = os.path.isfile(f"{doc_file_path}/{doc_filename}")

        assert is_dir_bool is True
        assert is_file_bool is True


    # ******************************************
    # Test the HTML file are built (END)
    # ******************************************
