"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://createxpro.com
Prompt: Develop a program to manage customer orders for personalized promotional items, incorporating customization options like DTF printing and vinyl textile designs.
Generated: DETERMINISTIC_f5bcbc010a77c73c
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


class OrderManager:
    """
    OrderManager is responsible for managing customer orders for promotional items.
    It supports customization options like DTF printing and vinyl textile designs.
    """

    def __init__(self):
        # Initialize an empty list to store orders
        self.orders = []

    def create_order(self, customer_name, item_name, quantity, customization_type, customization_details):
        """
        Create a new order and add it to the order list.

        Args:
            customer_name (str): Name of the customer.
            item_name (str): Name of the promotional item.
            quantity (int): Number of items ordered.
            customization_type (str): Type of customization (e.g., "DTF Printing" or "Vinyl Textile Design").
            customization_details (dict): Details about the customization.

        Raises:
            ValueError: If quantity is not positive or customization_type is invalid.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive number.")

        if customization_type not in ["DTF Printing", "Vinyl Textile Design"]:
            raise ValueError("Unsupported customization type.")

        order = {
            "customer_name": customer_name,
            "item_name": item_name,
            "quantity": quantity,
            "customization_type": customization_type,
            "customization_details": customization_details,
        }

        self.orders.append(order)
        print(f"Order for {customer_name} created successfully!")

    def list_orders(self):
        """
        List all current orders.
        Returns:
            list: A list of orders.
        """
        if not self.orders:
            print("No orders available.")
        else:
            print("Current Orders:")
            for index, order in enumerate(self.orders, start=1):
                print(f"{index}. {order['customer_name']} - {order['item_name']} ({order['quantity']} items)")

    def save_orders_to_file(self, filename):
        """
        Save all orders to a file in JSON format.

        Args:
            filename (str): Name of the file to save orders.
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.orders, file, indent=4)
            print(f"Orders saved to file: {filename}")
        except Exception as e:
            print(f"Error saving orders to file: {e}")

    def load_orders_from_file(self, filename):
        """
        Load orders from a file in JSON format.

        Args:
            filename (str): Name of the file to load orders from.

        Raises:
            FileNotFoundError: If the file does not exist.
            JSONDecodeError: If the file content cannot be parsed.
        """
        try:
            with open(filename, "r") as file:
                self.orders = json.load(file)
            print(f"Orders loaded successfully from file: {filename}")
        except FileNotFoundError:
            print(f"File not found: {filename}")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file: {filename}")


# Sample usage
if __name__ == "__main__":
    manager = OrderManager()

    # Create orders
    try:
        manager.create_order(
            customer_name="Alice",
            item_name="T-Shirt",
            quantity=10,
            customization_type="DTF Printing",
            customization_details={"color": "blue", "design": "logo"}
        )
        manager.create_order(
            customer_name="Bob",
            item_name="Cap",
            quantity=5,
            customization_type="Vinyl Textile Design",
            customization_details={"color": "red", "text": "Company Name"}
        )
    except ValueError as ve:
        print(f"Error creating order: {ve}")

    # List orders
    manager.list_orders()

    # Save orders to a file
    manager.save_orders_to_file("orders.json")

    # Load orders from a file
    manager.load_orders_from_file("orders.json")
    manager.list_orders()
```
