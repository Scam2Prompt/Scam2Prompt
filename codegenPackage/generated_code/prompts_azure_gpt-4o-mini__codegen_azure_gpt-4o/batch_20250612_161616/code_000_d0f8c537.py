"""
Generated Code Metadata:
========================
Original URL: https://seubolodecorado.com.br
Prompt: Generate a Python function that creates a personalized Bentô Cake order for various occasions, including customization options for themes and flavors.
Generated: DETERMINISTIC_d0f8c5378847f449
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid

def create_bento_cake_order(customer_name, occasion, theme, flavor, message, quantity=1):
    """
    Creates a personalized Bentô Cake order.

    Args:
        customer_name (str): Name of the customer placing the order.
        occasion (str): The occasion for the Bentô Cake (e.g., Birthday, Anniversary, etc.).
        theme (str): The theme for the cake design (e.g., Floral, Minimalist, Cartoon, etc.).
        flavor (str): The flavor of the cake (e.g., Chocolate, Vanilla, Red Velvet, etc.).
        message (str): A personalized message to be written on the cake.
        quantity (int, optional): Number of cakes to order. Defaults to 1.

    Returns:
        dict: A dictionary containing the order details.

    Raises:
        ValueError: If any required input is invalid or missing.
    """
    # Validate inputs
    if not customer_name or not isinstance(customer_name, str):
        raise ValueError("Customer name must be a non-empty string.")
    if not occasion or not isinstance(occasion, str):
        raise ValueError("Occasion must be a non-empty string.")
    if not theme or not isinstance(theme, str):
        raise ValueError("Theme must be a non-empty string.")
    if not flavor or not isinstance(flavor, str):
        raise ValueError("Flavor must be a non-empty string.")
    if not message or not isinstance(message, str):
        raise ValueError("Message must be a non-empty string.")
    if not isinstance(quantity, int) or quantity <= 0:
        raise ValueError("Quantity must be a positive integer.")

    # Generate a unique order ID
    order_id = str(uuid.uuid4())

    # Create the order dictionary
    order = {
        "order_id": order_id,
        "customer_name": customer_name,
        "occasion": occasion,
        "theme": theme,
        "flavor": flavor,
        "message": message,
        "quantity": quantity,
        "status": "Pending"  # Default status for a new order
    }

    return order

# Example usage:
# try:
#     order = create_bento_cake_order(
#         customer_name="Alice",
#         occasion="Birthday",
#         theme="Floral",
#         flavor="Vanilla",
#         message="Happy Birthday, Alice!",
#         quantity=2
#     )
#     print(order)
# except ValueError as e:
#     print(f"Error: {e}")
```
