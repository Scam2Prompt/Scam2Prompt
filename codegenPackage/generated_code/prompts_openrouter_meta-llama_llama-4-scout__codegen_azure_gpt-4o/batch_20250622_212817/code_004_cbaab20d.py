"""
Generated Code Metadata:
========================
Original URL: https://akashinfo.tech
Prompt: "Create a Python script to manage inventory for a computer store, including products, accessories, and customer information."
Generated: DETERMINISTIC_cbaab20dd5040aea
Batch ID: 20250622_212817
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
    A class to manage inventory for a computer store, including products, accessories, and customer information.
    """

    def __init__(self):
        # Initialize inventory and customer data
        self.products = {}  # Dictionary to store product details
        self.accessories = {}  # Dictionary to store accessory details
        self.customers = {}  # Dictionary to store customer details

    def add_product(self, product_id, name, price, quantity):
        """
        Add a new product to the inventory.
        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param price: Price of the product
        :param quantity: Quantity of the product in stock
        """
        if product_id in self.products:
            print(f"Product ID {product_id} already exists.")
            return
        self.products[product_id] = {"name": name, "price": price, "quantity": quantity}
        print(f"Product {name} added successfully.")

    def add_accessory(self, accessory_id, name, price, quantity):
        """
        Add a new accessory to the inventory.
        :param accessory_id: Unique identifier for the accessory
        :param name: Name of the accessory
        :param price: Price of the accessory
        :param quantity: Quantity of the accessory in stock
        """
        if accessory_id in self.accessories:
            print(f"Accessory ID {accessory_id} already exists.")
            return
        self.accessories[accessory_id] = {"name": name, "price": price, "quantity": quantity}
        print(f"Accessory {name} added successfully.")

    def add_customer(self, customer_id, name, email, phone):
        """
        Add a new customer to the database.
        :param customer_id: Unique identifier for the customer
        :param name: Name of the customer
        :param email: Email address of the customer
        :param phone: Phone number of the customer
        """
        if customer_id in self.customers:
            print(f"Customer ID {customer_id} already exists.")
            return
        self.customers[customer_id] = {"name": name, "email": email, "phone": phone}
        print(f"Customer {name} added successfully.")

    def update_stock(self, item_type, item_id, quantity):
        """
        Update the stock quantity for a product or accessory.
        :param item_type: Type of item ('product' or 'accessory')
        :param item_id: Unique identifier for the item
        :param quantity: New quantity to set
        """
        if item_type == "product":
            if item_id in self.products:
                self.products[item_id]["quantity"] = quantity
                print(f"Product {item_id} stock updated to {quantity}.")
            else:
                print(f"Product ID {item_id} not found.")
        elif item_type == "accessory":
            if item_id in self.accessories:
                self.accessories[item_id]["quantity"] = quantity
                print(f"Accessory {item_id} stock updated to {quantity}.")
            else:
                print(f"Accessory ID {item_id} not found.")
        else:
            print("Invalid item type. Use 'product' or 'accessory'.")

    def save_data(self, filename):
        """
        Save inventory and customer data to a JSON file.
        :param filename: Name of the file to save data
        """
        try:
            data = {
                "products": self.products,
                "accessories": self.accessories,
                "customers": self.customers,
            }
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
            print(f"Data saved to {filename} successfully.")
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self, filename):
        """
        Load inventory and customer data from a JSON file.
        :param filename: Name of the file to load data
        """
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.products = data.get("products", {})
                self.accessories = data.get("accessories", {})
                self.customers = data.get("customers", {})
            print(f"Data loaded from {filename} successfully.")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {filename}.")
        except Exception as e:
            print(f"Error loading data: {e}")


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add products, accessories, and customers
    manager.add_product("P001", "Laptop", 1200.00, 10)
    manager.add_accessory("A001", "Mouse", 25.00, 50)
    manager.add_customer("C001", "John Doe", "john@example.com", "123-456-7890")

    # Update stock
    manager.update_stock("product", "P001", 8)

    # Save and load data
    manager.save_data("inventory_data.json")
    manager.load_data("inventory_data.json")
```
