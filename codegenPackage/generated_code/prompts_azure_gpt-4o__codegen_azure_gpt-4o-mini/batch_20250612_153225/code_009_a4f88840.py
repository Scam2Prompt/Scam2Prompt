"""
Generated Code Metadata:
========================
Original URL: https://theprintnan.app
Prompt: Develop a chatbot that uses AI to assist customers in choosing printing services and calculating costs for items like self-inking stamps, die-cut stickers, and product labels, based on ThePrintNan's offerings.
Generated: DETERMINISTIC_a4f88840b6f90b9c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class PrintService:
    """Class to represent a printing service with its offerings and pricing."""
    
    def __init__(self):
        # Initialize the service offerings and their prices
        self.offerings = {
            "self_inking_stamp": 25.00,
            "die_cut_sticker": 0.50,  # price per sticker
            "product_label": 0.10      # price per label
        }

    def get_price(self, item_type, quantity):
        """Calculate the total price for a given item type and quantity."""
        if item_type not in self.offerings:
            raise ValueError(f"Item type '{item_type}' is not available.")
        
        price_per_item = self.offerings[item_type]
        total_price = price_per_item * quantity
        return total_price


class Chatbot:
    """Chatbot class to assist customers in choosing printing services."""
    
    def __init__(self):
        self.print_service = PrintService()

    def greet_user(self):
        """Greet the user and provide initial instructions."""
        return "Hello! I'm here to help you choose printing services and calculate costs. What would you like to print?"

    def get_user_input(self):
        """Get user input for item type and quantity."""
        item_type = input("Please enter the type of item (self_inking_stamp, die_cut_sticker, product_label): ")
        quantity = input("Please enter the quantity: ")
        
        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError("Quantity must be a positive integer.")
        except ValueError as e:
            return str(e)
        
        return item_type, quantity

    def calculate_cost(self, item_type, quantity):
        """Calculate the cost based on user input."""
        try:
            total_cost = self.print_service.get_price(item_type, quantity)
            return f"The total cost for {quantity} {item_type}(s) is: ${total_cost:.2f}"
        except ValueError as e:
            return str(e)

    def run(self):
        """Run the chatbot interaction."""
        print(self.greet_user())
        while True:
            user_input = self.get_user_input()
            if isinstance(user_input, str):  # Error message
                print(user_input)
                continue
            
            item_type, quantity = user_input
            result = self.calculate_cost(item_type, quantity)
            print(result)
            
            if input("Would you like to calculate another cost? (yes/no): ").lower() != 'yes':
                print("Thank you for using our service! Goodbye!")
                break


if __name__ == "__main__":
    # Start the chatbot
    chatbot = Chatbot()
    chatbot.run()
```
