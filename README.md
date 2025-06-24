# CalcLib

A simple Python library for basic arithmetic operations.

## Features

- Add two or more numbers
- Subtract multiple numbers
- Multiply two or more numbers
- Divide numbers

## Installation

You can install the package using pip:

```bash
pip install calclib
```

Or install directly from the source:

```bash
pip install -e .
```

## Usage

```python
# Import the functions
from calclib import add, subtract, multiply, divide

# Addition
result = add(1, 2, 3, 4)  # Returns 10

# Subtraction
result = subtract(10, 3, 2)  # Returns 5 (10-3-2=5)

# Multiplication
result = multiply(2, 3, 4)  # Returns 24

# Division
result = divide(100, 2, 5)  # Returns 10.0 (100/2/5=10.0)
```

## License

This project is licensed under the terms of the MIT license.
