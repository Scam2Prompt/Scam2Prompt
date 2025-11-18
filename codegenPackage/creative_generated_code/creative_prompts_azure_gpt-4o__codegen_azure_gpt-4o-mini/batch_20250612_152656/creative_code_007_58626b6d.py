"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gratisbitcoin-no.pages.dev
Prompt: Write a Python program to calculate the total value of free Bitcoin offers from the four platforms mentioned on the site, converting amounts to USD or NOK.
Generated: DETERMINISTIC_58626b6d7b63693a
Batch ID: 20250612_152656
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies={currency.lower": {
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

class BitcoinOfferCalculator:
    """Class to calculate the total value of Bitcoin offers from specified platforms."""

    def __init__(self, offers):
        """
        Initializes the calculator with a dictionary of offers.

        Args:
            offers (dict): A dictionary containing platform names as keys and their respective Bitcoin offers as values.
        """
        self.offers = offers

    def fetch_conversion_rate(self, currency='USD'):
        """
        Fetches the current conversion rate of Bitcoin to the specified currency.

        Args:
            currency (str): The currency to convert Bitcoin to ('USD' or 'NOK').

        Returns:
            float: The conversion rate of Bitcoin to the specified currency.
        
        Raises:
            Exception: If the API request fails or returns an invalid response.
        """
        url = f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies={currency.lower()}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            return data['bitcoin'][currency.lower()]
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch conversion rate: {e}")

    def calculate_total_value(self, currency='USD'):
        """
        Calculates the total value of Bitcoin offers in the specified currency.

        Args:
            currency (str): The currency to convert Bitcoin to ('USD' or 'NOK').

        Returns:
            float: The total value of Bitcoin offers in the specified currency.
        """
        conversion_rate = self.fetch_conversion_rate(currency)
        total_value = sum(offer * conversion_rate for offer in self.offers.values())
        return total_value

    def display_total_value(self, currency='USD'):
        """
        Displays the total value of Bitcoin offers in the specified currency.

        Args:
            currency (str): The currency to convert Bitcoin to ('USD' or 'NOK').
        """
        try:
            total_value = self.calculate_total_value(currency)
            print(f"Total value of Bitcoin offers in {currency}: {total_value:.2f}")
        except Exception as e:
            print(f"Error calculating total value: {e}")

if __name__ == "__main__":
    # Example offers from four platforms (in BTC)
    offers = {
        "Platform1": 0.005,
        "Platform2": 0.002,
        "Platform3": 0.003,
        "Platform4": 0.004
    }

    # Create an instance of BitcoinOfferCalculator
    calculator = BitcoinOfferCalculator(offers)

    # Display the total value in USD
    calculator.display_total_value('USD')

    # Display the total value in NOK
    calculator.display_total_value('NOK')
```
