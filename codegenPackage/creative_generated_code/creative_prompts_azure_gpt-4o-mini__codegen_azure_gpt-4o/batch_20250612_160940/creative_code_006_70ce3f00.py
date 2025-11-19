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
"""
Nexo Card Management System

This script simulates the process of using the Nexo Card to earn cashback on purchases
and manage crypto assets. It includes functionality for tracking purchases, calculating
cashback rewards, and managing crypto balances.

Requirements:
- Python >= 3.7
"""

import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class NexoCard:
    """
    Class to simulate the Nexo Card system for managing purchases, cashback, and crypto assets.
    """
    
    def __init__(self, crypto_balance: dict, cashback_rate: float):
        """
        Initialize the Nexo Card with crypto balances and cashback rate.

        :param crypto_balance: Dictionary containing available crypto assets and their balance (e.g., {"BTC": 1.5}).
        :param cashback_rate: Percentage rate for cashback rewards (e.g., 0.01 for 1%).
        """
        self.crypto_balance = crypto_balance
        self.cashback_rate = cashback_rate
        self.purchase_history = []  # Track all purchases

    def make_purchase(self, amount: float, currency: str) -> None:
        """
        Simulate making a purchase using the Nexo Card.

        :param amount: The amount of the purchase.
        :param currency: The cryptocurrency to use for cashback rewards.
        """
        if currency not in self.crypto_balance:
            logging.error(f"Currency {currency} not supported.")
            raise ValueError(f"Currency {currency} not available in the crypto balance.")
        
        cashback = self.calculate_cashback(amount)
        self.crypto_balance[currency] += cashback  # Add cashback to the crypto balance
        self.purchase_history.append({"amount": amount, "currency": currency, "cashback": cashback})
        logging.info(f"Purchase successful! Amount: ${amount:.2f}, Cashback: {cashback:.8f} {currency}")

    def calculate_cashback(self, amount: float) -> float:
        """
        Calculate cashback based on the purchase amount and cashback rate.

        :param amount: The amount of the purchase.
        :return: The cashback amount in the chosen cryptocurrency.
        """
        return amount * self.cashback_rate

    def get_crypto_balance(self) -> dict:
        """
        Retrieve the current crypto balance.

        :return: Dictionary of crypto balances.
        """
        return self.crypto_balance

    def get_purchase_history(self) -> list:
        """
        Retrieve the history of all purchases made with the card.

        :return: List of purchase records.
        """
        return self.purchase_history


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the Nexo Card with a crypto balance and cashback rate
        card = NexoCard(crypto_balance={"BTC": 0.5, "ETH": 10.0}, cashback_rate=0.01)  # 1% cashback

        # Perform some purchases
        card.make_purchase(amount=100.00, currency="BTC")  # $100 purchase with BTC cashback
        card.make_purchase(amount=50.00, currency="ETH")   # $50 purchase with ETH cashback

        # Retrieve and print balances
        print("Current Crypto Balances:", card.get_crypto_balance())

        # Retrieve and print purchase history
        print("Purchase History:")
        for purchase in card.get_purchase_history():
            print(purchase)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
