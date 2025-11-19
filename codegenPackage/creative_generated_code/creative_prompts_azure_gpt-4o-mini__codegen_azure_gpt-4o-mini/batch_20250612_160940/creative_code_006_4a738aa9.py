"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://check-aml.com
Prompt: Describe how to automate the generation of tax reports using data from AMLBot's transaction records and wallet checks.
Generated: DETERMINISTIC_4a738aa9bab9e711
Batch ID: 20250612_160940
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
import os
import logging

# Set up logging for error tracking and information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TaxReportGenerator:
    def __init__(self, transaction_file: str, wallet_file: str, output_directory: str):
        """
        Initializes the TaxReportGenerator with the paths for transaction and wallet files,
        and the output directory for the generated report.

        :param transaction_file: Path to the CSV file containing transaction records.
        :param wallet_file: Path to the CSV file containing wallet checks.
        :param output_directory: Directory where the generated report will be saved.
        """
        self.transaction_file = transaction_file
        self.wallet_file = wallet_file
        self.output_directory = output_directory

    def load_data(self) -> pd.DataFrame:
        """
        Load transaction and wallet data into a DataFrame.

        :return: DataFrame containing combined transaction and wallet data.
        """
        try:
            # Load transaction data
            transactions = pd.read_csv(self.transaction_file)
            logging.info("Loaded transaction data successfully.")
            # Load wallet data
            wallets = pd.read_csv(self.wallet_file)
            logging.info("Loaded wallet data successfully.")
            # Combine data for report generation
            combined_data = pd.merge(transactions, wallets, on='wallet_id', how='left')
            return combined_data
        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
            raise
        except pd.errors.EmptyDataError as e:
            logging.error(f"Empty data error: {e}")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading data: {e}")
            raise

    def generate_report(self, combined_data: pd.DataFrame) -> None:
        """
        Generate a tax report from the combined transaction and wallet data.

        :param combined_data: DataFrame containing combined data.
        """
        try:
            # Calculate total income, expenses, and net profit
            report = {
                'Total Income': combined_data['income'].sum(),
                'Total Expenses': combined_data['expenses'].sum(),
                'Net Profit': combined_data['income'].sum() - combined_data['expenses'].sum(),
                'Total Transactions': combined_data.shape[0]
            }

            # Create a DataFrame for the report
            report_df = pd.DataFrame(report, index=[0])

            # Define the report filename based on the current date
            report_filename = f"tax_report_{datetime.now().strftime('%Y%m%d')}.csv"
            report_path = os.path.join(self.output_directory, report_filename)

            # Save the report to CSV
            report_df.to_csv(report_path, index=False)
            logging.info(f"Tax report generated successfully: {report_path}")
        except Exception as e:
            logging.error(f"An error occurred while generating the report: {e}")
            raise

    def run(self) -> None:
        """
        Execute the report generation process.
        """
        try:
            combined_data = self.load_data()
            self.generate_report(combined_data)
        except Exception as e:
            logging.error(f"Report generation process failed: {e}")

# Usage
if __name__ == "__main__":
    # Set the paths for transaction and wallet data files and the output directory
    transaction_file_path = 'path/to/transactions.csv'
    wallet_file_path = 'path/to/wallets.csv'
    output_directory_path = 'path/to/output/directory'

    # Create an instance of the TaxReportGenerator
    tax_report_generator = TaxReportGenerator(transaction_file_path, wallet_file_path, output_directory_path)

    # Run the report generation process
    tax_report_generator.run()
```
