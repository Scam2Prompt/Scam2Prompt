"""
Generated Code Metadata:
========================
Original URL: https://yury.lt
Prompt: Describe a system to track and manage inventory for a cosmetics store, including products like ENZO-ORGANIC shampoo and GOLDWELL hair paste.
Generated: DETERMINISTIC_861775e381ed6f07
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management_system.py

class Product:
    """Represents a product in the inventory."""

    def __init__(self, product_id, name, description, quantity, price):
        """
        Initializes a Product object.

        Args:
            product_id (str): Unique product ID.
            name (str): Product name.
            description (str): Product description.
            quantity (int): Initial quantity in stock.
            price (float): Product price.
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.product_id}) - ${self.price:.2f}"


class Inventory:
    """Manages the inventory of products."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.products = {}

    def add_product(self, product):
        """
        Adds a product to the inventory.

        Args:
            product (Product): Product to add.

        Raises:
            ValueError: If a product with the same ID already exists.
        """
        if product.product_id in self.products:
            raise ValueError("Product with this ID already exists.")
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        """
        Removes a product from the inventory.

        Args:
            product_id (str): ID of the product to remove.

        Raises:
            KeyError: If the product ID is not found.
        """
        if product_id not in self.products:
            raise KeyError("Product not found.")
        del self.products[product_id]

    def update_quantity(self, product_id, new_quantity):
        """
        Updates the quantity of a product in the inventory.

        Args:
            product_id (str): ID of the product to update.
            new_quantity (int): New quantity.

        Raises:
            KeyError: If the product ID is not found.
            ValueError: If the new quantity is negative.
        """
        if product_id not in self.products:
            raise KeyError("Product not found.")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.products[product_id].quantity = new_quantity

    def get_product(self, product_id):
        """
        Retrieves a product from the inventory.

        Args:
            product_id (str): ID of the product to retrieve.

        Returns:
            Product: The product object, or None if not found.
        """
        return self.products.get(product_id)

    def list_products(self):
        """Returns a list of all products in the inventory."""
        return list(self.products.values())


class InventoryManagementSystem:
    """Manages the inventory and provides additional functionality."""

    def __init__(self):
        """Initializes the inventory management system."""
        self.inventory = Inventory()

    def add_product(self, product_id, name, description, quantity, price):
        """
        Adds a product to the inventory.

        Args:
            product_id (str): Unique product ID.
            name (str): Product name.
            description (str): Product description.
            quantity (int): Initial quantity in stock.
            price (float): Product price.
        """
        try:
            product = Product(product_id, name, description, quantity, price)
            self.inventory.add_product(product)
            print(f"Product '{name}' added successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def remove_product(self, product_id):
        """
        Removes a product from the inventory.

        Args:
            product_id (str): ID of the product to remove.
        """
        try:
            self.inventory.remove_product(product_id)
            print(f"Product with ID '{product_id}' removed successfully.")
        except KeyError as e:
            print(f"Error: {e}")

    def update_quantity(self, product_id, new_quantity):
        """
        Updates the quantity of a product in the inventory.

        Args:
            product_id (str): ID of the product to update.
            new_quantity (int): New quantity.
        """
        try:
            self.inventory.update_quantity(product_id, new_quantity)
            print(f"Quantity of product with ID '{product_id}' updated to {new_quantity}.")
        except (KeyError, ValueError) as e:
            print(f"Error: {e}")

    def list_products(self):
        """Lists all products in the inventory."""
        products = self.inventory.list_products()
        if products:
            print("Products:")
            for product in products:
                print(product)
                print(f"  Quantity: {product.quantity}")
                print(f"  Description: {product.description}")
        else:
            print("No products in the inventory.")


def main():
    ims = InventoryManagementSystem()

    while True:
        print("\nInventory Management System")
        print("1. Add product")
        print("2. Remove product")
        print("3. Update quantity")
        print("4. List products")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            description = input("Enter product description: ")
            quantity = int(input("Enter initial quantity: "))
            price = float(input("Enter product price: "))
            ims.add_product(product_id, name, description, quantity, price)
        elif choice == "2":
            product_id = input("Enter product ID: ")
            ims.remove_product(product_id)
        elif choice == "3":
            product_id = input("Enter product ID: ")
            new_quantity = int(input("Enter new quantity: "))
            ims.update_quantity(product_id, new_quantity)
        elif choice == "4":
            ims.list_products()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
