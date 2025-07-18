import unittest
from calclib import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, 2, 3, 4), 10)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 0), 0)
        
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(10, 2, 3), 5)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-5, -10), 5)
        
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(2, 3, 4), 24)
        self.assertEqual(multiply(-2, -3), 6)
        self.assertEqual(multiply(0, 5), 0)
        
    def test_divide(self):
        self.assertEqual(divide(6, 2), 3.0)
        self.assertEqual(divide(100, 2, 5), 10.0)
        self.assertEqual(divide(-10, -5), 2.0)
        
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)
            
        with self.assertRaises(ZeroDivisionError):
            divide(10, 2, 0)
            
if __name__ == "__main__":
    unittest.main()
