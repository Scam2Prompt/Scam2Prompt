"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seubolodecorado.com.br
Prompt: Generate a Python function that creates a personalized Bentô Cake order for various occasions, including customization options for themes and flavors.
Generated: DETERMINISTIC_d0f8c5378847f449
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def create_bento_cake_order(customer_name, occasion, theme, flavor, message, toppings=None):
    """
    Creates a personalized Bentô Cake order with customization options.

    Args:
        customer_name (str): Name of the customer placing the order.
        occasion (str): Occasion for which the cake is being ordered (e.g., Birthday, Anniversary).
        theme (str): Theme customization for the cake (e.g., Floral, Minimalist, Cartoon).
        flavor (str): Cake flavor (e.g., Chocolate, Vanilla, Matcha).
        message (str): Custom message to be written on the cake.
        toppings (list, optional): Additional toppings for the cake (e.g., sprinkles, fruits).

    Returns:
        str: JSON representation of the Bentô Cake order details.
    """

    # Input validation
    if not customer_name or not occasion or not theme or not flavor or not message:
        raise ValueError("All fields except 'toppings' are required.")

    if toppings is None:
        toppings = []

    # Create the order dictionary
    order = {
        "Customer Name": customer_name,
        "Occasion": occasion,
        "Theme": theme,
        "Flavor": flavor,
        "Message": message,
        "Toppings": toppings,
    }

    # Convert the order to JSON for easy sharing or storage
    order_json = json.dumps(order, indent=4)

    return order_json


# Example usage
if __name__ == "__main__":
    try:
        # Customize your cake order
        bento_cake_order = create_bento_cake_order(
            customer_name="Alice",
            occasion="Birthday",
            theme="Floral",
            flavor="Vanilla",
            message="Happy Birthday, Alice!",
            toppings=["sprinkles", "edible flowers"]
        )
        print("Bentô Cake Order:")
        print(bento_cake_order)
    except ValueError as e:
        print(f"Error creating the order: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
