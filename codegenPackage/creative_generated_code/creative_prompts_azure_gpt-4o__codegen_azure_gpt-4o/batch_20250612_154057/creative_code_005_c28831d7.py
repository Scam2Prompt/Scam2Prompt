"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://guardian-associates.com
Prompt: Write code to track and visualize Rolling Reserve account movements, providing real-time monitoring and detailed reporting, similar to the solutions offered by Guardian Associates.
Generated: DETERMINISTIC_c28831d7f3c87397
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import matplotlib.pyplot as plt
import logging


class RollingReserveTracker:
    """
    A class to track and visualize Rolling Reserve account movements.
    Provides real-time monitoring and generates detailed reports.
    """
    def __init__(self):
        """
        Initializes the RollingReserveTracker with empty data structures.
        """
        self.transactions = []  # List to store all transactions
        self.reserves = {}      # Dictionary to store reserve balances by date
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def add_transaction(self, transaction_date, amount, transaction_type):
        """
        Adds a transaction to the system.

        :param transaction_date: (datetime.date) The date of the transaction
        :param amount: (float) The amount of the transaction
        :param transaction_type: (str) Type of transaction ('credit' or 'debit')
        :raises ValueError: If transaction_type is not valid
        """
        if transaction_type not in ['credit', 'debit']:
            raise ValueError("Invalid transaction type. Must be 'credit' or 'debit'.")

        transaction = {
            'date': transaction_date,
            'amount': amount,
            'type': transaction_type
        }
        self.transactions.append(transaction)

        # Update reserve balances
        self._update_reserve_balance(transaction_date, amount, transaction_type)

        logging.info(f"Transaction added: {transaction}")

    def _update_reserve_balance(self, transaction_date, amount, transaction_type):
        """
        Updates the reserve balance based on the transaction.

        :param transaction_date: (datetime.date) The date of the transaction
        :param amount: (float) The amount of the transaction
        :param transaction_type: (str) Type of transaction ('credit' or 'debit')
        """
        if transaction_date not in self.reserves:
            self.reserves[transaction_date] = 0.0

        if transaction_type == 'credit':
            self.reserves[transaction_date] += amount
        elif transaction_type == 'debit':
            self.reserves[transaction_date] -= amount

    def generate_report(self):
        """
        Generates a detailed report of all transactions and reserves.

        :return: (str) Formatted report string
        """
        report = "Rolling Reserve Account Report\n"
        report += "-----------------------------------------\n"
        report += "Transactions:\n"
        for transaction in self.transactions:
            report += f"Date: {transaction['date']}, Amount: {transaction['amount']}, Type: {transaction['type']}\n"

        report += "\nReserve Balances:\n"
        for date, balance in sorted(self.reserves.items()):
            report += f"Date: {date}, Balance: {balance:.2f}\n"

        logging.info("Report generated.")
        return report

    def visualize_reserve_balance(self):
        """
        Visualizes the reserve balance over time using a line chart.
        """
        if not self.reserves:
            logging.warning("No reserve data available to visualize.")
            return

        dates = sorted(self.reserves.keys())
        balances = [self.reserves[date] for date in dates]

        plt.figure(figsize=(10, 6))
        plt.plot(dates, balances, marker='o', label='Reserve Balance')
        plt.title('Rolling Reserve Balance Over Time')
        plt.xlabel('Date')
        plt.ylabel('Balance')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

        logging.info("Reserve balance visualization displayed.")


# Example usage:
if __name__ == "__main__":
    tracker = RollingReserveTracker()

    # Adding sample transactions
    try:
        tracker.add_transaction(datetime.date(2023, 1, 1), 1000.0, 'credit')
        tracker.add_transaction(datetime.date(2023, 1, 2), 500.0, 'debit')
        tracker.add_transaction(datetime.date(2023, 1, 3), 2000.0, 'credit')
    except ValueError as e:
        logging.error(f"Error adding transaction: {e}")

    # Generate and print report
    print(tracker.generate_report())

    # Visualize reserve balance
    tracker.visualize_reserve_balance()
```
