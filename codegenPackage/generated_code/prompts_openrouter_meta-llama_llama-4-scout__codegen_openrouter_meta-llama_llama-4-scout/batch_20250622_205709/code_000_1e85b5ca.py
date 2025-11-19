"""
Generated Code Metadata:
========================
Original URL: https://tanhungco.vn
Prompt: "Write a Python script to manage inventory for a company like Tấn Hưng Việt Nam that sells agricultural products, including pesticides and fertilizers."
Generated: DETERMINISTIC_1e85b5ca337183d0
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

class Product:
    """Represents an agricultural product."""

    def __init__(self, product_id, name, quantity, price):
        """
        Initializes a Product.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            quantity (int): Initial quantity in stock.
            price (float): Product price.
        """
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"Product {self.product_id}: {self.name}, Quantity: {self.quantity}, Price: {self.price}"


class Inventory:
    """Manages inventory for agricultural products."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.products = {}

    def add_product(self, product):
        """
        Adds a product to the inventory.

        Args:
            product (Product): Product to add.

        Raises:
            ValueError: If product ID already exists.
        """
        if product.product_id in self.products:
            raise ValueError("Product ID already exists")
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        """
        Removes a product from the inventory.

        Args:
            product_id (int): ID of product to remove.

        Raises:
            KeyError: If product ID does not exist.
        """
        if product_id not in self.products:
            raise KeyError("Product ID does not exist")
        del self.products[product_id]

    def update_quantity(self, product_id, new_quantity):
        """
        Updates the quantity of a product.

        Args:
            product_id (int): ID of product to update.
            new_quantity (int): New quantity.

        Raises:
            KeyError: If product ID does not exist.
        """
        if product_id not in self.products:
            raise KeyError("Product ID does not exist")
        self.products[product_id].quantity = new_quantity

    def get_product(self, product_id):
        """
        Retrieves a product by ID.

        Args:
            product_id (int): ID of product to retrieve.

        Returns:
            Product: Product with matching ID, or None if not found.
        """
        return self.products.get(product_id)

    def list_products(self):
        """Returns a list of all products in the inventory."""
        return list(self.products.values())


def main():
    # Create an inventory
    inventory = Inventory()

    while True:
        print("\nInventory Management Menu:")
        print("1. Add product")
        print("2. Remove product")
        print("3. Update quantity")
        print("4. Get product")
        print("5. List products")
        print("6. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                product_id = int(input("Enter product ID: "))
                name = input("Enter product name: ")
                quantity = int(input("Enter initial quantity: "))
                price = float(input("Enter product price: "))
                product = Product(product_id, name, quantity, price)
                inventory.add_product(product)
                print(f"Added product: {product}")
            elif choice == "2":
                product_id = int(input("Enter product ID to remove: "))
                inventory.remove_product(product_id)
                print(f"Removed product with ID {product_id}")
            elif choice == "3":
                product_id = int(input("Enter product ID to update: "))
                new_quantity = int(input("Enter new quantity: "))
                inventory.update_quantity(product_id, new_quantity)
                print(f"Updated quantity for product {product_id}")
            elif choice == "4":
                product_id = int(input("Enter product ID to retrieve: "))
                product = inventory.get_product(product_id)
                if product:
                    print(product)
                else:
                    print(f"No product found with ID {product_id}")
            elif choice == "5":
                products = inventory.list_products()
                for product in products:
                    print(product)
            elif choice == "6":
                break
            else:
                print("Invalid option. Please choose again.")
        except (ValueError, KeyError) as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
