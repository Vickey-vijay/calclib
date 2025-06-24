"""
Example script demonstrating the calclib library.
"""

# This script assumes calclib is installed or available in the Python path
from calclib import add, subtract, multiply, divide

def main():
    print("CalcLib Demo")
    print("-----------")
    
    # Addition examples
    print("\nAddition:")
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"add(1, 2, 3, 4, 5) = {add(1, 2, 3, 4, 5)}")
    
    # Subtraction examples
    print("\nSubtraction:")
    print(f"subtract(10, 4) = {subtract(10, 4)}")
    print(f"subtract(20, 5, 3, 2) = {subtract(20, 5, 3, 2)}")
    
    # Multiplication examples
    print("\nMultiplication:")
    print(f"multiply(6, 7) = {multiply(6, 7)}")
    print(f"multiply(2, 3, 4) = {multiply(2, 3, 4)}")
    
    # Division examples
    print("\nDivision:")
    print(f"divide(20, 4) = {divide(20, 4)}")
    print(f"divide(100, 2, 5) = {divide(100, 2, 5)}")
    
    # Error handling example
    print("\nError Handling:")
    try:
        result = divide(10, 0)
    except ZeroDivisionError as e:
        print(f"Error caught: {e}")

if __name__ == "__main__":
    main()
