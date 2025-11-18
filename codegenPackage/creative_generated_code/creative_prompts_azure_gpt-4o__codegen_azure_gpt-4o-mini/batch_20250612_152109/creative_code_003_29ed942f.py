"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bpkad.lamongankab.go.id
Prompt: Provide a step-by-step guide to implement a digital cash budget system similar to the "e-Bendahara" application for managing SPD, SPP, SPM, and SP2D processes, as outlined on the BPKAD Lamongan website.
Generated: DETERMINISTIC_29ed942f53033f10
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# digital_cash_budget_system.py

"""
Digital Cash Budget System

This is a simple implementation of a digital cash budget system, 
allowing for management of budget processes similar to the "e-Bendahara" application. 
This code includes management of SPD, SPP, SPM, and SP2D.

Usage:
    1. Initialize the system.
    2. Create, update, or delete budget items.
    3. Generate reports for budget management.
"""

import logging
from datetime import datetime
from typing import List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BudgetItem:
    """Class representing a budget item in the system."""
    
    def __init__(self, item_id: int, name: str, amount: float, date_created: Optional[datetime] = None):
        """Initialize a new budget item."""
        self.item_id = item_id
        self.name = name
        self.amount = amount
        self.date_created = date_created if date_created else datetime.now()
        logging.info(f"Created BudgetItem: {self}")

class DigitalCashBudget:
    """Class for managing a digital cash budget system."""
    
    def __init__(self):
        """Initialize an empty budget system."""
        self.budget_items: List[BudgetItem] = []
    
    def add_budget_item(self, item_id: int, name: str, amount: float):
        """Add a new budget item to the system."""
        if amount <= 0:
            logging.error("Amount must be greater than zero.")
            raise ValueError("Amount must be greater than zero.")
        
        new_item = BudgetItem(item_id, name, amount)
        self.budget_items.append(new_item)
        logging.info(f"Added BudgetItem: {new_item}")

    def update_budget_item(self, item_id: int, name: Optional[str] = None, amount: Optional[float] = None):
        """Update an existing budget item."""
        item = self.find_budget_item(item_id)
        if not item:
            logging.error(f"BudgetItem with id {item_id} not found.")
            raise ValueError(f"BudgetItem with id {item_id} not found.")
        
        if name is not None:
            item.name = name
        if amount is not None:
            if amount <= 0:
                logging.error("Amount must be greater than zero.")
                raise ValueError("Amount must be greater than zero.")
            item.amount = amount
        
        logging.info(f"Updated BudgetItem: {item}")

    def delete_budget_item(self, item_id: int):
        """Delete a budget item from the system."""
        item = self.find_budget_item(item_id)
        if item:
            self.budget_items.remove(item)
            logging.info(f"Deleted BudgetItem: {item}")
        else:
            logging.error(f"BudgetItem with id {item_id} not found.")
            raise ValueError(f"BudgetItem with id {item_id} not found.")

    def find_budget_item(self, item_id: int) -> Optional[BudgetItem]:
        """Find a budget item by its ID."""
        for item in self.budget_items:
            if item.item_id == item_id:
                return item
        return None

    def generate_report(self) -> str:
        """Generate a report of all budget items."""
        report_lines = ["Budget Report:"]
        total_amount = 0.0
        
        for item in self.budget_items:
            report_lines.append(f"ID: {item.item_id}, Name: {item.name}, Amount: {item.amount}, Created: {item.date_created}")
            total_amount += item.amount
        
        report_lines.append(f"Total Budget Amount: {total_amount}")
        report = "\n".join(report_lines)
        logging.info("Generated report.")
        return report

# Example usage:
if __name__ == "__main__":
    try:
        budget_system = DigitalCashBudget()
        budget_system.add_budget_item(1, "SPD Payment", 1500.00)
        budget_system.add_budget_item(2, "SPP Payment", 2000.00)
        
        print(budget_system.generate_report())
        
        budget_system.update_budget_item(1, amount=1800.00)
        print(budget_system.generate_report())
        
        budget_system.delete_budget_item(2)
        print(budget_system.generate_report())
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```

This code defines a digital cash budget management system with classes and methods for adding, updating, deleting, and reporting budget items. It incorporates error handling and logging for better traceability in production scenarios.
