"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.guardian-associates.com
Prompt: Generate a sample report format for monitoring a Rolling Reserve account, including key metrics and financial movements.
Generated: DETERMINISTIC_662919c1e8014ab4
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import csv
from typing import List

# Define a class to represent the Rolling Reserve account
class RollingReserveAccount:
    def __init__(self, account_id: str, opening_balance: float):
        """
        Initialize the Rolling Reserve account.

        :param account_id: Unique identifier for the account
        :param opening_balance: The starting balance of the account
        """
        self.account_id = account_id
        self.opening_balance = opening_balance
        self.transactions = []  # List to store all financial movements

    def add_transaction(self, amount: float, description: str):
        """
        Add a new transaction to the account.

        :param amount: Positive for credit, negative for debit
        :param description: Description of the transaction
        """
        transaction = {
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "amount": amount,
            "description": description
        }
        self.transactions.append(transaction)

    def generate_report(self) -> List[dict]:
        """
        Generate a report of the account's activity and key metrics.

        :return: A list of dictionaries containing the report data
        """
        # Calculate key metrics
        closing_balance = self.opening_balance + sum(t["amount"] for t in self.transactions)
        total_credits = sum(t["amount"] for t in self.transactions if t["amount"] > 0)
        total_debits = sum(t["amount"] for t in self.transactions if t["amount"] < 0)

        # Build the report
        report = [
            {"Metric": "Opening Balance", "Value": self.opening_balance},
            {"Metric": "Total Credits", "Value": total_credits},
            {"Metric": "Total Debits", "Value": total_debits},
            {"Metric": "Closing Balance", "Value": closing_balance},
            {"Metric": "Number of Transactions", "Value": len(self.transactions)},
        ]

        return report

    def export_report_to_csv(self, file_name: str):
        """
        Export the account's report to a CSV file.

        :param file_name: Name of the output CSV file
        """
        report = self.generate_report()
        try:
            with open(file_name, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=["Metric", "Value"])
                writer.writeheader()
                writer.writerows(report)
            print(f"Report successfully exported to {file_name}")
        except Exception as e:
            print(f"Error exporting report to CSV: {e}")


# Main program
if __name__ == "__main__":
    # Initialize a Rolling Reserve account
    account = RollingReserveAccount(account_id="RR12345", opening_balance=10000.00)

    # Add some example transactions
    account.add_transaction(2000.00, "Reserve Addition")
    account.add_transaction(-500.00, "Reserve Withdrawal")
    account.add_transaction(300.00, "Interest Earned")

    # Generate and display the report
    report = account.generate_report()
    for item in report:
        print(f"{item['Metric']}: {item['Value']}")
    
    # Export the report to a CSV file
    account.export_report_to_csv("rolling_reserve_report.csv")
```
