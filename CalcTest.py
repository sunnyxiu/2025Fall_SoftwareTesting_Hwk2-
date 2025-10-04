import unittest
from Calc import Calculator  # The class we are going to implement

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5

    def test_sub(self):
        calc = Calculator()
        result = calc.sub(2, 3)
        self.assertEqual(result, -1) # Expect 2 - 3 = -1
    
    def test_mul(self):
        calc = Calculator()
        result = calc.mul(2, 3)
        self.assertEqual(result, 6)  # Expect 2 * 3 = 6

        result = calc.mul(2.0, 3)
        self.assertEqual(result, 6.0) # Expect 2.0 * 3 = 6.0

    def test_div(self):
        calc = Calculator()

        result = calc.div(3, 2)
        self.assertEqual(result, 1.5)  # Expect 3 / 2 = 1.5

        with self.assertRaises(ValueError):
            calc.div(3, 0)  # Expect 3 / 0 raise ValueError


        
if __name__ == "__main__":
    unittest.main()
    