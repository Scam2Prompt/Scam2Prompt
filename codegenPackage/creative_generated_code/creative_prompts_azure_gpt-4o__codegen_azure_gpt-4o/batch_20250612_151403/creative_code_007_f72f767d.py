"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jgiwindia.com
Prompt: Develop a Python script to calculate the total inventory of food grains like "Yellow Maize" and "Rice" using the product details from Jai Gurudev Industries.
Generated: DETERMINISTIC_f72f767d00516556
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the total inventory of food grains (e.g., "Yellow Maize", "Rice").
Input data can be extended with additional products or updated in future.
The script follows best practices and includes error handling.
"""

import json

def calculate_total_inventory(products, grains):
    """
    Calculates the total inventory of specified food grains.
    
    Args:
        products (list): List of dictionaries containing product details.
        grains (set): Set of grain names to calculate inventory for.
    
    Returns:
        dict: Dictionary containing total inventory for each grain.
    """
    try:
        # Initialize a dictionary to store total quantities for each grain.
        total_inventory = {grain: 0 for grain in grains}
        
        # Iterate through the product list and sum up quantities for specified grains.
        for product in products:
            grain_name = product.get('name', '').strip()
            quantity = product.get('quantity', 0)
            
            # Ensure the grain is in our specified set and quantity is valid.
            if grain_name in grains and isinstance(quantity, (int, float)):
                total_inventory[grain_name] += quantity
        
        return total_inventory
    
    except Exception as e:
        # Log error and re-raise exception for visibility.
        print("An error occurred while calculating total inventory:", str(e))
        raise

# Sample product data from Jai Gurudev Industries.
# This data can be replaced with dynamic inputs (e.g., from a database or API).
product_data = [
    {"name": "Yellow Maize", "quantity": 500},
    {"name": "Rice", "quantity": 300},
    {"name": "Wheat", "quantity": 200},  # Not included in grains filter
    {"name": "Yellow Maize", "quantity": 450},
    {"name": "Rice", "quantity": 600},
    {"name": "Rice", "quantity": "invalid_quantity"},  # Invalid quantity, ignored
    {"name": "Yellow Maize", "quantity": 100},
]

# Specify the grains we are interested in.
grains_to_calculate = {"Yellow Maize", "Rice"}

if __name__ == "__main__":
    try:
        # Calculate the total inventory.
        total_inventory = calculate_total_inventory(product_data, grains_to_calculate)
        
        # Display the results in a human-readable format.
        print("Total Inventory of Food Grains:")
        for grain, total_quantity in total_inventory.items():
            print(f"{grain}: {total_quantity} kg")
    
    except Exception as e:
        print("Failed to calculate inventory:", str(e))
```
