"""
Generated Code Metadata:
========================
Original URL: https://eximiousglobal.com
Prompt: Write a script to manage daily financial transactions such as recording sales, purchases, receipts, and payments, ensuring accurate bookkeeping as described in Eximious Global's administrative support services.
Generated: DETERMINISTIC_1d2cc46d7f28e475
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import datetime
import os
from typing import List, Dict, Optional

class Transaction:
    """Represents a financial transaction."""
    def __init__(self, date: str, description: str, amount: float, transaction_type: str, category: str):
        self.date = date
        self.description = description
        self.amount = amount
        self.type = transaction_type  # 'sale', 'purchase', 'receipt', 'payment'
        self.category = category

class FinancialManager:
    """Manages daily financial transactions."""
    def __init__(self, data_file: str = 'transactions.csv'):
        self.data_file = data_file
        self.transactions: List[Transaction] = []
        self._load_transactions()

    def _load_transactions(self) -> None:
        """Load transactions from CSV file if it exists."""
        if not os.path.exists(self.data_file):
            return

        with open(self.data_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    transaction = Transaction(
                        date=row['date'],
                        description=row['description'],
                        amount=float(row['amount']),
                        transaction_type=row['type'],
                        category=row['category']
                    )
                    self.transactions.append(transaction)
                except (ValueError, KeyError) as e:
                    print(f"Error loading transaction: {e}. Skipping row.")

    def _save_transactions(self) -> None:
        """Save transactions to CSV file."""
        fieldnames = ['date', 'description', 'amount', 'type', 'category']
        with open(self.data_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for transaction in self.transactions:
                writer.writerow({
                    'date': transaction.date,
                    'description': transaction.description,
                    'amount': transaction.amount,
                    'type': transaction.type,
                    'category': transaction.category
                })

    def add_transaction(self, description: str, amount: float, transaction_type: str, category: str) -> None:
        """Add a new transaction with current date."""
        try:
            date = datetime.datetime.now().strftime('%Y-%m-%d')
            transaction = Transaction(date, description, amount, transaction_type, category)
            self.transactions.append(transaction)
            self._save_transactions()
            print("Transaction added successfully.")
        except Exception as e:
            print(f"Error adding transaction: {e}")

    def get_transactions(self, start_date: Optional[str] = None, end_date: Optional[str] = None) -> List[Transaction]:
        """Retrieve transactions within a date range."""
        try:
            if not start_date and not end_date:
                return self.transactions

            filtered_transactions = []
            for transaction in self.transactions:
                trans_date = datetime.datetime.strptime(transaction.date, '%Y-%m-%d').date()
                
                if start_date:
                    start = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
                    if trans_date < start:
                        continue
                
                if end_date:
                    end = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
                    if trans_date > end:
                        continue
                
                filtered_transactions.append(transaction)
            
            return filtered_transactions
        except ValueError as e:
            print(f"Invalid date format: {e}. Use YYYY-MM-DD.")
            return []

    def get_summary(self) -> Dict[str, float]:
        """Get summary of transactions by type."""
        summary = {
            'sales': 0.0,
            'purchases': 0.0,
            'receipts': 0.0,
            'payments': 0.0,
            'total': 0.0
        }

        for transaction in self.transactions:
            summary[transaction.type + 's'] += transaction.amount
            summary['total'] += transaction.amount if transaction.type in ['sale', 'receipt'] else -transaction.amount

        return summary

    def delete_transaction(self, index: int) -> bool:
        """Delete a transaction by index."""
        try:
            if 0 <= index < len(self.transactions):
                del self.transactions[index]
                self._save_transactions()
                return True
            return False
        except Exception as e:
            print(f"Error deleting transaction: {e}")
            return False

def display_menu() -> None:
    """Display the main menu."""
    print("\nFinancial Transaction Manager")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. View Summary")
    print("4. Delete Transaction")
    print("5. Exit")

def main() -> None:
    """Main function to run the financial manager."""
    manager = FinancialManager()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            transaction_type = input("Enter type (sale/purchase/receipt/payment): ").lower()
            category = input("Enter category: ")
            manager.add_transaction(description, amount, transaction_type, category)

        elif choice == '2':
            start_date = input("Enter start date (YYYY-MM-DD) or leave blank: ")
            end_date = input("Enter end date (YYYY-MM-DD) or leave blank: ")
            transactions = manager.get_transactions(start_date or None, end_date or None)
            
            print("\nTransactions:")
            for idx, trans in enumerate(transactions):
                print(f"{idx}. {trans.date} - {trans.description} - {trans.type} - ${trans.amount:.2f} - {trans.category}")

        elif choice == '3':
            summary = manager.get_summary()
            print("\nFinancial Summary:")
            print(f"Sales: ${summary['sales']:.2f}")
            print(f"Purchases: ${summary['purchases']:.2f}")
            print(f"Receipts: ${summary['receipts']:.2f}")
            print(f"Payments: ${summary['payments']:.2f}")
            print(f"Net Total: ${summary['total']:.2f}")

        elif choice == '4':
            index = int(input("Enter transaction index to delete: "))
            if manager.delete_transaction(index):
                print("Transaction deleted successfully.")
            else:
                print("Invalid transaction index.")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
