"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coniproasset.com
Prompt: Create a Python program to generate a report of weekly transactions and active accounts for a cryptocurrency investment platform, inspired by the statistics shared on the Coni Pro Asset website.
Generated: DETERMINISTIC_10a0fd4806151a42
Batch ID: 20250612_154542
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
from datetime import datetime, timedelta
import logging

# Set up logging to handle errors and provide information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CryptoTransactionReport:
    def __init__(self, transaction_data):
        """
        Initializes the report generation with transaction data.

        :param transaction_data: DataFrame containing transaction records
        """
        self.transaction_data = transaction_data

    def filter_weekly_data(self):
        """
        Filters transactions to include only those from the past week.
        
        :return: DataFrame filtered to last week's transactions
        """
        try:
            # Getting the current date and the date one week ago
            end_date = datetime.now()
            start_date = end_date - timedelta(days=7)

            # Filtering the transaction data based on the date range
            weekly_data = self.transaction_data[(self.transaction_data['date'] >= start_date) & 
                                                (self.transaction_data['date'] <= end_date)]
            logging.info(f"Filtered data for the week from {start_date} to {end_date}")
            return weekly_data
        except Exception as e:
            logging.error("Error filtering weekly data: %s", e)
            raise

    def generate_report(self):
        """
        Generates a report of total transactions and active accounts for the past week.

        :return: Dictionary containing report data
        """
        try:
            weekly_data = self.filter_weekly_data()

            # Total transactions
            total_transactions = len(weekly_data)

            # Active accounts
            active_accounts = weekly_data['account_id'].nunique()

            report = {
                'total_transactions': total_transactions,
                'active_accounts': active_accounts,
                'report_date': datetime.now()
            }

            logging.info("Report generated successfully")
            return report
        except Exception as e:
            logging.error("Error generating report: %s", e)
            raise

def load_data(file_path):
    """
    Load transaction data from a CSV file.

    :param file_path: Path to the CSV file
    :return: DataFrame containing transaction data
    """
    try:
        data = pd.read_csv(file_path, parse_dates=['date'])
        logging.info("Data loaded successfully from %s", file_path)
        return data
    except FileNotFoundError:
        logging.error("File not found: %s", file_path)
        raise
    except pd.errors.EmptyDataError:
        logging.error("No data in the file: %s", file_path)
        raise
    except Exception as e:
        logging.error("An error occurred while loading data: %s", e)
        raise

def main():
    """
    Main function to execute the report generation.
    """
    try:
        # Load the transaction data
        transaction_data = load_data('transactions.csv')

        # Create a report generator instance
        report_generator = CryptoTransactionReport(transaction_data)

        # Generate the weekly report
        report = report_generator.generate_report()

        # Print the report
        print("Weekly Transaction Report")
        print("=========================")
        print(f"Total Transactions: {report['total_transactions']}")
        print(f"Active Accounts: {report['active_accounts']}")
        print(f"Report Date: {report['report_date']}")

    except Exception as e:
        logging.error("Failed to generate report: %s", e)

if __name__ == "__main__":
    main()
```
