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
import pandas as pd

class BankReconciliation:
    def __init__(self, bank_statement_file, ledger_file):
        """
        Initializes the BankReconciliation class with the provided bank statement and ledger files.

        :param bank_statement_file: Path to the bank statement CSV file.
        :param ledger_file: Path to the ledger CSV file.
        """
        self.bank_statement_file = bank_statement_file
        self.ledger_file = ledger_file
        self.bank_statement = None
        self.ledger = None

    def load_data(self):
        """
        Loads the bank statement and ledger data from CSV files into pandas DataFrames.
        """
        try:
            self.bank_statement = pd.read_csv(self.bank_statement_file)
            self.ledger = pd.read_csv(self.ledger_file)
            print("Data loaded successfully.")
        except FileNotFoundError as e:
            print(f"Error: {e}. Please check the file paths.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: One of the files is empty.")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

    def reconcile(self):
        """
        Reconciles the bank statement with the ledger to identify discrepancies.
        
        :return: A DataFrame containing matched transactions and discrepancies.
        """
        if self.bank_statement is None or self.ledger is None:
            print("Data not loaded. Please call load_data() first.")
            return None

        # Normalize the transaction columns for matching
        self.bank_statement['Transaction'] = self.bank_statement['Transaction'].str.strip().str.lower()
        self.ledger['Transaction'] = self.ledger['Transaction'].str.strip().str.lower()

        # Merge the bank statement and ledger on the 'Transaction' column
        merged_data = pd.merge(self.bank_statement, self.ledger, on='Transaction', how='outer', indicator=True)

        # Identify discrepancies
        discrepancies = merged_data[merged_data['_merge'] != 'both']

        return merged_data, discrepancies

    def save_results(self, merged_data, discrepancies, output_file):
        """
        Saves the merged data and discrepancies to an output CSV file.

        :param merged_data: DataFrame containing merged transactions.
        :param discrepancies: DataFrame containing discrepancies.
        :param output_file: Path to the output CSV file.
        """
        try:
            with pd.ExcelWriter(output_file) as writer:
                merged_data.to_csv(writer, sheet_name='Merged Transactions', index=False)
                discrepancies.to_csv(writer, sheet_name='Discrepancies', index=False)
            print(f"Results saved to {output_file}.")
        except Exception as e:
            print(f"Error saving results: {e}")
            raise

if __name__ == "__main__":
    # Example usage
    bank_statement_path = 'bank_statement.csv'
    ledger_path = 'ledger.csv'
    output_path = 'reconciliation_results.xlsx'

    reconciliation = BankReconciliation(bank_statement_path, ledger_path)
    reconciliation.load_data()
    merged_data, discrepancies = reconciliation.reconcile()
    
    if merged_data is not None and discrepancies is not None:
        reconciliation.save_results(merged_data, discrepancies, output_path)
```
