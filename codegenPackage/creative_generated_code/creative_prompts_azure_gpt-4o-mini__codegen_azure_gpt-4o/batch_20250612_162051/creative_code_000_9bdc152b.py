"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://andiasfrozenyogurt.com
Prompt: Generate a code snippet for an online ordering system that allows customers to customize their frozen yogurt with over 100 toppings and 14 unique flavors, similar to Andias Frozen Yogurt's offerings.
Generated: DETERMINISTIC_9bdc152b08abb798
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class FrozenYogurtOrderingSystem:
    def __init__(self):
        # List of available flavors and toppings
        self.flavors = [
            "Vanilla", "Chocolate", "Strawberry", "Mango", "Blueberry",
            "Peach", "Coconut", "Green Tea", "Coffee", "Caramel",
            "Mint", "Banana", "Lemon", "Cookies and Cream"
        ]
        self.toppings = [
            "Sprinkles", "Chocolate Chips", "Peanuts", "Almonds", "Walnuts",
            "Gummy Bears", "Marshmallows", "Caramel Sauce", "Hot Fudge",
            "Whipped Cream", "Fruit Jelly", "Oreo Crumbs", "Strawberry Sauce",
            # Add additional toppings to reach over 100
        ] + [f"Topping-{i}" for i in range(1, 88)]  # Dummy toppings to exceed 100

    def display_menu(self):
        """Displays the list of available flavors and toppings."""
        print("Available Frozen Yogurt Flavors:")
        for i, flavor in enumerate(self.flavors, 1):
            print(f"{i}. {flavor}")
        print("\nAvailable Toppings:")
        for i, topping in enumerate(self.toppings, 1):
            print(f"{i}. {topping}")

    def place_order(self):
        """Allows customers to customize their frozen yogurt order."""
        try:
            # Select flavor
            print("\nSelect a flavor (enter the number):")
            flavor_choice = int(input("Your choice: "))
            if flavor_choice < 1 or flavor_choice > len(self.flavors):
                raise ValueError("Invalid flavor choice.")
            selected_flavor = self.flavors[flavor_choice - 1]

            # Select toppings
            print("\nSelect toppings (enter numbers separated by commas):")
            print("Press ENTER if you don't want any toppings.")
            topping_choices = input("Your choices: ")
            selected_toppings = []
            if topping_choices.strip():
                topping_indices = [int(x.strip()) for x in topping_choices.split(",")]
                for index in topping_indices:
                    if index < 1 or index > len(self.toppings):
                        raise ValueError("Invalid topping choice.")
                    selected_toppings.append(self.toppings[index - 1])

            # Generate order summary
            order_summary = {
                "Flavor": selected_flavor,
                "Toppings": selected_toppings
            }
            print("\nYour Order Summary:")
            print(json.dumps(order_summary, indent=4))

            return order_summary  # Return order for further processing

        except ValueError as e:
            print(f"Error: {e}. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

    def run(self):
        """Runs the main ordering system workflow."""
        print("Welcome to Frozen Yogurt Ordering System!")
        self.display_menu()
        self.place_order()


if __name__ == "__main__":
    # Initialize and run the ordering system
    system = FrozenYogurtOrderingSystem()
    system.run()
```
