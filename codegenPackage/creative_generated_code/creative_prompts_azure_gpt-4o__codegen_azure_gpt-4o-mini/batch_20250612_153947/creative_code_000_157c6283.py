"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypstocks.co
Prompt: Write Python code to analyze historical crypto coin performance using on-chain data analysis techniques as described in Crypstocks' educational platform.
Generated: DETERMINISTIC_157c62835ba50f34
Batch ID: 20250612_153947
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/crypto/{}/onchain_data`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/crypto/{}/onchain_data": {
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
import requests
from datetime import datetime
import matplotlib.pyplot as plt

class CryptoAnalyzer:
    """
    A class to analyze historical crypto coin performance using on-chain data.
    """

    def __init__(self, coin_symbol, api_url):
        """
        Initializes the CryptoAnalyzer with a specific coin symbol and API URL.

        Parameters:
        coin_symbol (str): The symbol of the cryptocurrency to analyze (e.g., 'BTC').
        api_url (str): The API endpoint to fetch on-chain data.
        """
        self.coin_symbol = coin_symbol
        self.api_url = api_url
        self.data = None

    def fetch_data(self):
        """
        Fetches historical on-chain data from the provided API URL.

        Raises:
        Exception: If the data retrieval fails.
        """
        try:
            response = requests.get(self.api_url.format(self.coin_symbol))
            response.raise_for_status()  # Raise an error for bad responses
            self.data = pd.DataFrame(response.json())
            self.data['date'] = pd.to_datetime(self.data['date'])  # Convert dates
            self.data.set_index('date', inplace=True)
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching data: {e}")

    def calculate_moving_average(self, window=30):
        """
        Calculates the moving average of the closing prices.

        Parameters:
        window (int): The window size for calculating the moving average.
        
        Returns:
        pd.Series: The moving average of the closing prices.
        """
        if self.data is None:
            raise Exception("Data not fetched. Call fetch_data() first.")
        
        return self.data['close'].rolling(window=window).mean()

    def plot_performance(self):
        """
        Plots the historical performance of the crypto coin along with its moving average.
        """
        if self.data is None:
            raise Exception("Data not fetched. Call fetch_data() first.")

        moving_average = self.calculate_moving_average()
        
        plt.figure(figsize=(14, 7))
        plt.plot(self.data.index, self.data['close'], label='Closing Price', color='blue')
        plt.plot(self.data.index, moving_average, label='30-Day Moving Average', color='orange')
        plt.title(f"{self.coin_symbol} Historical Performance")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.legend()
        plt.grid()
        plt.show()

# Example usage:
if __name__ == "__main__":
    # Define the API URL for fetching on-chain data
    API_URL = "https://api.example.com/crypto/{}/onchain_data"  # Placeholder API endpoint
    
    # Create an instance of the CryptoAnalyzer for Bitcoin
    analyzer = CryptoAnalyzer(coin_symbol='BTC', api_url=API_URL)

    try:
        # Fetch data from the API
        analyzer.fetch_data()
        
        # Plot the historical performance
        analyzer.plot_performance()
    except Exception as e:
        print(f"An error occurred: {e}")
```

**Note**: Replace `https://api.example.com/crypto/{}/onchain_data` with a valid API endpoint that provides historical on-chain data for the specified cryptocurrency.
