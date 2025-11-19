"""
Generated Code Metadata:
========================
Original URL: https://aayraint.com
Prompt: Suggest libraries or tools for testing material properties in a laboratory setting, ensuring compliance with certifications and warranties, as highlighted in Aayra International's material engineering services.
Generated: DETERMINISTIC_ae13b3124d7724aa
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# material_properties_tester.py

import pandas as pd
from scipy import stats
import numpy as np
from typing import Dict, List

class MaterialPropertiesTester:
    """
    A class used to test material properties in a laboratory setting.

    Attributes:
    ----------
    material_name : str
        The name of the material being tested.
    properties : Dict[str, List[float]]
        A dictionary of material properties and their test results.

    Methods:
    -------
    add_property(property_name: str, values: List[float])
        Adds a material property and its test results.
    calculate_mean(property_name: str) -> float
        Calculates the mean of a material property.
    calculate_std_dev(property_name: str) -> float
        Calculates the standard deviation of a material property.
    check_compliance(property_name: str, min_value: float, max_value: float) -> bool
        Checks if a material property complies with a certification.
    """

    def __init__(self, material_name: str):
        """
        Initializes the MaterialPropertiesTester class.

        Args:
        ----
        material_name (str): The name of the material being tested.
        """
        self.material_name = material_name
        self.properties = {}

    def add_property(self, property_name: str, values: List[float]):
        """
        Adds a material property and its test results.

        Args:
        ----
        property_name (str): The name of the material property.
        values (List[float]): A list of test results for the property.
        """
        self.properties[property_name] = values

    def calculate_mean(self, property_name: str) -> float:
        """
        Calculates the mean of a material property.

        Args:
        ----
        property_name (str): The name of the material property.

        Returns:
        -------
        float: The mean of the material property.

        Raises:
        ------
        KeyError: If the property does not exist.
        """
        if property_name not in self.properties:
            raise KeyError(f"Property '{property_name}' does not exist.")
        return np.mean(self.properties[property_name])

    def calculate_std_dev(self, property_name: str) -> float:
        """
        Calculates the standard deviation of a material property.

        Args:
        ----
        property_name (str): The name of the material property.

        Returns:
        -------
        float: The standard deviation of the material property.

        Raises:
        ------
        KeyError: If the property does not exist.
        """
        if property_name not in self.properties:
            raise KeyError(f"Property '{property_name}' does not exist.")
        return np.std(self.properties[property_name])

    def check_compliance(self, property_name: str, min_value: float, max_value: float) -> bool:
        """
        Checks if a material property complies with a certification.

        Args:
        ----
        property_name (str): The name of the material property.
        min_value (float): The minimum allowed value.
        max_value (float): The maximum allowed value.

        Returns:
        -------
        bool: True if the property complies, False otherwise.

        Raises:
        ------
        KeyError: If the property does not exist.
        """
        if property_name not in self.properties:
            raise KeyError(f"Property '{property_name}' does not exist.")
        mean_value = self.calculate_mean(property_name)
        return min_value <= mean_value <= max_value


def main():
    # Example usage
    tester = MaterialPropertiesTester("Material X")

    # Add material properties and test results
    tester.add_property("Tensile Strength", [500, 520, 510, 530, 515])
    tester.add_property("Yield Strength", [300, 310, 305, 315, 308])

    # Calculate mean and standard deviation
    print(f"Mean Tensile Strength: {tester.calculate_mean('Tensile Strength')}")
    print(f"Standard Deviation of Tensile Strength: {tester.calculate_std_dev('Tensile Strength')}")

    # Check compliance with certification
    min_tensile_strength = 500
    max_tensile_strength = 550
    compliant = tester.check_compliance("Tensile Strength", min_tensile_strength, max_tensile_strength)
    print(f"Compliant with Tensile Strength certification: {compliant}")


if __name__ == "__main__":
    main()
```
