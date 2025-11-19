"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://watpac.in
Prompt: Write a Python function that calculates the total cost of purchasing various Watpac waterproofing chemicals, including GST for products like cement additives and water sealers.
Generated: DETERMINISTIC_017d524420d123d5
Batch ID: 20250612_162051
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

def calculate_total_cost(products: List[Dict[str, float]], gst_rate: float = 0.1) -> float:
    """
    Calculates the total cost of purchasing Watpac waterproofing chemicals including GST.

    Args:
        products (List[Dict[str, float]]): A list of dictionaries where each dictionary represents a product.
            Each product should have the following keys:
                - 'name' (str): Name of the product.
                - 'price' (float): Price of the product excluding GST.
                - 'quantity' (float): Quantity of the product being purchased.
        gst_rate (float): The GST rate as a decimal. Default is 0.1 (10%).

    Returns:
        float: The total cost including GST.

    Raises:
        ValueError: If any product price or quantity is negative.
    """
    total_cost_excl_gst = 0.0

    for product in products:
        price = product.get("price", 0.0)
        quantity = product.get("quantity", 0.0)

        # Input validation
        if price < 0 or quantity < 0:
            raise ValueError(f"Invalid product data: price and quantity must be non-negative. Found: {product}")

        # Add the cost of the current product to the total cost
        total_cost_excl_gst += price * quantity

    # Calculate GST
    gst_amount = total_cost_excl_gst * gst_rate

    # Calculate total cost including GST
    total_cost_incl_gst = total_cost_excl_gst + gst_amount

    return round(total_cost_incl_gst, 2)

# Example Usage
if __name__ == "__main__":
    # List of products
    products = [
        {"name": "Cement Additive", "price": 25.00, "quantity": 3},
        {"name": "Water Sealer", "price": 15.50, "quantity": 2},
    ]

    try:
        total_cost = calculate_total_cost(products)
        print(f"Total cost including GST: ${total_cost}")
    except ValueError as e:
        print(f"Error: {e}")
```
