"""
Generated Code Metadata:
========================
Original URL: https://mannamarkets.com
Prompt: Write a Python script that simulates a hands-off vending machine operation, inspired by the features of Manna Markets.
Generated: DETERMINISTIC_506331202cdd6200
Batch ID: 20250612_162220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import sys

class VendingMachine:
    """
    A class to simulate a hands-off vending machine operation.
    Inspired by Manna Markets, this vending machine is fully automated.
    """

    def __init__(self):
        # Initialize the vending machine with available items and their prices
        self.inventory = {
            "Chips": {"price": 1.50, "stock": 10},
            "Soda": {"price": 1.25, "stock": 8},
            "Candy": {"price": 0.75, "stock": 15},
            "Water": {"price": 1.00, "stock": 20},
        }
        self.balance = 0.0  # Tracks the user's current balance

    def display_items(self):
        """Display available items, their prices, and stock."""
        print("\nAvailable Items:")
        for item, details in self.inventory.items():
            print(f"{item}: ${details['price']:.2f} (Stock: {details['stock']})")
        print()

    def insert_money(self, amount):
        """
        Simulate inserting money into the vending machine.
        :param amount: The amount of money to insert (float).
        """
        if amount <= 0:
            print("Error: Please insert a valid amount of money.")
            return
        self.balance += amount
        print(f"Money inserted: ${amount:.2f}. Current balance: ${self.balance:.2f}")

    def select_item(self, item_name):
        """
        Simulate selecting an item from the vending machine.
        :param item_name: The name of the item to purchase (string).
        """
        if item_name not in self.inventory:
            print("Error: Item not found. Please select a valid item.")
            return

        item = self.inventory[item_name]
        if item["stock"] <= 0:
            print(f"Error: {item_name} is out of stock.")
            return

        if self.balance < item["price"]:
            print(f"Error: Insufficient balance. {item_name} costs ${item['price']:.2f}.")
            return

        # Deduct the price and dispense the item
        self.balance -= item["price"]
        item["stock"] -= 1
        print(f"Dispensing {item_name}. Remaining balance: ${self.balance:.2f}")

    def return_change(self):
        """Return any remaining balance to the user."""
        if self.balance > 0:
            print(f"Returning change: ${self.balance:.2f}")
            self.balance = 0.0
        else:
            print("No change to return.")

    def run(self):
        """Main loop to simulate the vending machine operation."""
        print("Welcome to the Hands-Off Vending Machine!")
        while True:
            try:
                print("\nOptions:")
                print("1. Display Items")
                print("2. Insert Money")
                print("3. Select Item")
                print("4. Return Change")
                print("5. Exit")
                choice = input("Please select an option (1-5): ").strip()

                if choice == "1":
                    self.display_items()
                elif choice == "2":
                    amount = float(input("Enter the amount to insert: ").strip())
                    self.insert_money(amount)
                elif choice == "3":
                    item_name = input("Enter the name of the item to select: ").strip()
                    self.select_item(item_name)
                elif choice == "4":
                    self.return_change()
                elif choice == "5":
                    print("Thank you for using the vending machine. Goodbye!")
                    self.return_change()
                    break
                else:
                    print("Invalid option. Please try again.")
            except ValueError:
                print("Error: Invalid input. Please try again.")
            except KeyboardInterrupt:
                print("\nOperation interrupted. Returning change and exiting.")
                self.return_change()
                sys.exit(0)
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                sys.exit(1)


if __name__ == "__main__":
    # Create an instance of the vending machine and start the simulation
    vending_machine = VendingMachine()
    vending_machine.run()
```
