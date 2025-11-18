"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supremeprofund.com
Prompt: Generate code to simulate deposit and withdrawal transactions for SupremeProFund's platform, ensuring the funds used in ongoing trades are excluded from the withdrawal amount.
Generated: DETERMINISTIC_4df677d5ff0b47ba
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# SupremeProFund Transaction Simulator
# Language: Python 3
# Description: Simulates deposit and withdrawal transactions while ensuring funds allocated to ongoing trades cannot be withdrawn.

class SupremeProFundAccount:
    def __init__(self, account_id):
        """
        Initialize the account with given account ID.
        """
        self.account_id = account_id
        self.total_balance = 0.0  # Total balance in the account
        self.funds_in_trades = 0.0  # Funds locked in ongoing trades

    def deposit(self, amount):
        """
        Deposits specified amount into the account.

        :param amount: Amount to deposit (must be positive)
        :raises ValueError: If deposit amount is not positive
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        self.total_balance += amount
        print(f"Deposit successful. New balance: ${self.total_balance:.2f}")

    def withdraw(self, amount):
        """
        Withdraws specified amount from the account, ensuring funds locked in trades are excluded.

        :param amount: Amount to withdraw (must be positive and within withdrawable funds)
        :raises ValueError: If withdrawal amount is invalid
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")
        
        withdrawable_balance = self.total_balance - self.funds_in_trades
        if amount > withdrawable_balance:
            raise ValueError(f"Insufficient withdrawable funds. Maximum available: ${withdrawable_balance:.2f}")
        
        self.total_balance -= amount
        print(f"Withdrawal successful. New balance: ${self.total_balance:.2f}")

    def allocate_trade_funds(self, amount):
        """
        Allocates specified amount of funds to trades, locking them from withdrawal.

        :param amount: Amount to allocate (must be positive and within total balance)
        :raises ValueError: If allocation amount is invalid
        """
        if amount <= 0:
            raise ValueError("Trade allocation amount must be greater than 0.")
        if amount > self.total_balance - self.funds_in_trades:
            raise ValueError(f"Insufficient funds to allocate to trades. Available balance: ${self.total_balance - self.funds_in_trades:.2f}")
        
        self.funds_in_trades += amount
        print(f"Funds allocated to trades successfully. Funds in trades: ${self.funds_in_trades:.2f}")

    def release_trade_funds(self, amount):
        """
        Releases specified amount of funds from trades, making them available for withdrawal.

        :param amount: Amount to release (must be positive and within funds locked in trades)
        :raises ValueError: If release amount is invalid
        """
        if amount <= 0:
            raise ValueError("Release amount must be greater than 0.")
        if amount > self.funds_in_trades:
            raise ValueError(f"Insufficient funds in trades to release. Current funds in trades: ${self.funds_in_trades:.2f}")
        
        self.funds_in_trades -= amount
        print(f"Funds released from trades successfully. Funds in trades: ${self.funds_in_trades:.2f}")

    def get_account_summary(self):
        """
        Returns a summary of the account status.

        :return: Dictionary containing account details
        """
        return {
            "Account ID": self.account_id,
            "Total Balance": self.total_balance,
            "Funds in Trades": self.funds_in_trades,
            "Withdrawable Balance": self.total_balance - self.funds_in_trades
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create a new account
        account = SupremeProFundAccount(account_id="SPF12345")

        # Simulate transactions
        account.deposit(1000)
        account.allocate_trade_funds(300)  # Lock $300 for trades
        account.withdraw(500)             # Attempt to withdraw $500
        account.release_trade_funds(200)  # Release $200 from trades
        account.withdraw(400)             # Attempt another withdrawal

        # Display account summary
        summary = account.get_account_summary()
        print("\nAccount Summary:")
        for key, value in summary.items():
            print(f"{key}: ${value:.2f}" if isinstance(value, float) else f"{key}: {value}")

    except Exception as e:
        print(f"Error: {e}")
```
