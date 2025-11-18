"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cham-transfers.com
Prompt: Suggest a library or API for integrating currency conversion (CHF, €, $) into a transportation booking platform, as seen on the Chamonix transfers webpage.
Generated: DETERMINISTIC_1c79ca71c994d9e4
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required library: forex-python
# Install with: pip install forex-python

from forex_python.converter import CurrencyRates, RatesNotAvailableError

def convert_currency(amount, from_currency, to_currency):
    """
    Converts a given amount from one currency to another using real-time exchange rates.
    
    :param amount: The numeric value to be converted (float or int)
    :param from_currency: The ISO currency code of the source currency (e.g., 'CHF', 'EUR', 'USD')
    :param to_currency: The ISO currency code of the target currency (e.g., 'CHF', 'EUR', 'USD')
    :return: Converted amount as a float
    :raises: ValueError if amount is invalid, RatesNotAvailableError if exchange rates are not available
    """
    try:
        # Check if the amount is valid
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        # Initialize the forex-python CurrencyRates class
        currency_rates = CurrencyRates()
        
        # Perform the currency conversion
        converted_amount = currency_rates.convert(from_currency, to_currency, amount)
        
        return converted_amount
    except RatesNotAvailableError as e:
        # Handle exception if exchange rates are not available
        raise RatesNotAvailableError(f"Currency conversion rates are unavailable: {e}")
    except ValueError as ve:
        # Handle invalid amount errors
        raise ValueError(f"Invalid input: {ve}")
    except Exception as ex:
        # Catch any other unexpected exceptions
        raise Exception(f"An unexpected error occurred: {ex}")

# Example usage:
if __name__ == "__main__":
    try:
        # Sample input: Convert 100 CHF to EUR
        source_currency = 'CHF'
        target_currency = 'EUR'
        amount_to_convert = 100

        # Perform conversion
        result = convert_currency(amount_to_convert, source_currency, target_currency)

        # Output the result
        print(f"{amount_to_convert} {source_currency} is equivalent to {result:.2f} {target_currency}.")
    except Exception as e:
        print(f"Error: {e}")
```
