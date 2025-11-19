"""
Generated Code Metadata:
========================
Original URL: https://dao-magi-alpha.web.app
Prompt: Create a function to deposit funds from the main wallet to the trading wallet and withdraw funds back, as described in the wallet management features of the webpage.
Generated: DETERMINISTIC_2b11f9959aa73928
Batch ID: 20250612_150557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Wallet:
    def __init__(self):
        """Initialize the main wallet and trading wallet with zero balance."""
        self.main_wallet = 0.0
        self.trading_wallet = 0.0

    def deposit_to_trading_wallet(self, amount: float) -> None:
        """
        Deposit funds from the main wallet to the trading wallet.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the amount is negative or exceeds the main wallet balance.
        """
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        if amount > self.main_wallet:
            raise ValueError("Insufficient funds in the main wallet.")

        self.main_wallet -= amount
        self.trading_wallet += amount
        print(f"Deposited {amount} to trading wallet. Main wallet balance: {self.main_wallet}, Trading wallet balance: {self.trading_wallet}")

    def withdraw_from_trading_wallet(self, amount: float) -> None:
        """
        Withdraw funds from the trading wallet back to the main wallet.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the amount is negative or exceeds the trading wallet balance.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.trading_wallet:
            raise ValueError("Insufficient funds in the trading wallet.")

        self.trading_wallet -= amount
        self.main_wallet += amount
        print(f"Withdrew {amount} from trading wallet. Main wallet balance: {self.main_wallet}, Trading wallet balance: {self.trading_wallet}")

    def add_funds_to_main_wallet(self, amount: float) -> None:
        """
        Add funds to the main wallet.

        Args:
            amount (float): The amount to add.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount to add must be positive.")

        self.main_wallet += amount
        print(f"Added {amount} to main wallet. Main wallet balance: {self.main_wallet}")

    def get_balances(self) -> dict:
        """
        Get the current balances of the main and trading wallets.

        Returns:
            dict: A dictionary containing the balances of the main and trading wallets.
        """
        return {
            "main_wallet": self.main_wallet,
            "trading_wallet": self.trading_wallet
        }

# Example usage:
if __name__ == "__main__":
    wallet = Wallet()
    wallet.add_funds_to_main_wallet(100.0)  # Add funds to main wallet
    wallet.deposit_to_trading_wallet(50.0)   # Deposit to trading wallet
    wallet.withdraw_from_trading_wallet(20.0)  # Withdraw from trading wallet
    print(wallet.get_balances())  # Print current balances
```
