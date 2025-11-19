"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kantor-usdc.com
Prompt: Develop a function that simulates a cash exchange transaction for cryptocurrencies, incorporating a minimum amount of 250 PLN.
Generated: DETERMINISTIC_31a200da4aacaf69
Batch ID: 20250612_162408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InsufficientFundsError(Exception):
    """Custom exception class for insufficient funds."""
    pass

class CurrencyExchange:
    def __init__(self, exchange_rate):
        """
        Initialize the CurrencyExchange class with an exchange rate.

        :param exchange_rate: The rate at which the currency is exchanged.
        """
        self.exchange_rate = exchange_rate
    
    def exchange(self, amount, currency):
        """
        Simulate a cash exchange transaction for cryptocurrencies.

        :param amount: The amount of money to exchange.
        :param currency: The currency to exchange into.
        :raises InsufficientFundsError: If the amount is below the minimum.
        :return: The exchanged amount in the specified currency.
        """
        MINIMUM_AMOUNT = 250  # Minimum amount for the transaction in PLN
        
        # Check if the amount is sufficient for the transaction
        if amount < MINIMUM_AMOUNT:
            raise InsufficientFundsError(f"Transaction amount must be at least {MINIMUM_AMOUNT} PLN.")

        # Calculate the exchanged amount
        exchanged_amount = amount * self.exchange_rate

        # Log transaction details
        print(f"Exchanged {amount} PLN to {exchanged_amount} {currency} at a rate of {self.exchange_rate}.")
        
        return exchanged_amount

def main():
    # Example usage
    try:
        # Set up an exchange rate (example: 1 PLN = 0.22 BTC)
        exchange_rate = 0.22
        transaction = CurrencyExchange(exchange_rate)
        
        # Attempt to exchange an amount
        amount_to_exchange = 300  # This can be adjusted for testing
        currency = "BTC"
        result = transaction.exchange(amount_to_exchange, currency)
        
        print(f"Successfully exchanged to {result} {currency}.")
    except InsufficientFundsError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
