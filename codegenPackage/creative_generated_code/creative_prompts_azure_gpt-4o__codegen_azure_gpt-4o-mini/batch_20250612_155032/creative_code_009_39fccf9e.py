"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kantor-usdc.com
Prompt: Create a script to automate the calculation of exchange rates and commissions for multiple cryptocurrencies (USDC, Bitcoin, Ethereum) as described by Kantor USDC Białystok.
Generated: DETERMINISTIC_39fccf9e450edb46
Batch ID: 20250612_155032
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/exchange-rates": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests

class CryptoExchangeCalculator:
    """
    A class to handle cryptocurrency exchange rates and commission calculations for
    USDC, Bitcoin, and Ethereum based on data from a cryptocurrency API.
    """

    def __init__(self, api_url: str, commission_rate: float):
        """
        Initializes the CryptoExchangeCalculator with the API URL and commission rate.

        :param api_url: URL of the cryptocurrency exchange rates API
        :param commission_rate: Commission rate as a decimal (e.g., 0.01 for 1%)
        """
        self.api_url = api_url
        self.commission_rate = commission_rate
        self.exchange_rates = self.get_exchange_rates()

    def get_exchange_rates(self):
        """
        Fetches the current exchange rates for USDC, Bitcoin, and Ethereum.

        :return: A dictionary containing exchange rates
        :raises Exception: If the API request fails or returns an error
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            data = response.json()

            # Assuming the API returns rates in a certain structure
            return {
                'USDC': data['rates']['USDC'],
                'Bitcoin': data['rates']['BTC'],
                'Ethereum': data['rates']['ETH']
            }
        except requests.RequestException as e:
            raise Exception(f"Error fetching exchange rates: {e}")

    def calculate_total_with_commission(self, amount: float, currency: str):
        """
        Calculates the total amount after applying the commission for a given currency.

        :param amount: The amount of cryptocurrency
        :param currency: The currency type (USDC, Bitcoin, Ethereum)
        :return: The total amount after commission
        :raises ValueError: If the currency is not supported
        """
        if currency not in self.exchange_rates:
            raise ValueError(f"Currency '{currency}' is not supported.")

        # Calculate commission
        commission = amount * self.commission_rate
        total_amount = amount - commission

        # Get exchange rate and convert to USDC
        exchange_rate = self.exchange_rates[currency]
        total_in_usdc = total_amount * exchange_rate

        return total_in_usdc

# Example usage
if __name__ == "__main__":
    API_URL = "https://api.example.com/exchange-rates"  # Replace with a real API
    COMMISSION_RATE = 0.01  # 1% commission

    calculator = CryptoExchangeCalculator(API_URL, COMMISSION_RATE)

    try:
        # Example: Calculate total in USDC after commission for 1 Bitcoin
        amount = 1.0  # Amount in Bitcoin
        currency = 'Bitcoin'
        total_usdc = calculator.calculate_total_with_commission(amount, currency)
        print(f"Total in USDC after commission for {amount} {currency}: {total_usdc:.2f} USDC")
    except Exception as e:
        print(f"An error occurred: {e}")
```

Make sure to replace the placeholder `API_URL` with a real API endpoint that provides exchange rates for the specified cryptocurrencies.
