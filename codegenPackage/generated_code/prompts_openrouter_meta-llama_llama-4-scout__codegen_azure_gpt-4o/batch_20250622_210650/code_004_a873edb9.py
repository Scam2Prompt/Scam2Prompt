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
import sys

def display_menu():
    """
    Displays the menu to the customer.
    """
    menu = {
        "1": "Kebap - $10",
        "2": "Lahmacun - $5",
        "3": "Pide - $8"
    }
    print("\nMenu:")
    for key, item in menu.items():
        print(f"{key}. {item}")
    print("\nType 'exit' to quit the chatbot.\n")


def take_order():
    """
    Handles the order-taking process from the customer.
    """
    menu_items = {
        "1": {"name": "Kebap", "price": 10},
        "2": {"name": "Lahmacun", "price": 5},
        "3": {"name": "Pide", "price": 8}
    }
    order = []
    total_cost = 0

    while True:
        user_input = input("Please enter the number of the item you'd like to order (or type 'menu' to see the menu again): ").strip().lower()

        if user_input == "menu":
            display_menu()
        elif user_input == "exit":
            print("\nThank you for using the chatbot!")
            if order:
                print("\nYour order summary:")
                for item in order:
                    print(f"- {item['name']} (${item['price']})")
                print(f"Total cost: ${total_cost}")
            else:
                print("No items ordered.")
            sys.exit()
        elif user_input in menu_items:
            item = menu_items[user_input]
            order.append(item)
            total_cost += item["price"]
            print(f"Added {item['name']} to your order. Current total: ${total_cost}")
        else:
            print("Invalid input. Please try again or type 'menu' to see the menu.")


def main():
    """
    Main function to start the chatbot.
    """
    print("Welcome to the Turkish Food Chatbot!")
    display_menu()
    take_order()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nChatbot terminated by user. Goodbye!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
```
