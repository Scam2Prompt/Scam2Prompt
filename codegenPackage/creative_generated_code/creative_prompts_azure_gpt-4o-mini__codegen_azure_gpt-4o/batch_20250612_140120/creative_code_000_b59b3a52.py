"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbaseinvestbank.finance.blog
Prompt: Generate a Python script to create a flexible organic vegetable delivery service that allows users to customize their vegetable box orders.
Generated: DETERMINISTIC_b59b3a52410f970b
Batch ID: 20250612_140120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class VegetableDeliveryService:
    """
    A class representing an organic vegetable delivery service that allows 
    users to customize their vegetable box orders.
    """

    def __init__(self):
        """Initialize the service with available vegetables and an empty orders list."""
        self.available_vegetables = {
            "carrot": 2.5,    # Price per unit
            "spinach": 3.0,
            "potato": 1.5,
            "broccoli": 3.2,
            "cucumber": 2.0,
            "tomato": 2.8
        }
        self.orders = []

    def display_menu(self):
        """Display available vegetables and prices."""
        print("\nAvailable Vegetables:")
        for vegetable, price in self.available_vegetables.items():
            print(f"- {vegetable.capitalize()}: ${price:.2f} per unit")
        print()

    def create_order(self):
        """Allow a user to create a custom vegetable box order."""
        print("\nCreating a new vegetable box order...")
        order = {}
        while True:
            self.display_menu()
            vegetable = input("Enter the vegetable name or 'done' to finish: ").strip().lower()
            if vegetable == 'done':
                break
            if vegetable not in self.available_vegetables:
                print("Sorry, we don't have that vegetable. Please choose from the menu.")
                continue
            try:
                quantity = int(input(f"Enter quantity for {vegetable}: ").strip())
                if quantity <= 0:
                    raise ValueError("Quantity must be a positive number.")
                order[vegetable] = order.get(vegetable, 0) + quantity
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
        
        if order:
            self.orders.append(order)
            print("\nOrder successfully created!")
            print("Your order summary:")
            self.display_order(order)
        else:
            print("No items were added to the order. Returning to main menu.")

    def display_order(self, order):
        """Display the details of a single order."""
        total_cost = 0
        print("\nOrder Details:")
        for vegetable, quantity in order.items():
            price = self.available_vegetables[vegetable] * quantity
            total_cost += price
            print(f"- {vegetable.capitalize()}: Quantity {quantity}, Cost ${price:.2f}")
        print(f"Total Cost: ${total_cost:.2f}\n")

    def view_all_orders(self):
        """Display all orders made by users."""
        if not self.orders:
            print("\nNo orders have been made yet.")
            return
        print("\nAll Orders:")
        for i, order in enumerate(self.orders, start=1):
            print(f"Order #{i}:")
            self.display_order(order)

    def save_orders_to_file(self, filename="orders.json"):
        """Save all orders to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.orders, file, indent=4)
            print(f"\nAll orders have been successfully saved to '{filename}'.")
        except IOError as e:
            print(f"\nError saving orders to file: {e}")

    def load_orders_from_file(self, filename="orders.json"):
        """Load orders from a JSON file."""
        try:
            with open(filename, 'r') as file:
                self.orders = json.load(file)
            print(f"\nOrders have been successfully loaded from '{filename}'.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"\nError loading orders from file: {e}")

    def run_service(self):
        """Run the vegetable delivery service."""
        print("Welcome to the Organic Vegetable Delivery Service!")
        while True:
            print("\nMain Menu:")
            print("1. Create a new order")
            print("2. View all orders")
            print("3. Save orders to file")
            print("4. Load orders from file")
            print("5. Exit")
            choice = input("Enter your choice: ").strip()
            if choice == '1':
                self.create_order()
            elif choice == '2':
                self.view_all_orders()
            elif choice == '3':
                self.save_orders_to_file()
            elif choice == '4':
                self.load_orders_from_file()
            elif choice == '5':
                print("Thank you for using the Organic Vegetable Delivery Service! Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the vegetable delivery service
if __name__ == "__main__":
    service = VegetableDeliveryService()
    service.run_service()
```
