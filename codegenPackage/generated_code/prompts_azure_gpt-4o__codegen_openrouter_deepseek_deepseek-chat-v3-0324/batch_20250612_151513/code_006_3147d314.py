"""
Generated Code Metadata:
========================
Original URL: https://hispanicservices.com
Prompt: Write a Python script to reconcile bank statements and generate a general ledger report for small businesses, as part of the accounting services provided by Hispanic Services.
Generated: DETERMINISTIC_3147d3149000f297
Batch ID: 20250612_151513
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
from collections import defaultdict
from typing import List, Dict, Tuple, Optional

class BankTransaction:
    """Represents a single bank transaction."""
    
    def __init__(self, date: str, description: str, amount: float, category: str = "Uncategorized"):
        self.date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        self.description = description.strip()
        self.amount = float(amount)
        self.category = category.strip()
    
    def __repr__(self):
        return f"BankTransaction(date={self.date}, description='{self.description}', amount={self.amount}, category='{self.category}')"

class GeneralLedgerEntry:
    """Represents a general ledger entry."""
    
    def __init__(self, date: datetime.date, account: str, debit: float = 0.0, credit: float = 0.0, description: str = ""):
        self.date = date
        self.account = account.strip()
        self.debit = float(debit)
        self.credit = float(credit)
        self.description = description.strip()
    
    def __repr__(self):
        return f"GeneralLedgerEntry(date={self.date}, account='{self.account}', debit={self.debit}, credit={self.credit}, description='{self.description}')"

class BankReconciler:
    """Handles bank statement reconciliation and general ledger generation."""
    
    def __init__(self):
        self.transactions: List[BankTransaction] = []
        self.ledger_entries: List[GeneralLedgerEntry] = []
        self.account_mapping: Dict[str, str] = {
            "Sales": "Income",
            "Rent": "Expenses",
            "Utilities": "Expenses",
            "Supplies": "Expenses",
            "Payroll": "Expenses",
            "Taxes": "Liabilities",
            "Uncategorized": "Equity"
        }
    
    def load_transactions(self, file_path: str) -> None:
        """Load transactions from a CSV file."""
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        transaction = BankTransaction(
                            date=row['Date'],
                            description=row['Description'],
                            amount=row['Amount'],
                            category=row.get('Category', 'Uncategorized')
                        )
                        self.transactions.append(transaction)
                    except (ValueError, KeyError) as e:
                        print(f"Error processing row {row}: {str(e)}")
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
        except Exception as e:
            print(f"Unexpected error loading transactions: {str(e)}")
    
    def categorize_transactions(self, custom_mapping: Optional[Dict[str, str]] = None) -> None:
        """Apply categorization to transactions based on description keywords."""
        mapping = {
            "sale": "Sales",
            "payment": "Sales",
            "rent": "Rent",
            "electric": "Utilities",
            "water": "Utilities",
            "internet": "Utilities",
            "supply": "Supplies",
            "payroll": "Payroll",
            "tax": "Taxes"
        }
        
        if custom_mapping:
            mapping.update(custom_mapping)
        
        for transaction in self.transactions:
            if transaction.category == "Uncategorized":
                for keyword, category in mapping.items():
                    if keyword.lower() in transaction.description.lower():
                        transaction.category = category
                        break
    
    def generate_ledger_entries(self) -> None:
        """Generate general ledger entries from transactions."""
        for transaction in self.transactions:
            account = self.account_mapping.get(transaction.category, "Equity")
            
            if transaction.amount >= 0:
                # Income or reduction in expense
                self.ledger_entries.append(GeneralLedgerEntry(
                    date=transaction.date,
                    account=account,
                    credit=transaction.amount,
                    description=transaction.description
                ))
                self.ledger_entries.append(GeneralLedgerEntry(
                    date=transaction.date,
                    account="Bank",
                    debit=transaction.amount,
                    description=transaction.description
                ))
            else:
                # Expense or reduction in income
                amount = abs(transaction.amount)
                self.ledger_entries.append(GeneralLedgerEntry(
                    date=transaction.date,
                    account=account,
                    debit=amount,
                    description=transaction.description
                ))
                self.ledger_entries.append(GeneralLedgerEntry(
                    date=transaction.date,
                    account="Bank",
                    credit=amount,
                    description=transaction.description
                ))
    
    def generate_report(self, output_file: str) -> None:
        """Generate a general ledger report in CSV format."""
        try:
            with open(output_file, mode='w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Date', 'Account', 'Debit', 'Credit', 'Description'])
                
                for entry in sorted(self.ledger_entries, key=lambda x: x.date):
                    writer.writerow([
                        entry.date.strftime("%Y-%m-%d"),
                        entry.account,
                        entry.debit,
                        entry.credit,
                        entry.description
                    ])
        except Exception as e:
            print(f"Error generating report: {str(e)}")
    
    def reconcile(self, input_file: str, output_file: str, custom_mapping: Optional[Dict[str, str]] = None) -> None:
        """Complete reconciliation process."""
        self.load_transactions(input_file)
        self.categorize_transactions(custom_mapping)
        self.generate_ledger_entries()
        self.generate_report(output_file)

def main():
    """Main execution function."""
    print("Bank Statement Reconciliation Tool for Hispanic Services")
    print("------------------------------------------------------")
    
    input_file = input("Enter path to bank statement CSV: ").strip()
    output_file = input("Enter path for output ledger CSV: ").strip()
    
    reconciler = BankReconciler()
    
    # Optional: Load custom category mapping
    use_custom = input("Do you want to use custom category mapping? (y/n): ").strip().lower()
    custom_mapping = None
    
    if use_custom == 'y':
        custom_mapping = {}
        print("Enter custom mappings (description keyword: account category)")
        print("Enter 'done' when finished")
        while True:
            mapping = input("Enter mapping (format 'keyword:category'): ").strip()
            if mapping.lower() == 'done':
                break
            if ':' in mapping:
                key, val = mapping.split(':', 1)
                custom_mapping[key.strip()] = val.strip()
    
    reconciler.reconcile(input_file, output_file, custom_mapping)
    print(f"Reconciliation complete. Report saved to {output_file}")

if __name__ == "__main__":
    main()
```
