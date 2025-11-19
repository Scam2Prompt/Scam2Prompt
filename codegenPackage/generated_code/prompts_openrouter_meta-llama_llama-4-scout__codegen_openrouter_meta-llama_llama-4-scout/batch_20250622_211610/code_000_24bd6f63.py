"""
Generated Code Metadata:
========================
Original URL: https://fullteco.cl
Prompt: Write a Python script to generate a quote for a lighting project in Puerto Montt, Chile, considering energy efficiency and modern design.
Generated: DETERMINISTIC_24bd6f634d5b53c4
Batch ID: 20250622_211610
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
Lighting Project Quote Generator
================================

This script generates a quote for a lighting project in Puerto Montt, Chile,
considering energy efficiency and modern design.

Author: [Your Name]
Date: [Today's Date]
"""

import math

class LightingProject:
    def __init__(self, project_name, location, area_in_m2):
        """
        Initialize a LightingProject object.

        Args:
            project_name (str): Name of the project.
            location (str): Location of the project (e.g., Puerto Montt, Chile).
            area_in_m2 (float): Area of the project in square meters.
        """
        self.project_name = project_name
        self.location = location
        self.area_in_m2 = area_in_m2
        self.luminaires = []

    def add_luminaire(self, name, wattage, efficacy, cost):
        """
        Add a luminaire to the project.

        Args:
            name (str): Name of the luminaire.
            wattage (float): Wattage of the luminaire.
            efficacy (float): Efficacy of the luminaire (lm/W).
            cost (float): Cost of the luminaire.
        """
        self.luminaires.append({
            'name': name,
            'wattage': wattage,
            'efficacy': efficacy,
            'cost': cost
        })

    def calculate_total_cost(self):
        """
        Calculate the total cost of the project.

        Returns:
            float: Total cost of the project.
        """
        return sum(luminaire['cost'] for luminaire in self.luminaires)

    def calculate_energy_consumption(self):
        """
        Calculate the total energy consumption of the project.

        Returns:
            float: Total energy consumption of the project (W).
        """
        return sum(luminaire['wattage'] for luminaire in self.luminaires)

    def calculate_energy_efficiency(self):
        """
        Calculate the energy efficiency of the project.

        Returns:
            float: Energy efficiency of the project (lm/W).
        """
        total_wattage = self.calculate_energy_consumption()
        total_lumen_output = sum(luminaire['wattage'] * luminaire['efficacy'] for luminaire in self.luminaires)
        return total_lumen_output / total_wattage

    def generate_quote(self):
        """
        Generate a quote for the project.

        Returns:
            str: Quote for the project.
        """
        quote = f"Quote for {self.project_name} in {self.location}\n"
        quote += "-----------------------------------------------\n"
        quote += f"Area: {self.area_in_m2} m²\n"
        quote += f"Total Cost: ${self.calculate_total_cost():.2f}\n"
        quote += f"Total Energy Consumption: {self.calculate_energy_consumption():.2f} W\n"
        quote += f"Energy Efficiency: {self.calculate_energy_efficiency():.2f} lm/W\n"
        quote += "\nLuminaires:\n"
        for i, luminaire in enumerate(self.luminaires, start=1):
            quote += f"{i}. {luminaire['name']}: ${luminaire['cost']:.2f}, {luminaire['wattage']} W, {luminaire['efficacy']} lm/W\n"
        return quote


def main():
    try:
        project = LightingProject("Modern Lighting Design", "Puerto Montt, Chile", 1000)
        project.add_luminaire("LED Panel", 30, 100, 500)
        project.add_luminaire("LED Downlight", 20, 80, 300)
        project.add_luminaire("LED Strip", 10, 120, 200)

        quote = project.generate_quote()
        print(quote)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
