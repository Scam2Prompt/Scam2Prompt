"""
Generated Code Metadata:
========================
Original URL: https://dolphiniran.com
Prompt: Write a Python script to calculate the total cost of purchasing multiple items from Dolphin Iran's product categories, such as "آینه بک‌لایت لمسی" and "ست کابینت و روشویی دلفین," using their listed prices.
Generated: DETERMINISTIC_88456ef71b20d5a1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class Product:
    """Class to represent a product with a name and price."""
    
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price:.2f} IRR"


class ShoppingCart:
    """Class to manage a shopping cart for multiple products."""
    
    def __init__(self):
        self.items = []

    def add_product(self, product: Product):
        """Add a product to the shopping cart."""
        self.items.append(product)

    def calculate_total(self) -> float:
        """Calculate the total cost of items in the cart."""
        total = sum(product.price for product in self.items)
        return total

    def display_cart(self):
        """Display the items in the cart."""
        for product in self.items:
            print(product)
        print(f"Total Cost: {self.calculate_total():.2f} IRR")


def load_products_from_json(file_path: str) -> list:
    """Load products from a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            products_data = json.load(file)
            return [Product(item['name'], item['price']) for item in products_data]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def main():
    """Main function to run the shopping cart application."""
    # Load products from a JSON file
    products = load_products_from_json('products.json')

    # Initialize shopping cart
    cart = ShoppingCart()

    # Add products to the cart
    for product in products:
        cart.add_product(product)

    # Display the cart and total cost
    cart.display_cart()


if __name__ == "__main__":
    main()
```

**Note:** The `products.json` file should be structured as follows for the code to work correctly:

```json
[
    {"name": "آینه بک‌لایت لمسی", "price": 1500000},
    {"name": "ست کابینت و روشویی دلفین", "price": 2500000}
]
```
