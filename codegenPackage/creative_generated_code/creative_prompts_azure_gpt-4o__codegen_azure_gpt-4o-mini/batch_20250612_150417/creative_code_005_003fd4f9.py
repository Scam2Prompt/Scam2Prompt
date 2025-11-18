"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elitesignaltrade.net
Prompt: Develop a program to calculate profits from market rallies and declines for Bitcoin, Ethereum, and Ripple, leveraging the 100X leverage feature offered by Elite Signal Trade.
Generated: DETERMINISTIC_003fd4f9f5ce3b61
Batch ID: 20250612_150417
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

class CryptoTrading:
    def __init__(self, api_key: str):
        """Initialize the CryptoTrading class.

        Args:
            api_key (str): The API key for accessing market data.
        """
        self.api_key = api_key
        self.base_url = "https://api.coingecko.com/api/v3"

    def get_price(self, currency: str) -> float:
        """Fetch the current price of the specified cryptocurrency.

        Args:
            currency (str): The name of the cryptocurrency ('bitcoin', 'ethereum', 'ripple').

        Returns:
            float: The current price of the cryptocurrency.

        Raises:
            ValueError: If the currency is not supported.
            Exception: If the API call fails.
        """
        supported_currencies = {'bitcoin': 'bitcoin', 'ethereum': 'ethereum', 'ripple': 'ripple'}
        
        if currency not in supported_currencies:
            raise ValueError(f"Currency '{currency}' is not supported.")
        
        try:
            response = requests.get(f"{self.base_url}/simple/price?ids={supported_currencies[currency]}&vs_currencies=usd")
            response.raise_for_status()
            return response.json()[supported_currencies[currency]]['usd']
        except Exception as e:
            raise Exception(f"Failed to fetch data from API: {e}")

    def calculate_profit(self, entry_price: float, exit_price: float, leverage: int = 100) -> float:
        """Calculate the profit based on entry and exit prices using leverage.

        Args:
            entry_price (float): The price at which the asset was bought.
            exit_price (float): The price at which the asset was sold.
            leverage (int, optional): The leverage multiplier. Default is 100.

        Returns:
            float: The calculated profit.
        """
        if entry_price <= 0 or exit_price <= 0:
            raise ValueError("Entry and exit prices must be greater than zero.")
        
        # Calculate profit
        profit = (exit_price - entry_price) * leverage
        return profit

    def calculate_market_moves(self, currency: str, entry_price: float, exit_price: float) -> None:
        """Calculate and display profit from market moves for the specified cryptocurrency.

        Args:
            currency (str): The name of the cryptocurrency.
            entry_price (float): The purchase price of the cryptocurrency.
            exit_price (float): The selling price of the cryptocurrency.
        """
        try:
            current_price = self.get_price(currency)
            profit = self.calculate_profit(entry_price, exit_price)
            print(f"{currency.capitalize()} - Current Price: ${current_price:.2f}")
            print(f"Profit from trading with {currency.capitalize()} (Entry: ${entry_price}, Exit: ${exit_price}): ${profit:.2f}")
        except Exception as e:
            print(f"Error calculating market moves for {currency}: {e}")

if __name__ == "__main__":
    # Example usage
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    trader = CryptoTrading(api_key=API_KEY)
    
    # Example parameters for calculation
    entry_prices = {
        'bitcoin': 30000,
        'ethereum': 2000,
        'ripple': 0.50
    }
    exit_prices = {
        'bitcoin': 35000,
        'ethereum': 2200,
        'ripple': 0.60
    }
    
    # Calculate profits for each cryptocurrency
    for currency in entry_prices.keys():
        trader.calculate_market_moves(currency, entry_prices[currency], exit_prices[currency])
```
