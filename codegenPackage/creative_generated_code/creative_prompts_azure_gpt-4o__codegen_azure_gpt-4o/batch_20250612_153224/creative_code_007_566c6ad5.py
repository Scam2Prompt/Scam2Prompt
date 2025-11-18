"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elagrocorrentino.com.ar
Prompt: Write code to calculate the cost of the basic food basket for families in Corrientes, Argentina, using the data provided by "El Agro Correntino."
Generated: DETERMINISTIC_566c6ad55bcc193a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Function to calculate the total cost of the basic food basket
def calculate_food_basket_cost(data):
    """
    Calculate the total cost of the basic food basket based on input data.

    Args:
        data (list of dict): A list of dictionaries representing the food items, each containing:
            - 'name': Name of the item (str)
            - 'price_per_kg': Price per kilogram (float)
            - 'quantity_kg': Quantity in kilograms required for the basket (float)

    Returns:
        float: Total cost of the basic food basket.
    """
    try:
        total_cost = 0.0
        for item in data:
            # Ensure all required keys are present in the item
            if 'price_per_kg' not in item or 'quantity_kg' not in item:
                raise ValueError(f"Missing required keys in item: {item}")

            # Calculate the cost for the item and add to the total cost
            item_cost = item['price_per_kg'] * item['quantity_kg']
            total_cost += item_cost
        
        return total_cost
    except TypeError:
        raise TypeError("Invalid data format. Expected a list of dictionaries.")
    except Exception as e:
        raise Exception(f"An error occurred during calculation: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data from "El Agro Correntino"
    food_basket_data = [
        {"name": "Rice", "price_per_kg": 120.5, "quantity_kg": 5},
        {"name": "Beans", "price_per_kg": 150.0, "quantity_kg": 3},
        {"name": "Flour", "price_per_kg": 80.0, "quantity_kg": 2},
        {"name": "Sugar", "price_per_kg": 90.0, "quantity_kg": 1.5},
        {"name": "Cooking oil", "price_per_kg": 200.0, "quantity_kg": 2},
    ]

    try:
        # Calculate the total cost of the basket
        total_cost = calculate_food_basket_cost(food_basket_data)
        print(f"The total cost of the basic food basket is: ${total_cost:.2f}")
    except Exception as e:
        print(f"Error: {e}")
```
