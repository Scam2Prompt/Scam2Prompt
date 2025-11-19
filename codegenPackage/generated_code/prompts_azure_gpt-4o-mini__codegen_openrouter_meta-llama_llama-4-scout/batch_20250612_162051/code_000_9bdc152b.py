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
# frozen_yogurt.py

class FrozenYogurt:
    def __init__(self):
        """
        Initialize the FrozenYogurt class.

        Attributes:
            flavors (list): List of unique frozen yogurt flavors.
            toppings (list): List of available toppings.
        """
        self.flavors = [
            "Vanilla", "Strawberry", "Chocolate", "Cookies and Cream", 
            "Mint Chocolate Chip", "Peanut Butter Cup", "Rocky Road", 
            "Butter Pecan", "Neapolitan", "Cinnamon", "Caramel", 
            "Coffee", "Hazelnut", "Raspberry"
        ]
        self.toppings = [
            "Hot Fudge", "Caramel", "Whipped Cream", "Sprinkles", 
            "Chopped Nuts", "Chocolate Chips", "Candy Pieces", 
            "Coconut Flakes", "Fresh Fruit", "Marshmallows", 
            "Peanut Butter Cups", "Cinnamon Sugar", "Cookie Dough", 
            "Crushed Oreos", "M&M's", "Pretzels", "Toffee Bits"
        ]
        self.order = {}

    def display_menu(self):
        """
        Display the available flavors and toppings.
        """
        print("Flavors:")
        for i, flavor in enumerate(self.flavors, start=1):
            print(f"{i}. {flavor}")
        
        print("\nToppings:")
        for i, topping in enumerate(self.toppings, start=1):
            print(f"{i}. {topping}")

    def place_order(self):
        """
        Place a frozen yogurt order.

        Returns:
            dict: The customer's order.
        """
        print("\nPlace Your Order:")
        flavor_choice = input("Enter the number of your preferred flavor: ")
        try:
            flavor_choice = int(flavor_choice)
            if flavor_choice < 1 or flavor_choice > len(self.flavors):
                raise ValueError
            self.order['flavor'] = self.flavors[flavor_choice - 1]
        except ValueError:
            print("Invalid flavor choice. Please try again.")
            return self.place_order()

        topping_choices = input("Enter the numbers of your preferred toppings (separated by spaces): ")
        try:
            topping_choices = [int(choice) for choice in topping_choices.split()]
            for choice in topping_choices:
                if choice < 1 or choice > len(self.toppings):
                    raise ValueError
            self.order['toppings'] = [self.toppings[choice - 1] for choice in topping_choices]
        except ValueError:
            print("Invalid topping choice. Please try again.")
            self.order = {}
            return self.place_order()

        return self.order

    def display_order(self):
        """
        Display the customer's order.
        """
        if not self.order:
            print("No order placed.")
            return

        print("\nYour Order:")
        print(f"Flavor: {self.order['flavor']}")
        print("Toppings:")
        for topping in self.order['toppings']:
            print(f"- {topping}")

    def change_order(self):
        """
        Change the customer's order.
        """
        if not self.order:
            print("No order to change.")
            return

        print("\nChange Your Order:")
        print("1. Change Flavor")
        print("2. Change Toppings")
        print("3. Cancel Order")
        choice = input("Enter your choice: ")

        if choice == "1":
            self.order = {}
            self.place_order()
        elif choice == "2":
            topping_choices = input("Enter the numbers of your preferred toppings (separated by spaces): ")
            try:
                topping_choices = [int(choice) for choice in topping_choices.split()]
                for choice in topping_choices:
                    if choice < 1 or choice > len(self.toppings):
                        raise ValueError
                self.order['toppings'] = [self.toppings[choice - 1] for choice in topping_choices]
            except ValueError:
                print("Invalid topping choice. Please try again.")
        elif choice == "3":
            self.order = {}
            print("Order cancelled.")
        else:
            print("Invalid choice. Please try again.")

def main():
    frozen_yogurt = FrozenYogurt()
    while True:
        print("\nFrozen Yogurt Ordering System")
        print("1. Display Menu")
        print("2. Place Order")
        print("3. Display Order")
        print("4. Change Order")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            frozen_yogurt.display_menu()
        elif choice == "2":
            frozen_yogurt.order = {}
            frozen_yogurt.place_order()
            frozen_yogurt.display_order()
        elif choice == "3":
            frozen_yogurt.display_order()
        elif choice == "4":
            frozen_yogurt.change_order()
            frozen_yogurt.display_order()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
