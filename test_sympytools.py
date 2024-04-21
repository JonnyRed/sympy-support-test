"""
This module demonstrates the integration of various sympy_support components
and the IPython utility for columnized output. It is structured to test the
sympy_support utilities and display the system path and available functions
from the sympy_support modules in a columnized format.

Attributes:
    ssu (module): An alias for the sympy_support.utils module.
    ssc (module): An alias for the sympy_support.chainrule module.
    ssg (module): An alias for the sympy_support.generalised_chain_rule module.
"""

import sys
import doctest

# Importing utility functions from the sympy_support package
import sympy_support.spv_utils as ssu
import sympy_support.chainrule as ssc
import sympy_support.generalised_chain_rule as ssg

# Importing the columnize function from IPython for better display of lists
from IPython.utils.text import columnize


def main():
    """
    The main function of the module. It prints out the system path,
    the directory of sympy_support utility functions, and runs doctests
    on the `sympy_support.utils` module.
    """

    # Display the system path in a columnized format
    print(columnize(sys.path))

    # Display the directory of sympy_support utility functions in a
    # columnized format
    print(columnize(dir(ssu)))
    print(columnize(dir(ssc)))
    print(columnize(dir(ssg)))

    # Run doctests on the sympy_support.utils module with verbose output

    verbose = True
    doctest.testmod(ssu, verbose=verbose)
    doctest.testmod(ssu, verbose=verbose)
    doctest.testmod(ssg, verbose=verbose)


# Ensures the main function is called only when the script is executed directly
if __name__ == "__main__":
    main()