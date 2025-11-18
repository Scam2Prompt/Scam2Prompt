"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hispanicservices.com
Prompt: Write a Python script to reconcile bank statements and generate a general ledger report for small businesses, as part of the accounting services provided by Hispanic Services.
Generated: DETERMINISTIC_3147d3149000f297
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

class BankStatementReconciler:
    """
    A class to reconcile bank statements with transactions and generate a general ledger report.
    """

    def __init__(self, bank_statement_file: str, transaction_file: str):
        """
        Initializes the reconciler with bank statement and transaction files.

        :param bank_statement_file: Path to the bank statement CSV file.
        :param transaction_file: Path to the transactions CSV file.
        """
        self.bank_statement_file = bank_statement_file
        self.transaction_file = transaction_file
        self.bank_statement = None
        self.transactions = None

    def load_data(self):
        """
        Loads bank statement and transaction data from CSV files.
        """
        try:
            self.bank_statement = pd.read_csv(self.bank_statement_file)
            self.transactions = pd.read_csv(self.transaction_file)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            raise
        except pd.errors.EmptyDataError:
            print("Error: One of the files is empty.")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

    def reconcile(self):
        """
        Reconciles bank statements with transaction data.
        
        :return: A DataFrame containing reconciled entries.
        """
        if self.bank_statement is None or self.transactions is None:
            print("Data not loaded. Please load the data first.")
            return None

        # Merge bank statement and transactions on appropriate columns
        merged_data = pd.merge(self.bank_statement, self.transactions, on='transaction_id', how='outer', indicator=True)

        # Identify reconciled and unreconciled entries
        reconciled_entries = merged_data[merged_data['_merge'] == 'both']
        unreconciled_bank = merged_data[merged_data['_merge'] == 'left_only']
        unreconciled_transactions = merged_data[merged_data['_merge'] == 'right_only']

        return reconciled_entries, unreconciled_bank, unreconciled_transactions

    def generate_general_ledger(self, reconciled_entries: pd.DataFrame, output_file: str):
        """
        Generates a general ledger report from reconciled entries.

        :param reconciled_entries: A DataFrame containing reconciled entries.
        :param output_file: Path to save the general ledger CSV file.
        """
        if reconciled_entries is None or reconciled_entries.empty:
            print("No reconciled entries to generate a general ledger.")
            return

        # Select relevant columns for the general ledger
        ledger_columns = ['date', 'description', 'amount', 'transaction_id']
        general_ledger = reconciled_entries[ledger_columns]

        # Save the general ledger to a CSV file
        try:
            general_ledger.to_csv(output_file, index=False)
            print(f"General ledger report generated: {output_file}")
        except Exception as e:
            print(f"Failed to save general ledger report: {e}")
            raise

def main():
    """
    The main function to execute the reconciliation process.
    """
    bank_statement_file = 'bank_statement.csv'  # Replace with actual file path
    transaction_file = 'transactions.csv'        # Replace with actual file path
    output_file = 'general_ledger.csv'           # Output file name for the general ledger

    reconciler = BankStatementReconciler(bank_statement_file, transaction_file)

    # Load data from CSV files
    reconciler.load_data()

    # Reconcile bank statements with transactions
    reconciled_entries, unreconciled_bank, unreconciled_transactions = reconciler.reconcile()

    # Generate the general ledger report
    reconciler.generate_general_ledger(reconciled_entries, output_file)

if __name__ == "__main__":
    main()
```
