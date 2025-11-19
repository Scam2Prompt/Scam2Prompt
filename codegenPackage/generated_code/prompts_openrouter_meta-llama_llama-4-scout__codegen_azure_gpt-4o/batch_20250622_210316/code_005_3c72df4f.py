"""
Generated Code Metadata:
========================
Original URL: https://aprisacv.com.mx
Prompt: "Write a code snippet in Python to calculate the total cost of refractory products for a specific industrial application, considering factors like product quantity, unit price, and taxes."
Generated: DETERMINISTIC_3c72df4fb2c18bd6
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import sys

def calculate_total_cost(product_details, tax_rate):
    """
    Calculate the total cost of refractory products including taxes.

    Args:
        product_details (list of dict): A list of dictionaries where each dictionary contains:
            - 'product_name' (str): Name of the product.
            - 'quantity' (int): Quantity of the product.
            - 'unit_price' (float): Unit price of the product.
        tax_rate (float): Tax rate as a percentage (e.g., 10 for 10%).

    Returns:
        float: Total cost including taxes.
    """
    try:
        # Validate input
        if not isinstance(product_details, list) or not all(isinstance(item, dict) for item in product_details):
            raise ValueError("Invalid product details format. Expected a list of dictionaries.")
        if not isinstance(tax_rate, (int, float)) or tax_rate < 0:
            raise ValueError("Invalid tax rate. Must be a non-negative number.")

        # Calculate subtotal
        subtotal = 0
        for product in product_details:
            # Extract product details
            product_name = product.get('product_name', 'Unknown Product')
            quantity = product.get('quantity', 0)
            unit_price = product.get('unit_price', 0.0)

            # Validate product details
            if not isinstance(quantity, int) or quantity < 0:
                raise ValueError(f"Invalid quantity for {product_name}. Must be a non-negative integer.")
            if not isinstance(unit_price, (int, float)) or unit_price < 0:
                raise ValueError(f"Invalid unit price for {product_name}. Must be a non-negative number.")

            # Calculate cost for the product
            product_cost = quantity * unit_price
            subtotal += product_cost

        # Calculate total cost including taxes
        tax_amount = (tax_rate / 100) * subtotal
        total_cost = subtotal + tax_amount

        return total_cost

    except Exception as e:
        # Handle unexpected errors
        print(f"Error: {e}", file=sys.stderr)
        return None


# Example usage
if __name__ == "__main__":
    # Define product details
    products = [
        {"product_name": "Firebrick", "quantity": 100, "unit_price": 2.5},
        {"product_name": "Ceramic Fiber Blanket", "quantity": 50, "unit_price": 10.0},
        {"product_name": "Castable Refractory", "quantity": 20, "unit_price": 15.0}
    ]

    # Define tax rate
    tax_rate = 8.0  # 8%

    # Calculate total cost
    total_cost = calculate_total_cost(products, tax_rate)

    if total_cost is not None:
        print(f"Total cost including taxes: ${total_cost:.2f}")
```
