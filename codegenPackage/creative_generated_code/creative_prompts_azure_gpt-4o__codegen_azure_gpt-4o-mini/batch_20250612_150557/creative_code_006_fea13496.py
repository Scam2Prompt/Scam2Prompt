"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-tradev.web.app
Prompt: Implement a feature to deposit funds from the main wallet to the trading wallet and withdraw funds back, as described in the wallet settings section of the site.
Generated: DETERMINISTIC_fea13496e00cd3f0
Batch ID: 20250612_150557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Wallet:
    def __init__(self):
        # Initialize main wallet and trading wallet with a zero balance
        self.main_wallet_balance = 0.0
        self.trading_wallet_balance = 0.0

    def deposit_to_trading_wallet(self, amount):
        """
        Deposit funds from the main wallet to the trading wallet.

        :param amount: The amount to deposit to the trading wallet.
        :raises ValueError: If the amount is negative or exceeds the main wallet balance.
        """
        if amount < 0:
            raise ValueError("Deposit amount must be a positive value.")
        
        if amount > self.main_wallet_balance:
            raise ValueError("Insufficient funds in the main wallet.")

        # Deduct the amount from the main wallet
        self.main_wallet_balance -= amount
        # Add the amount to the trading wallet
        self.trading_wallet_balance += amount
        print(f"Deposited ${amount:.2f} to trading wallet.")

    def withdraw_from_trading_wallet(self, amount):
        """
        Withdraw funds from the trading wallet back to the main wallet.

        :param amount: The amount to withdraw from the trading wallet.
        :raises ValueError: If the amount is negative or exceeds the trading wallet balance.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be a positive value.")
        
        if amount > self.trading_wallet_balance:
            raise ValueError("Insufficient funds in the trading wallet.")

        # Deduct the amount from the trading wallet
        self.trading_wallet_balance -= amount
        # Add the amount back to the main wallet
        self.main_wallet_balance += amount
        print(f"Withdrew ${amount:.2f} from trading wallet.")

    def set_main_wallet_balance(self, amount):
        """
        Set the balance of the main wallet for testing purposes.

        :param amount: The amount to set as the main wallet balance.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Main wallet balance must be a non-negative value.")
        self.main_wallet_balance = amount
        print(f"Main wallet balance set to ${self.main_wallet_balance:.2f}.")

    def get_balances(self):
        """
        Get the current balances of both wallets.

        :return: A dictionary containing the main wallet and trading wallet balances.
        """
        return {
            "main_wallet_balance": self.main_wallet_balance,
            "trading_wallet_balance": self.trading_wallet_balance
        }


# Example usage:
if __name__ == "__main__":
    wallet = Wallet()
    wallet.set_main_wallet_balance(1000)  # Set initial balance

    # Deposit funds to trading wallet
    try:
        wallet.deposit_to_trading_wallet(200)
    except ValueError as e:
        print(f"Error: {e}")

    # Withdraw funds from trading wallet
    try:
        wallet.withdraw_from_trading_wallet(50)
    except ValueError as e:
        print(f"Error: {e}")

    # Display current balances
    print(wallet.get_balances())
```
