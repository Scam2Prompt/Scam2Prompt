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
import pandas as pd
import numpy as np

class BankStatementReconciler:
    """
    A class to reconcile bank statements and generate a general ledger report.
    """

    def __init__(self, bank_statement_file, ledger_file):
        """
        Initializes the reconciler with bank statement and ledger file paths.

        :param bank_statement_file: Path to the bank statement CSV file.
        :param ledger_file: Path to the general ledger CSV file.
        """
        self.bank_statement_file = bank_statement_file
        self.ledger_file = ledger_file
        self.bank_statement = None
        self.ledger = None

    def load_data(self):
        """
        Loads bank statement and ledger data from CSV files.
        """
        try:
            self.bank_statement = pd.read_csv(self.bank_statement_file)
            self.ledger = pd.read_csv(self.ledger_file)
            print("Data loaded successfully.")
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
        Reconciles the bank statement with the ledger.
        
        :return: A DataFrame containing reconciled transactions.
        """
        if self.bank_statement is None or self.ledger is None:
            raise ValueError("Data not loaded. Please call load_data() first.")

        # Normalize column names for consistency
        self.bank_statement.columns = self.bank_statement.columns.str.strip().str.lower()
        self.ledger.columns = self.ledger.columns.str.strip().str.lower()

        # Merge bank statement and ledger on transaction details
        reconciled = pd.merge(self.bank_statement, self.ledger, on='transaction_id', how='outer', indicator=True)

        # Identify matched and unmatched transactions
        matched = reconciled[reconciled['_merge'] == 'both']
        unmatched_bank = reconciled[reconciled['_merge'] == 'left_only']
        unmatched_ledger = reconciled[reconciled['_merge'] == 'right_only']

        return matched, unmatched_bank, unmatched_ledger

    def generate_report(self, matched, unmatched_bank, unmatched_ledger):
        """
        Generates a reconciliation report.

        :param matched: DataFrame of matched transactions.
        :param unmatched_bank: DataFrame of unmatched bank transactions.
        :param unmatched_ledger: DataFrame of unmatched ledger transactions.
        """
        report = {
            'matched_transactions': matched,
            'unmatched_bank_transactions': unmatched_bank,
            'unmatched_ledger_transactions': unmatched_ledger
        }

        # Save the report to a CSV file
        report_file = 'reconciliation_report.csv'
        with pd.ExcelWriter(report_file) as writer:
            matched.to_csv(writer, sheet_name='Matched Transactions', index=False)
            unmatched_bank.to_csv(writer, sheet_name='Unmatched Bank Transactions', index=False)
            unmatched_ledger.to_csv(writer, sheet_name='Unmatched Ledger Transactions', index=False)

        print(f"Reconciliation report generated: {report_file}")

def main():
    """
    Main function to execute the reconciliation process.
    """
    bank_statement_file = 'bank_statement.csv'  # Path to the bank statement CSV
    ledger_file = 'general_ledger.csv'           # Path to the general ledger CSV

    reconciler = BankStatementReconciler(bank_statement_file, ledger_file)

    try:
        reconciler.load_data()
        matched, unmatched_bank, unmatched_ledger = reconciler.reconcile()
        reconciler.generate_report(matched, unmatched_bank, unmatched_ledger)
    except Exception as e:
        print(f"Reconciliation process failed: {e}")

if __name__ == "__main__":
    main()
```
