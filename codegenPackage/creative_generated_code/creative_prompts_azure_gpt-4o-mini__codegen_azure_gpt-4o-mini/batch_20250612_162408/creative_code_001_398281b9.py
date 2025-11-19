"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kantor-usdc.com
Prompt: Write a code snippet that calculates the transaction fee for exchanging Bitcoin to Euro at a rate of 4.7%.
Generated: DETERMINISTIC_398281b9ed788553
Batch ID: 20250612_162408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CurrencyExchange:
    """
    A class to represent a currency exchange operation.
    """

    def __init__(self, exchange_rate: float):
        """
        Initializes the CurrencyExchange with a specific exchange rate.

        :param exchange_rate: The rate at which Bitcoin is exchanged for Euro.
        """
        if exchange_rate <= 0:
            raise ValueError("Exchange rate must be a positive number.")
        self.exchange_rate = exchange_rate

    def calculate_transaction_fee(self, amount_in_btc: float) -> float:
        """
        Calculates the transaction fee for converting Bitcoin to Euro.

        :param amount_in_btc: The amount of Bitcoin to be converted.
        :return: The transaction fee in Euro.
        """
        if amount_in_btc < 0:
            raise ValueError("Amount in Bitcoin must be a non-negative number.")
        
        # Calculate the fee as a percentage of the amount in Bitcoin
        fee_percentage = self.exchange_rate / 100
        fee_in_euro = amount_in_btc * fee_percentage
        
        return fee_in_euro

# Example usage
if __name__ == "__main__":
    try:
        # Instantiate the CurrencyExchange with a rate of 4.7%
        exchange = CurrencyExchange(4.7)

        # Amount of Bitcoin to exchange
        amount_bitcoin = 1.0  # Example amount

        # Calculate the transaction fee
        transaction_fee = exchange.calculate_transaction_fee(amount_bitcoin)

        print(f"The transaction fee for exchanging {amount_bitcoin} BTC to Euro is: {transaction_fee:.2f} EUR")
    
    except ValueError as e:
        print(f"Error: {e}")
```
