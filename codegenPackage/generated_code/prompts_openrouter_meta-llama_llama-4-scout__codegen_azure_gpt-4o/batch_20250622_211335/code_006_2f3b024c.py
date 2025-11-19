"""
Generated Code Metadata:
========================
Original URL: https://guapzenith.com
Prompt: Write a code snippet to calculate and display the performance metrics of a cryptocurrency investment platform, including user growth, transactions, and withdrawal/deposit amounts, similar to Guapzenith's statistics.
Generated: DETERMINISTIC_2f3b024cfa60dff6
Batch ID: 20250622_211335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import random

class CryptoInvestmentPlatform:
    """
    A class to simulate and calculate performance metrics for a cryptocurrency investment platform.
    """

    def __init__(self):
        # Initialize platform statistics
        self.start_date = datetime.date(2020, 1, 1)
        self.current_date = datetime.date.today()
        self.user_growth = []  # List to store user growth over time
        self.transactions = []  # List to store transaction counts over time
        self.deposit_amounts = []  # List to store deposit amounts over time
        self.withdrawal_amounts = []  # List to store withdrawal amounts over time

    def simulate_data(self):
        """
        Simulates platform data for user growth, transactions, deposits, and withdrawals.
        """
        days_active = (self.current_date - self.start_date).days

        for day in range(days_active):
            # Simulate daily user growth
            self.user_growth.append(random.randint(50, 200))  # Random user growth per day

            # Simulate daily transactions
            self.transactions.append(random.randint(100, 500))  # Random transaction count per day

            # Simulate daily deposit amounts
            self.deposit_amounts.append(random.uniform(10000, 50000))  # Random deposit amount per day

            # Simulate daily withdrawal amounts
            self.withdrawal_amounts.append(random.uniform(5000, 30000))  # Random withdrawal amount per day

    def calculate_metrics(self):
        """
        Calculates and returns performance metrics for the platform.
        """
        total_users = sum(self.user_growth)
        total_transactions = sum(self.transactions)
        total_deposits = sum(self.deposit_amounts)
        total_withdrawals = sum(self.withdrawal_amounts)

        return {
            "Total Users": total_users,
            "Total Transactions": total_transactions,
            "Total Deposit Amount": round(total_deposits, 2),
            "Total Withdrawal Amount": round(total_withdrawals, 2),
            "Net Deposit Amount": round(total_deposits - total_withdrawals, 2)
        }

    def display_metrics(self):
        """
        Displays the calculated performance metrics in a readable format.
        """
        metrics = self.calculate_metrics()
        print("Performance Metrics for Cryptocurrency Investment Platform:")
        print(f"Start Date: {self.start_date}")
        print(f"Current Date: {self.current_date}")
        print(f"Total Users: {metrics['Total Users']}")
        print(f"Total Transactions: {metrics['Total Transactions']}")
        print(f"Total Deposit Amount: ${metrics['Total Deposit Amount']}")
        print(f"Total Withdrawal Amount: ${metrics['Total Withdrawal Amount']}")
        print(f"Net Deposit Amount: ${metrics['Net Deposit Amount']}")

# Main execution
if __name__ == "__main__":
    try:
        # Create an instance of the platform
        platform = CryptoInvestmentPlatform()

        # Simulate data
        platform.simulate_data()

        # Display performance metrics
        platform.display_metrics()
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")
```
