"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-urex-gpt.com
Prompt: Create a script for automating cryptocurrency portfolio management using GPT-based AI technology, inspired by the features of the Bit GPT Urex platform.
Generated: DETERMINISTIC_692d2175f880f8db
Batch ID: 20250612_150843
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3": {
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
import json
import logging
from datetime import datetime
from typing import List, Dict, Any

# Set up logging for the script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CryptoPortfolioManager:
    def __init__(self, api_key: str, portfolio: Dict[str, float]):
        """
        Initialize the CryptoPortfolioManager with an API key and portfolio.
        
        :param api_key: API key for accessing cryptocurrency data
        :param portfolio: Dictionary containing the cryptocurrency symbols and their corresponding amounts
        """
        self.api_key = api_key
        self.portfolio = portfolio
        self.base_url = "https://api.coingecko.com/api/v3"

    def get_portfolio_value(self) -> float:
        """
        Calculate the total value of the cryptocurrency portfolio in USD.
        
        :return: Total portfolio value in USD
        """
        total_value = 0.0
        for symbol, amount in self.portfolio.items():
            price = self.get_current_price(symbol)
            total_value += price * amount
        return total_value

    def get_current_price(self, symbol: str) -> float:
        """
        Get the current price of a given cryptocurrency in USD.
        
        :param symbol: The symbol of the cryptocurrency (e.g., 'bitcoin')
        :return: Current price in USD
        """
        try:
            response = requests.get(f"{self.base_url}/simple/price?ids={symbol}&vs_currencies=usd")
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            return data[symbol]['usd']
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
        except KeyError:
            logging.error(f"Could not find price for symbol: {symbol}")
        except Exception as err:
            logging.error(f"An error occurred: {err}")
        
        return 0.0  # Return 0 if there is an error

    def display_portfolio(self):
        """
        Display the current portfolio and its total value.
        """
        logging.info("Current Portfolio:")
        for symbol, amount in self.portfolio.items():
            price = self.get_current_price(symbol)
            total_value = price * amount
            logging.info(f"{symbol.capitalize()}: {amount} @ ${price} each = ${total_value:.2f}")

        total_portfolio_value = self.get_portfolio_value()
        logging.info(f"Total Portfolio Value: ${total_portfolio_value:.2f}")

# Example usage:
if __name__ == "__main__":
    # Replace with your actual API key and portfolio
    API_KEY = "your_api_key_here"  # Not used directly in this example, but can be integrated
    portfolio = {
        "bitcoin": 0.5,
        "ethereum": 2,
        "dogecoin": 1000
    }

    manager = CryptoPortfolioManager(API_KEY, portfolio)
    manager.display_portfolio()
```
