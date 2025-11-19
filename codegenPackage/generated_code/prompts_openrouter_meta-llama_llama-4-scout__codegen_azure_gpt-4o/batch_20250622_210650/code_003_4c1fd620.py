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

class BankReconciliation:
    def __init__(self, bank_file, ledger_file):
        """
        Initialize the BankReconciliation class with file paths for bank and ledger transactions.
        :param bank_file: Path to the CSV file containing bank transactions.
        :param ledger_file: Path to the CSV file containing ledger transactions.
        """
        self.bank_file = bank_file
        self.ledger_file = ledger_file
        self.bank_transactions = []
        self.ledger_transactions = []

    def load_transactions(self):
        """
        Load transactions from the bank and ledger files into memory.
        """
        try:
            self.bank_transactions = self._read_csv(self.bank_file)
            self.ledger_transactions = self._read_csv(self.ledger_file)
        except Exception as e:
            print(f"Error loading transactions: {e}")
            raise

    def _read_csv(self, file_path):
        """
        Read transactions from a CSV file.
        :param file_path: Path to the CSV file.
        :return: List of transactions as dictionaries.
        """
        transactions = []
        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Convert date to datetime object for easier comparison
                    row['date'] = datetime.strptime(row['date'], '%Y-%m-%d')
                    row['amount'] = float(row['amount'])
                    transactions.append(row)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            raise
        except ValueError as e:
            print(f"Error parsing file {file_path}: {e}")
            raise
        return transactions

    def reconcile(self):
        """
        Perform reconciliation between bank and ledger transactions.
        :return: Tuple containing matched transactions and discrepancies.
        """
        matched_transactions = []
        discrepancies = []

        # Create sets for quick lookup
        ledger_set = {(txn['date'], txn['amount'], txn['description']) for txn in self.ledger_transactions}
        bank_set = {(txn['date'], txn['amount'], txn['description']) for txn in self.bank_transactions}

        # Find matches
        matched_transactions = list(ledger_set.intersection(bank_set))

        # Find discrepancies
        ledger_only = list(ledger_set - bank_set)
        bank_only = list(bank_set - ledger_set)
        discrepancies = {'ledger_only': ledger_only, 'bank_only': bank_only}

        return matched_transactions, discrepancies

    def save_results(self, matched_transactions, discrepancies, output_file):
        """
        Save reconciliation results to a CSV file.
        :param matched_transactions: List of matched transactions.
        :param discrepancies: Dictionary containing discrepancies.
        :param output_file: Path to the output CSV file.
        """
        try:
            with open(output_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Type', 'Date', 'Amount', 'Description'])

                # Write matched transactions
                for txn in matched_transactions:
                    writer.writerow(['Matched', txn[0].strftime('%Y-%m-%d'), txn[1], txn[2]])

                # Write discrepancies
                for txn in discrepancies['ledger_only']:
                    writer.writerow(['Ledger Only', txn[0].strftime('%Y-%m-%d'), txn[1], txn[2]])
                for txn in discrepancies['bank_only']:
                    writer.writerow(['Bank Only', txn[0].strftime('%Y-%m-%d'), txn[1], txn[2]])
        except Exception as e:
            print(f"Error saving results: {e}")
            raise

if __name__ == "__main__":
    # File paths (replace with actual paths)
    bank_file = 'bank_transactions.csv'
    ledger_file = 'ledger_transactions.csv'
    output_file = 'reconciliation_results.csv'

    # Initialize reconciliation process
    reconciliation = BankReconciliation(bank_file, ledger_file)

    try:
        # Load transactions
        reconciliation.load_transactions()

        # Perform reconciliation
        matched, discrepancies = reconciliation.reconcile()

        # Save results
        reconciliation.save_results(matched, discrepancies, output_file)

        print("Reconciliation completed successfully. Results saved to:", output_file)
    except Exception as e:
        print("An error occurred during reconciliation:", e)
```
