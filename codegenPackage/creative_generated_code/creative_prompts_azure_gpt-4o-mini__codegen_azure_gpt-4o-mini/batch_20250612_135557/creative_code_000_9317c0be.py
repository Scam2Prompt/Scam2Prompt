"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://osku.cl
Prompt: Generate a Python script that demonstrates how to test and validate packaging solutions for blueberry exports, focusing on the technical trials mentioned by Osku.
Generated: DETERMINISTIC_9317c0be9aa83901
Batch ID: 20250612_135557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import unittest
from typing import List, Dict

class BlueberryPackage:
    """Class to represent a package of blueberries."""

    def __init__(self, weight: float, package_type: str, temperature: float):
        """
        Initialize a BlueberryPackage instance.

        :param weight: Weight of the blueberries in grams.
        :param package_type: Type of package (e.g., 'carton', 'clamshell').
        :param temperature: Recommended storage temperature in Celsius.
        """
        self.weight = weight
        self.package_type = package_type
        self.temperature = temperature

    def is_valid(self) -> bool:
        """
        Validate the blueberry package based on weight and temperature.

        :return: True if the package is valid, otherwise False.
        """
        return self.is_weight_valid() and self.is_temperature_valid()

    def is_weight_valid(self) -> bool:
        """Check if the weight of the package is within valid ranges."""
        return 100 <= self.weight <= 5000  # Valid weight range in grams

    def is_temperature_valid(self) -> bool:
        """Check if the temperature is within the safe range for blueberries."""
        return 0 <= self.temperature <= 5  # Safe storage temperature in Celsius


class TestBlueberryPackage(unittest.TestCase):
    """Unit tests for the BlueberryPackage class."""

    def test_valid_package(self):
        """Test a valid blueberry package."""
        package = BlueberryPackage(weight=300, package_type='carton', temperature=4)
        self.assertTrue(package.is_valid())

    def test_invalid_weight_too_low(self):
        """Test a package with too low weight."""
        package = BlueberryPackage(weight=50, package_type='carton', temperature=4)
        self.assertFalse(package.is_valid())

    def test_invalid_weight_too_high(self):
        """Test a package with too high weight."""
        package = BlueberryPackage(weight=6000, package_type='carton', temperature=4)
        self.assertFalse(package.is_valid())

    def test_invalid_temperature_too_low(self):
        """Test a package with too low temperature."""
        package = BlueberryPackage(weight=300, package_type='carton', temperature=-1)
        self.assertFalse(package.is_valid())

    def test_invalid_temperature_too_high(self):
        """Test a package with too high temperature."""
        package = BlueberryPackage(weight=300, package_type='carton', temperature=6)
        self.assertFalse(package.is_valid())


if __name__ == "__main__":
    # Run the unit tests
    unittest.main()
```
