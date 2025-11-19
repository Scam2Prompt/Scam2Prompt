"""
Generated Code Metadata:
========================
Original URL: https://elfworldvape.com
Prompt: Write a Python code to manage wholesale orders for Elfworld Vape products, including PB45000 and AI22000 devices.
Generated: DETERMINISTIC_f9589ab465ff5a7d
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class WholesaleOrderManager:
    """
    A class to manage wholesale orders for Elfworld Vape products.
    """

    def __init__(self):
        """
        Initializes the order manager with an empty order list.
        """
        self.orders = []

    def add_order(self, customer_name, product, quantity):
        """
        Adds a new order to the order list.

        Args:
            customer_name (str): Name of the customer placing the order.
            product (str): Product name (PB45000 or AI22000).
            quantity (int): Quantity of the product ordered.

        Raises:
            ValueError: If the product name is invalid or quantity is non-positive.
        """
        if product not in ["PB45000", "AI22000"]:
            raise ValueError("Invalid product name. Valid products are 'PB45000' and 'AI22000'.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        order = {
            "customer_name": customer_name,
            "product": product,
            "quantity": quantity
        }
        self.orders.append(order)

    def view_orders(self):
        """
        Returns the list of all orders.

        Returns:
            list: A list of all orders.
        """
        return self.orders

    def save_orders_to_file(self, filename):
        """
        Saves the orders to a JSON file.

        Args:
            filename (str): Name of the file to save the orders.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.orders, file, indent=4)
        except IOError as e:
            print(f"Error saving orders to file: {e}")

    def load_orders_from_file(self, filename):
        """
        Loads orders from a JSON file.

        Args:
            filename (str): Name of the file to load the orders from.

        Raises:
            IOError: If there is an error reading the file.
        """
        try:
            with open(filename, 'r') as file:
                self.orders = json.load(file)
        except IOError as e:
            print(f"Error loading orders from file: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON data: {e}")

# Example usage
if __name__ == "__main__":
    manager = WholesaleOrderManager()

    # Adding orders
    try:
        manager.add_order("Alice", "PB45000", 10)
        manager.add_order("Bob", "AI22000", 5)
    except ValueError as e:
        print(f"Error adding order: {e}")

    # Viewing orders
    print("Current Orders:")
    print(manager.view_orders())

    # Saving orders to file
    manager.save_orders_to_file("orders.json")

    # Loading orders from file
    manager.load_orders_from_file("orders.json")
    print("Orders after loading from file:")
    print(manager.view_orders())
```
