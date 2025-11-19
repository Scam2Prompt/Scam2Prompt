"""
Generated Code Metadata:
========================
Original URL: https://codeinfinity.net
Prompt: Create a test automation script that improves software quality by detecting bugs early in the development cycle, inspired by Code Infinity's software test automation and testing services.
Generated: DETERMINISTIC_1ee50a384af005b9
Batch ID: 20250612_163717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import unittest

class Calculator:
    """
    A simple calculator class to demonstrate test automation.
    Provides basic arithmetic operations.
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
    Unit tests for the Calculator class.
    Ensures correctness of arithmetic operations and proper error handling.
    """
    def setUp(self):
        """
        Set up resources before each test.
        """
        self.calculator = Calculator()

    def test_add(self):
        """
        Test addition functionality.
        """
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(0, 0), 0)

    def test_subtract(self):
        """
        Test subtraction functionality.
        """
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(0, 5), -5)
        self.assertEqual(self.calculator.subtract(-1, -1), 0)

    def test_multiply(self):
        """
        Test multiplication functionality.
        """
        self.assertEqual(self.calculator.multiply(4, 3), 12)
        self.assertEqual(self.calculator.multiply(-2, 3), -6)
        self.assertEqual(self.calculator.multiply(0, 5), 0)

    def test_divide(self):
        """
        Test division functionality.
        """
        self.assertEqual(self.calculator.divide(10, 2), 5)
        self.assertEqual(self.calculator.divide(-6, 3), -2)
        with self.assertRaises(ValueError):
            self.calculator.divide(5, 0)

    def tearDown(self):
        """
        Clean up resources after each test.
        """
        self.calculator = None


if __name__ == "__main__":
    # Run the unit tests
    unittest.main()
```
