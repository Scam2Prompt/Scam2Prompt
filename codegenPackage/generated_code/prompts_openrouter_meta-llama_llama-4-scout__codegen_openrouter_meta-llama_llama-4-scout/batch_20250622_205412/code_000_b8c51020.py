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
# italian_restaurant.py

class MenuItem:
    """Represents a menu item with name, description, and price."""

    def __init__(self, name, description, price):
        """
        Initializes a MenuItem.

        Args:
            name (str): Name of the menu item.
            description (str): Description of the menu item.
            price (float): Price of the menu item.
        """
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.description}, ${self.price:.2f}"


class Order:
    """Represents an online order with a list of menu items."""

    def __init__(self):
        """Initializes an empty Order."""
        self.items = []

    def add_item(self, item):
        """
        Adds a menu item to the order.

        Args:
            item (MenuItem): Menu item to add.
        """
        self.items.append(item)

    def remove_item(self, item_name):
        """
        Removes a menu item from the order by name.

        Args:
            item_name (str): Name of the menu item to remove.

        Returns:
            bool: True if the item was removed, False otherwise.
        """
        self.items = [item for item in self.items if item.name != item_name]
        return len(self.items) < len(self.items) + 1

    def calculate_total(self):
        """
        Calculates the total cost of the order.

        Returns:
            float: Total cost of the order.
        """
        return sum(item.price for item in self.items)

    def __str__(self):
        order_str = "Order:\n"
        for i, item in enumerate(self.items, 1):
            order_str += f"{i}. {item}\n"
        order_str += f"Total: ${self.calculate_total():.2f}"
        return order_str


class Reservation:
    """Represents a table reservation with date, time, and party size."""

    def __init__(self, date, time, party_size):
        """
        Initializes a Reservation.

        Args:
            date (str): Date of the reservation (YYYY-MM-DD).
            time (str): Time of the reservation (HH:MM).
            party_size (int): Number of people in the party.
        """
        self.date = date
        self.time = time
        self.party_size = party_size

    def __str__(self):
        return f"Reservation on {self.date} at {self.time} for {self.party_size} people"


class ItalianRestaurant:
    """Manages online ordering and reservations for an Italian restaurant."""

    def __init__(self):
        """Initializes the restaurant with a menu and empty orders and reservations."""
        self.menu = [
            MenuItem("Fettuccine Carbonara", "Rich and creamy carbonara with fettuccine.", 18.99),
            MenuItem("Lasagna", "Layered pasta with meat sauce and melted mozzarella.", 16.99),
            # Add more menu items here...
        ]
        self.orders = []
        self.reservations = []

    def display_menu(self):
        """Displays the restaurant menu."""
        print("Menu:")
        for i, item in enumerate(self.menu, 1):
            print(f"{i}. {item}")

    def place_order(self):
        """Places an online order."""
        order = Order()
        while True:
            self.display_menu()
            choice = input("Enter the number of the item to add, or 'done' to finish: ")
            if choice.lower() == 'done':
                break
            try:
                choice = int(choice) - 1
                if choice < 0 or choice >= len(self.menu):
                    raise ValueError
                order.add_item(self.menu[choice])
            except (ValueError, IndexError):
                print("Invalid choice. Please try again.")
        self.orders.append(order)
        print("\nOrder placed successfully!")
        print(order)

    def make_reservation(self):
        """Makes a table reservation."""
        date = input("Enter date (YYYY-MM-DD): ")
        time = input("Enter time (HH:MM): ")
        while True:
            try:
                party_size = int(input("Enter party size: "))
                if party_size <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid party size. Please try again.")
        reservation = Reservation(date, time, party_size)
        self.reservations.append(reservation)
        print("\nReservation made successfully!")
        print(reservation)

    def view_orders(self):
        """Displays all online orders."""
        if not self.orders:
            print("No orders placed.")
        else:
            for i, order in enumerate(self.orders, 1):
                print(f"\nOrder {i}:")
                print(order)

    def view_reservations(self):
        """Displays all table reservations."""
        if not self.reservations:
            print("No reservations made.")
        else:
            for i, reservation in enumerate(self.reservations, 1):
                print(f"\nReservation {i}:")
                print(reservation)


def main():
    restaurant = ItalianRestaurant()
    while True:
        print("\nItalian Restaurant Management")
        print("1. Display Menu")
        print("2. Place Order")
        print("3. Make Reservation")
        print("4. View Orders")
        print("5. View Reservations")
        print("6. Exit")
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
            if choice < 1 or choice > 6:
                raise ValueError
            if choice == 1:
                restaurant.display_menu()
            elif choice == 2:
                restaurant.place_order()
            elif choice == 3:
                restaurant.make_reservation()
            elif choice == 4:
                restaurant.view_orders()
            elif choice == 5:
                restaurant.view_reservations()
            elif choice == 6:
                print("Exiting program.")
                break
        except ValueError:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```
