"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ortopedic.cl
Prompt: Write a script to automate the calculation of shipping costs for orders placed on the Ortopedic website, considering regional delivery options and product categories like "Sillas de Ruedas" and "Ayudas técnicas."
Generated: DETERMINISTIC_2db553e594c70b84
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ShippingCostCalculator:
    def __init__(self, base_rates):
        """
        Initialize the ShippingCostCalculator with base rates for different regions.
        
        :param base_rates: A dictionary containing base shipping rates for each region.
        """
        self.base_rates = base_rates

    def calculate_shipping_cost(self, region, product_category, weight):
        """
        Calculate the shipping cost based on the region, product category, and weight.
        
        :param region: The delivery region as a string.
        :param product_category: The category of the product as a string.
        :param weight: The weight of the product in kilograms.
        :return: The calculated shipping cost.
        :raises ValueError: If the region or product category is not valid.
        """
        try:
            base_rate = self.base_rates[region]
        except KeyError:
            raise ValueError(f"Invalid region: {region}. Valid regions are {list(self.base_rates.keys())}.")

        if product_category not in ['Sillas de Ruedas', 'Ayudas técnicas']:
            raise ValueError(f"Invalid product category: {product_category}. Valid categories are 'Sillas de Ruedas' and 'Ayudas técnicas'.")

        # Calculate total shipping cost
        cost = base_rate + (weight * 0.5)  # Example cost calculation
        return round(cost, 2)  # Round to 2 decimal places


def load_base_rates(filepath):
    """
    Load base shipping rates from a JSON file.
    
    :param filepath: The path to the JSON file containing base rates.
    :return: A dictionary with base rates.
    :raises FileNotFoundError: If the specified file does not exist.
    :raises json.JSONDecodeError: If the file contains invalid JSON.
    """
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Base rates file not found: {filepath}") from e
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON from {filepath}") from e


def main():
    # Load base shipping rates from a JSON configuration file
    base_rates_filepath = 'base_rates.json'
    try:
        base_rates = load_base_rates(base_rates_filepath)
    except Exception as e:
        print(f"Error loading base rates: {e}")
        return

    # Initialize the shipping cost calculator with the loaded base rates
    calculator = ShippingCostCalculator(base_rates)

    # Example order details
    orders = [
        {"region": "North", "product_category": "Sillas de Ruedas", "weight": 10},
        {"region": "South", "product_category": "Ayudas técnicas", "weight": 5},
        {"region": "East", "product_category": "Sillas de Ruedas", "weight": 15},
        {"region": "West", "product_category": "Invalid Category", "weight": 8},
        {"region": "Invalid Region", "product_category": "Ayudas técnicas", "weight": 3},
    ]

    # Calculate and display shipping costs for each order
    for order in orders:
        try:
            cost = calculator.calculate_shipping_cost(order['region'], order['product_category'], order['weight'])
            print(f"Shipping cost for {order['product_category']} to {order['region']} ({order['weight']} kg): ${cost}")
        except ValueError as ve:
            print(f"Error calculating cost for order {order}: {ve}")


if __name__ == "__main__":
    main()
```
