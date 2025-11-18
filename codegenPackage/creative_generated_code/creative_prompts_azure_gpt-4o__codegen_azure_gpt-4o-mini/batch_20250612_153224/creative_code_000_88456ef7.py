"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dolphiniran.com
Prompt: Write a Python script to calculate the total cost of purchasing multiple items from Dolphin Iran's product categories, such as "آینه بک‌لایت لمسی" and "ست کابینت و روشویی دلفین," using their listed prices.
Generated: DETERMINISTIC_88456ef71b20d5a1
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

class Product:
    """Class to represent a product with a name and price."""
    
    def __init__(self, name: str, price: float):
        """
        Initializes a Product instance.

        Parameters:
            name (str): The name of the product.
            price (float): The price of the product.
        """
        self.name = name
        self.price = price

class ShoppingCart:
    """Class to manage a shopping cart for purchasing products."""
    
    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = []

    def add_product(self, product: Product):
        """Adds a product to the shopping cart.

        Parameters:
            product (Product): The product to add.
        """
        self.items.append(product)

    def calculate_total(self) -> float:
        """Calculates the total cost of items in the cart.

        Returns:
            float: The total cost.
        """
        return sum(item.price for item in self.items)

def load_products_from_json(file_path: str) -> list:
    """Loads products from a JSON file.

    Parameters:
        file_path (str): The path to the JSON file.

    Returns:
        list: A list of Product instances.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file is not a valid JSON.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return [Product(name=item['name'], price=item['price']) for item in data['products']]
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' is not a valid JSON.")
        return []

def main():
    """Main function to execute the shopping cart functionality."""
    # Load products from a JSON file
    products = load_products_from_json('products.json')
    
    # Initialize shopping cart
    cart = ShoppingCart()

    # Example products to add to the cart
    product_names = ["آینه بک‌لایت لمسی", "ست کابینت و روشویی دلفین"]

    # Add matching products to the cart
    for product in products:
        if product.name in product_names:
            cart.add_product(product)

    # Calculate and display the total cost
    total_cost = cart.calculate_total()
    print(f"Total cost of selected products: {total_cost:.2f} تومان")

if __name__ == "__main__":
    main()
```

**Note:** Ensure you have a `products.json` file formatted similarly to this example:

```json
{
    "products": [
        {"name": "آینه بک‌لایت لمسی", "price": 1500000},
        {"name": "ست کابینت و روشویی دلفین", "price": 3000000},
        {"name": "Another Product", "price": 2000000}
    ]
}
```

This structure allows the script to load product data correctly.
