"""
Generated Code Metadata:
========================
Original URL: https://wallet-pi-nine.vercel.app
Prompt: Generate a function to calculate the total balance of a user's wallet, including available, delegated, rewards claimable, and undelegating balances, as shown on the webpage.
Generated: DETERMINISTIC_3528ed9a837f083d
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Wallet:
    def __init__(self, available: float, delegated: float, rewards_claimable: float, undelegating: float):
        """
        Initializes the Wallet instance with the given balances.

        :param available: The available balance in the wallet.
        :param delegated: The amount delegated from the wallet.
        :param rewards_claimable: The rewards that can be claimed.
        :param undelegating: The amount that is currently undelegating.
        """
        self.available = available
        self.delegated = delegated
        self.rewards_claimable = rewards_claimable
        self.undelegating = undelegating

    def calculate_total_balance(self) -> float:
        """
        Calculates the total balance of the wallet.

        Total balance is the sum of available, delegated, rewards claimable, and undelegating balances.

        :return: The total balance of the wallet.
        :raises ValueError: If any balance is negative.
        """
        # Validate that all balances are non-negative
        if any(balance < 0 for balance in [self.available, self.delegated, self.rewards_claimable, self.undelegating]):
            raise ValueError("Balances cannot be negative.")

        # Calculate total balance
        total_balance = (self.available + self.delegated +
                         self.rewards_claimable + self.undelegating)
        
        return total_balance


# Example usage
if __name__ == "__main__":
    try:
        # Create a wallet instance with sample balances
        user_wallet = Wallet(available=100.0, delegated=50.0, rewards_claimable=10.0, undelegating=5.0)
        
        # Calculate and print the total balance
        total_balance = user_wallet.calculate_total_balance()
        print(f"Total balance: {total_balance:.2f}")
    except ValueError as e:
        print(f"Error calculating total balance: {e}")
```
