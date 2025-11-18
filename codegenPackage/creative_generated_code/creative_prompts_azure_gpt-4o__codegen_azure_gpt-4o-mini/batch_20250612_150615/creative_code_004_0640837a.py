"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panchsheelbank.com
Prompt: Write code to generate eStatements for savings accounts, referencing the banking services offered by Panchsheel Mercantile Co-op. Bank Ltd.
Generated: DETERMINISTIC_0640837a58c0c11b
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
from typing import List, Dict, Any

class SavingsAccount:
    """
    A class representing a savings account in Panchsheel Mercantile Co-op Bank Ltd.

    Attributes:
        account_number (str): The unique identifier for the savings account.
        account_holder (str): The name of the account holder.
        balance (float): The current balance of the account.
        transactions (List[Dict[str, Any]]): A list of transactions for the account.
    """

    def __init__(self, account_number: str, account_holder: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount: float) -> None:
        """Deposits a specified amount into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        self.transactions.append({
            "date": datetime.datetime.now(),
            "amount": amount,
            "type": "deposit"
        })

    def withdraw(self, amount: float) -> None:
        """Withdraws a specified amount from the account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= amount
        self.transactions.append({
            "date": datetime.datetime.now(),
            "amount": -amount,
            "type": "withdrawal"
        })

    def generate_statement(self) -> Dict[str, Any]:
        """Generates a statement for the savings account."""
        statement = {
            "account_number": self.account_number,
            "account_holder": self.account_holder,
            "balance": self.balance,
            "transactions": self.transactions,
            "date_generated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return statement


def save_statement_to_file(statement: Dict[str, Any], filename: str) -> None:
    """Saves the generated statement to a JSON file."""
    try:
        with open(filename, 'w') as f:
            json.dump(statement, f, indent=4)
    except IOError as e:
        print(f"Error saving statement to file: {e}")


def main():
    """Main function to demonstrate eStatement generation for a savings account."""
    try:
        # Creating a savings account instance
        account = SavingsAccount("123456", "John Doe", 1000.0)

        # Performing some transactions
        account.deposit(250.0)
        account.withdraw(100.0)

        # Generating the account statement
        statement = account.generate_statement()

        # Saving the statement to a file
        save_statement_to_file(statement, "estatement.json")
        print("eStatement generated successfully and saved to 'estatement.json'.")

    except ValueError as ve:
        print(f"ValueError occurred: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
