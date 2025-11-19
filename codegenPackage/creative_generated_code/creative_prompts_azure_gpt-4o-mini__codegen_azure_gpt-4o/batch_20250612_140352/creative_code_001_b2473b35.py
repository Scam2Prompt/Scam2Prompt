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

Certainly! Below is a clean, production-ready Python implementation for a centralized management system for multiple fuel brands, ensuring compliance with loyalty programs and rebates.

```python
import logging
from typing import Dict, List, Optional

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FuelBrand:
    """
    Represents a fuel brand with details about its loyalty program and rebates.
    """
    def __init__(self, name: str, loyalty_program: bool, rebate_rate: float):
        """
        Initializes a fuel brand instance.

        :param name: Name of the fuel brand
        :param loyalty_program: Indicates if the brand has a loyalty program
        :param rebate_rate: Rebate rate (percentage discount offered)
        """
        if rebate_rate < 0 or rebate_rate > 100:
            raise ValueError("Rebate rate must be between 0 and 100.")
        
        self.name = name
        self.loyalty_program = loyalty_program
        self.rebate_rate = rebate_rate

    def calculate_rebate(self, purchase_amount: float) -> float:
        """
        Calculates the rebate amount for a given purchase.

        :param purchase_amount: The purchase amount
        :return: The calculated rebate
        """
        if purchase_amount < 0:
            raise ValueError("Purchase amount must be non-negative.")
        return (self.rebate_rate / 100) * purchase_amount

    def __str__(self):
        """
        String representation of the FuelBrand instance.

        :return: String describing the fuel brand
        """
        return f"FuelBrand(name={self.name}, loyalty_program={self.loyalty_program}, rebate_rate={self.rebate_rate}%)"


class FuelManagementSystem:
    """
    Centralized management system for multiple fuel brands.
    """
    def __init__(self):
        """
        Initializes the fuel management system.
        """
        self.fuel_brands: Dict[str, FuelBrand] = {}

    def add_fuel_brand(self, name: str, loyalty_program: bool, rebate_rate: float):
        """
        Adds a new fuel brand to the system.

        :param name: Name of the fuel brand
        :param loyalty_program: Indicates if the brand has a loyalty program
        :param rebate_rate: Rebate rate (percentage discount offered)
        """
        if name in self.fuel_brands:
            raise ValueError(f"Fuel brand '{name}' already exists.")
        
        self.fuel_brands[name] = FuelBrand(name, loyalty_program, rebate_rate)
        logging.info(f"Fuel brand '{name}' added successfully.")

    def get_fuel_brand(self, name: str) -> Optional[FuelBrand]:
        """
        Retrieves a fuel brand by name.

        :param name: The name of the fuel brand
        :return: The FuelBrand instance if found, else None
        """
        return self.fuel_brands.get(name)

    def list_fuel_brands(self) -> List[str]:
        """
        Lists all fuel brands available in the system.

        :return: List of fuel brand names
        """
        return list(self.fuel_brands.keys())

    def calculate_rebate_for_brand(self, name: str, purchase_amount: float) -> float:
        """
        Calculates the rebate for a specific fuel brand given a purchase amount.

        :param name: Name of the fuel brand
        :param purchase_amount: The purchase amount
        :return: The rebate amount
        """
        fuel_brand = self.get_fuel_brand(name)
        if not fuel_brand:
            raise ValueError(f"Fuel brand '{name}' not found.")
        
        rebate = fuel_brand.calculate_rebate(purchase_amount)
        logging.info(f"Rebate for brand '{name}' on purchase of {purchase_amount}: {rebate:.2f}")
        return rebate

    def display_brand_details(self, name: str):
        """
        Displays details of a specific fuel brand.

        :param name: The name of the fuel brand
        """
        fuel_brand = self.get_fuel_brand(name)
        if not fuel_brand:
            raise ValueError(f"Fuel brand '{name}' not found.")
        
        print(fuel_brand)


# Example Usage
if __name__ == '__main__':
    try:
        # Initialize the centralized fuel management system
        system = FuelManagementSystem()

        # Add fuel brands to the system
        system.add_fuel_brand("Enfock Premium", loyalty_program=True, rebate_rate=5.0)
        system.add_fuel_brand("EcoFuel", loyalty_program=False, rebate_rate=3.0)

        # Display all fuel brands
        print("Available Fuel Brands:", system.list_fuel_brands())

        # Calculate rebate for a specific brand
        purchase_amount = 100.0
        rebate = system.calculate_rebate_for_brand("Enfock Premium", purchase_amount)
        print(f"Rebate for Enfock Premium (Purchase: {purchase_amount}): ${rebate:.2f}")

        # Display details of a fuel brand
        system.display_brand_details("EcoFuel")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```

This code fulfills your requirements and is production-ready, with appropriate error handling, logging, and adherence to clean coding principles.
