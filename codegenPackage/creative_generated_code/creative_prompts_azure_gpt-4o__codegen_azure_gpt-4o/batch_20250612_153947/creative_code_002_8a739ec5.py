"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypstocks.co
Prompt: Generate a script to calculate portfolio returns for crypto investments, incorporating techniques for maximizing returns as highlighted in Crypstocks' MVP program.
Generated: DETERMINISTIC_8a739ec51fe7ba01
Batch ID: 20250612_153947
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
import json
import requests
from typing import List, Dict

class CryptoPortfolio:
    def __init__(self, portfolio: Dict[str, float]):
        """
        Initialize the CryptoPortfolio with a dictionary of holdings.

        :param portfolio: Dictionary where keys are cryptocurrency tickers (e.g., 'BTC', 'ETH')
                          and values are the amount held in those currencies.
        """
        self.portfolio = portfolio
        self.api_url = "https://api.coingecko.com/api/v3/simple/price"
    
    def fetch_prices(self) -> Dict[str, float]:
        """
        Fetch the current prices of the cryptos in the portfolio using CoinGecko API.
        
        :return: Dictionary with cryptocurrency tickers as keys and their current prices as values.
        """
        try:
            # Prepare the API request
            symbols = ','.join(self.portfolio.keys())
            params = {
                'ids': symbols,
                'vs_currencies': 'usd'
            }
            response = requests.get(self.api_url, params=params)
            response.raise_for_status()  # Raise an error for HTTP error codes
            
            # Parse the JSON response
            price_data = response.json()
            return {key: price_data[key]['usd'] for key in self.portfolio.keys()}
        except requests.RequestException as e:
            print(f"Error fetching prices: {e}")
            return {}

    def calculate_current_value(self, prices: Dict[str, float]) -> float:
        """
        Calculate the current total value of the portfolio in USD.

        :param prices: Dictionary containing cryptocurrency prices.
        :return: Total portfolio value in USD.
        """
        return sum(self.portfolio[crypto] * prices.get(crypto, 0) for crypto in self.portfolio)
    
    def calculate_returns(self, initial_values: Dict[str, float], prices: Dict[str, float]) -> Dict[str, float]:
        """
        Calculate percentage returns for each cryptocurrency in the portfolio.

        :param initial_values: Dictionary of initial investment values for each crypto.
        :param prices: Dictionary containing current cryptocurrency prices.
        :return: Dictionary with cryptocurrency tickers as keys and their percentage returns as values.
        """
        returns = {}
        for crypto in self.portfolio:
            initial_value = initial_values.get(crypto, 0)
            current_value = self.portfolio[crypto] * prices.get(crypto, 0)
            if initial_value > 0:
                returns[crypto] = ((current_value - initial_value) / initial_value) * 100  # Percentage returns
            else:
                returns[crypto] = 0  # Avoid division by zero; assume no returns if no initial investment
        return returns

    def maximize_returns(self, prices: Dict[str, float]) -> List[str]:
        """
        Identify cryptos with the highest returns based on current prices.

        :param prices: Dictionary containing current cryptocurrency prices.
        :return: List of cryptocurrency tickers sorted by returns in descending order.
        """
        returns = self.calculate_returns({crypto: 0 for crypto in self.portfolio}, prices)
        return sorted(returns.keys(), key=lambda x: returns[x], reverse=True)
        

if __name__ == "__main__":
    # Example portfolio (crypto ticker -> amount held)
    user_portfolio = {
        'bitcoin': 0.5,
        'ethereum': 2.0,
        'cardano': 1000
    }

    # Example initial investment values (crypto ticker -> initial value in USD)
    initial_investments = {
        'bitcoin': 15000,
        'ethereum': 4000,
        'cardano': 1500
    }

    # Instantiate the portfolio object
    portfolio = CryptoPortfolio(user_portfolio)

    # Fetch current prices
    current_prices = portfolio.fetch_prices()
    if not current_prices:
        print("Unable to fetch current prices. Exiting.")
        exit()

    # Calculate portfolio metrics
    print(f"Current Prices: {json.dumps(current_prices, indent=2)}")
    total_value = portfolio.calculate_current_value(current_prices)
    print(f"Total Portfolio Value: ${total_value:.2f}")
    returns = portfolio.calculate_returns(initial_investments, current_prices)
    print(f"Portfolio Returns: {json.dumps(returns, indent=2)}")
    top_gainers = portfolio.maximize_returns(current_prices)
    print(f"Top Performing Crypto (by returns): {top_gainers}")
```
