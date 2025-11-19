"""
Generated Code Metadata:
========================
Original URL: https://jupiterdigitalasset.com
Prompt: Write Python code to calculate the value of Bitcoin holdings over time, incorporating the concept of Bitcoin as a "scarce asset" with a maximum supply of 21 million, as described on the Jupiter Digital Asset website.
Generated: DETERMINISTIC_6c3a4c780e41ad54
Batch ID: 20250612_154601
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coindesk.com/v1/bpi/currentprice/BTC.json": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import datetime

class BitcoinHoldings:
    MAX_SUPPLY = 21_000_000  # Maximum supply of Bitcoin
    API_URL = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"  # API to get current Bitcoin price

    def __init__(self, initial_investment: float, bitcoin_amount: float):
        """
        Initialize the BitcoinHoldings instance.

        :param initial_investment: The initial investment amount in USD.
        :param bitcoin_amount: The amount of Bitcoin held.
        """
        self.initial_investment = initial_investment
        self.bitcoin_amount = bitcoin_amount
        self.current_price = self.get_current_bitcoin_price()

    def get_current_bitcoin_price(self) -> float:
        """
        Fetch the current price of Bitcoin in USD.

        :return: Current Bitcoin price in USD.
        :raises Exception: If the API request fails or returns an invalid response.
        """
        try:
            response = requests.get(self.API_URL)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            return float(data['bpi']['USD']['rate'].replace(',', ''))  # Convert price to float
        except (requests.RequestException, ValueError) as e:
            raise Exception("Error fetching Bitcoin price: " + str(e))

    def calculate_current_value(self) -> float:
        """
        Calculate the current value of the Bitcoin holdings.

        :return: Current value of the Bitcoin holdings in USD.
        """
        return self.bitcoin_amount * self.current_price

    def calculate_return_on_investment(self) -> float:
        """
        Calculate the return on investment (ROI) for the Bitcoin holdings.

        :return: ROI as a percentage.
        """
        current_value = self.calculate_current_value()
        return ((current_value - self.initial_investment) / self.initial_investment) * 100

    def display_holdings_summary(self):
        """
        Display a summary of the Bitcoin holdings, including current value and ROI.
        """
        current_value = self.calculate_current_value()
        roi = self.calculate_return_on_investment()
        print(f"Initial Investment: ${self.initial_investment:.2f}")
        print(f"Bitcoin Amount: {self.bitcoin_amount:.6f} BTC")
        print(f"Current Bitcoin Price: ${self.current_price:.2f}")
        print(f"Current Value of Holdings: ${current_value:.2f}")
        print(f"Return on Investment (ROI): {roi:.2f}%")

if __name__ == "__main__":
    # Example usage
    try:
        initial_investment = 1000.00  # Example initial investment in USD
        bitcoin_amount = 0.05  # Example amount of Bitcoin held
        holdings = BitcoinHoldings(initial_investment, bitcoin_amount)
        holdings.display_holdings_summary()
    except Exception as e:
        print(f"An error occurred: {e}")
```
