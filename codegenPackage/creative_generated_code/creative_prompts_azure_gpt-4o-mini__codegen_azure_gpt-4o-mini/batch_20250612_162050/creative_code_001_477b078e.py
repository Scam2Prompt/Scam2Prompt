"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cgbokhald.is
Prompt: How can I implement a bank reconciliation feature in my accounting software based on the services offered by CGBókhald?
Generated: DETERMINISTIC_477b078e2b3e8f56
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from datetime import datetime

class BankReconciliation:
    def __init__(self, bank_statements_file, accounting_records_file):
        """
        Initialize the bank reconciliation with bank statements and accounting records.

        :param bank_statements_file: Path to the bank statements CSV file
        :param accounting_records_file: Path to the accounting records CSV file
        """
        self.bank_statements_file = bank_statements_file
        self.accounting_records_file = accounting_records_file
        self.bank_statements = self.load_data(bank_statements_file)
        self.accounting_records = self.load_data(accounting_records_file)

    def load_data(self, file_path):
        """
        Load CSV data into a pandas DataFrame.

        :param file_path: Path to the CSV file
        :return: DataFrame containing the data
        """
        try:
            data = pd.read_csv(file_path)
            print(f"Loaded data from {file_path} successfully.")
            return data
        except FileNotFoundError:
            raise Exception(f"File not found: {file_path}")
        except pd.errors.EmptyDataError:
            raise Exception(f"No data: {file_path} is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {str(e)}")

    def reconcile(self):
        """
        Reconcile bank statements with accounting records and return discrepancies.
        
        :return: DataFrame of discrepancies found during reconciliation
        """
        try:
            # Convert date columns to datetime for accurate comparisons
            self.bank_statements['Date'] = pd.to_datetime(self.bank_statements['Date'])
            self.accounting_records['Date'] = pd.to_datetime(self.accounting_records['Date'])
            
            # Merge the two dataframes on Date and Amount
            merged = pd.merge(self.bank_statements, self.accounting_records,
                              on=['Date', 'Amount'], how='outer', indicator=True)

            # Identify discrepancies
            discrepancies = merged[merged['_merge'] != 'both']
            if discrepancies.empty:
                print("No discrepancies found. Reconciliation successful.")
            else:
                print("Discrepancies found:")
                print(discrepancies)
                
            return discrepancies
        except Exception as e:
            raise Exception(f"An error occurred during reconciliation: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        bank_file = 'bank_statements.csv'
        accounting_file = 'accounting_records.csv'
        
        reconciliation = BankReconciliation(bank_file, accounting_file)
        discrepancies = reconciliation.reconcile()
        discrepancies.to_csv('discrepancies.csv', index=False)
    except Exception as e:
        print(f"Error: {str(e)}")
```
