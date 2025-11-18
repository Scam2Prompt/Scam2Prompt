"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dow.spb.ru
Prompt: Write code to simulate an inventory management system for a dealership that uses "Гарант" as a supplier for automotive glass adhesives and primers.
Generated: DETERMINISTIC_a328d6f4d26fc0b0
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class Product:
    """
    Represents a product in the inventory.
    """

    def __init__(self, product_id, name, supplier, stock, unit_price):
        """
        Initialize a product instance.
        :param product_id: Unique identifier for the product.
        :param name: Name of the product.
        :param supplier: Name of the supplier for the product.
        :param stock: Current stock level.
        :param unit_price: Price per unit of the product.
        """
        self.product_id = product_id
        self.name = name
        self.supplier = supplier
        self.stock = stock
        self.unit_price = unit_price

    def __str__(self):
        """
        Return a string representation of the product.
        """
        return f"Product ID: {self.product_id}, Name: {self.name}, Supplier: {self.supplier}, Stock: {self.stock}, Unit Price: ${self.unit_price:.2f}"


class Inventory:
    """
    Represents the inventory for the dealership.
    """

    def __init__(self):
        """
        Initialize an empty inventory.
        """
        self.products = {}

    def add_product(self, product):
        """
        Add a new product to the inventory.
        :param product: A Product instance to add.
        """
        if product.product_id in self.products:
            raise ValueError(f"Product ID {product.product_id} already exists in the inventory.")
        self.products[product.product_id] = product

    def update_stock(self, product_id, quantity):
        """
        Update the stock for a specific product.
        :param product_id: The ID of the product to update.
        :param quantity: The quantity to add (positive) or remove (negative) from the stock.
        """
        if product_id not in self.products:
            raise KeyError(f"Product ID {product_id} not found in the inventory.")
        if self.products[product_id].stock + quantity < 0:
            raise ValueError(f"Insufficient stock for Product ID {product_id}.")
        self.products[product_id].stock += quantity

    def get_product_info(self, product_id):
        """
        Retrieve information about a specific product.
        :param product_id: The ID of the product to query.
        :return: A string representation of the product.
        """
        if product_id not in self.products:
            raise KeyError(f"Product ID {product_id} not found in the inventory.")
        return str(self.products[product_id])

    def list_products(self):
        """
        List all products in the inventory.
        :return: A list of string representations of all products.
        """
        if not self.products:
            return ["No products in the inventory."]
        return [str(product) for product in self.products.values()]


class DealershipSimulation:
    """
    Simulates the dealership inventory management system.
    """

    def __init__(self, supplier_name):
        """
        Initialize the simulation with a supplier name.
        :param supplier_name: Name of the supplier (e.g., "Гарант").
        """
        self.inventory = Inventory()
        self.supplier_name = supplier_name

    def run(self):
        """
        Run the simulation.
        """
        print(f"Welcome to the Dealership Inventory Management System!")
        print(f"Supplier: {self.supplier_name}")

        while True:
            print("\nOptions:")
            print("1. Add product")
            print("2. Update stock")
            print("3. View product info")
            print("4. List all products")
            print("5. Exit")

            try:
                choice = int(input("Select an option (1-5): "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")
                continue

            if choice == 1:  # Add product
                try:
                    product_id = input("Enter Product ID: ")
                    name = input("Enter Product Name: ")
                    stock = int(input("Enter Stock Quantity: "))
                    unit_price = float(input("Enter Unit Price: "))
                    product = Product(product_id, name, self.supplier_name, stock, unit_price)
                    self.inventory.add_product(product)
                    print("Product added successfully!")
                except ValueError as ve:
                    print(f"Error: {ve}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")

            elif choice == 2:  # Update stock
                try:
                    product_id = input("Enter Product ID: ")
                    quantity = int(input("Enter Quantity to Add/Remove (negative to remove): "))
                    self.inventory.update_stock(product_id, quantity)
                    print("Stock updated successfully!")
                except KeyError as ke:
                    print(f"Error: {ke}")
                except ValueError as ve:
                    print(f"Error: {ve}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")

            elif choice == 3:  # View product info
                try:
                    product_id = input("Enter Product ID: ")
                    print(self.inventory.get_product_info(product_id))
                except KeyError as ke:
                    print(f"Error: {ke}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")

            elif choice == 4:  # List all products
                for product_info in self.inventory.list_products():
                    print(product_info)

            elif choice == 5:  # Exit
                print("Exiting the simulation. Goodbye!")
                break

            else:
                print("Invalid option. Please select a number between 1 and 5.")


if __name__ == "__main__":
    dealership_system = DealershipSimulation(supplier_name="Гарант")
    dealership_system.run()
```
