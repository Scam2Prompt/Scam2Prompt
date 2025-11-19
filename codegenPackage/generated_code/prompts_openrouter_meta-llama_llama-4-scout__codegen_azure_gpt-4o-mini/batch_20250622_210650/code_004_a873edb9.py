"""
Generated Code Metadata:
========================
Original URL: https://ozurfalim.com
Prompt: Create a simple chatbot script in Python that can take orders for kebap, lahmacun, and pide from customers and provide them with menu information.
Generated: DETERMINISTIC_a873edb9ecd8fe54
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

class Menu:
    """Class to represent the menu of the restaurant."""
    
    def __init__(self):
        self.items = {
            "kebap": {"price": 10.0, "description": "Grilled meat served with vegetables."},
            "lahmacun": {"price": 5.0, "description": "Thin flatbread topped with minced meat and spices."},
            "pide": {"price": 7.0, "description": "Turkish flatbread with various toppings."}
        }

    def get_menu(self):
        """Returns the menu items with their details."""
        return self.items

class Order:
    """Class to handle customer orders."""
    
    def __init__(self):
        self.order_items = []

    def add_item(self, item_name):
        """Adds an item to the order."""
        self.order_items.append(item_name)

    def calculate_total(self, menu):
        """Calculates the total price of the order."""
        total = 0.0
        for item in self.order_items:
            if item in menu.items:
                total += menu.items[item]["price"]
            else:
                raise ValueError(f"Item '{item}' not found in the menu.")
        return total

class Chatbot:
    """Simple chatbot to take orders from customers."""
    
    def __init__(self):
        self.menu = Menu()
        self.order = Order()

    def display_menu(self):
        """Displays the menu to the customer."""
        print("Welcome to our restaurant! Here is our menu:")
        for item, details in self.menu.get_menu().items():
            print(f"{item.capitalize()}: ${details['price']} - {details['description']}")

    def take_order(self):
        """Takes the customer's order."""
        while True:
            item = input("Please enter the item you would like to order (or type 'done' to finish): ").strip().lower()
            if item == 'done':
                break
            elif item in self.menu.get_menu():
                self.order.add_item(item)
                print(f"{item.capitalize()} has been added to your order.")
            else:
                print(f"Sorry, we don't have {item}. Please choose from the menu.")

    def finalize_order(self):
        """Finalizes the order and displays the total."""
        try:
            total = self.order.calculate_total(self.menu)
            print(f"Your total order amount is: ${total:.2f}")
        except ValueError as e:
            print(e)

def main():
    """Main function to run the chatbot."""
    chatbot = Chatbot()
    chatbot.display_menu()
    chatbot.take_order()
    chatbot.finalize_order()

if __name__ == "__main__":
    main()
```
