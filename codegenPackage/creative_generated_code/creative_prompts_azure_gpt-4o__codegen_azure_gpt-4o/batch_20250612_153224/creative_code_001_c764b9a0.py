"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alwan.om
Prompt: Recommend a library or API for integrating multi-currency support (e.g., OMR and USD) into an e-commerce site like Alwan.
Generated: DETERMINISTIC_c764b9a0be850b51
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: currency_integration.py

"""
This script demonstrates how to integrate multi-currency support using the 'forex-python' library.
The 'forex-python' library provides an easy-to-use API for currency exchange rates, conversions, and formatting.

Installation: 
Run `pip install forex-python` to install the library.

Production Usage:
Ensure proper error handling for network issues and invalid currency codes.
"""

from forex_python.converter import CurrencyRates, CurrencyCodes
from forex_python.bitcoin import BtcConverter
import logging

# Set up logging for error tracking and debugging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Initialize forex-python components
currency_rates = CurrencyRates()
currency_codes = CurrencyCodes()

def convert_currency(amount, from_currency, to_currency):
    """
    Converts an amount from one currency to another using live exchange rates.
    
    Args:
        amount (float): The amount to convert.
        from_currency (str): The source currency code (e.g., 'USD').
        to_currency (str): The target currency code (e.g., 'OMR').
    
    Returns:
        float: The converted amount.
    
    Raises:
        ValueError: If currency codes are invalid or amount is negative.
    """
    try:
        # Validate input
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        if not currency_codes.get_currency_name(from_currency):
            raise ValueError(f"Invalid source currency code: {from_currency}")
        if not currency_codes.get_currency_name(to_currency):
            raise ValueError(f"Invalid target currency code: {to_currency}")

        # Perform currency conversion
        converted_amount = currency_rates.convert(from_currency, to_currency, amount)
        return converted_amount
    
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

def get_currency_symbol(currency_code):
    """
    Retrieves the symbol of a given currency code.

    Args:
        currency_code (str): The currency code (e.g., 'USD').

    Returns:
        str: The currency symbol (e.g., '$').
    
    Raises:
        ValueError: If the currency code is invalid.
    """
    try:
        symbol = currency_codes.get_symbol(currency_code)
        if not symbol:
            raise ValueError(f"Invalid currency code: {currency_code}")
        return symbol
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

def main():
    """
    Demonstrates converting USD to OMR and retrieving currency symbols.
    """
    try:
        # Example usage
        amount = 100  # Convert $100 USD to OMR
        from_currency = 'USD'
        to_currency = 'OMR'

        logging.info(f"Converting {amount} {from_currency} to {to_currency}...")
        converted_amount = convert_currency(amount, from_currency, to_currency)
        symbol = get_currency_symbol(to_currency)

        logging.info(f"Converted Amount: {converted_amount:.2f} {symbol}")
    except Exception as e:
        logging.error(f"Failed to perform operations: {e}")

if __name__ == "__main__":
    main()
```
