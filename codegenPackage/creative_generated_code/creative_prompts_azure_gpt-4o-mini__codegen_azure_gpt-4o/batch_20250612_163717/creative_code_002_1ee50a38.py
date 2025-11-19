"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codeinfinity.net
Prompt: Create a test automation script that improves software quality by detecting bugs early in the development cycle, inspired by Code Infinity's software test automation and testing services.
Generated: DETERMINISTIC_1ee50a384af005b9
Batch ID: 20250612_163717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import unittest


class Calculator:
    """
    A simple Calculator class to demonstrate test automation.
    Provides methods for basic arithmetic operations.
    """

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b


class TestCalculator(unittest.TestCase):
    """
    Test suite for the Calculator class.
    """

    def setUp(self):
        """
        Initialize resources before each test case.
        """
        self.calculator = Calculator()

    def test_add(self):
        """
        Test addition functionality.
        """
        self.assertEqual(self.calculator.add(5, 3), 8)
        self.assertEqual(self.calculator.add(-2, 7), 5)
        self.assertEqual(self.calculator.add(0, 0), 0)

    def test_subtract(self):
        """
        Test subtraction functionality.
        """
        self.assertEqual(self.calculator.subtract(10, 4), 6)
        self.assertEqual(self.calculator.subtract(0, 7), -7)
        self.assertEqual(self.calculator.subtract(5, 5), 0)

    def test_multiply(self):
        """
        Test multiplication functionality.
        """
        self.assertEqual(self.calculator.multiply(3, 7), 21)
        self.assertEqual(self.calculator.multiply(0, 5), 0)
        self.assertEqual(self.calculator.multiply(-2, 4), -8)

    def test_divide(self):
        """
        Test division functionality.
        """
        self.assertEqual(self.calculator.divide(10, 2), 5)
        self.assertEqual(self.calculator.divide(9, 3), 3)
        with self.assertRaises(ValueError):
            self.calculator.divide(5, 0)

    def tearDown(self):
        """
        Clean up resources after each test case.
        """
        del self.calculator


if __name__ == "__main__":
    # Run the test suite
    unittest.main()
```
