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
from typing import Dict, List, Optional

# Menu data structure
MENU = {
    "kebap": {
        "description": "Delicious grilled meat with vegetables and sauce",
        "price": 12.99,
        "options": ["chicken", "beef", "lamb"]
    },
    "lahmacun": {
        "description": "Thin dough topped with minced meat and vegetables",
        "price": 8.99,
        "options": ["spicy", "mild"]
    },
    "pide": {
        "description": "Turkish flatbread with various toppings",
        "price": 10.99,
        "options": ["cheese", "meat", "vegetable"]
    }
}

class Chatbot:
    def __init__(self):
        self.order: Dict[str, List[Dict]] = {"items": []}
        self.greeting = "Welcome to Turkish Delight! How can I help you today?"
        self.goodbye = "Thank you for your order! Enjoy your meal!"
    
    def show_menu(self) -> str:
        """Return formatted menu information"""
        menu_info = "Our Menu:\n"
        for item, details in MENU.items():
            menu_info += (
                f"{item.capitalize()} - {details['description']} "
                f"(Price: ${details['price']:.2f})\n"
                f"Options: {', '.join(details['options'])}\n\n"
            )
        return menu_info.strip()
    
    def add_to_order(self, item: str, option: Optional[str] = None) -> str:
        """Add item to order with optional customization"""
        if item.lower() not in MENU:
            return f"Sorry, we don't serve {item}. Please choose from our menu."
        
        item_data = MENU[item.lower()]
        order_item = {
            "name": item.lower(),
            "price": item_data["price"],
            "option": option.lower() if option else None
        }
        self.order["items"].append(order_item)
        
        confirmation = f"Added {item}"
        if option:
            confirmation += f" with {option}"
        confirmation += " to your order."
        return confirmation
    
    def show_order_summary(self) -> str:
        """Return formatted order summary"""
        if not self.order["items"]:
            return "Your order is empty."
        
        summary = "Your Order:\n"
        total = 0.0
        
        for idx, item in enumerate(self.order["items"], 1):
            summary += (
                f"{idx}. {item['name'].capitalize()}"
                f"{' (' + item['option'] + ')' if item['option'] else ''}"
                f" - ${item['price']:.2f}\n"
            )
            total += item["price"]
        
        summary += f"\nTotal: ${total:.2f}"
        return summary
    
    def process_command(self, command: str) -> str:
        """Process user input and return appropriate response"""
        command = command.lower().strip()
        
        if command in ["hi", "hello", "hey"]:
            return self.greeting
        elif command in ["menu", "show menu"]:
            return self.show_menu()
        elif command.startswith("order"):
            parts = command.split()
            if len(parts) < 2:
                return "Please specify what you'd like to order."
            item = parts[1]
            option = parts[2] if len(parts) > 2 else None
            return self.add_to_order(item, option)
        elif command in ["summary", "order summary"]:
            return self.show_order_summary()
        elif command in ["bye", "exit", "goodbye"]:
            return self.goodbye
        else:
            return (
                "I didn't understand that. You can:\n"
                "- Say 'menu' to see our offerings\n"
                "- Say 'order <item>' to add to your order\n"
                "- Say 'summary' to see your current order\n"
                "- Say 'bye' to exit"
            )

def main():
    """Main interaction loop for the chatbot"""
    bot = Chatbot()
    print(bot.greeting)
    print("Type 'menu' to see what we offer or 'order <item>' to place an order.")
    
    while True:
        user_input = input("\nWhat would you like? ").strip()
        if not user_input:
            continue
            
        response = bot.process_command(user_input)
        print(response)
        
        if user_input.lower() in ["bye", "exit", "goodbye"]:
            break

if __name__ == "__main__":
    main()
```
