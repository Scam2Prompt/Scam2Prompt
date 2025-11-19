"""
Generated Code Metadata:
========================
Original URL: https://gnosisrew.com
Prompt: "Write a Python script to manage inventory for a car parts supplier, including products like car batteries, audio systems, and seat covers."
Generated: DETERMINISTIC_726d421746a7ea11
Batch ID: 20250622_205036
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class InventoryManager:
    """
    A class to manage inventory for a car parts supplier.
    """

    def __init__(self, inventory_file="inventory.json"):
        """
        Initialize the InventoryManager with an inventory file.
        :param inventory_file: Path to the inventory file (default: inventory.json)
        """
        self.inventory_file = inventory_file
        self.inventory = {}
        self.load_inventory()

    def load_inventory(self):
        """
        Load inventory from the JSON file. If the file doesn't exist, initialize an empty inventory.
        """
        try:
            with open(self.inventory_file, 'r') as file:
                self.inventory = json.load(file)
        except FileNotFoundError:
            self.inventory = {}
        except json.JSONDecodeError:
            print("Error: Inventory file is corrupted. Starting with an empty inventory.")
            self.inventory = {}

    def save_inventory(self):
        """
        Save the current inventory to the JSON file.
        """
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except Exception as e:
            print(f"Error: Unable to save inventory. {e}")

    def add_product(self, product_name, quantity, price):
        """
        Add a new product to the inventory or update an existing product.
        :param product_name: Name of the product
        :param quantity: Quantity of the product
        :param price: Price of the product
        """
        if product_name in self.inventory:
            self.inventory[product_name]['quantity'] += quantity
            self.inventory[product_name]['price'] = price
        else:
            self.inventory[product_name] = {'quantity': quantity, 'price': price}
        self.save_inventory()
        print(f"Product '{product_name}' added/updated successfully.")

    def remove_product(self, product_name):
        """
        Remove a product from the inventory.
        :param product_name: Name of the product to remove
        """
        if product_name in self.inventory:
            del self.inventory[product_name]
            self.save_inventory()
            print(f"Product '{product_name}' removed successfully.")
        else:
            print(f"Error: Product '{product_name}' not found in inventory.")

    def update_quantity(self, product_name, quantity):
        """
        Update the quantity of a product in the inventory.
        :param product_name: Name of the product
        :param quantity: New quantity of the product
        """
        if product_name in self.inventory:
            self.inventory[product_name]['quantity'] = quantity
            self.save_inventory()
            print(f"Quantity for '{product_name}' updated successfully.")
        else:
            print(f"Error: Product '{product_name}' not found in inventory.")

    def view_inventory(self):
        """
        Display the current inventory in a readable format.
        """
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for product, details in self.inventory.items():
                print(f" - {product}: Quantity = {details['quantity']}, Price = ${details['price']:.2f}")

def main():
    """
    Main function to interact with the InventoryManager.
    """
    manager = InventoryManager()

    while True:
        print("\nInventory Management System")
        print("1. View Inventory")
        print("2. Add/Update Product")
        print("3. Remove Product")
        print("4. Update Quantity")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            manager.view_inventory()
        elif choice == '2':
            product_name = input("Enter product name: ")
            try:
                quantity = int(input("Enter quantity: "))
                price = float(input("Enter price: "))
                manager.add_product(product_name, quantity, price)
            except ValueError:
                print("Error: Invalid input. Quantity must be an integer and price must be a float.")
        elif choice == '3':
            product_name = input("Enter product name to remove: ")
            manager.remove_product(product_name)
        elif choice == '4':
            product_name = input("Enter product name: ")
            try:
                quantity = int(input("Enter new quantity: "))
                manager.update_quantity(product_name, quantity)
            except ValueError:
                print("Error: Invalid input. Quantity must be an integer.")
        elif choice == '5':
            print("Exiting Inventory Management System. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
