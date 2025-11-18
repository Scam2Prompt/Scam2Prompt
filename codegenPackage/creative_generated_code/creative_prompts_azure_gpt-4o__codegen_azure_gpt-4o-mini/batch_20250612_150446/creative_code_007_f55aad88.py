"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eunitedcryptofx.com
Prompt: Generate a script to calculate and display total deposits, investments, and withdrawals, similar to the statistics shown on eunitedcryptofx.com.
Generated: DETERMINISTIC_f55aad888f2aa476
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class FinancialStatistics:
    def __init__(self):
        """Initialize total deposits, investments, and withdrawals."""
        self.total_deposits = 0.0
        self.total_investments = 0.0
        self.total_withdrawals = 0.0

    def add_deposit(self, amount):
        """Add a deposit amount to total deposits."""
        if amount < 0:
            raise ValueError("Deposit amount must be non-negative.")
        self.total_deposits += amount

    def add_investment(self, amount):
        """Add an investment amount to total investments."""
        if amount < 0:
            raise ValueError("Investment amount must be non-negative.")
        self.total_investments += amount

    def add_withdrawal(self, amount):
        """Add a withdrawal amount to total withdrawals."""
        if amount < 0:
            raise ValueError("Withdrawal amount must be non-negative.")
        self.total_withdrawals += amount

    def get_statistics(self):
        """Return a summary of the financial statistics."""
        return {
            "Total Deposits": self.total_deposits,
            "Total Investments": self.total_investments,
            "Total Withdrawals": self.total_withdrawals,
        }

    def display_statistics(self):
        """Display the financial statistics in a readable format."""
        stats = self.get_statistics()
        print("\nFinancial Statistics:")
        print("---------------------")
        for key, value in stats.items():
            print(f"{key}: ${value:.2f}")

def load_transactions(file_path):
    """Load transactions from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            transactions = json.load(file)
        return transactions
    except FileNotFoundError:
        raise FileNotFoundError("The specified file does not exist.")
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON data.")

def process_transactions(transactions, stats):
    """Process a list of transactions and update statistics."""
    for transaction in transactions:
        trans_type = transaction.get("type")
        amount = transaction.get("amount", 0.0)

        if trans_type == "deposit":
            stats.add_deposit(amount)
        elif trans_type == "investment":
            stats.add_investment(amount)
        elif trans_type == "withdrawal":
            stats.add_withdrawal(amount)
        else:
            raise ValueError(f"Unknown transaction type: {trans_type}")

def main():
    """Main function to execute the program."""
    stats = FinancialStatistics()
    
    # Specify the path to the transactions file
    transactions_file = "transactions.json"
    
    try:
        transactions = load_transactions(transactions_file)
        process_transactions(transactions, stats)
        stats.display_statistics()
    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
```
