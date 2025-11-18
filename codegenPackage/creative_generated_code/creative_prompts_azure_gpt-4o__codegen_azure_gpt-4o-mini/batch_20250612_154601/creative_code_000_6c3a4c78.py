"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupiterdigitalasset.com
Prompt: Write Python code to calculate the value of Bitcoin holdings over time, incorporating the concept of Bitcoin as a "scarce asset" with a maximum supply of 21 million, as described on the Jupiter Digital Asset website.
Generated: DETERMINISTIC_6c3a4c780e41ad54
Batch ID: 20250612_154601
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart": {
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
from datetime import datetime
import matplotlib.pyplot as plt

class BitcoinHoldings:
    MAX_SUPPLY = 21_000_000  # Maximum supply of Bitcoin

    def __init__(self, initial_investment: float, btc_price: float):
        """
        Initialize the BitcoinHoldings instance.
        
        Args:
        - initial_investment (float): The initial amount invested in Bitcoin.
        - btc_price (float): Current price of Bitcoin.
        """
        self.initial_investment = initial_investment
        self.btc_price = btc_price
        self.btc_amount = self.calculate_btc_amount()

    def calculate_btc_amount(self) -> float:
        """
        Calculate the amount of Bitcoin that can be purchased with the initial investment.

        Returns:
        - float: The amount of Bitcoin purchased.
        """
        if self.btc_price <= 0:
            raise ValueError("Bitcoin price must be greater than zero.")
        return self.initial_investment / self.btc_price

    def get_historical_prices(self, days: int) -> list:
        """
        Fetch historical Bitcoin prices for the last 'days' days.

        Args:
        - days (int): Number of days in the past to fetch price data.

        Returns:
        - list: A list of historical Bitcoin prices.
        """
        try:
            url = f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
            params = {
                'vs_currency': 'usd',
                'days': days,
                'interval': 'daily'
            }
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            prices = response.json()['prices']
            return [price[1] for price in prices]
        except requests.exceptions.RequestException as e:
            print(f"Error fetching historical prices: {e}")
            return []

    def calculate_value_over_time(self, days: int) -> list:
        """
        Calculate the value of Bitcoin holdings over a specified number of days.

        Args:
        - days (int): Number of days to calculate the value.

        Returns:
        - list: A list of values of the Bitcoin holdings over time.
        """
        historical_prices = self.get_historical_prices(days)
        return [self.btc_amount * price for price in historical_prices]

    def plot_value_over_time(self, days: int):
        """
        Plot the value of Bitcoin holdings over a specified number of days.

        Args:
        - days (int): Number of days to plot the value.
        """
        values = self.calculate_value_over_time(days)
        dates = [datetime.now().date() - timedelta(days=i) for i in range(len(values))]
        
        plt.figure(figsize=(10, 5))
        plt.plot(dates[::-1], values[::-1], marker='o')
        plt.title('Bitcoin Holdings Value Over Time')
        plt.xlabel('Date')
        plt.ylabel('Value in USD')
        plt.xticks(rotation=45)
        plt.grid()
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Example usage of the BitcoinHoldings class
    initial_investment = 5000.0  # Amount invested in USD
    btc_price = 30000.0  # Current BTC price in USD

    try:
        portfolio = BitcoinHoldings(initial_investment, btc_price)
        portfolio.plot_value_over_time(days=30)  # Plotting for the last 30 days
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
