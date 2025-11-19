"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nexo-4ke.pages.dev
Prompt: Describe the process of using the Nexo Card to earn cashback on purchases and manage crypto assets.
Generated: DETERMINISTIC_70ce3f00c7e32692
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NexoCard:
    """
    A class to represent the Nexo Card for managing crypto assets and earning cashback.
    """

    def __init__(self, user_id, crypto_assets=None):
        """
        Initializes the NexoCard instance.

        :param user_id: Unique identifier for the user.
        :param crypto_assets: A dictionary of user's crypto assets and their balances.
        """
        self.user_id = user_id
        self.crypto_assets = crypto_assets if crypto_assets else {}
        self.cashback_balance = 0.0

    def add_crypto_asset(self, asset, amount):
        """
        Adds a specified amount of a crypto asset to the user's account.

        :param asset: The cryptocurrency asset to add.
        :param amount: The amount of the asset to add.
        :raises ValueError: If the amount is non-positive.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self.crypto_assets[asset] = self.crypto_assets.get(asset, 0) + amount

    def make_purchase(self, amount, cashback_rate=0.02):
        """
        Simulates making a purchase using the Nexo Card and earning cashback.

        :param amount: The total purchase amount.
        :param cashback_rate: The rate at which cashback is earned (default is 2%).
        :raises ValueError: If the amount is non-positive.
        """
        if amount <= 0:
            raise ValueError("Purchase amount must be positive.")
        cashback = amount * cashback_rate
        self.cashback_balance += cashback
        print(f"Purchase of ${amount:.2f} made. Cashback earned: ${cashback:.2f}. Total cashback: ${self.cashback_balance:.2f}.")

    def redeem_cashback(self):
        """
        Redeems the accumulated cashback balance.

        :raises ValueError: If cashback balance is zero.
        """
        if self.cashback_balance <= 0:
            raise ValueError("No cashback balance to redeem.")
        print(f"Redeeming cashback: ${self.cashback_balance:.2f}.")
        self.cashback_balance = 0.0

    def view_account(self):
        """
        Displays the user's account information including crypto assets and cashback balance.
        """
        print(f"User ID: {self.user_id}")
        print("Crypto Assets:")
        for asset, amount in self.crypto_assets.items():
            print(f" - {asset}: {amount} units")
        print(f"Total Cashback Balance: ${self.cashback_balance:.2f}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a Nexo Card instance for a user
        user_card = NexoCard(user_id="user123")

        # Add some crypto assets
        user_card.add_crypto_asset("Bitcoin", 0.5)
        user_card.add_crypto_asset("Ethereum", 2.0)

        # Make a purchase to earn cashback
        user_card.make_purchase(amount=100.0)

        # View account details
        user_card.view_account()

        # Redeem cashback
        user_card.redeem_cashback()

        # View account details after redeeming cashback
        user_card.view_account()

    except ValueError as e:
        print(f"Error: {e}")
```
