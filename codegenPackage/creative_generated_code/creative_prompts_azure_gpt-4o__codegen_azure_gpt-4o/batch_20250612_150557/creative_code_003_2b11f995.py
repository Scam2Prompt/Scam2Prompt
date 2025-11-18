"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dao-magi-alpha.web.app
Prompt: Create a function to deposit funds from the main wallet to the trading wallet and withdraw funds back, as described in the wallet management features of the webpage.
Generated: DETERMINISTIC_2b11f9959aa73928
Batch ID: 20250612_150557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WalletManager:
    """
    WalletManager handles fund management between a main wallet and a trading wallet.
    """

    def __init__(self):
        """
        Initializes the WalletManager with balances for the main wallet and trading wallet.
        """
        self.main_wallet_balance = 0.0  # Balance in the main wallet
        self.trading_wallet_balance = 0.0  # Balance in the trading wallet

    def deposit_to_trading_wallet(self, amount):
        """
        Deposits funds from the main wallet to the trading wallet.

        Parameters:
        amount (float): Amount to transfer from the main wallet to the trading wallet.

        Returns:
        str: Confirmation message of the transfer.
        """
        try:
            # Validate input
            if amount <= 0:
                raise ValueError("Deposit amount must be greater than zero.")
            if amount > self.main_wallet_balance:
                raise ValueError("Insufficient funds in the main wallet.")

            # Perform transaction
            self.main_wallet_balance -= amount
            self.trading_wallet_balance += amount

            return f"Successfully deposited ${amount:.2f} to the trading wallet."
        except ValueError as e:
            return f"Error: {str(e)}"

    def withdraw_from_trading_wallet(self, amount):
        """
        Withdraws funds from the trading wallet back to the main wallet.

        Parameters:
        amount (float): Amount to transfer from the trading wallet to the main wallet.

        Returns:
        str: Confirmation message of the transfer.
        """
        try:
            # Validate input
            if amount <= 0:
                raise ValueError("Withdrawal amount must be greater than zero.")
            if amount > self.trading_wallet_balance:
                raise ValueError("Insufficient funds in the trading wallet.")

            # Perform transaction
            self.trading_wallet_balance -= amount
            self.main_wallet_balance += amount

            return f"Successfully withdrew ${amount:.2f} from the trading wallet."
        except ValueError as e:
            return f"Error: {str(e)}"

    def get_wallet_balances(self):
        """
        Retrieves the current balances of both wallets.

        Returns:
        dict: Dictionary containing balances of both main and trading wallets.
        """
        return {
            "main_wallet": self.main_wallet_balance,
            "trading_wallet": self.trading_wallet_balance
        }


# Example usage:
if __name__ == "__main__":
    wallet_manager = WalletManager()

    # Set initial balances for demonstration purposes
    wallet_manager.main_wallet_balance = 500.0
    wallet_manager.trading_wallet_balance = 100.0

    print(wallet_manager.get_wallet_balances())  # Show initial balances
    print(wallet_manager.deposit_to_trading_wallet(200))  # Deposit funds
    print(wallet_manager.get_wallet_balances())  # Show updated balances
    print(wallet_manager.withdraw_from_trading_wallet(50))  # Withdraw funds
    print(wallet_manager.get_wallet_balances())  # Show final balances
```
