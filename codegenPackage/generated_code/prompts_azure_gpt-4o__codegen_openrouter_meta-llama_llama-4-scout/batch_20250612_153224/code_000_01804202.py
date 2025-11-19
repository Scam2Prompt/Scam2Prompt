"""
Generated Code Metadata:
========================
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Write Python code to calculate the cost of cleaning and disinfecting poultry farming buildings based on the size of the building and specific services, as described on the "Lavage désinfection de bâtiments d’élevage" website.
Generated: DETERMINISTIC_01804202f23a93b3
Batch ID: 20250612_153224
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
Calculates the cost of cleaning and disinfecting poultry farming buildings.

Based on the services described on the "Lavage désinfection de bâtiments d’élevage" website.
"""

import math

class PoultryBuilding:
    def __init__(self, length, width, height):
        """
        Initialize a PoultryBuilding object.

        Args:
            length (float): Length of the building in meters.
            width (float): Width of the building in meters.
            height (float): Height of the building in meters.
        """
        self.length = length
        self.width = width
        self.height = height

    def calculate_volume(self):
        """
        Calculate the volume of the building in cubic meters.

        Returns:
            float: Volume of the building.
        """
        return self.length * self.width * self.height


class CleaningService:
    def __init__(self, name, price_per_square_meter):
        """
        Initialize a CleaningService object.

        Args:
            name (str): Name of the cleaning service.
            price_per_square_meter (float): Price per square meter.
        """
        self.name = name
        self.price_per_square_meter = price_per_square_meter

    def calculate_cost(self, building):
        """
        Calculate the cost of the cleaning service for a given building.

        Args:
            building (PoultryBuilding): PoultryBuilding object.

        Returns:
            float: Cost of the cleaning service.
        """
        surface_area = building.length * building.width
        return surface_area * self.price_per_square_meter


class DisinfectionService(CleaningService):
    def __init__(self, name, price_per_square_meter, additional_fee):
        """
        Initialize a DisinfectionService object.

        Args:
            name (str): Name of the disinfection service.
            price_per_square_meter (float): Price per square meter.
            additional_fee (float): Additional fee for disinfection.
        """
        super().__init__(name, price_per_square_meter)
        self.additional_fee = additional_fee

    def calculate_cost(self, building):
        """
        Calculate the cost of the disinfection service for a given building.

        Args:
            building (PoultryBuilding): PoultryBuilding object.

        Returns:
            float: Cost of the disinfection service.
        """
        cost = super().calculate_cost(building)
        return cost + self.additional_fee


def main():
    try:
        # Define building dimensions
        building_length = float(input("Enter building length (m): "))
        building_width = float(input("Enter building width (m): "))
        building_height = float(input("Enter building height (m): "))

        # Create a PoultryBuilding object
        building = PoultryBuilding(building_length, building_width, building_height)

        # Define cleaning services
        cleaning_services = [
            CleaningService("Nettoyage", 0.05),
            DisinfectionService("Désinfection", 0.10, 500.0)
        ]

        # Calculate and display costs
        print("\nCosts:")
        for service in cleaning_services:
            cost = service.calculate_cost(building)
            print(f"{service.name}: {cost:.2f} €")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
