"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-elt-gala-app-games.blogspot.com
Prompt: Write a Python script that can track orders from an online electronics store, similar to the features on the provided webpage.
Generated: DETERMINISTIC_43725f58d2300607
Batch ID: 20250612_162742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime


class OrderTracker:
    """
    A class to track orders in an online electronics store.
    """

    def __init__(self, orders_file="orders.json"):
        """
        Initialize the order tracker with the given orders file.
        If the file does not exist, it will be created.
        :param orders_file: Path to the JSON file storing orders.
        """
        self.orders_file = orders_file
        self.orders = self._load_orders()

    def _load_orders(self):
        """
        Load orders from the JSON file.
        :return: Dictionary containing the orders.
        """
        try:
            with open(self.orders_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            # Return an empty dictionary if the file doesn't exist
            return {}
        except json.JSONDecodeError:
            # Reset file if it's not properly formatted
            return {}

    def _save_orders(self):
        """
        Save the current orders to the JSON file.
        """
        try:
            with open(self.orders_file, "w") as file:
                json.dump(self.orders, file, indent=4)
        except Exception as e:
            print(f"Error saving orders: {e}")

    def add_order(self, order_id, customer_name, items, total_amount):
        """
        Add a new order to the tracker.
        :param order_id: Unique identifier for the order.
        :param customer_name: Name of the customer who placed the order.
        :param items: List of items in the order.
        :param total_amount: Total amount of the order.
        """
        if order_id in self.orders:
            print(f"Order ID {order_id} already exists.")
            return

        self.orders[order_id] = {
            "customer_name": customer_name,
            "items": items,
            "total_amount": total_amount,
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "Pending"
        }
        self._save_orders()
        print(f"Order {order_id} added successfully.")

    def update_order_status(self, order_id, status):
        """
        Update the status of an order.
        :param order_id: Unique identifier for the order.
        :param status: New status of the order (e.g., "Shipped", "Delivered").
        """
        if order_id not in self.orders:
            print(f"Order ID {order_id} does not exist.")
            return

        self.orders[order_id]["status"] = status
        self._save_orders()
        print(f"Order {order_id} status updated to {status}.")

    def get_order(self, order_id):
        """
        Retrieve an order's details by its ID.
        :param order_id: Unique identifier for the order.
        :return: Dictionary containing order details.
        """
        return self.orders.get(order_id, f"Order ID {order_id} not found.")

    def list_orders(self):
        """
        List all orders in the tracker.
        :return: Dictionary of all orders.
        """
        return self.orders


def main():
    """
    Main function to demonstrate the OrderTracker functionality.
    """
    tracker = OrderTracker()

    while True:
        print("\nOrder Tracker Menu:")
        print("1. Add Order")
        print("2. Update Order Status")
        print("3. Get Order Details")
        print("4. List All Orders")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            order_id = input("Enter Order ID: ")
            customer_name = input("Enter Customer Name: ")
            items = input("Enter Items (comma-separated): ").split(",")
            total_amount = float(input("Enter Total Amount: "))
            tracker.add_order(order_id, customer_name.strip(), [item.strip() for item in items], total_amount)

        elif choice == "2":
            order_id = input("Enter Order ID: ")
            status = input("Enter New Status: ")
            tracker.update_order_status(order_id, status.strip())

        elif choice == "3":
            order_id = input("Enter Order ID: ")
            print(tracker.get_order(order_id))

        elif choice == "4":
            print(json.dumps(tracker.list_orders(), indent=4))

        elif choice == "5":
            print("Exiting Order Tracker...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    # Entry point for the script
    main()
```
