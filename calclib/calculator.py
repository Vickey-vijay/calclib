"""
Calculator module providing basic arithmetic operations.
"""

def add(*args):
    """
    Add two or more numbers together.
    
    Args:
        *args: Numbers to be added.
        
    Returns:
        float or int: The sum of all input numbers.
        
    Examples:
        >>> add(1, 2)
        3
        >>> add(1, 2, 3, 4)
        10
    """
    if not args:
        raise ValueError("At least one number is required")
    return sum(args)


def subtract(a, b, *args):
    """
    Subtract the second and subsequent numbers from the first.
    
    Args:
        a: The first number.
        b: The second number to subtract from the first.
        *args: Additional numbers to subtract.
        
    Returns:
        float or int: The result after subtracting all subsequent numbers from the first.
        
    Examples:
        >>> subtract(10, 5)
        5
        >>> subtract(20, 5, 3, 2)
        10
    """
    result = a - b
    for num in args:
        result -= num
    return result


def multiply(*args):
    """
    Multiply two or more numbers together.
    
    Args:
        *args: Numbers to be multiplied.
        
    Returns:
        float or int: The product of all input numbers.
        
    Examples:
        >>> multiply(2, 3)
        6
        >>> multiply(2, 3, 4)
        24
    """
    if not args:
        raise ValueError("At least one number is required")
    
    result = 1
    for num in args:
        result *= num
    return result


def divide(a, b, *args):
    """
    Divide the first number by the second and subsequent numbers.
    
    Args:
        a: The numerator or dividend.
        b: The first denominator or divisor.
        *args: Additional divisors.
        
    Returns:
        float: The result of the division.
        
    Raises:
        ZeroDivisionError: If any divisor is zero.
        
    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(100, 2, 5)
        10.0
    """
    if b == 0 or any(num == 0 for num in args):
        raise ZeroDivisionError("Division by zero is not allowed")
    
    result = a / b
    for num in args:
        result /= num
    return result
