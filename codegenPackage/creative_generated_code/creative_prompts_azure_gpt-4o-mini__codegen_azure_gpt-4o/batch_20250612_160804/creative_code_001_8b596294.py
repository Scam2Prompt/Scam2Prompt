"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meatmaster.pe
Prompt: Write a function that calculates the shipping cost for orders over S/ 500 for the Meat Master products, considering the free shipping offer in Lima Metropolitana.
Generated: DETERMINISTIC_8b59629463112950
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Dict

def calculate_shipping_cost(order_total: float, location: str, products: List[Dict[str, float]]) -> float:
    """
    Calculates the shipping cost for Meat Master orders based on the order total, location, 
    and whether the products belong to the "Meat Master" category.
    
    Parameters:
        order_total (float): The total amount of the order.
        location (str): The location for the shipping. Example: 'Lima Metropolitana'.
        products (List[Dict[str, float]]): A list of dictionaries representing products in the order. 
                                           Each dictionary contains 'name' and 'price' keys.
    
    Returns:
        float: The calculated shipping cost. Free shipping applies for orders over S/ 500 
               for Meat Master products in Lima Metropolitana.
    """
    
    # Define free shipping conditions
    FREE_SHIPPING_LOCATION = "Lima Metropolitana"
    FREE_SHIPPING_THRESHOLD = 500.0
    
    # Verify if all products belong to "Meat Master"
    is_meat_master_order = all("Meat Master" in product["name"] for product in products)
    
    # Check if conditions for free shipping are met
    if (location == FREE_SHIPPING_LOCATION and 
        order_total >= FREE_SHIPPING_THRESHOLD and 
        is_meat_master_order):
        return 0.0  # Free shipping
    
    # Default shipping cost (if conditions are not met)
    DEFAULT_SHIPPING_COST = 50.0
    return DEFAULT_SHIPPING_COST


# Example usage:
if __name__ == "__main__":
    # Example order with Meat Master products
    order_products = [
        {"name": "Meat Master Beef", "price": 300.0},
        {"name": "Meat Master Chicken", "price": 250.0}
    ]
    order_total = sum(product["price"] for product in order_products)
    location = "Lima Metropolitana"

    try:
        shipping_cost = calculate_shipping_cost(order_total, location, order_products)
        print(f"Shipping Cost: S/ {shipping_cost}")
    except Exception as e:
        print(f"An error occurred while calculating shipping cost: {e}")
```
