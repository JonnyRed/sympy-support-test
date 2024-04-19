# Sympy Support Module Integration

This module demonstrates the integration of various components from the `sympy_support` package and IPython's `columnize` function. It is structured to test the `sympy_support` utilities and display the system path and available functions from the `sympy_support` modules in a columnized format.

## Usage

### Installation

Before running the code, ensure you have the required packages installed. You can install them via pip:

```bash
pip install sympy IPython
```

### Running the Code

To run the module, simply execute the `main()` function:

```bash
python module_integration.py
```

The `main()` function prints out the system path, the directory of `sympy_support` utility functions, and runs doctests on the `sympy_support.utils` and `sympy_support.chainrule` modules.

## Components

- **utils (ssu)**: Module containing utility functions for Sympy support.
- **chainrule (ssc)**: Module implementing chain rule functionality.
- **generalised_chain_rule (ssg)**: Module implementing generalized chain rule functionality.

## Requirements

- Python 3.x
- Sympy
- IPython

## File Structure

- `module_integration.py`: Main Python script demonstrating module integration.
- `sympy_support/`: Package containing utility functions for Sympy support.
  - `utils.py`: Utility functions for Sympy support.
  - `chainrule.py`: Implementation of chain rule functionality.
  - `generalised_chain_rule.py`: Implementation of generalized chain 
  rule functionality.

This README provides an overview of the module, instructions for usage, 
information about the components, requirements, and file structure. 
