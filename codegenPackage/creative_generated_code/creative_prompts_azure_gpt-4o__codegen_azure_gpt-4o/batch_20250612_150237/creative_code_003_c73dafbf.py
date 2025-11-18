"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fxbinaryinvestpro.com
Prompt: Provide a script for monitoring account balances and transaction logs, as described in Fxbinaryinvestpro's investment dashboard.
Generated: DETERMINISTIC_c73dafbf0472a86e
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='investment_dashboard.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class InvestmentDashboardMonitor:
    """
    A class to monitor account balances and transaction logs from an investment dashboard.
    """

    def __init__(self, account_data_file, transaction_log_file):
        """
        Initialize the monitor with file paths for account data and transaction logs.

        Args:
            account_data_file (str): Path to the JSON file containing account balance data.
            transaction_log_file (str): Path to the JSON file containing transaction log data.
        """
        self.account_data_file = account_data_file
        self.transaction_log_file = transaction_log_file

    def load_data(self, file_path):
        """
        Load JSON data from a file.

        Args:
            file_path (str): Path to the JSON file.

        Returns:
            dict: Parsed JSON data.

        Raises:
            Exception: If the file cannot be read or JSON parsing fails.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError as e:
            logging.error(f"File not found: {file_path}. Exception: {e}")
            raise
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON from file: {file_path}. Exception: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error loading file {file_path}. Exception: {e}")
            raise

    def monitor_balances(self):
        """
        Monitor account balances and log warnings if balance is below a threshold.
        """
        try:
            account_data = self.load_data(self.account_data_file)
            for account in account_data.get("accounts", []):
                account_id = account.get("account_id")
                balance = account.get("balance", 0)
                if balance < 500:  # Example threshold
                    logging.warning(f"Account {account_id} has a low balance: ${balance:.2f}")
                else:
                    logging.info(f"Account {account_id} balance is healthy: ${balance:.2f}")
        except Exception as e:
            logging.error(f"Failed to monitor balances. Exception: {e}")

    def monitor_transactions(self):
        """
        Monitor transaction logs and log any suspicious transactions.
        """
        try:
            transaction_logs = self.load_data(self.transaction_log_file)
            for transaction in transaction_logs.get("transactions", []):
                transaction_id = transaction.get("transaction_id")
                amount = transaction.get("amount", 0)
                transaction_type = transaction.get("type", "").lower()

                # Example of flagging high-value or suspicious transactions
                if amount > 10000:  # Example threshold for high-value transactions
                    logging.warning(
                        f"Suspicious transaction detected. ID: {transaction_id}, Amount: ${amount:.2f}, Type: {transaction_type}"
                    )
                else:
                    logging.info(
                        f"Transaction logged. ID: {transaction_id}, Amount: ${amount:.2f}, Type: {transaction_type}"
                    )
        except Exception as e:
            logging.error(f"Failed to monitor transactions. Exception: {e}")

    def run_monitoring(self):
        """
        Run monitoring for both balances and transactions.
        """
        logging.info("Starting monitoring...")
        self.monitor_balances()
        self.monitor_transactions()
        logging.info("Monitoring completed.")

# Example usage
if __name__ == "__main__":
    # Replace 'account_data.json' and 'transaction_logs.json' with actual file paths
    monitor = InvestmentDashboardMonitor('account_data.json', 'transaction_logs.json')
    monitor.run_monitoring()
```
