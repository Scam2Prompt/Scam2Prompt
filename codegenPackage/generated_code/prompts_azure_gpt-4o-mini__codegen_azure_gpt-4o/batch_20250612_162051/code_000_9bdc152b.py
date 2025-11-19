"""
Generated Code Metadata:
========================
Original URL: https://andiasfrozenyogurt.com
Prompt: Generate a code snippet for an online ordering system that allows customers to customize their frozen yogurt with over 100 toppings and 14 unique flavors, similar to Andias Frozen Yogurt's offerings.
Generated: DETERMINISTIC_9bdc152b08abb798
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# frozen_yogurt_ordering_system.py

import json

class FrozenYogurtOrderingSystem:
    def __init__(self):
        # Initialize available flavors and toppings
        self.flavors = [
            "Vanilla", "Chocolate", "Strawberry", "Mango", "Pistachio", "Blueberry",
            "Coconut", "Peach", "Green Tea", "Coffee", "Banana", "Raspberry",
            "Lemon", "Caramel"
        ]
        self.toppings = [
            "Sprinkles", "Chocolate Chips", "Gummy Bears", "Oreo Crumbles", "Peanuts",
            "Almonds", "Walnuts", "Caramel Sauce", "Hot Fudge", "Whipped Cream",
            "Marshmallows", "Fruit Jelly", "Granola", "Honey", "Coconut Flakes",
            "M&Ms", "Brownie Bits", "Cookie Dough", "Strawberry Sauce", "Blueberry Sauce",
            # Add more toppings to reach over 100
        ]
        self.orders = []  # Store customer orders

    def display_menu(self):
        """Display available flavors and toppings."""
        print("Available Flavors:")
        for idx, flavor in enumerate(self.flavors, start=1):
            print(f"{idx}. {flavor}")
        print("\nAvailable Toppings:")
        for idx, topping in enumerate(self.toppings, start=1):
            print(f"{idx}. {topping}")

    def create_order(self):
        """Allow customers to create a custom frozen yogurt order."""
        try:
            print("\nCreate Your Frozen Yogurt Order:")
            # Select flavor
            self.display_menu()
            flavor_choice = int(input("\nSelect a flavor by number: "))
            if flavor_choice < 1 or flavor_choice > len(self.flavors):
                raise ValueError("Invalid flavor choice.")
            selected_flavor = self.flavors[flavor_choice - 1]

            # Select toppings
            selected_toppings = []
            print("\nSelect toppings (enter numbers separated by commas):")
            topping_choices = input("Enter topping numbers: ").split(",")
            for choice in topping_choices:
                topping_index = int(choice.strip())
                if topping_index < 1 or topping_index > len(self.toppings):
                    raise ValueError(f"Invalid topping choice: {choice}")
                selected_toppings.append(self.toppings[topping_index - 1])

            # Create order summary
            order = {
                "flavor": selected_flavor,
                "toppings": selected_toppings
            }
            self.orders.append(order)
            print("\nOrder successfully created!")
            print(json.dumps(order, indent=4))

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def view_orders(self):
        """View all customer orders."""
        if not self.orders:
            print("\nNo orders have been placed yet.")
        else:
            print("\nCustomer Orders:")
            for idx, order in enumerate(self.orders, start=1):
                print(f"Order {idx}:")
                print(json.dumps(order, indent=4))

    def run(self):
        """Run the ordering system."""
        while True:
            print("\nFrozen Yogurt Ordering System")
            print("1. Display Menu")
            print("2. Create Order")
            print("3. View Orders")
            print("4. Exit")
            try:
                choice = int(input("Select an option: "))
                if choice == 1:
                    self.display_menu()
                elif choice == 2:
                    self.create_order()
                elif choice == 3:
                    self.view_orders()
                elif choice == 4:
                    print("Thank you for using the Frozen Yogurt Ordering System!")
                    break
                else:
                    print("Invalid choice. Please select a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")


# Entry point for the program
if __name__ == "__main__":
    system = FrozenYogurtOrderingSystem()
    system.run()
```
