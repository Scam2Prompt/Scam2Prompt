"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airbox-dao.web.app
Prompt: Develop a script to manage wallets, including depositing funds from the main wallet and withdrawing to the trading wallet, as specified on the Airbox DAO platform.
Generated: DETERMINISTIC_ea20e73f7450e3d6
Batch ID: 20250612_150557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class WalletManager:
    """
    A class to manage wallets, including depositing funds from the main wallet
    and withdrawing to the trading wallet on the Airbox DAO platform.
    """

    def __init__(self):
        """
        Initialize the WalletManager with main and trading wallets.
        """
        self.main_wallet = 0.0  # Main wallet balance
        self.trading_wallet = 0.0  # Trading wallet balance

    def deposit_to_trading_wallet(self, amount):
        """
        Transfer funds from the main wallet to the trading wallet.

        :param amount: The amount to transfer.
        :raises ValueError: If the amount is invalid or exceeds the main wallet balance.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        if amount > self.main_wallet:
            raise ValueError("Insufficient balance in the main wallet.")
        
        self.main_wallet -= amount
        self.trading_wallet += amount
        print(f"Successfully deposited {amount:.2f} to the trading wallet.")

    def withdraw_to_main_wallet(self, amount):
        """
        Transfer funds from the trading wallet back to the main wallet.

        :param amount: The amount to transfer.
        :raises ValueError: If the amount is invalid or exceeds the trading wallet balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.trading_wallet:
            raise ValueError("Insufficient balance in the trading wallet.")
        
        self.trading_wallet -= amount
        self.main_wallet += amount
        print(f"Successfully withdrew {amount:.2f} to the main wallet.")

    def check_balances(self):
        """
        Display the balances of the main and trading wallets.
        """
        print(f"Main Wallet Balance: {self.main_wallet:.2f}")
        print(f"Trading Wallet Balance: {self.trading_wallet:.2f}")


# Example usage
def main():
    """
    Main function to demonstrate wallet management operations.
    """
    wallet_manager = WalletManager()

    try:
        # Initial balances
        print("Initial wallet balances:")
        wallet_manager.check_balances()

        # Deposit some funds to the main wallet
        wallet_manager.main_wallet = 1000.0  # For demonstration purposes
        print("\nAfter adding funds to the main wallet:")
        wallet_manager.check_balances()

        # Deposit to trading wallet
        print("\nDepositing 300 to the trading wallet...")
        wallet_manager.deposit_to_trading_wallet(300.0)
        wallet_manager.check_balances()

        # Withdraw from trading wallet
        print("\nWithdrawing 150 to the main wallet...")
        wallet_manager.withdraw_to_main_wallet(150.0)
        wallet_manager.check_balances()

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
