"""
Generated Code Metadata:
========================
Original URL: https://www.specialmetal.ir
Prompt: Write Python code to determine the compatibility of nickel-based superalloys like INCONEL ALLOY 625 with DIN and ASTM standards for aerospace applications.
Generated: DETERMINISTIC_143b5e786d1003de
Batch ID: 20250612_150917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Nickel-Based Superalloy Compatibility Checker
=============================================

This script checks the compatibility of nickel-based superalloys like INCONEL ALLOY 625 
with DIN and ASTM standards for aerospace applications.
"""

import pandas as pd

class SuperalloyCompatibilityChecker:
    def __init__(self):
        # Define the chemical composition of INCONEL ALLOY 625
        self.inconel_625_composition = {
            'Ni': 58.0, 'Cr': 22.0, 'Mo': 9.0, 'Nb': 3.5, 'Fe': 5.0,
            'Al': 0.4, 'Ti': 0.2, 'C': 0.1, 'B': 0.005, 'Si': 0.5
        }

        # Define the DIN and ASTM standards for INCONEL ALLOY 625
        self.din_standard = {
            'DIN 2.4856': {
                'Ni': (58.0, 61.0), 'Cr': (21.0, 23.0), 'Mo': (8.0, 10.0), 
                'Nb': (3.0, 4.0), 'Fe': (4.0, 6.0), 'Al': (0.2, 0.6), 
                'Ti': (0.1, 0.4), 'C': (0.04, 0.10), 'B': (0.002, 0.010), 
                'Si': (0.2, 0.8)
            }
        }

        self.astm_standard = {
            'ASTM B446': {
                'Ni': (58.0, 61.0), 'Cr': (21.0, 23.0), 'Mo': (8.0, 10.0), 
                'Nb': (3.0, 4.0), 'Fe': (4.0, 6.0), 'Al': (0.2, 0.6), 
                'Ti': (0.1, 0.4), 'C': (0.04, 0.10), 'B': (0.002, 0.010), 
                'Si': (0.2, 0.8)
            }
        }

    def check_compatibility(self, alloy_composition, standard):
        """
        Check if the alloy composition meets the specified standard.

        Args:
            alloy_composition (dict): The chemical composition of the alloy.
            standard (dict): The standard to check against.

        Returns:
            bool: True if the alloy composition meets the standard, False otherwise.
        """
        for element, (min_val, max_val) in standard.items():
            if element not in alloy_composition:
                raise ValueError(f"Composition does not contain {element}")
            if not min_val <= alloy_composition[element] <= max_val:
                return False
        return True

    def check_inconel_625_compatibility(self):
        """
        Check the compatibility of INCONEL ALLOY 625 with DIN and ASTM standards.

        Returns:
            dict: A dictionary containing the compatibility results.
        """
        results = {}

        # Check compatibility with DIN standard
        for standard, composition_limits in self.din_standard.items():
            compatible = self.check_compatibility(self.inconel_625_composition, composition_limits)
            results[standard] = compatible

        # Check compatibility with ASTM standard
        for standard, composition_limits in self.astm_standard.items():
            compatible = self.check_compatibility(self.inconel_625_composition, composition_limits)
            results[standard] = compatible

        return results


def main():
    try:
        checker = SuperalloyCompatibilityChecker()
        results = checker.check_inconel_625_compatibility()

        print("Compatibility Results:")
        for standard, compatible in results.items():
            print(f"{standard}: {compatible}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
