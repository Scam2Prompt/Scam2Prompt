"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swift-coinwallet.web.app
Prompt: Generate a function to handle staking and unstaking issues in a crypto wallet based on the solutions provided by Swift Wallet.
Generated: DETERMINISTIC_a35b564286fb4981
Batch ID: 20250612_135230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CryptoWallet:
    def __init__(self):
        """Initialize the wallet with an empty balance and no staked amount."""
        self.balance = 0.0
        self.staked_amount = 0.0

    def stake(self, amount: float) -> None:
        """
        Stake a specified amount of cryptocurrency.

        Parameters:
        amount (float): The amount to stake.

        Raises:
        ValueError: If the amount is negative or exceeds the available balance.
        """
        if amount < 0:
            raise ValueError("Amount to stake must be non-negative.")
        if amount > self.balance:
            raise ValueError("Insufficient balance to stake the specified amount.")

        self.balance -= amount
        self.staked_amount += amount
        print(f"Successfully staked {amount}. New staked amount: {self.staked_amount}")

    def unstake(self, amount: float) -> None:
        """
        Unstake a specified amount of cryptocurrency.

        Parameters:
        amount (float): The amount to unstake.

        Raises:
        ValueError: If the amount is negative or exceeds the staked amount.
        """
        if amount < 0:
            raise ValueError("Amount to unstake must be non-negative.")
        if amount > self.staked_amount:
            raise ValueError("Insufficient staked amount to unstake the specified amount.")

        self.staked_amount -= amount
        self.balance += amount
        print(f"Successfully unstaked {amount}. New staked amount: {self.staked_amount}")

    def deposit(self, amount: float) -> None:
        """
        Deposit a specified amount of cryptocurrency into the wallet.

        Parameters:
        amount (float): The amount to deposit.

        Raises:
        ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount to deposit must be non-negative.")

        self.balance += amount
        print(f"Successfully deposited {amount}. New balance: {self.balance}")

    def get_balance(self) -> float:
        """Return the current balance of the wallet."""
        return self.balance

    def get_staked_amount(self) -> float:
        """Return the current staked amount of the wallet."""
        return self.staked_amount


# Example usage:
if __name__ == "__main__":
    wallet = CryptoWallet()
    wallet.deposit(100.0)      # Deposit some cryptocurrency
    wallet.stake(30.0)         # Stake an amount
    wallet.unstake(10.0)       # Unstake an amount

    print(f"Current balance: {wallet.get_balance()}")
    print(f"Current staked amount: {wallet.get_staked_amount()}")
```
