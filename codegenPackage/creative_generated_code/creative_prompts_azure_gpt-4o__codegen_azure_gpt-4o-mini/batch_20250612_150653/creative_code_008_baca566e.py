"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reckonmexico.com
Prompt: Generate code to implement a control system for monitoring internal financial processes, inspired by Reckon Business Consulting's audit services.
Generated: DETERMINISTIC_baca566e0a50c779
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from dataclasses import dataclass, field
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class FinancialTransaction:
    transaction_id: str
    amount: float
    transaction_type: str  # 'income' or 'expense'
    description: str
    date: str  # YYYY-MM-DD format

@dataclass
class FinancialReport:
    transactions: List[FinancialTransaction] = field(default_factory=list)

    def add_transaction(self, transaction: FinancialTransaction):
        """Adds a financial transaction to the report."""
        if not isinstance(transaction, FinancialTransaction):
            logging.error("Invalid transaction type")
            raise ValueError("Invalid transaction type")
        self.transactions.append(transaction)
        logging.info(f"Transaction added: {transaction}")

    def generate_summary(self) -> Dict[str, Any]:
        """Generates a summary report of all transactions."""
        total_income = sum(t.amount for t in self.transactions if t.transaction_type == 'income')
        total_expenses = sum(t.amount for t in self.transactions if t.transaction_type == 'expense')
        balance = total_income - total_expenses

        summary = {
            "total_income": total_income,
            "total_expenses": total_expenses,
            "balance": balance
        }

        logging.info(f"Generated summary report: {summary}")
        return summary

class FinancialControlSystem:
    def __init__(self):
        """Initializes the financial control system with an empty report."""
        self.report = FinancialReport()
        logging.info("Financial Control System initialized.")

    def process_transaction(self, transaction_data: Dict[str, Any]):
        """Processes a new financial transaction."""
        try:
            transaction = FinancialTransaction(
                transaction_id=transaction_data['transaction_id'],
                amount=float(transaction_data['amount']),
                transaction_type=transaction_data['transaction_type'],
                description=transaction_data['description'],
                date=transaction_data['date']
            )
            self.report.add_transaction(transaction)
        except KeyError as e:
            logging.error(f"Missing key in transaction data: {e}")
            raise ValueError(f"Missing key in transaction data: {e}")
        except ValueError as e:
            logging.error(f"Error processing transaction: {e}")
            raise ValueError(f"Error processing transaction: {e}")

    def get_report_summary(self) -> Dict[str, Any]:
        """Retrieves the summary report."""
        return self.report.generate_summary()

# Example usage:
if __name__ == "__main__":
    fcs = FinancialControlSystem()

    # Sample data for transactions
    transactions_data = [
        {"transaction_id": "1", "amount": 1000.0, "transaction_type": "income", "description": "Consulting Revenue", "date": "2023-10-01"},
        {"transaction_id": "2", "amount": 300.0, "transaction_type": "expense", "description": "Office Supplies", "date": "2023-10-02"},
        {"transaction_id": "3", "amount": 150.0, "transaction_type": "expense", "description": "Software License", "date": "2023-10-03"},
    ]

    # Process transactions
    for data in transactions_data:
        try:
            fcs.process_transaction(data)
        except ValueError as e:
            logging.error(e)

    # Get report summary
    summary = fcs.get_report_summary()
    logging.info(f"Final Financial Summary: {summary}")
```
