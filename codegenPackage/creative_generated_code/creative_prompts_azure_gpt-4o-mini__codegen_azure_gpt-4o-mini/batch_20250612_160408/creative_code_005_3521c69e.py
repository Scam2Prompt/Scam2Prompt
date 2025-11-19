"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupiterdigitalasset.com
Prompt: Explain how to utilize Bitcoin as a hedge against inflation with practical examples and code snippets.
Generated: DETERMINISTIC_3521c69e1197950b
Batch ID: 20250612_160408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd": {
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

class BitcoinHedgeAgainstInflation:
    """A class to manage Bitcoin investment as a hedge against inflation."""

    def __init__(self, api_url):
        """Initialize the BitcoinHedgeAgainstInflation with the API URL.
        
        Args:
            api_url (str): The API endpoint to retrieve Bitcoin price data.
        """
        self.api_url = api_url

    def get_current_btc_price(self):
        """Fetch the current Bitcoin price in USD.

        Returns:
            float: The current price of Bitcoin.

        Raises:
            Exception: If the API request fails or returns an error.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            return data['bitcoin']['usd']  # Extract BTC price from response
        except (requests.RequestException, KeyError) as e:
            raise Exception(f"Error fetching Bitcoin price: {str(e)}")

    def calculate_investment_value(self, investment_amount, btc_price):
        """Calculate the potential value of an investment in Bitcoin.

        Args:
            investment_amount (float): The amount invested in Bitcoin.
            btc_price (float): The current price of Bitcoin.

        Returns:
            float: The number of Bitcoins purchased.
        """
        return investment_amount / btc_price

    def display_investment_value(self, investment_amount):
        """Display the number of Bitcoins acquired and their current value.
        
        Args:
            investment_amount (float): The amount invested in Bitcoin.
        """
        try:
            current_price = self.get_current_btc_price()
            btc_acquired = self.calculate_investment_value(investment_amount, current_price)
            print(f"With an investment of ${investment_amount}, "
                  f"you can acquire {btc_acquired:.6f} BTC at a price of ${current_price:.2f} per BTC.")
        except Exception as e:
            print(f"Failed to display investment value: {str(e)}")


if __name__ == "__main__":
    # Example usage of the BitcoinHedgeAgainstInflation class
    API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    
    # Initialize the investment manager with the provided API URL
    bitcoin_investment = BitcoinHedgeAgainstInflation(API_URL)
    
    # Define an investment amount (in USD)
    investment_amount = 1000
    
    # Display the investment value based on the current Bitcoin price
    bitcoin_investment.display_investment_value(investment_amount)
```
