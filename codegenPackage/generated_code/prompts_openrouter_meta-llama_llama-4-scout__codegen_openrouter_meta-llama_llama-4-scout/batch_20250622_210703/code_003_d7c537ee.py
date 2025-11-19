"""
Generated Code Metadata:
========================
Original URL: https://marinekiosk.gr
Prompt: "Generate a Python code snippet to manage the inventory of products for a cannabis store like Marine Kiosk, including product name, type, quantity, and price."
Generated: DETERMINISTIC_d7c537eee9c67ef1
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class Product:
    """Represents a cannabis product."""

    def __init__(self, name: str, product_type: str, quantity: int, price: float):
        """
        Initializes a Product.

        Args:
            name (str): Product name.
            product_type (str): Product type (e.g., flower, edible, vape).
            quantity (int): Product quantity in stock.
            price (float): Product price.
        """
        self.name = name
        self.product_type = product_type
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f"Product('{self.name}', '{self.product_type}', {self.quantity}, {self.price})"


class Inventory:
    """Manages the inventory of cannabis products."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.products = {}

    def add_product(self, product: Product):
        """
        Adds a product to the inventory.

        Args:
            product (Product): Product to add.

        Raises:
            ValueError: If a product with the same name already exists.
        """
        if product.name in self.products:
            raise ValueError(f"Product '{product.name}' already exists in the inventory.")
        self.products[product.name] = product

    def remove_product(self, name: str):
        """
        Removes a product from the inventory.

        Args:
            name (str): Name of the product to remove.

        Raises:
            KeyError: If the product does not exist in the inventory.
        """
        if name not in self.products:
            raise KeyError(f"Product '{name}' does not exist in the inventory.")
        del self.products[name]

    def update_quantity(self, name: str, new_quantity: int):
        """
        Updates the quantity of a product in the inventory.

        Args:
            name (str): Name of the product to update.
            new_quantity (int): New quantity.

        Raises:
            KeyError: If the product does not exist in the inventory.
            ValueError: If the new quantity is negative.
        """
        if name not in self.products:
            raise KeyError(f"Product '{name}' does not exist in the inventory.")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.products[name].quantity = new_quantity

    def update_price(self, name: str, new_price: float):
        """
        Updates the price of a product in the inventory.

        Args:
            name (str): Name of the product to update.
            new_price (float): New price.

        Raises:
            KeyError: If the product does not exist in the inventory.
            ValueError: If the new price is negative.
        """
        if name not in self.products:
            raise KeyError(f"Product '{name}' does not exist in the inventory.")
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        self.products[name].price = new_price

    def get_product(self, name: str) -> Product:
        """
        Retrieves a product from the inventory.

        Args:
            name (str): Name of the product to retrieve.

        Returns:
            Product: The product if found.

        Raises:
            KeyError: If the product does not exist in the inventory.
        """
        if name not in self.products:
            raise KeyError(f"Product '{name}' does not exist in the inventory.")
        return self.products[name]

    def list_products(self):
        """Lists all products in the inventory."""
        return list(self.products.values())


def main():
    # Example usage
    inventory = Inventory()

    try:
        # Create products
        product1 = Product("Strawberry Cough", "flower", 100, 10.99)
        product2 = Product("Sour Diesel", "flower", 50, 9.99)

        # Add products to inventory
        inventory.add_product(product1)
        inventory.add_product(product2)

        # List products
        print("Products:")
        for product in inventory.list_products():
            print(product)

        # Update quantity and price
        inventory.update_quantity("Strawberry Cough", 80)
        inventory.update_price("Sour Diesel", 10.49)

        # Retrieve product
        print("\nUpdated Product:")
        print(inventory.get_product("Strawberry Cough"))

        # Remove product
        inventory.remove_product("Sour Diesel")

        # List products again
        print("\nProducts after removal:")
        for product in inventory.list_products():
            print(product)

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
