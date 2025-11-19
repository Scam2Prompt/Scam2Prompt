"""
Generated Code Metadata:
========================
Original URL: https://sif.com.bo
Prompt: Create a Python program to manage preventive, administrative, extrajudicial, and judicial debt collection processes, inspired by the cobranzas services described on SIF's site.
Generated: DETERMINISTIC_9303c9821654e6a5
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import logging
from typing import List, Dict, Optional

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Debt:
    """Class representing a debt with its details."""
    
    def __init__(self, debtor_name: str, amount: float, due_date: datetime.date):
        self.debtor_name = debtor_name
        self.amount = amount
        self.due_date = due_date
        self.status = 'Pending'  # Status can be 'Pending', 'Paid', 'In Collection'

    def mark_as_paid(self):
        """Mark the debt as paid."""
        self.status = 'Paid'
        logging.info(f"Debt for {self.debtor_name} marked as paid.")

    def __str__(self):
        return f"Debt(debtor_name={self.debtor_name}, amount={self.amount}, due_date={self.due_date}, status={self.status})"


class DebtCollectionManager:
    """Class to manage debt collection processes."""
    
    def __init__(self):
        self.debts: List[Debt] = []

    def add_debt(self, debtor_name: str, amount: float, due_date: datetime.date):
        """Add a new debt to the collection."""
        if amount <= 0:
            logging.error("Attempted to add a debt with a non-positive amount.")
            raise ValueError("Debt amount must be positive.")
        if due_date < datetime.date.today():
            logging.error("Attempted to add a debt with a past due date.")
            raise ValueError("Due date must be in the future.")
        
        new_debt = Debt(debtor_name, amount, due_date)
        self.debts.append(new_debt)
        logging.info(f"Added debt: {new_debt}")

    def collect_debt(self, debtor_name: str):
        """Simulate the collection process for a specific debtor."""
        for debt in self.debts:
            if debt.debtor_name == debtor_name and debt.status == 'Pending':
                # Simulate collection process
                debt.mark_as_paid()
                logging.info(f"Debt collected from {debtor_name}.")
                return
        logging.warning(f"No pending debt found for {debtor_name}.")

    def get_debts(self) -> List[Dict[str, Optional[str]]]:
        """Return a list of all debts in a structured format."""
        return [{"debtor_name": debt.debtor_name, "amount": debt.amount, "due_date": debt.due_date, "status": debt.status} for debt in self.debts]

    def get_pending_debts(self) -> List[Dict[str, Optional[str]]]:
        """Return a list of all pending debts."""
        return [debt for debt in self.get_debts() if debt['status'] == 'Pending']


def main():
    """Main function to demonstrate the debt collection manager."""
    manager = DebtCollectionManager()
    
    try:
        # Adding debts
        manager.add_debt("John Doe", 1500.00, datetime.date(2023, 12, 1))
        manager.add_debt("Jane Smith", 2500.00, datetime.date(2024, 1, 15))
        
        # Collecting a debt
        manager.collect_debt("John Doe")
        
        # Displaying all debts
        logging.info("All debts:")
        for debt in manager.get_debts():
            logging.info(debt)
        
        # Displaying pending debts
        logging.info("Pending debts:")
        for debt in manager.get_pending_debts():
            logging.info(debt)

    except ValueError as e:
        logging.error(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
```
