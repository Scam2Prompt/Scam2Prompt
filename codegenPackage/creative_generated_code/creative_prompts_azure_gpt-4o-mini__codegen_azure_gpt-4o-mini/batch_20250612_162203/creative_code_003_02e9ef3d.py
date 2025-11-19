"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lkinc.co.za
Prompt: Develop a script that performs auditing checks on financial statements, referencing the auditing services offered by Lund & Kieck.
Generated: DETERMINISTIC_02e9ef3d0e0901e4
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import logging

# Setting up logging to capture audit processes and errors
logging.basicConfig(filename='audit_log.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class FinancialStatementAuditor:
    def __init__(self, statement_file):
        """
        Initializes the auditor with a financial statement file.

        :param statement_file: Path to the CSV file containing financial statements
        """
        self.statement_file = statement_file
        self.df = self.load_statement()

    def load_statement(self):
        """
        Loads the financial statement from a CSV file.

        :return: DataFrame containing the financial statement
        """
        try:
            df = pd.read_csv(self.statement_file)
            logging.info("Financial statement loaded successfully.")
            return df
        except Exception as e:
            logging.error(f"Error loading the financial statement: {e}")
            raise

    def check_balance_sheet(self):
        """
        Checks if the balance sheet is balanced (Assets = Liabilities + Equity).

        :return: Boolean indicating if the balance sheet is balanced
        """
        try:
            total_assets = self.df['Total Assets'].sum()
            total_liabilities = self.df['Total Liabilities'].sum()
            total_equity = self.df['Total Equity'].sum()
            balanced = total_assets == (total_liabilities + total_equity)
            logging.info(f"Balance Sheet Check: {'Balanced' if balanced else 'Not Balanced'}")
            return balanced
        except KeyError as e:
            logging.error(f"Column missing in financial statement: {e}")
            raise

    def check_profit_loss(self):
        """
        Checks if the net income calculated from revenues and expenses matches the reported net income.

        :return: Boolean indicating if the profit and loss statement is accurate
        """
        try:
            total_revenues = self.df['Total Revenues'].sum()
            total_expenses = self.df['Total Expenses'].sum()
            reported_net_income = self.df['Net Income'].sum()
            calculated_net_income = total_revenues - total_expenses
            accurate = reported_net_income == calculated_net_income
            logging.info(f"Profit and Loss Check: {'Accurate' if accurate else 'Inaccurate'}")
            return accurate
        except KeyError as e:
            logging.error(f"Column missing in financial statement: {e}")
            raise

    def run_audit(self):
        """
        Runs the complete audit process.

        :return: Dictionary with audit results
        """
        try:
            results = {
                "Balance Sheet Balanced": self.check_balance_sheet(),
                "Profit and Loss Accurate": self.check_profit_loss()
            }
            logging.info("Audit completed successfully.")
            return results
        except Exception as e:
            logging.error(f"Audit failed: {e}")
            raise

if __name__ == "__main__":
    # Example usage of the FinancialStatementAuditor class
    try:
        auditor = FinancialStatementAuditor("financial_statements.csv")
        audit_results = auditor.run_audit()
        print(audit_results)
    except Exception as e:
        print(f"An error occurred during auditing: {e}")
```
