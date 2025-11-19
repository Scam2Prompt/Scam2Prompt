"""
Generated Code Metadata:
========================
Original URL: https://aceitescondadoloma.com
Prompt: Write a Python script to manage olive oil export orders, including customer information, order quantities, and international shipping logistics, considering the steps outlined by Aceites Condado Loma for exporting olive oil.
Generated: DETERMINISTIC_7dfdf64ddec5ac86
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime

class OliveOilExportManager:
    """
    A class to manage olive oil export orders, including customer information,
    order quantities, and international shipping logistics.
    """

    def __init__(self):
        # Initialize an empty list to store orders
        self.orders = []

    def add_order(self, customer_name, customer_address, order_quantity, destination_country):
        """
        Add a new export order.

        Args:
            customer_name (str): Name of the customer.
            customer_address (str): Address of the customer.
            order_quantity (float): Quantity of olive oil in liters.
            destination_country (str): Destination country for shipping.

        Returns:
            dict: The newly created order.
        """
        try:
            # Validate input
            if order_quantity <= 0:
                raise ValueError("Order quantity must be greater than zero.")

            # Create a new order
            order = {
                "order_id": len(self.orders) + 1,
                "customer_name": customer_name,
                "customer_address": customer_address,
                "order_quantity": order_quantity,
                "destination_country": destination_country,
                "order_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "status": "Pending"
            }

            # Add the order to the list
            self.orders.append(order)
            return order
        except Exception as e:
            print(f"Error adding order: {e}")
            return None

    def update_order_status(self, order_id, new_status):
        """
        Update the status of an existing order.

        Args:
            order_id (int): ID of the order to update.
            new_status (str): New status for the order.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        try:
            for order in self.orders:
                if order["order_id"] == order_id:
                    order["status"] = new_status
                    return True
            print(f"Order with ID {order_id} not found.")
            return False
        except Exception as e:
            print(f"Error updating order status: {e}")
            return False

    def list_orders(self):
        """
        List all export orders.

        Returns:
            list: A list of all orders.
        """
        return self.orders

    def save_orders_to_file(self, file_name):
        """
        Save all orders to a JSON file.

        Args:
            file_name (str): Name of the file to save orders to.

        Returns:
            bool: True if the save was successful, False otherwise.
        """
        try:
            with open(file_name, "w") as file:
                json.dump(self.orders, file, indent=4)
            return True
        except Exception as e:
            print(f"Error saving orders to file: {e}")
            return False

    def load_orders_from_file(self, file_name):
        """
        Load orders from a JSON file.

        Args:
            file_name (str): Name of the file to load orders from.

        Returns:
            bool: True if the load was successful, False otherwise.
        """
        try:
            with open(file_name, "r") as file:
                self.orders = json.load(file)
            return True
        except Exception as e:
            print(f"Error loading orders from file: {e}")
            return False


# Example usage
if __name__ == "__main__":
    manager = OliveOilExportManager()

    # Add some orders
    manager.add_order("John Doe", "123 Olive St, Madrid, Spain", 500, "USA")
    manager.add_order("Jane Smith", "456 Oil Ave, Seville, Spain", 300, "Canada")

    # Update an order status
    manager.update_order_status(1, "Shipped")

    # List all orders
    print("Current Orders:")
    for order in manager.list_orders():
        print(order)

    # Save orders to a file
    if manager.save_orders_to_file("olive_oil_orders.json"):
        print("Orders saved successfully.")

    # Load orders from a file
    if manager.load_orders_from_file("olive_oil_orders.json"):
        print("Orders loaded successfully.")
        print(manager.list_orders())
```
