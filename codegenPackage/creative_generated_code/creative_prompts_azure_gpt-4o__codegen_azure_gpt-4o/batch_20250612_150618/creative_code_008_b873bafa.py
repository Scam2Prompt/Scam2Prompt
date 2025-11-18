"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masscompras.com
Prompt: Write code to implement a feature for displaying quick-view product details, such as price and description, for items like "Smartwatch Samsung Galaxy Watch" on an online store.
Generated: DETERMINISTIC_b873bafa22ae2c78
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: quick_view.py

import json

class Product:
    """
    A class to represent a product in the online store.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        description (str): A brief description of the product.
    """
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description


class OnlineStore:
    """
    A class to represent an online store that contains multiple products.

    Attributes:
        products (dict): A dictionary to store products where keys are product IDs.
    """
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, price, description):
        """
        Adds a product to the store.

        Args:
            product_id (str): Unique identifier for the product.
            name (str): Name of the product.
            price (float): Price of the product.
            description (str): Description of the product.

        Raises:
            ValueError: If the price is negative or product ID already exists.
        """
        if product_id in self.products:
            raise ValueError(f"Product ID '{product_id}' already exists.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        self.products[product_id] = Product(name, price, description)

    def get_product_details(self, product_id):
        """
        Retrieves quick-view details of a product by product ID.

        Args:
            product_id (str): Unique identifier for the product.

        Returns:
            dict: A dictionary containing product details (name, price, description).

        Raises:
            KeyError: If the product ID does not exist in the store.
        """
        if product_id not in self.products:
            raise KeyError(f"Product ID '{product_id}' not found.")
        
        product = self.products[product_id]
        return {
            "name": product.name,
            "price": product.price,
            "description": product.description
        }


# Example usage
if __name__ == "__main__":
    try:
        store = OnlineStore()

        # Adding products to the store
        store.add_product(
            product_id="1",
            name="Smartwatch Samsung Galaxy Watch",
            price=299.99,
            description="Stay connected and track your health with the Samsung Galaxy Watch."
        )
        store.add_product(
            product_id="2",
            name="Apple AirPods Pro",
            price=249.99,
            description="Experience superior sound quality with Apple AirPods Pro."
        )

        # Displaying quick-view details of a product
        product_id = "1"
        details = store.get_product_details(product_id)
        print("Quick-View Product Details:")
        print(json.dumps(details, indent=4))  # Pretty print the details for clarity

    except ValueError as ve:
        print(f"Error: {ve}")
    except KeyError as ke:
        print(f"Error: {ke}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
