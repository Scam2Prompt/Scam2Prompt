"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://topdigitaltrade.com.simplebittstockoption.com
Prompt: Create a script that fetches live cryptocurrency prices (BTC, ETH, XMR, LTC, DASH) and calculates percentage changes, as shown on Topdigitaltrade's trading platform.
Generated: DETERMINISTIC_c408785869a16359
Batch ID: 20250612_154609
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price": {
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
import time

class CryptoPriceFetcher:
    """
    A class to fetch live cryptocurrency prices and calculate percentage changes.
    Supported cryptocurrencies: BTC, ETH, XMR, LTC, DASH.
    """
    
    BASE_URL = 'https://api.coingecko.com/api/v3/simple/price'
    CRYPTOCURRENCIES = ['bitcoin', 'ethereum', 'monero', 'litecoin', 'dash']
    
    def __init__(self):
        self.last_prices = {crypto: 0 for crypto in self.CRYPTOCURRENCIES}

    def fetch_prices(self):
        """
        Fetch the current prices of the specified cryptocurrencies from the API.
        Returns a dictionary with cryptocurrency symbols as keys and their prices as values.
        """
        params = {
            'ids': ','.join(self.CRYPTOCURRENCIES),
            'vs_currencies': 'usd'
        }
        
        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def calculate_percentage_change(self, current_price, last_price):
        """
        Calculate the percentage change between current and last prices.
        """
        if last_price == 0:
            return 0  # Avoid division by zero
        
        return ((current_price - last_price) / last_price) * 100

    def update_prices(self):
        """
        Fetch current prices and calculate percentage changes.
        """
        current_prices = self.fetch_prices()
        
        if current_prices is None:
            return  # Exit if there was an error fetching prices
        
        for crypto, data in current_prices.items():
            current_price = data['usd']
            last_price = self.last_prices[crypto]
            percentage_change = self.calculate_percentage_change(current_price, last_price)
            
            # Update last price for future calculations
            self.last_prices[crypto] = current_price
            
            # Print the results
            print(f"{crypto.capitalize()} - Current Price: ${current_price:.2f}, "
                  f"Percentage Change: {percentage_change:.2f}%")

    def run(self, interval=60):
        """
        Continuously fetch and print cryptocurrency prices at a specified interval.
        :param interval: Time in seconds between price fetches.
        """
        while True:
            self.update_prices()
            time.sleep(interval)

if __name__ == "__main__":
    fetcher = CryptoPriceFetcher()
    fetcher.run(interval=60)  # Update every 60 seconds
```
