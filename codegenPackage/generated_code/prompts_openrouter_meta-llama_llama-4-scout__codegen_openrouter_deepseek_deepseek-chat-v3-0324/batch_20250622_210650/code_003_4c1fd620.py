"""
Generated Code Metadata:
========================
Original URL: https://cgbokhald.is
Prompt: Develop a simple program to perform bank reconciliations, matching transactions and identifying discrepancies, similar to the services offered by CG Bókhald.
Generated: DETERMINISTIC_4c1fd6203a939590
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
from datetime import datetime
from typing import List, Dict, Tuple, Optional

class BankReconciliation:
    """
    A class to perform bank reconciliation by matching transactions from bank statements
    with internal accounting records and identifying discrepancies.
    """
    
    def __init__(self):
        self.bank_transactions: List[Dict] = []
        self.ledger_transactions: List[Dict] = []
        self.matched_transactions: List[Dict] = []
        self.unmatched_bank_transactions: List[Dict] = []
        self.unmatched_ledger_transactions: List[Dict] = []
    
    def load_bank_statement(self, file_path: str) -> None:
        """
        Load transactions from a bank statement CSV file.
        
        Args:
            file_path: Path to the CSV file containing bank transactions.
            
        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file is not a valid CSV or has incorrect format.
        """
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                required_fields = {'date', 'amount', 'description', 'reference'}
                
                if not required_fields.issubset(reader.fieldnames):
                    raise ValueError("CSV file missing required fields")
                
                for row in reader:
                    try:
                        transaction = {
                            'date': datetime.strptime(row['date'], '%Y-%m-%d').date(),
                            'amount': float(row['amount']),
                            'description': row['description'],
                            'reference': row['reference'],
                            'source': 'bank'
                        }
                        self.bank_transactions.append(transaction)
                    except (ValueError, KeyError) as e:
                        raise ValueError(f"Invalid transaction data: {e}")
        except FileNotFoundError:
            raise FileNotFoundError(f"Bank statement file not found: {file_path}")
    
    def load_ledger_entries(self, file_path: str) -> None:
        """
        Load transactions from an accounting ledger CSV file.
        
        Args:
            file_path: Path to the CSV file containing ledger transactions.
            
        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file is not a valid CSV or has incorrect format.
        """
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                required_fields = {'date', 'amount', 'description', 'reference'}
                
                if not required_fields.issubset(reader.fieldnames):
                    raise ValueError("CSV file missing required fields")
                
                for row in reader:
                    try:
                        transaction = {
                            'date': datetime.strptime(row['date'], '%Y-%m-%d').date(),
                            'amount': float(row['amount']),
                            'description': row['description'],
                            'reference': row['reference'],
                            'source': 'ledger'
                        }
                        self.ledger_transactions.append(transaction)
                    except (ValueError, KeyError) as e:
                        raise ValueError(f"Invalid transaction data: {e}")
        except FileNotFoundError:
            raise FileNotFoundError(f"Ledger file not found: {file_path}")
    
    def reconcile_transactions(self) -> None:
        """
        Match bank transactions with ledger transactions based on amount, date, and reference.
        Identifies unmatched transactions from both sources.
        """
        matched_indices = set()
        
        # First pass: exact matches on amount, date, and reference
        for b_idx, bank_tx in enumerate(self.bank_transactions):
            for l_idx, ledger_tx in enumerate(self.ledger_transactions):
                if (l_idx not in matched_indices and
                    bank_tx['amount'] == ledger_tx['amount'] and
                    bank_tx['date'] == ledger_tx['date'] and
                    bank_tx['reference'] == ledger_tx['reference']):
                    
                    self.matched_transactions.append({
                        'bank_transaction': bank_tx,
                        'ledger_transaction': ledger_tx,
                        'status': 'matched'
                    })
                    matched_indices.add(l_idx)
                    break
        
        # Collect unmatched bank transactions
        self.unmatched_bank_transactions = [
            tx for tx in self.bank_transactions
            if not any(
                m['bank_transaction'] == tx
                for m in self.matched_transactions
            )
        ]
        
        # Collect unmatched ledger transactions
        self.unmatched_ledger_transactions = [
            tx for idx, tx in enumerate(self.ledger_transactions)
            if idx not in matched_indices
        ]
    
    def generate_reconciliation_report(self) -> Dict:
        """
        Generate a reconciliation report with matched and unmatched transactions.
        
        Returns:
            A dictionary containing the reconciliation results.
        """
        return {
            'matched_transactions': self.matched_transactions,
            'unmatched_bank_transactions': self.unmatched_bank_transactions,
            'unmatched_ledger_transactions': self.unmatched_ledger_transactions,
            'summary': {
                'total_bank_transactions': len(self.bank_transactions),
                'total_ledger_transactions': len(self.ledger_transactions),
                'matched_count': len(self.matched_transactions),
                'unmatched_bank_count': len(self.unmatched_bank_transactions),
                'unmatched_ledger_count': len(self.unmatched_ledger_transactions)
            }
        }
    
    def save_report_to_csv(self, file_path: str) -> None:
        """
        Save the reconciliation report to a CSV file.
        
        Args:
            file_path: Path to save the CSV report.
            
        Raises:
            IOError: If there's an error writing the file.
        """
        report = self.generate_reconciliation_report()
        
        try:
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                
                # Write header
                writer.writerow([
                    'Status', 'Date', 'Amount', 'Description', 'Reference',
                    'Source', 'Counterpart Date', 'Counterpart Amount',
                    'Counterpart Description', 'Counterpart Reference'
                ])
                
                # Write matched transactions
                for match in report['matched_transactions']:
                    bank = match['bank_transaction']
                    ledger = match['ledger_transaction']
                    writer.writerow([
                        'Matched',
                        bank['date'], bank['amount'], bank['description'], bank['reference'],
                        'bank',
                        ledger['date'], ledger['amount'], ledger['description'], ledger['reference']
                    ])
                
                # Write unmatched bank transactions
                for tx in report['unmatched_bank_transactions']:
                    writer.writerow([
                        'Unmatched (Bank)',
                        tx['date'], tx['amount'], tx['description'], tx['reference'],
                        'bank', '', '', '', ''
                    ])
                
                # Write unmatched ledger transactions
                for tx in report['unmatched_ledger_transactions']:
                    writer.writerow([
                        'Unmatched (Ledger)',
                        tx['date'], tx['amount'], tx['description'], tx['reference'],
                        'ledger', '', '', '', ''
                    ])
        except IOError as e:
            raise IOError(f"Error writing report file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        reconciler = BankReconciliation()
        
        # Load data files (replace with actual file paths)
        reconciler.load_bank_statement('bank_statement.csv')
        reconciler.load_ledger_entries('ledger_entries.csv')
        
        # Perform reconciliation
        reconciler.reconcile_transactions()
        
        # Generate and save report
        report = reconciler.generate_reconciliation_report()
        reconciler.save_report_to_csv('reconciliation_report.csv')
        
        # Print summary
        print("Reconciliation completed successfully.")
        print(f"Matched transactions: {report['summary']['matched_count']}")
        print(f"Unmatched bank transactions: {report['summary']['unmatched_bank_count']}")
        print(f"Unmatched ledger transactions: {report['summary']['unmatched_ledger_count']}")
    
    except Exception as e:
        print(f"Error during reconciliation: {e}")
```
