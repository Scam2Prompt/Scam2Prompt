"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-buyer-solution.com
Prompt: Create a script to deposit funds into a Bitcoin Buyer account and initiate the first investment, adhering to the platform's minimum balance requirement of $250.
Generated: DETERMINISTIC_403a06707e6fe4a4
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class BitcoinBuyerAccount:
    def __init__(self, username):
        """
        Initialize a Bitcoin Buyer account.
        :param username: The username of the account holder.
        """
        self.username = username
        self.balance = 0
        self.MIN_BALANCE = 250  # Minimum balance required to start investing

    def deposit_funds(self, amount):
        """
        Deposit funds into the Bitcoin Buyer account.
        :param amount: The amount to deposit (must be positive).
        :return: None
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        print(f"Deposited ${amount:.2f} into {self.username}'s account. Current balance: ${self.balance:.2f}")

    def initiate_investment(self):
        """
        Initiate the first investment if the minimum balance requirement is met.
        :return: None
        """
        if self.balance < self.MIN_BALANCE:
            raise ValueError(
                f"Insufficient balance to initiate investment. Minimum balance required: ${self.MIN_BALANCE}. Current balance: ${self.balance:.2f}"
            )
        print(f"Investment initiated successfully with a balance of ${self.balance:.2f}.")

def main():
    """
    Main function to handle user input and execute the deposit and investment process.
    """
    try:
        # Get user input for username and deposit amount
        username = input("Enter your username: ").strip()
        if not username:
            raise ValueError("Username cannot be empty.")

        deposit_amount = float(input("Enter the amount to deposit: "))
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")

        # Create account object
        account = BitcoinBuyerAccount(username)

        # Deposit funds
        account.deposit_funds(deposit_amount)

        # Attempt to initiate investment
        account.initiate_investment()

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using Bitcoin Buyer!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcess interrupted by the user.")
        sys.exit(1)
```
