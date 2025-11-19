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
import json
from typing import Dict, List, Optional, Tuple

class VendingMachine:
    """
    A class to simulate a hands-off vending machine operation.
    Inspired by Manna Markets features.
    """
    
    def __init__(self, inventory_file: str = "inventory.json"):
        """
        Initialize the vending machine with inventory from a JSON file.
        
        Args:
            inventory_file: Path to JSON file containing inventory data
        """
        self.inventory = self._load_inventory(inventory_file)
        self.balance = 0.0
        self.transaction_history = []
        
    def _load_inventory(self, file_path: str) -> Dict[str, Dict]:
        """
        Load inventory from JSON file.
        
        Args:
            file_path: Path to JSON file
            
        Returns:
            Dictionary containing inventory data
            
        Raises:
            FileNotFoundError: If inventory file doesn't exist
            json.JSONDecodeError: If inventory file is malformed
        """
        try:
            with open(file_path, 'r') as f:
                inventory = json.load(f)
            return inventory
        except FileNotFoundError:
            raise FileNotFoundError(f"Inventory file {file_path} not found")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON in inventory file", "", 0)
    
    def display_items(self) -> None:
        """Display available items in the vending machine."""
        print("\nAvailable Items:")
        print("----------------")
        for item_id, details in self.inventory.items():
            if details['quantity'] > 0:
                print(f"{item_id}. {details['name']} - ${details['price']:.2f} ({details['quantity']} left)")
        print()
    
    def insert_money(self, amount: float) -> float:
        """
        Insert money into the vending machine.
        
        Args:
            amount: Amount of money to insert
            
        Returns:
            Updated balance
            
        Raises:
            ValueError: If amount is negative
        """
        if amount < 0:
            raise ValueError("Cannot insert negative amount")
        self.balance += amount
        return self.balance
    
    def select_item(self, item_id: str) -> Tuple[Optional[str], float]:
        """
        Select an item from the vending machine.
        
        Args:
            item_id: ID of the item to select
            
        Returns:
            Tuple of (item_name, change) or (None, 0) if unsuccessful
            
        Raises:
            KeyError: If item ID doesn't exist
        """
        if item_id not in self.inventory:
            raise KeyError(f"Item {item_id} not found")
            
        item = self.inventory[item_id]
        
        if item['quantity'] <= 0:
            print(f"Sorry, {item['name']} is out of stock")
            return None, 0
            
        if self.balance < item['price']:
            print(f"Insufficient funds. Need ${item['price'] - self.balance:.2f} more")
            return None, 0
            
        # Process purchase
        item['quantity'] -= 1
        self.balance -= item['price']
        change = self.balance
        self.balance = 0.0
        
        # Record transaction
        self.transaction_history.append({
            'item_id': item_id,
            'item_name': item['name'],
            'amount': item['price'],
            'change': change
        })
        
        return item['name'], change
    
    def get_transaction_history(self) -> List[Dict]:
        """Return the transaction history."""
        return self.transaction_history
    
    def save_inventory(self, file_path: str = "inventory.json") -> None:
        """
        Save current inventory to JSON file.
        
        Args:
            file_path: Path to save inventory file
            
        Raises:
            IOError: If file cannot be written
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.inventory, f, indent=2)
        except IOError:
            raise IOError(f"Could not write to inventory file {file_path}")


def main():
    """Main function to run the vending machine simulation."""
    try:
        # Initialize vending machine
        vending_machine = VendingMachine()
        
        while True:
            print("\nManna Markets Vending Machine")
            print("1. Display Items")
            print("2. Insert Money")
            print("3. Select Item")
            print("4. View Transaction History")
            print("5. Exit")
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == "1":
                vending_machine.display_items()
                
            elif choice == "2":
                try:
                    amount = float(input("Enter amount to insert: $"))
                    balance = vending_machine.insert_money(amount)
                    print(f"Current balance: ${balance:.2f}")
                except ValueError:
                    print("Invalid amount. Please enter a positive number.")
                    
            elif choice == "3":
                vending_machine.display_items()
                item_id = input("Enter item ID to purchase: ")
                try:
                    item_name, change = vending_machine.select_item(item_id)
                    if item_name:
                        print(f"Dispensing {item_name}...")
                        if change > 0:
                            print(f"Returning change: ${change:.2f}")
                except KeyError:
                    print("Invalid item ID. Please try again.")
                    
            elif choice == "4":
                history = vending_machine.get_transaction_history()
                if not history:
                    print("No transactions yet")
                else:
                    print("\nTransaction History:")
                    for idx, transaction in enumerate(history, 1):
                        print(f"{idx}. {transaction['item_name']} - ${transaction['amount']:.2f} (Change: ${transaction['change']:.2f})")
                    
            elif choice == "5":
                # Save inventory before exiting
                vending_machine.save_inventory()
                print("Thank you for using Manna Markets!")
                break
                
            else:
                print("Invalid choice. Please enter a number between 1-5.")
                
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Please restart the vending machine.")


if __name__ == "__main__":
    main()
```
