"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rexas-de.web.app
Prompt: Create a step-by-step tutorial for investing in real estate through Rexas Estate, including co-ownership and earning passive income in stablecoins.
Generated: DETERMINISTIC_002d667e38fef4b8
Batch ID: 20250612_145444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Real Estate Investment Tutorial with Rexas Estate

This script provides a step-by-step guide to investing in real estate through Rexas Estate,
including options for co-ownership and earning passive income in stablecoins.
"""

import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RexasEstate:
    """
    A class to represent the Rexas Estate platform for real estate investment.
    """

    def __init__(self):
        self.properties = []
        self.investors = []

    def add_property(self, property_name, property_value):
        """
        Add a new property to the Rexas Estate platform.

        Parameters:
        property_name (str): The name of the property.
        property_value (float): The value of the property.
        """
        if property_value <= 0:
            logging.error("Property value must be greater than zero.")
            raise ValueError("Property value must be greater than zero.")
        
        property_data = {
            'name': property_name,
            'value': property_value,
            'investors': []
        }
        self.properties.append(property_data)
        logging.info(f"Property '{property_name}' added successfully.")

    def invest(self, property_name, investor_name, amount):
        """
        Allow an investor to invest in a property.

        Parameters:
        property_name (str): The name of the property to invest in.
        investor_name (str): The name of the investor.
        amount (float): The investment amount.
        """
        if amount <= 0:
            logging.error("Investment amount must be greater than zero.")
            raise ValueError("Investment amount must be greater than zero.")

        property_found = False
        for property_data in self.properties:
            if property_data['name'] == property_name:
                property_found = True
                property_data['investors'].append({'name': investor_name, 'amount': amount})
                logging.info(f"{investor_name} invested {amount} in {property_name}.")
                break

        if not property_found:
            logging.error(f"Property '{property_name}' not found.")
            raise ValueError(f"Property '{property_name}' not found.")

    def calculate_passive_income(self, property_name, stablecoin_rate):
        """
        Calculate passive income generated from a property in stablecoins.

        Parameters:
        property_name (str): The name of the property for passive income calculation.
        stablecoin_rate (float): The rate of passive income per investment in stablecoins.
        
        Returns:
        float: Total passive income in stablecoins.
        """
        total_income = 0.0
        property_found = False
        
        for property_data in self.properties:
            if property_data['name'] == property_name:
                property_found = True
                for investor in property_data['investors']:
                    total_income += investor['amount'] * stablecoin_rate
                break

        if not property_found:
            logging.error(f"Property '{property_name}' not found.")
            raise ValueError(f"Property '{property_name}' not found.")

        logging.info(f"Total passive income for '{property_name}' is {total_income} in stablecoins.")
        return total_income

# Example usage
if __name__ == "__main__":
    try:
        rexas_estate = RexasEstate()

        # Step 1: Add properties
        rexas_estate.add_property("Luxury Condo", 300000)
        rexas_estate.add_property("Beach House", 500000)

        # Step 2: Invest in properties
        rexas_estate.invest("Luxury Condo", "Alice", 50000)
        rexas_estate.invest("Beach House", "Bob", 100000)

        # Step 3: Calculate passive income
        passive_income = rexas_estate.calculate_passive_income("Luxury Condo", 0.1)
        print(f"Passive income earned: {passive_income} stablecoins")

    except ValueError as e:
        logging.error(f"An error occurred: {e}")
```
