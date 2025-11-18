"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masitsolutions.net
Prompt: Suggest a customized software solution for enterprise resource planning (ERP) based on MASIT Solutions' approach to tailored client-centric services.
Generated: DETERMINISTIC_8fe03e0ce9eacca1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
ERP System for MASIT Solutions

This module implements a customized Enterprise Resource Planning (ERP) system based 
on a client-centric approach, ensuring flexibility and scalability to meet enterprise needs.

Modules included:
- User Management
- Inventory Management
- Financial Management
- Reporting
"""

class User:
    """Class representing a user in the ERP system."""
    
    def __init__(self, username: str, role: str):
        self.username = username
        self.role = role


class InventoryItem:
    """Class representing an item in the inventory."""
    
    def __init__(self, item_id: str, name: str, quantity: int, price: float):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, amount: int):
        """Update the quantity of the inventory item."""
        if amount < 0 and abs(amount) > self.quantity:
            raise ValueError("Cannot reduce quantity below zero.")
        self.quantity += amount


class FinancialRecord:
    """Class representing a financial record."""
    
    def __init__(self, record_id: str, amount: float, transaction_type: str):
        self.record_id = record_id
        self.amount = amount
        self.transaction_type = transaction_type


class ERPSystem:
    """Main class for the ERP system, managing users, inventory, and finances."""
    
    def __init__(self):
        self.users = []
        self.inventory = {}
        self.financial_records = []

    def add_user(self, username: str, role: str):
        """Add a new user to the system."""
        user = User(username, role)
        self.users.append(user)

    def add_inventory_item(self, item_id: str, name: str, quantity: int, price: float):
        """Add a new item to the inventory."""
        if item_id in self.inventory:
            raise ValueError("Item ID already exists in inventory.")
        self.inventory[item_id] = InventoryItem(item_id, name, quantity, price)

    def record_financial_transaction(self, record_id: str, amount: float, transaction_type: str):
        """Record a financial transaction."""
        if transaction_type not in ['income', 'expense']:
            raise ValueError("Transaction type must be 'income' or 'expense'.")
        record = FinancialRecord(record_id, amount, transaction_type)
        self.financial_records.append(record)

    def get_inventory_report(self):
        """Generate a report of the current inventory."""
        report = {}
        for item in self.inventory.values():
            report[item.item_id] = {
                "name": item.name,
                "quantity": item.quantity,
                "price": item.price
            }
        return report

    def get_financial_report(self):
        """Generate a report of the financial transactions."""
        report = {}
        for record in self.financial_records:
            report[record.record_id] = {
                "amount": record.amount,
                "transaction_type": record.transaction_type
            }
        return report


# Example of initializing the ERP system and adding data
if __name__ == "__main__":
    try:
        erp_system = ERPSystem()
        
        # Adding users
        erp_system.add_user("admin", "Administrator")
        
        # Adding inventory items
        erp_system.add_inventory_item("item001", "Laptop", 10, 1200.00)
        erp_system.add_inventory_item("item002", "Monitor", 15, 300.00)

        # Recording financial transactions
        erp_system.record_financial_transaction("trans001", 12000, "income")
        erp_system.record_financial_transaction("trans002", 1500, "expense")

        # Generating reports
        inventory_report = erp_system.get_inventory_report()
        financial_report = erp_system.get_financial_report()

        print("Inventory Report:", inventory_report)
        print("Financial Report:", financial_report)

    except Exception as e:
        print(f"An error occurred: {e}")
```
