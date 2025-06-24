# Installation and Usage Guide for CalcLib

## Installation

There are two ways to install CalcLib:

### Method 1: Install in Development Mode

This method is best if you plan to modify the library code.

1. Open a terminal or command prompt
2. Navigate to the directory containing the `setup.py` file
3. Run the following command:

```bash
pip install -e .
```

The `-e` flag installs the package in "development" or "editable" mode, which means any changes you make to the library code will be immediately available without needing to reinstall.

### Method 2: Install as a Regular Package

If you just want to use the library without making changes:

1. Open a terminal or command prompt
2. Navigate to the directory containing the `setup.py` file
3. Run the following command:

```bash
pip install .
```

## Verifying Installation

To verify that the installation was successful, you can run the included tests:

```bash
python -m unittest discover tests
```

Or try running the example script:

```bash
python examples/demo.py
```

## Usage

Here's how you can use CalcLib in your own Python projects:

```python
# Import the functions you need
from calclib import add, subtract, multiply, divide

# Examples
result1 = add(5, 10, 15)  # 30
result2 = subtract(20, 5, 3)  # 12
result3 = multiply(2, 3, 4)  # 24
result4 = divide(100, 4, 5)  # 5.0

print(result1, result2, result3, result4)
```

## Function Documentation

### add(*args)
Adds two or more numbers together.

### subtract(a, b, *args)
Subtracts the second and subsequent numbers from the first.

### multiply(*args)
Multiplies two or more numbers together.

### divide(a, b, *args)
Divides the first number by the second and subsequent numbers.
