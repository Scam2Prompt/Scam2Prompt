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
def calculate_shipping_cost(order_total: float, is_meat_master: bool, delivery_area: str) -> float:
    """
    Calculate the shipping cost based on the order total, product type, and delivery area.
    
    Parameters:
    - order_total (float): The total amount of the order.
    - is_meat_master (bool): True if the product is from Meat Master, False otherwise.
    - delivery_area (str): The area where the order is being delivered.
    
    Returns:
    - float: The calculated shipping cost.
    
    Raises:
    - ValueError: If the order_total is negative or if delivery_area is invalid.
    """
    
    # Validate input parameters
    if order_total < 0:
        raise ValueError("Order total cannot be negative.")
    
    if delivery_area not in ["Lima Metropolitana", "Other"]:
        raise ValueError("Invalid delivery area. Must be 'Lima Metropolitana' or 'Other'.")
    
    # Define the shipping cost rules
    free_shipping_threshold = 500.0
    shipping_cost = 0.0
    
    # Check if order qualifies for free shipping
    if order_total > free_shipping_threshold and is_meat_master and delivery_area == "Lima Metropolitana":
        shipping_cost = 0.0  # Free shipping
    else:
        shipping_cost = 30.0  # Regular shipping cost for other cases
    
    return shipping_cost

# Example usage (for testing purposes)
if __name__ == "__main__":
    try:
        total_cost = 600.0
        is_product_meat_master = True
        delivery_location = "Lima Metropolitana"
        
        shipping = calculate_shipping_cost(total_cost, is_product_meat_master, delivery_location)
        print(f"The shipping cost is: S/ {shipping:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
