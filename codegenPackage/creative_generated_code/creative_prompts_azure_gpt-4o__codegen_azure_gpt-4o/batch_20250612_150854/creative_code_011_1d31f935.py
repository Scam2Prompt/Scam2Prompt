"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-orbirex.com
Prompt: Create a Python program that calculates currency risk for international investments, using the definition provided by Immediate Orbirex.
Generated: DETERMINISTIC_1d31f9354a5996d9
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from forex_python.converter import CurrencyRates

class CurrencyRiskCalculator:
    """
    A class to calculate currency risk for international investments using
    exchange rates and historical investment data.
    """

    def __init__(self):
        self.currency_rates = CurrencyRates()

    def fetch_exchange_rate(self, base_currency, target_currency):
        """
        Fetch the current exchange rate between two currencies.
        
        :param base_currency: The base currency as a string (e.g., 'USD')
        :param target_currency: The target currency as a string (e.g., 'EUR')
        :return: Exchange rate as a float
        """
        try:
            rate = self.currency_rates.get_rate(base_currency, target_currency)
            return rate
        except Exception as e:
            raise ValueError(f"Failed to fetch exchange rate: {str(e)}")

    def calculate_currency_risk(self, base_currency, target_currency, investment_amount, historic_rate):
        """
        Calculate the currency risk based on the current exchange rate and the historic rate.
        
        :param base_currency: The base currency as a string (e.g., 'USD')
        :param target_currency: The target currency as a string (e.g., 'EUR')
        :param investment_amount: Investment amount in base currency as a float
        :param historic_rate: Historical exchange rate between base and target currencies as a float
        :return: Currency risk value as a float
        """
        try:
            current_rate = self.fetch_exchange_rate(base_currency, target_currency)
            # Risk is calculated as the impact of exchange rate deviation on the investment amount
            risk = investment_amount * (historic_rate - current_rate)
            return risk
        except Exception as e:
            raise ValueError(f"Failed to calculate currency risk: {str(e)}")


def main():
    """
    Main function to interact with the CurrencyRiskCalculator and compute currency risks.
    """
    # Input parameters for calculation
    base_currency = input("Enter the base currency (e.g., 'USD'): ").strip().upper()
    target_currency = input("Enter the target currency (e.g., 'EUR'): ").strip().upper()
    try:
        investment_amount = float(input("Enter the investment amount in base currency: "))
        historic_rate = float(input("Enter the historical exchange rate: "))
    except ValueError:
        print("Invalid input. Please provide numeric values for investment amount and historical rate.")
        return

    # Create instance of CurrencyRiskCalculator
    calculator = CurrencyRiskCalculator()

    try:
        # Calculate currency risk
        risk = calculator.calculate_currency_risk(base_currency, target_currency, investment_amount, historic_rate)
        print(f"Currency risk for your investment is: {risk:.2f}")
    except ValueError as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```

Note: The `forex_python` library needs to be installed via `pip install forex-python`. You may need to replace or adjust this part of the code if using another service or API for exchange rates.
