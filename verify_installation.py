"""
Quick demo script to verify calclib installation.

Run this script after installing the calclib package to verify it's working correctly.
"""

def main():
    try:
        # Attempt to import from the installed package
        from calclib import add, subtract, multiply, divide
        
        print("CalcLib successfully imported!")
        print("Performing some calculations...")
        
        print(f"5 + 3 = {add(5, 3)}")
        print(f"10 - 4 = {subtract(10, 4)}")
        print(f"6 × 7 = {multiply(6, 7)}")
        print(f"20 ÷ 5 = {divide(20, 5)}")
        
        print("\nAll functions working correctly!")
        
    except ImportError:
        print("Failed to import calclib. Please make sure it's installed correctly.")
        print("You can install it by running: pip install -e .")
    
if __name__ == "__main__":
    main()
