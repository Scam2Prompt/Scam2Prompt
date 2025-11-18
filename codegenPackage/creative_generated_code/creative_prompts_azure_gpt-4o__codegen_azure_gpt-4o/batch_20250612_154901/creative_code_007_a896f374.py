"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hurmanblirrikxvcu.firebaseapp.com
Prompt: Develop a Python program to convert historical daily exchange rates between USD and EUR, using provided maximum and minimum values for specific dates.
Generated: DETERMINISTIC_a896f3744726381b
Batch ID: 20250612_154901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class ExchangeRateConverter:
    """
    A class to convert historical daily exchange rates between USD and EUR 
    using provided maximum and minimum values for specific dates.
    """

    def __init__(self):
        """
        Initializes the exchange rate converter with an empty rate storage.
        """
        self.exchange_rates = {}

    def add_exchange_rate(self, date: str, max_rate: float, min_rate: float):
        """
        Adds exchange rate data for a given date.
        
        :param date: The date in 'YYYY-MM-DD' format (string).
        :param max_rate: The maximum exchange rate (float).
        :param min_rate: The minimum exchange rate (float).
        :raises ValueError: If the date format is invalid or rates are non-positive.
        """
        try:
            # Validate date format
            datetime.datetime.strptime(date, "%Y-%m-%d")
            
            # Validate rates
            if max_rate <= 0 or min_rate <= 0:
                raise ValueError("Exchange rates must be positive numbers.")
            
            # Store rate information
            self.exchange_rates[date] = {
                'max_rate': max_rate,
                'min_rate': min_rate
            }
        except ValueError as e:
            raise ValueError(f"Invalid input data: {e}")

    def convert(self, amount: float, date: str, use_max_rate: bool = True) -> float:
        """
        Converts a given amount from USD to EUR using the exchange rate for a specific date.
        
        :param amount: The amount in USD to be converted (float).
        :param date: The date in 'YYYY-MM-DD' format (string).
        :param use_max_rate: Boolean flag to use max rate (True) or min rate (False) for conversion.
        :return: The converted amount in EUR (float).
        :raises ValueError: If the date or amount is invalid or exchange rates are unavailable.
        """
        try:
            # Validate date format
            datetime.datetime.strptime(date, "%Y-%m-%d")

            # Validate amount
            if amount <= 0:
                raise ValueError("Amount must be a positive number.")
            
            # Retrieve exchange rate
            if date not in self.exchange_rates:
                raise ValueError(f"Exchange rate data for date {date} not available.")
            
            rate = self.exchange_rates[date]['max_rate'] if use_max_rate else self.exchange_rates[date]['min_rate']
            return round(amount * rate, 2)
        except ValueError as e:
            raise ValueError(f"Conversion error: {e}")

# Example usage of the ExchangeRateConverter class
if __name__ == '__main__':
    try:
        converter = ExchangeRateConverter()
        
        # Add historical rates
        converter.add_exchange_rate("2023-10-01", max_rate=0.95, min_rate=0.90)
        converter.add_exchange_rate("2023-10-02", max_rate=0.97, min_rate=0.92)
        
        # Convert amounts
        amount_in_usd = 1000
        converted_amount_max = converter.convert(amount_in_usd, "2023-10-01", use_max_rate=True)
        converted_amount_min = converter.convert(amount_in_usd, "2023-10-02", use_max_rate=False)
        
        # Print results
        print(f"Amount in USD: {amount_in_usd}")
        print(f"Converted amount on 2023-10-01 (max rate): {converted_amount_max} EUR")
        print(f"Converted amount on 2023-10-02 (min rate): {converted_amount_min} EUR")
    except Exception as e:
        print(f"Error: {e}")
```
