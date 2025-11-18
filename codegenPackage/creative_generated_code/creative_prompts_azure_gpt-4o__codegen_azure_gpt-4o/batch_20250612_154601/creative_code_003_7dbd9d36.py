"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeimpactpro.com
Prompt: Create a function in Python to simulate withdrawals and deposits for an investment account, ensuring the funds used for open positions are excluded, as described on Finance Impact Pro.
Generated: DETERMINISTIC_7dbd9d36e725bac1
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentAccount:
    def __init__(self, total_balance: float, funds_for_open_positions: float):
        """
        Initialize the InvestmentAccount with total balance and funds allocated for open positions.
        :param total_balance: Total amount of money in the account.
        :param funds_for_open_positions: Amount of money locked in open positions.
        """
        if total_balance < funds_for_open_positions:
            raise ValueError("Funds for open positions cannot exceed total balance.")
        self.total_balance = total_balance
        self.funds_for_open_positions = funds_for_open_positions
        self.available_balance = total_balance - funds_for_open_positions

    def deposit(self, amount: float):
        """
        Deposit an amount into the investment account.
        :param amount: Amount to deposit (must be positive).
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.total_balance += amount
        self.available_balance += amount
        print(f"Deposited ${amount:.2f}. Total Balance: ${self.total_balance:.2f}, Available Balance: ${self.available_balance:.2f}")

    def withdraw(self, amount: float):
        """
        Withdraw an amount from the available balance of the investment account.
        :param amount: Amount to withdraw (must be positive and <= available balance).
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.available_balance:
            raise ValueError("Insufficient available balance for withdrawal.")
        self.total_balance -= amount
        self.available_balance -= amount
        print(f"Withdrawn ${amount:.2f}. Total Balance: ${self.total_balance:.2f}, Available Balance: ${self.available_balance:.2f}")

    def __str__(self):
        """
        Return a string representation of the account's balances.
        """
        return (f"Total Balance: ${self.total_balance:.2f}, "
                f"Funds for Open Positions: ${self.funds_for_open_positions:.2f}, "
                f"Available Balance: ${self.available_balance:.2f}")


# Example usage:
if __name__ == "__main__":
    try:
        # Create an account with $1000 total balance and $300 allocated to open positions
        account = InvestmentAccount(total_balance=1000, funds_for_open_positions=300)
        print(account)

        # Perform a deposit of $200
        account.deposit(200)

        # Perform a withdrawal of $150
        account.withdraw(150)

        # Print final account state
        print(account)

    except ValueError as e:
        print(f"Error: {e}")
```
