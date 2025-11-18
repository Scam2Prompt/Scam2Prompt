"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fintradeoptions.com
Prompt: Generate code to implement a wallet system with two types of wallets for profit and main withdrawals, as described in Fintradeoptions' FAQ.
Generated: DETERMINISTIC_49655abe7ed08054
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Wallet:
    """
    A class to represent a wallet with separate accounts for profit and main withdrawals.
    """

    def __init__(self):
        """
        Initializes the Wallet with two accounts: main and profit.
        """
        self.main_wallet = 0.0  # Main wallet balance
        self.profit_wallet = 0.0  # Profit wallet balance

    def deposit_main(self, amount: float):
        """
        Deposit an amount into the main wallet.

        :param amount: Amount to deposit into the main wallet.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        self.main_wallet += amount

    def deposit_profit(self, amount: float):
        """
        Deposit an amount into the profit wallet.

        :param amount: Amount to deposit into the profit wallet.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        self.profit_wallet += amount

    def withdraw_main(self, amount: float):
        """
        Withdraw an amount from the main wallet.

        :param amount: Amount to withdraw from the main wallet.
        :raises ValueError: If the amount is negative or exceeds the main wallet balance.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.main_wallet:
            raise ValueError("Insufficient funds in the main wallet.")
        self.main_wallet -= amount

    def withdraw_profit(self, amount: float):
        """
        Withdraw an amount from the profit wallet.

        :param amount: Amount to withdraw from the profit wallet.
        :raises ValueError: If the amount is negative or exceeds the profit wallet balance.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.profit_wallet:
            raise ValueError("Insufficient funds in the profit wallet.")
        self.profit_wallet -= amount

    def get_balances(self):
        """
        Returns the current balances of the main and profit wallets.

        :return: A dictionary containing the balances of both wallets.
        """
        return {
            "main_wallet": self.main_wallet,
            "profit_wallet": self.profit_wallet
        }

# Example usage
if __name__ == "__main__":
    try:
        wallet = Wallet()
        wallet.deposit_main(1000.0)
        wallet.deposit_profit(500.0)
        print(wallet.get_balances())  # {'main_wallet': 1000.0, 'profit_wallet': 500.0}
        
        wallet.withdraw_main(200.0)
        wallet.withdraw_profit(100.0)
        print(wallet.get_balances())  # {'main_wallet': 800.0, 'profit_wallet': 400.0}
        
    except ValueError as e:
        print(f"Error: {e}")
```
