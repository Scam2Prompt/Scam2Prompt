"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://curaheridas.com
Prompt: Provide Python code to calculate shipping costs for an online store offering free shipping for orders above $1,999 MXN, with products like "Ceraplus Ostomy Barriers".
Generated: DETERMINISTIC_6f34ea2482da9f3a
Batch ID: 20250612_152426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shipping_cost_calculator.py

# Constants
FREE_SHIPPING_THRESHOLD = 1999.00  # MXN
SHIPPING_COST = 150.00  # Fixed shipping cost in MXN

# Function to calculate shipping cost
def calculate_shipping_cost(order_total: float) -> float:
    """
    Calculate the shipping cost for an online store based on the order total.

    :param order_total: The total amount of the order in MXN.
    :return: The shipping cost in MXN. Returns 0 for free shipping.
    """
    try:
        # Validate the input
        if order_total < 0:
            raise ValueError("Order total cannot be negative.")

        # Determine if shipping is free
        if order_total >= FREE_SHIPPING_THRESHOLD:
            return 0.0  # Free shipping for orders above the threshold
        else:
            return SHIPPING_COST  # Fixed shipping cost for orders below the threshold
    except ValueError as ve:
        print(f"Error: {ve}")
        return -1  # Return a sentinel value for invalid input

# Main function to demonstrate functionality
if __name__ == "__main__":
    try:
        # Example product information
        product_name = "Ceraplus Ostomy Barriers"
        product_price = 500.00  # MXN
        product_quantity = 4
        
        # Calculate the total order amount
        order_total = product_price * product_quantity

        # Output product and order details
        print(f"Product: {product_name}")
        print(f"Price per unit: {product_price:.2f} MXN")
        print(f"Quantity: {product_quantity}")
        print(f"Order Total: {order_total:.2f} MXN")

        # Calculate the shipping cost
        shipping_cost = calculate_shipping_cost(order_total)

        # Print shipping cost
        if shipping_cost >= 0:
            print(f"Shipping cost: {shipping_cost:.2f} MXN")
        else:
            print("Failed to calculate shipping cost due to invalid input.")

    except Exception as e:
        # Catch any unforeseen errors
        print(f"An unexpected error occurred: {e}")
```
