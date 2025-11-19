"""
Generated Code Metadata:
========================
Original URL: https://aulaferretera.com
Prompt: Write Python code to create a financial control template for a hardware store, incorporating features like inventory tracking and expense management, as described in "Plantillas para control Financiero en la Ferretería" from Aula Ferretera.
Generated: DETERMINISTIC_c1303db14ff2df1c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import os
from datetime import datetime
from typing import List, Dict, Optional

class InventoryItem:
    """Class to represent an inventory item"""
    def __init__(self, item_id: str, name: str, category: str, quantity: int, 
                 unit_cost: float, selling_price: float, supplier: str):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.unit_cost = unit_cost
        self.selling_price = selling_price
        self.supplier = supplier

    def to_dict(self) -> Dict:
        """Convert item to dictionary for CSV storage"""
        return {
            'item_id': self.item_id,
            'name': self.name,
            'category': self.category,
            'quantity': self.quantity,
            'unit_cost': self.unit_cost,
            'selling_price': self.selling_price,
            'supplier': self.supplier
        }

class FinancialTransaction:
    """Class to represent a financial transaction"""
    def __init__(self, transaction_id: str, date: str, description: str, 
                 amount: float, transaction_type: str, category: str):
        self.transaction_id = transaction_id
        self.date = date
        self.description = description
        self.amount = amount
        self.transaction_type = transaction_type  # 'income' or 'expense'
        self.category = category

    def to_dict(self) -> Dict:
        """Convert transaction to dictionary for CSV storage"""
        return {
            'transaction_id': self.transaction_id,
            'date': self.date,
            'description': self.description,
            'amount': self.amount,
            'transaction_type': self.transaction_type,
            'category': self.category
        }

class HardwareStoreFinancialControl:
    """Main class for hardware store financial control system"""
    
    def __init__(self, data_dir: str = 'data'):
        self.data_dir = data_dir
        self.inventory_file = os.path.join(data_dir, 'inventory.csv')
        self.transactions_file = os.path.join(data_dir, 'transactions.csv')
        
        # Create data directory if it doesn't exist
        os.makedirs(data_dir, exist_ok=True)
        
        # Initialize files if they don't exist
        self._initialize_files()
    
    def _initialize_files(self):
        """Initialize CSV files with headers if they don't exist"""
        if not os.path.exists(self.inventory_file):
            with open(self.inventory_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=[
                    'item_id', 'name', 'category', 'quantity', 
                    'unit_cost', 'selling_price', 'supplier'
                ])
                writer.writeheader()
        
        if not os.path.exists(self.transactions_file):
            with open(self.transactions_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=[
                    'transaction_id', 'date', 'description', 
                    'amount', 'transaction_type', 'category'
                ])
                writer.writeheader()
    
    def add_inventory_item(self, item: InventoryItem) -> bool:
        """Add a new item to inventory"""
        try:
            with open(self.inventory_file, 'a', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=[
                    'item_id', 'name', 'category', 'quantity', 
                    'unit_cost', 'selling_price', 'supplier'
                ])
                writer.writerow(item.to_dict())
            return True
        except Exception as e:
            print(f"Error adding inventory item: {e}")
            return False
    
    def update_inventory_item(self, item_id: str, quantity_change: int) -> bool:
        """Update inventory quantity for an item"""
        try:
            items = []
            updated = False
            
            with open(self.inventory_file, 'r', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['item_id'] == item_id:
                        row['quantity'] = str(int(row['quantity']) + quantity_change)
                        updated = True
                    items.append(row)
            
            if updated:
                with open(self.inventory_file, 'w', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=[
                        'item_id', 'name', 'category', 'quantity', 
                        'unit_cost', 'selling_price', 'supplier'
                    ])
                    writer.writeheader()
                    writer.writerows(items)
                return True
            return False
        except Exception as e:
            print(f"Error updating inventory item: {e}")
            return False
    
    def get_inventory_item(self, item_id: str) -> Optional[InventoryItem]:
        """Get an inventory item by ID"""
        try:
            with open(self.inventory_file, 'r', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['item_id'] == item_id:
                        return InventoryItem(
                            item_id=row['item_id'],
                            name=row['name'],
                            category=row['category'],
                            quantity=int(row['quantity']),
                            unit_cost=float(row['unit_cost']),
                            selling_price=float(row['selling_price']),
                            supplier=row['supplier']
                        )
            return None
        except Exception as e:
            print(f"Error getting inventory item: {e}")
            return None
    
    def list_inventory(self) -> List[InventoryItem]:
        """List all inventory items"""
        items = []
        try:
            with open(self.inventory_file, 'r', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    items.append(InventoryItem(
                        item_id=row['item_id'],
                        name=row['name'],
                        category=row['category'],
                        quantity=int(row['quantity']),
                        unit_cost=float(row['unit_cost']),
                        selling_price=float(row['selling_price']),
                        supplier=row['supplier']
                    ))
        except Exception as e:
            print(f"Error listing inventory: {e}")
        return items
    
    def add_transaction(self, transaction: FinancialTransaction) -> bool:
        """Add a financial transaction"""
        try:
            with open(self.transactions_file, 'a', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=[
                    'transaction_id', 'date', 'description', 
                    'amount', 'transaction_type', 'category'
                ])
                writer.writerow(transaction.to_dict())
            return True
        except Exception as e:
            print(f"Error adding transaction: {e}")
            return False
    
    def list_transactions(self, start_date: str = None, end_date: str = None) -> List[FinancialTransaction]:
        """List all transactions, optionally filtered by date range"""
        transactions = []
        try:
            with open(self.transactions_file, 'r', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if start_date and end_date:
                        if not (start_date <= row['date'] <= end_date):
                            continue
                    transactions.append(FinancialTransaction(
                        transaction_id=row['transaction_id'],
                        date=row['date'],
                        description=row['description'],
                        amount=float(row['amount']),
                        transaction_type=row['transaction_type'],
                        category=row['category']
                    ))
        except Exception as e:
            print(f"Error listing transactions: {e}")
        return transactions
    
    def get_financial_summary(self, start_date: str = None, end_date: str = None) -> Dict:
        """Get financial summary (total income, expenses, and balance)"""
        transactions = self.list_transactions(start_date, end_date)
        income = 0.0
        expenses = 0.0
        
        for t in transactions:
            if t.transaction_type == 'income':
                income += t.amount
            else:
                expenses += t.amount
        
        return {
            'total_income': income,
            'total_expenses': expenses,
            'balance': income - expenses
        }
    
    def get_inventory_value(self) -> float:
        """Calculate total inventory value"""
        inventory = self.list_inventory()
        total_value = 0.0
        
        for item in inventory:
            total_value += item.quantity * item.unit_cost
        
        return total_value
    
    def generate_sales_report(self, start_date: str, end_date: str) -> Dict:
        """Generate sales report by category"""
        transactions = self.list_transactions(start_date, end_date)
        report = {}
        
        for t in transactions:
            if t.transaction_type == 'income':
                if t.category not in report:
                    report[t.category] = 0.0
                report[t.category] += t.amount
        
        return report

# Example usage
if __name__ == "__main__":
    store = HardwareStoreFinancialControl()
    
    # Add inventory items
    hammer = InventoryItem(
        item_id="TOOL001",
        name="Hammer",
        category="Tools",
        quantity=50,
        unit_cost=5.99,
        selling_price=12.99
