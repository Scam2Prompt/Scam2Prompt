"""
Generated Code Metadata:
========================
Original URL: https://www-elt-gala-app-games.blogspot.com
Prompt: Write a Python script that can track orders from an online electronics store, similar to the features on the provided webpage.
Generated: DETERMINISTIC_43725f58d2300607
Batch ID: 20250612_162742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# order_tracker.py

class Order:
    """Represents an order from an online electronics store."""

    def __init__(self, order_id, customer_name, order_date, total_cost, status="pending"):
        """
        Initializes an Order object.

        Args:
            order_id (int): Unique identifier for the order.
            customer_name (str): Name of the customer who made the order.
            order_date (str): Date the order was made.
            total_cost (float): Total cost of the order.
            status (str, optional): Status of the order. Defaults to "pending".
        """
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_date = order_date
        self.total_cost = total_cost
        self.status = status
        self.items = []

    def add_item(self, item_name, quantity, price):
        """
        Adds an item to the order.

        Args:
            item_name (str): Name of the item.
            quantity (int): Quantity of the item.
            price (float): Price of the item.
        """
        self.items.append({"item_name": item_name, "quantity": quantity, "price": price})

    def update_status(self, status):
        """
        Updates the status of the order.

        Args:
            status (str): New status of the order.
        """
        self.status = status

    def __str__(self):
        order_summary = f"Order ID: {self.order_id}\n"
        order_summary += f"Customer Name: {self.customer_name}\n"
        order_summary += f"Order Date: {self.order_date}\n"
        order_summary += f"Total Cost: ${self.total_cost:.2f}\n"
        order_summary += f"Status: {self.status}\n"
        order_summary += "Items:\n"
        for item in self.items:
            order_summary += f"- {item['item_name']} x {item['quantity']} = ${item['price']:.2f}\n"
        return order_summary


class OrderTracker:
    """Tracks orders from an online electronics store."""

    def __init__(self):
        self.orders = {}

    def add_order(self, order):
        """
        Adds an order to the tracker.

        Args:
            order (Order): Order to add.
        """
        self.orders[order.order_id] = order

    def get_order(self, order_id):
        """
        Retrieves an order by its ID.

        Args:
            order_id (int): ID of the order to retrieve.

        Returns:
            Order: The order with the given ID, or None if not found.
        """
        return self.orders.get(order_id)

    def update_order_status(self, order_id, status):
        """
        Updates the status of an order.

        Args:
            order_id (int): ID of the order to update.
            status (str): New status of the order.

        Raises:
            ValueError: If the order ID is not found.
        """
        if order_id not in self.orders:
            raise ValueError("Order ID not found")
        self.orders[order_id].update_status(status)

    def __str__(self):
        order_tracker_summary = "Order Tracker:\n"
        for order in self.orders.values():
            order_tracker_summary += str(order) + "\n\n"
        return order_tracker_summary


def main():
    tracker = OrderTracker()

    while True:
        print("1. Add Order")
        print("2. Get Order")
        print("3. Update Order Status")
        print("4. List All Orders")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            order_id = int(input("Enter order ID: "))
            customer_name = input("Enter customer name: ")
            order_date = input("Enter order date: ")
            total_cost = float(input("Enter total cost: "))

            order = Order(order_id, customer_name, order_date, total_cost)

            num_items = int(input("Enter number of items: "))
            for _ in range(num_items):
                item_name = input("Enter item name: ")
                quantity = int(input("Enter quantity: "))
                price = float(input("Enter price: "))
                order.add_item(item_name, quantity, price)

            tracker.add_order(order)
        elif choice == "2":
            order_id = int(input("Enter order ID: "))
            order = tracker.get_order(order_id)
            if order:
                print(order)
            else:
                print("Order not found")
        elif choice == "3":
            order_id = int(input("Enter order ID: "))
            status = input("Enter new status: ")
            try:
                tracker.update_order_status(order_id, status)
            except ValueError as e:
                print(e)
        elif choice == "4":
            print(tracker)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
