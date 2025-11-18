"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gopulsecom.com
Prompt: Generate code to calculate the percentage change in token prices (e.g., PLS, HEX, and INC) over different time intervals (e.g., 5m, 1h, 24h) using data from GoPulse.com.
Generated: DETERMINISTIC_2f80893ad624a1bf
Batch ID: 20250612_153925
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.gopulse.com/v1/tokens": {
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
import pandas as pd
from datetime import datetime, timedelta

class TokenPriceAnalyzer:
    BASE_URL = "https://api.gopulse.com/v1/tokens"  # Example API endpoint

    def __init__(self, tokens):
        """
        Initializes the TokenPriceAnalyzer with a list of tokens.

        :param tokens: List of token symbols to analyze (e.g., ['PLS', 'HEX', 'INC'])
        """
        self.tokens = tokens

    def fetch_token_prices(self, token, interval):
        """
        Fetches token prices for a specified interval.

        :param token: Token symbol to fetch prices for
        :param interval: Time interval for price data (e.g., '5m', '1h', '24h')
        :return: List of price data or raises an exception on failure
        """
        try:
            response = requests.get(f"{self.BASE_URL}/{token}/history", params={"interval": interval})
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Assume the response is in JSON format
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {token} at {interval}: {e}")
            return []

    def calculate_percentage_change(self, prices):
        """
        Calculates the percentage change from the first to the last price.

        :param prices: List of prices
        :return: Percentage change or None if not enough data
        """
        if len(prices) < 2:
            return None  # Not enough data to calculate change

        initial_price = prices[0]['price']  # Assuming each price entry has a 'price' field
        final_price = prices[-1]['price']
        
        try:
            percentage_change = ((final_price - initial_price) / initial_price) * 100
            return round(percentage_change, 2)  # Round to 2 decimal places
        except ZeroDivisionError:
            return None  # Prevent division by zero

    def analyze_tokens(self, interval):
        """
        Analyzes the percentage change for all tokens over a specified interval.

        :param interval: Time interval for analysis (e.g., '5m', '1h', '24h')
        :return: Dictionary with tokens and their percentage changes
        """
        results = {}
        for token in self.tokens:
            prices = self.fetch_token_prices(token, interval)
            if prices:
                change = self.calculate_percentage_change(prices)
                results[token] = change
            else:
                results[token] = None  # No data available

        return results


def main():
    tokens = ['PLS', 'HEX', 'INC']  # Example tokens
    intervals = ['5m', '1h', '24h']  # Different time intervals

    analyzer = TokenPriceAnalyzer(tokens)

    # Analyze for each interval
    for interval in intervals:
        print(f"Percentage changes for interval {interval}:")
        changes = analyzer.analyze_tokens(interval)
        for token, change in changes.items():
            if change is not None:
                print(f"  {token}: {change}%")
            else:
                print(f"  {token}: No data available")

if __name__ == "__main__":
    main()
```
