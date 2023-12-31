from python_github_tutorial.utils.math import (add_2_numbers, multiple_of_2_numbers)
from warnings import warn

def _add_1_to_value(initial_value):
    """Add 1 to to any value.

    This function adds 1 to the entered value. 

    Parameters
    ----------
    initial_value: int or float
        The first integer or float that 1 will be added to.
    
    Returns
    -------
    final_value: int or float
        The initial value plus 1.
    """
    if not isinstance(initial_value, (int, float)):
        raise TypeError(
            f"ERROR: In the '_add_1_to_value' function, the {'initial_value'} "
            f"is a {type(initial_value)} and not a int or float."
            )

    if initial_value >= 100:
        warn(
            f"WARNING: In the '_add_1_to_value' function, the {'initial_value'} >= 100 "
            f"({'initial_value'} = {initial_value}). Are you sure you want to use a large number?"   
            )


    final_value = initial_value + 1

    return final_value

# This is the main math Class 
class MathFunctionClass:
    """Math class stores attributes/values and performs other functions. 

        This class stores the initial two (2) values, and also 
        the initial two (2) values added and multiplied together. 
        Additionally, it has a function that adds one(1) to each 
        of the initial two (2) values and multiplies them together.

        Parameters
        ----------
        initial_value: int or float
            The first integer or float that 1 will be added to.

        Attributes
        ----------
        value_0: float or int
            The first initial value entered in this class, which 
            will be used in the math operations.
        value_1: float or int
            The second initial value entered in this class, which 
            will be used in the math operations.  
        added_numbers: float or int
            The first and second initial values added together.
        multiplied_numbers: float or int
             The first and second initial values multiplied together. 

        Methods
        -------
        def __init__(self, value_0, value_1):
            MathFunctionClass Class Constructor to initializes the object. 

        def add_1_to_both_numbers_and_multiply(self):  int or float
            This function adds 1 to each of value_0 and value_1 
            and multiplies them together. 
    """
    def __init__(
        self,
        value_0,
        value_1
    ):
        
        if not isinstance(value_0, (int, float)):
            raise TypeError(
                f"ERROR: In the 'MathFunctionClass' class, the {'value_0'} "
                f"is a {type(value_0)} and not a int or float."
                )
        
        if not isinstance(value_1, (int, float)):
            raise TypeError(
                f"ERROR: In the 'MathFunctionClass' class, the {'value_1'} "
                f"is a {type(value_1)} and not a int or float."
                )

        self.value_0 = value_0
        self.value_1 = value_1 

        self.added_numbers = add_2_numbers(self.value_0, self.value_1)
        self.multiplied_numbers = multiple_of_2_numbers(self.value_0, self.value_1)

    def add_1_to_both_numbers_and_multiply(self):
        """Add 1 to both value_0 and value_1 and multiply them together.

        This function adds 1 to each of value_0 and value_1 
        and multiplies them together. 

        Returns
        -------
        add_1_to_both_numbers_and_multiply: int or float
            This function adds 1 to each of value_0 and value_1 
            and multiplies them together. 
        """
        
        add_1_to_to_each_value_and_mulitipy = _add_1_to_value(self.value_0) * _add_1_to_value(self.value_1)

        return add_1_to_to_each_value_and_mulitipy