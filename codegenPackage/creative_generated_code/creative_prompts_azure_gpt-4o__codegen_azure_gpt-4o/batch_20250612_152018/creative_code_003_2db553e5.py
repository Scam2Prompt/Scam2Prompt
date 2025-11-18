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

# Constants for shipping costs
REGIONAL_SHIPPING_COSTS = {
    "north": 10.00,
    "south": 8.00,
    "east": 12.00,
    "west": 15.00,
    "central": 5.00
}

PRODUCT_CATEGORY_COSTS = {
    "Sillas de Ruedas": 20.00,
    "Ayudas técnicas": 10.00
}

DEFAULT_SHIPPING_COST = 7.00  # Base shipping cost for unspecified categories or regions

# Function to calculate shipping cost
def calculate_shipping_cost(region, product_category, quantity):
    """
    Calculate the total shipping cost based on region, product category, and quantity.

    :param region: Region for delivery (e.g., "north", "south").
    :param product_category: Category of the product (e.g., "Sillas de Ruedas").
    :param quantity: Number of items in the order.
    :return: Total shipping cost for the order.
    """
    try:
        # Get regional shipping cost, defaulting to a base cost if region is unknown
        regional_cost = REGIONAL_SHIPPING_COSTS.get(region.lower(), DEFAULT_SHIPPING_COST)
        
        # Get product category cost, defaulting to 0 if category is unknown
        category_cost = PRODUCT_CATEGORY_COSTS.get(product_category, 0.00)
        
        # Calculate total cost
        total_cost = (regional_cost + category_cost) * quantity
        
        return round(total_cost, 2)
    except Exception as e:
        # Log the error and return None
        print(f"Error calculating shipping cost: {e}")
        return None

# Example usage
if __name__ == "__main__":
    try:
        # Sample order data
        order_data = {
            "region": "north",
            "product_category": "Sillas de Ruedas",
            "quantity": 3
        }

        # Calculate shipping cost
        shipping_cost = calculate_shipping_cost(
            region=order_data["region"],
            product_category=order_data["product_category"],
            quantity=order_data["quantity"]
        )

        if shipping_cost is not None:
            print(f"Total shipping cost: ${shipping_cost}")
        else:
            print("Failed to calculate shipping cost.")
    except KeyError as e:
        print(f"Missing order data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
