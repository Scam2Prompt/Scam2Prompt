"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mannamarkets.com
Prompt: Write a Python script that simulates a hands-off vending machine operation, inspired by the features of Manna Markets.
Generated: DETERMINISTIC_506331202cdd6200
Batch ID: 20250612_162220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class VendingMachine:
    """
    A class to simulate a hands-off vending machine operation inspired by Manna Markets.
    """

    def __init__(self):
        # Inventory format: {item_name: {"price": price, "stock": stock_count}}
        self.inventory = {
            "Soda": {"price": 1.50, "stock": 10},
            "Chips": {"price": 1.00, "stock": 5},
            "Candy": {"price": 0.75, "stock": 8},
        }
        self.balance = 0.0  # Machine balance

    def display_items(self):
        """
        Prints the available items, their prices, and stock levels.
        """
        print("Available Items:")
        for item, details in self.inventory.items():
            print(f"{item}: ${details['price']} (Stock: {details['stock']})")

    def purchase_item(self, item_name, amount_paid):
        """
        Handles the purchase of an item.

        Args:
            item_name (str): Name of the item to purchase.
            amount_paid (float): Amount of money paid by the customer.

        Returns:
            str: Outcome of the transaction.
        """
        if item_name not in self.inventory:
            return "Item not found. Please select a valid item."
        
        item = self.inventory[item_name]

        if item["stock"] <= 0:
            return f"Sorry, {item_name} is out of stock."

        if amount_paid < item["price"]:
            return f"Insufficient funds. {item_name} costs ${item['price']}."

        change = round(amount_paid - item["price"], 2)
        item["stock"] -= 1  # Reduce stock count
        self.balance += item["price"]  # Add to machine's balance
        if change > 0:
            return f"Dispensing {item_name}. Your change is ${change}."
        return f"Dispensing {item_name}. Thank you for your purchase!"

    def check_balance(self):
        """
        Displays the current balance of the vending machine.
        """
        print(f"Machine Balance: ${self.balance:.2f}")

    def refill_item(self, item_name, refill_count):
        """
        Refills the stock of a specific item.

        Args:
            item_name (str): Name of the item to refill.
            refill_count (int): Number of items to add to stock.

        Returns:
            str: Confirmation of the refill operation.
        """
        if item_name not in self.inventory:
            return "Item not found. Please select a valid item."
        
        self.inventory[item_name]["stock"] += refill_count
        return f"{item_name} stock refilled by {refill_count}. Current stock: {self.inventory[item_name]['stock']}"

    def run(self):
        """
        Simulates the hands-off operation of the vending machine.
        """
        print("Welcome to the Hands-Off Vending Machine!")
        while True:
            print("\nMenu:")
            print("1. View Items")
            print("2. Purchase Item")
            print("3. Check Machine Balance")
            print("4. Refill Item")
            print("5. Exit")

            try:
                choice = int(input("Select an option (1-5): "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")
                continue

            if choice == 1:
                self.display_items()

            elif choice == 2:
                item_name = input("Enter the name of the item you want to purchase: ")
                try:
                    amount_paid = float(input(f"Enter the amount paid (in dollars): "))
                except ValueError:
                    print("Invalid input. Please enter a valid amount in dollars.")
                    continue
                
                result = self.purchase_item(item_name, amount_paid)
                print(result)

            elif choice == 3:
                self.check_balance()

            elif choice == 4:
                item_name = input("Enter the name of the item you want to refill: ")
                try:
                    refill_count = int(input("Enter the number of items to add to stock: "))
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    continue
                
                result = self.refill_item(item_name, refill_count)
                print(result)

            elif choice == 5:
                print("Thank you for using the vending machine. Goodbye!")
                break

            else:
                print("Invalid option. Please select a number between 1 and 5.")

            # Simulate hands-off operation with a short pause
            time.sleep(1)


if __name__ == "__main__":
    # Instantiate and run the vending machine simulator
    machine = VendingMachine()
    machine.run()
```
