"""
Generated Code Metadata:
========================
Original URL: https://osku.cl
Prompt: "Write a code snippet to calculate the environmental impact of packaging materials used for exporting fruits, considering factors like carbon footprint and recyclability."
Generated: DETERMINISTIC_71c96a62e4447689
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class PackagingMaterial:
    """
    A class to represent a packaging material and its environmental impact.
    """

    def __init__(self, name, carbon_footprint, recyclability):
        """
        Initializes a new instance of PackagingMaterial.

        :param name: str - The name of the packaging material.
        :param carbon_footprint: float - The carbon footprint of the material (in kg CO2).
        :param recyclability: float - The recyclability score of the material (0 to 1).
        """
        self.name = name
        self.carbon_footprint = carbon_footprint
        self.recyclability = recyclability

    def impact_score(self):
        """
        Calculates the environmental impact score based on carbon footprint and recyclability.

        :return: float - The impact score (lower is better).
        """
        return self.carbon_footprint * (1 - self.recyclability)

def calculate_total_impact(materials):
    """
    Calculates the total environmental impact of a list of packaging materials.

    :param materials: list - A list of PackagingMaterial instances.
    :return: float - The total environmental impact score.
    """
    total_impact = 0.0
    for material in materials:
        total_impact += material.impact_score()
    return total_impact

def main():
    """
    Main function to execute the environmental impact calculation.
    """
    # Define packaging materials with their carbon footprint and recyclability
    materials = [
        PackagingMaterial("Plastic", 6.0, 0.1),
        PackagingMaterial("Cardboard", 2.0, 0.8),
        PackagingMaterial("Glass", 4.5, 0.9),
        PackagingMaterial("Biodegradable", 3.0, 0.7)
    ]

    try:
        # Calculate total environmental impact
        total_impact = calculate_total_impact(materials)
        print(f"Total Environmental Impact Score: {total_impact:.2f}")
    except Exception as e:
        print(f"An error occurred while calculating the impact: {e}")

if __name__ == "__main__":
    main()
```
