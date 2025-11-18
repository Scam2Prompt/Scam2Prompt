"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypstocks.co
Prompt: Create a program to track and visualize crypto market trends using tools suitable for beginners and experts, as emphasized in Crypstocks' educational materials.
Generated: DETERMINISTIC_be5985b2a89fe3de
Batch ID: 20250612_153947
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/coins/{self.crypto_symbol}/market_chart": {
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
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from datetime import datetime, timedelta

class CryptoMarketTracker:
    """
    A class to track and visualize cryptocurrency market trends.
    """

    def __init__(self, crypto_symbol, days=30):
        """
        Initializes the CryptoMarketTracker with a specified cryptocurrency symbol.

        Parameters:
            crypto_symbol (str): The symbol of the cryptocurrency to track.
            days (int): Number of past days to retrieve data for.
        """
        self.crypto_symbol = crypto_symbol
        self.days = days
        self.data = None

    def fetch_data(self):
        """
        Fetch historical price data for the cryptocurrency from a public API.
        """
        try:
            end_date = datetime.now()
            start_date = end_date - timedelta(days=self.days)

            url = f"https://api.coingecko.com/api/v3/coins/{self.crypto_symbol}/market_chart"
            params = {
                'vs_currency': 'usd',
                'days': self.days,
                'interval': 'daily'
            }
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an error for bad responses

            # Extract the prices and timestamps from the response
            prices = response.json().get('prices', [])
            if not prices:
                raise ValueError("No price data found for the given cryptocurrency.")

            # Create a DataFrame from the fetched data
            self.data = pd.DataFrame(prices, columns=['timestamp', 'price'])
            self.data['timestamp'] = pd.to_datetime(self.data['timestamp'], unit='ms')
            self.data.set_index('timestamp', inplace=True)

        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def visualize_data(self):
        """
        Visualizes the fetched cryptocurrency price data.
        """
        if self.data is None:
            print("No data available to visualize. Please fetch data first.")
            return
        
        plt.figure(figsize=(12, 6))
        plt.plot(self.data.index, self.data['price'], label=self.crypto_symbol.upper(), color='blue')
        plt.title(f'{self.crypto_symbol.upper()} Price Trend Over the Last {self.days} Days')
        plt.xlabel('Date')
        plt.ylabel('Price in USD')
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Example usage of the CryptoMarketTracker class
    crypto_symbol = input("Enter the cryptocurrency symbol (e.g., bitcoin, ethereum): ").lower()
    tracker = CryptoMarketTracker(crypto_symbol)
    
    tracker.fetch_data()
    tracker.visualize_data()
```
