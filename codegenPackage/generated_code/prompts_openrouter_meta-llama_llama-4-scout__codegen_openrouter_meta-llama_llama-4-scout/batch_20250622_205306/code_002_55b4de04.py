"""
Generated Code Metadata:
========================
Original URL: https://tamstrucks.com
Prompt: Generate a code snippet for a basic warehouse management system that can be used by a company like TAMS TRUCKS.
Generated: DETERMINISTIC_55b4de04a09eb2c5
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# warehouse_management_system.py

class Product:
    """Represents a product in the warehouse."""

    def __init__(self, product_id, name, quantity, weight, dimensions):
        """
        Initializes a Product object.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            quantity (int): Product quantity.
            weight (float): Product weight in kg.
            dimensions (str): Product dimensions (e.g., "10x20x30").
        """
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.weight = weight
        self.dimensions = dimensions

    def __str__(self):
        return f"Product {self.product_id}: {self.name}, Quantity: {self.quantity}"


class Warehouse:
    """Represents a warehouse with products."""

    def __init__(self):
        """Initializes an empty warehouse."""
        self.products = {}

    def add_product(self, product):
        """
        Adds a product to the warehouse.

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
        Removes a product from the warehouse.

        Args:
            product_id (int): ID of product to remove.

        Raises:
            KeyError: If product ID does not exist.
        """
        if product_id not in self.products:
            raise KeyError("Product ID does not exist")
        del self.products[product_id]

    def update_product_quantity(self, product_id, new_quantity):
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
            Product: Product object or None if not found.
        """
        return self.products.get(product_id)

    def list_products(self):
        """Returns a list of all products in the warehouse."""
        return list(self.products.values())


class WarehouseManagementSystem:
    """Represents the warehouse management system."""

    def __init__(self):
        """Initializes the warehouse management system."""
        self.warehouse = Warehouse()

    def run(self):
        """Runs the warehouse management system."""
        while True:
            print("\nWarehouse Management System")
            print("1. Add Product")
            print("2. Remove Product")
            print("3. Update Product Quantity")
            print("4. Get Product")
            print("5. List Products")
            print("6. Exit")

            choice = input("Choose an option: ")

            try:
                if choice == "1":
                    self.add_product()
                elif choice == "2":
                    self.remove_product()
                elif choice == "3":
                    self.update_product_quantity()
                elif choice == "4":
                    self.get_product()
                elif choice == "5":
                    self.list_products()
                elif choice == "6":
                    break
                else:
                    print("Invalid option. Please choose a valid option.")
            except Exception as e:
                print(f"An error occurred: {e}")

    def add_product(self):
        """Adds a product to the warehouse."""
        product_id = int(input("Enter product ID: "))
        name = input("Enter product name: ")
        quantity = int(input("Enter product quantity: "))
        weight = float(input("Enter product weight (kg): "))
        dimensions = input("Enter product dimensions: ")

        product = Product(product_id, name, quantity, weight, dimensions)
        self.warehouse.add_product(product)
        print(f"Product {product_id} added successfully")

    def remove_product(self):
        """Removes a product from the warehouse."""
        product_id = int(input("Enter product ID: "))
        self.warehouse.remove_product(product_id)
        print(f"Product {product_id} removed successfully")

    def update_product_quantity(self):
        """Updates the quantity of a product."""
        product_id = int(input("Enter product ID: "))
        new_quantity = int(input("Enter new quantity: "))
        self.warehouse.update_product_quantity(product_id, new_quantity)
        print(f"Product {product_id} quantity updated successfully")

    def get_product(self):
        """Retrieves a product by ID."""
        product_id = int(input("Enter product ID: "))
        product = self.warehouse.get_product(product_id)
        if product:
            print(product)
            print(f"Weight: {product.weight} kg")
            print(f"Dimensions: {product.dimensions}")
        else:
            print("Product not found")

    def list_products(self):
        """Lists all products in the warehouse."""
        products = self.warehouse.list_products()
        for product in products:
            print(product)


if __name__ == "__main__":
    wms = WarehouseManagementSystem()
    wms.run()
```
