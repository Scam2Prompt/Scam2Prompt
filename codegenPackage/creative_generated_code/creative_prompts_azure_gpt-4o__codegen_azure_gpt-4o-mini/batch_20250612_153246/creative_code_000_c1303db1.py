"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aulaferretera.com
Prompt: Write Python code to create a financial control template for a hardware store, incorporating features like inventory tracking and expense management, as described in "Plantillas para control Financiero en la Ferretería" from Aula Ferretera.
Generated: DETERMINISTIC_c1303db14ff2df1c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

class InventoryItem:
    """Represents an item in the inventory."""
    
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.quantity} units at ${self.price:.2f} each"

    def total_value(self):
        """Calculates the total value of the item in inventory."""
        return self.quantity * self.price


class Expense:
    """Represents an expense entry."""
    
    def __init__(self, description: str, amount: float, date: str = None):
        self.description = description
        self.amount = amount
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    def __str__(self):
        return f"{self.date}: {self.description} - ${self.amount:.2f}"


class FinancialControl:
    """Manages inventory and expenses for the hardware store."""
    
    def __init__(self):
        self.inventory = {}
        self.expenses = []

    def add_inventory_item(self, name: str, quantity: int, price: float):
        """Adds an item to the inventory."""
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price must be non-negative.")
        
        item = InventoryItem(name, quantity, price)
        self.inventory[name] = item
        print(f"Added inventory item: {item}")

    def update_inventory_item(self, name: str, quantity: int = None, price: float = None):
        """Updates an existing inventory item."""
        if name not in self.inventory:
            raise KeyError(f"Item '{name}' not found in inventory.")
        
        if quantity is not None:
            self.inventory[name].quantity = quantity
        if price is not None:
            self.inventory[name].price = price
        
        print(f"Updated inventory item: {self.inventory[name]}")

    def add_expense(self, description: str, amount: float):
        """Adds an expense entry."""
        if amount < 0:
            raise ValueError("Expense amount must be non-negative.")
        
        expense = Expense(description, amount)
        self.expenses.append(expense)
        print(f"Added expense: {expense}")

    def total_inventory_value(self):
        """Calculates the total value of the inventory."""
        return sum(item.total_value() for item in self.inventory.values())

    def total_expenses(self):
        """Calculates the total expenses."""
        return sum(expense.amount for expense in self.expenses)

    def save_to_file(self, filename: str):
        """Saves inventory and expenses to a JSON file."""
        data = {
            "inventory": {name: vars(item) for name, item in self.inventory.items()},
            "expenses": [vars(expense) for expense in self.expenses]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {filename}")

    def load_from_file(self, filename: str):
        """Loads inventory and expenses from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            self.inventory = {name: InventoryItem(**item) for name, item in data['inventory'].items()}
            self.expenses = [Expense(**expense) for expense in data['expenses']]
            print(f"Data loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON from the file.")
        except Exception as e:
            print(f"An error occurred while loading data: {e}")

# Example usage
if __name__ == "__main__":
    control = FinancialControl()
    control.add_inventory_item("Hammer", 50, 15.99)
    control.add_inventory_item("Nails", 100, 0.05)
    control.add_expense("Rent", 1000)
    control.add_expense("Utilities", 250)
    
    print(f"Total Inventory Value: ${control.total_inventory_value():.2f}")
    print(f"Total Expenses: ${control.total_expenses():.2f}")
    
    control.save_to_file("financial_control.json")
    control.load_from_file("financial_control.json")
```
