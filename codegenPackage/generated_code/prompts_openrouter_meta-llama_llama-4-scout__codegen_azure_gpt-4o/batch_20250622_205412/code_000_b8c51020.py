"""
Generated Code Metadata:
========================
Original URL: https://amici.nz
Prompt: Write a Python script to manage online ordering and reservations for an Italian restaurant like Amici in Whangarei, including menu items such as Fettuccine Carbonara and Lasagna.
Generated: DETERMINISTIC_b8c5102005e50392
Batch ID: 20250622_205412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

# Define the menu items
MENU = {
    "Fettuccine Carbonara": 18.50,
    "Lasagna": 20.00,
    "Margherita Pizza": 15.00,
    "Tiramisu": 8.00,
    "Garlic Bread": 5.50
}

# Define a class to manage orders and reservations
class ItalianRestaurant:
    def __init__(self):
        self.orders = []  # List to store orders
        self.reservations = []  # List to store reservations

    def display_menu(self):
        """Display the menu items and their prices."""
        print("Menu:")
        for item, price in MENU.items():
            print(f"{item}: ${price:.2f}")
        print()

    def place_order(self, customer_name, items):
        """
        Place an order for the customer.
        :param customer_name: Name of the customer
        :param items: List of menu items ordered
        """
        try:
            # Validate items
            for item in items:
                if item not in MENU:
                    raise ValueError(f"Item '{item}' is not on the menu.")

            # Calculate total price
            total_price = sum(MENU[item] for item in items)

            # Create order record
            order = {
                "customer_name": customer_name,
                "items": items,
                "total_price": total_price,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.orders.append(order)

            print(f"Order placed successfully for {customer_name}. Total: ${total_price:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

    def make_reservation(self, customer_name, date_time, num_people):
        """
        Make a reservation for the customer.
        :param customer_name: Name of the customer
        :param date_time: Date and time of the reservation (string format: YYYY-MM-DD HH:MM)
        :param num_people: Number of people for the reservation
        """
        try:
            # Validate date and time format
            reservation_datetime = datetime.strptime(date_time, "%Y-%m-%d %H:%M")

            # Create reservation record
            reservation = {
                "customer_name": customer_name,
                "date_time": reservation_datetime.strftime("%Y-%m-%d %H:%M"),
                "num_people": num_people
            }
            self.reservations.append(reservation)

            print(f"Reservation made successfully for {customer_name} on {date_time} for {num_people} people.")
        except ValueError:
            print("Error: Invalid date and time format. Please use 'YYYY-MM-DD HH:MM'.")

    def view_orders(self):
        """View all orders."""
        print("Orders:")
        for order in self.orders:
            print(json.dumps(order, indent=4))
        print()

    def view_reservations(self):
        """View all reservations."""
        print("Reservations:")
        for reservation in self.reservations:
            print(json.dumps(reservation, indent=4))
        print()

# Main script
if __name__ == "__main__":
    restaurant = ItalianRestaurant()

    # Display menu
    restaurant.display_menu()

    # Example usage
    restaurant.place_order("Alice", ["Fettuccine Carbonara", "Tiramisu"])
    restaurant.place_order("Bob", ["Lasagna", "Garlic Bread"])
    restaurant.make_reservation("Alice", "2023-10-15 19:00", 4)
    restaurant.make_reservation("Bob", "2023-10-16 18:30", 2)

    # View orders and reservations
    restaurant.view_orders()
    restaurant.view_reservations()
```
