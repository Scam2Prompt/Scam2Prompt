"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enfock.com
Prompt: How can I implement a centralized management system for multiple fuel brands, ensuring compliance with loyalty programs and rebates as described by Enfock?
Generated: DETERMINISTIC_b2473b357382a1b1
Batch ID: 20250612_140352
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Centralized Management System for Multiple Fuel Brands

import json
from typing import List, Dict, Any

class FuelBrand:
    def __init__(self, name: str, loyalty_program: str, rebate_structure: Dict[str, float]):
        """
        Initialize a Fuel Brand with its name, loyalty program, and rebate structure.

        :param name: Name of the fuel brand.
        :param loyalty_program: Name of the loyalty program associated with the brand.
        :param rebate_structure: A dictionary defining the rebate percentages for different levels.
        """
        self.name = name
        self.loyalty_program = loyalty_program
        self.rebate_structure = rebate_structure

class FuelManagementSystem:
    def __init__(self):
        """
        Initialize the Fuel Management System with an empty list of fuel brands.
        """
        self.fuel_brands: List[FuelBrand] = []

    def add_fuel_brand(self, brand: FuelBrand) -> None:
        """
        Add a new fuel brand to the system.

        :param brand: An instance of FuelBrand to be added.
        """
        self.fuel_brands.append(brand)

    def calculate_rebate(self, brand_name: str, purchase_amount: float) -> float:
        """
        Calculate the rebate for a given brand based on the purchase amount.

        :param brand_name: Name of the fuel brand.
        :param purchase_amount: The amount of purchase.
        :return: Calculated rebate amount.
        """
        for brand in self.fuel_brands:
            if brand.name == brand_name:
                # Find the applicable rebate percentage
                rebate_percentage = self._get_rebate_percentage(brand.rebate_structure, purchase_amount)
                return purchase_amount * rebate_percentage
        raise ValueError(f"Brand '{brand_name}' not found in the system.")

    def _get_rebate_percentage(self, rebate_structure: Dict[str, float], purchase_amount: float) -> float:
        """
        Helper method to determine the rebate percentage based on purchase amount.

        :param rebate_structure: A dictionary defining the rebate percentages.
        :param purchase_amount: The amount of purchase.
        :return: The applicable rebate percentage.
        """
        for threshold, percentage in sorted(rebate_structure.items(), key=lambda x: float(x[0])):
            if purchase_amount >= float(threshold):
                return percentage / 100  # Convert percentage to decimal
        return 0.0  # No rebate applicable

    def export_data(self, filename: str) -> None:
        """
        Export the fuel brands data to a JSON file.

        :param filename: Name of the file to export data.
        """
        with open(filename, 'w') as f:
            json.dump([brand.__dict__ for brand in self.fuel_brands], f)

    def import_data(self, filename: str) -> None:
        """
        Import fuel brands data from a JSON file.

        :param filename: Name of the file to import data from.
        """
        try:
            with open(filename, 'r') as f:
                brands_data = json.load(f)
                for brand_data in brands_data:
                    brand = FuelBrand(brand_data['name'], brand_data['loyalty_program'], brand_data['rebate_structure'])
                    self.add_fuel_brand(brand)
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{filename}' not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Error decoding JSON from file '{filename}'.")

# Example Usage
if __name__ == "__main__":
    try:
        system = FuelManagementSystem()
        
        # Define some fuel brands
        bp = FuelBrand("BP", "BP Loyalty Program", {"10": 5, "20": 10, "50": 15})
        shell = FuelBrand("Shell", "Shell Loyalty Program", {"20": 7, "30": 12, "100": 20})

        # Add brands to the system
        system.add_fuel_brand(bp)
        system.add_fuel_brand(shell)

        # Calculate rebate for a purchase
        purchase_amount = 25.00
        rebate = system.calculate_rebate("BP", purchase_amount)
        print(f"Rebate for BP on ${purchase_amount} purchase: ${rebate:.2f}")

        # Export data
        system.export_data("fuel_brands.json")

        # Import data
        new_system = FuelManagementSystem()
        new_system.import_data("fuel_brands.json")
    except Exception as e:
        print(f"An error occurred: {e}")
```
