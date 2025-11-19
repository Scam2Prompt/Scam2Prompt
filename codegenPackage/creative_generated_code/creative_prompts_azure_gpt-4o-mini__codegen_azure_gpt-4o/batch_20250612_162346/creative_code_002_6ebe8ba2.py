"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherfi-turbo-etherfi-corp.vercel.app
Prompt: Explain how to use the ether.fi credit card for crypto payments and the benefits of earning cash back on purchases.
Generated: DETERMINISTIC_6ebe8ba22fb0db6d
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script explains how to use the ether.fi credit card for crypto payments
and calculates cashback benefits from purchases. The script is well-documented and follows
best practices, including error handling and production-ready standards.
"""

class EtherFiCreditCard:
    """
    A class representing the ether.fi credit card.
    """

    def __init__(self, cashback_rate: float):
        """
        Initialize the EtherFiCreditCard.

        :param cashback_rate: The percentage of cashback earned on purchases (e.g., 1.5 for 1.5%).
        """
        self.cashback_rate = cashback_rate
        self.transaction_history = []

    def make_payment(self, amount: float, crypto_type: str) -> float:
        """
        Simulate making a payment with the ether.fi credit card in cryptocurrency.

        :param amount: The purchase amount in USD.
        :param crypto_type: The cryptocurrency used for payment (e.g., 'ETH', 'BTC').
        :return: The amount of cashback earned.
        :raises ValueError: If the amount is less than or equal to zero.
        :raises ValueError: If the cryptocurrency type is not supported.
        """
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")
        
        supported_cryptos = ['ETH', 'BTC', 'USDC']
        if crypto_type not in supported_cryptos:
            raise ValueError(f"Unsupported cryptocurrency type: {crypto_type}. Supported types are {supported_cryptos}.")

        cashback = self._calculate_cashback(amount)
        self.transaction_history.append({
            "amount": amount,
            "crypto_type": crypto_type,
            "cashback_earned": cashback
        })
        return cashback

    def _calculate_cashback(self, amount: float) -> float:
        """
        Calculate the cashback earned on a purchase.

        :param amount: The purchase amount in USD.
        :return: The cashback amount in USD.
        """
        return round(amount * (self.cashback_rate / 100), 2)

    def get_transaction_history(self) -> list:
        """
        Get a list of all transactions made using the ether.fi credit card.

        :return: A list of transaction records.
        """
        return self.transaction_history

    def display_benefits(self):
        """
        Display the benefits of using the ether.fi credit card.
        """
        benefits = (
            "Benefits of using the ether.fi credit card:\n"
            "- Earn cashback on every purchase.\n"
            "- Make payments directly with supported cryptocurrencies (ETH, BTC, USDC).\n"
            "- Simplify your finances by integrating crypto payments easily."
        )
        print(benefits)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the card with a cashback rate of 1.5%
        etherfi_card = EtherFiCreditCard(cashback_rate=1.5)

        # Display card benefits
        etherfi_card.display_benefits()

        # Make a payment of $200 using Ethereum (ETH)
        cashback = etherfi_card.make_payment(amount=200, crypto_type="ETH")
        print(f"Cashback earned: ${cashback}")

        # View transaction history
        transactions = etherfi_card.get_transaction_history()
        print("Transaction History:", transactions)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
