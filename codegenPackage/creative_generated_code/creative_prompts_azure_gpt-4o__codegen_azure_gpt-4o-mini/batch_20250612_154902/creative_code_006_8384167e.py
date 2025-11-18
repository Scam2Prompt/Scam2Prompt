"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thenafl.org
Prompt: Write a tutorial on how to implement perpetual contract trading with leverage, inspired by THENA FI's "Trade Perps" feature.
Generated: DETERMINISTIC_8384167ea93d1c3e
Batch ID: 20250612_154902
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.thena.fi": {
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

class PerpetualContractTrader:
    """
    A class to implement perpetual contract trading with leverage.
    Includes methods for placing orders and managing positions.
    """

    BASE_URL = "https://api.thena.fi"  # Placeholder for the actual API URL

    def __init__(self, api_key: str):
        """
        Initializes the trader with the API key.

        :param api_key: User's API key for authentication
        """
        self.api_key = api_key
        self.session = self._create_session()

    def _create_session(self):
        """
        Creates a requests session with the necessary headers.

        :return: requests.Session object
        """
        session = requests.Session()
        session.headers.update({"Authorization": f"Bearer {self.api_key}"})
        return session

    def get_market_data(self, symbol: str):
        """
        Fetches market data for a given trading pair.

        :param symbol: Trading pair symbol (e.g., 'BTCUSDT')
        :return: Market data as JSON
        """
        try:
            response = self.session.get(f"{self.BASE_URL}/market/{symbol}")
            response.raise_for_status()  # Raise an error for HTTP errors
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching market data: {e}")
            return None

    def place_order(self, symbol: str, order_type: str, quantity: float, leverage: int):
        """
        Places an order on the perpetual contract market.

        :param symbol: Trading pair symbol (e.g., 'BTCUSDT')
        :param order_type: Type of order ('buy' or 'sell')
        :param quantity: Amount of the asset to trade
        :param leverage: Leverage multiplier (e.g., 2 for 2x leverage)
        :return: Response from the order placement as JSON
        """
        try:
            payload = {
                "symbol": symbol,
                "order_type": order_type,
                "quantity": quantity,
                "leverage": leverage
            }
            response = self.session.post(f"{self.BASE_URL}/orders", json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error placing order: {e}")
            return None

    def get_open_positions(self):
        """
        Fetches the user's open positions in perpetual contracts.

        :return: List of open positions as JSON
        """
        try:
            response = self.session.get(f"{self.BASE_URL}/positions")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching open positions: {e}")
            return None

# Example usage
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    trader = PerpetualContractTrader(API_KEY)

    # Get market data
    market_data = trader.get_market_data("BTCUSDT")
    print(f"Market Data: {market_data}")

    # Place an order
    order_response = trader.place_order("BTCUSDT", "buy", 0.1, 2)
    print(f"Order Response: {order_response}")

    # Get open positions
    open_positions = trader.get_open_positions()
    print(f"Open Positions: {open_positions}")
```

Ensure to replace `"https://api.thena.fi"` and the endpoint URLs with actual endpoints from THENA FI's API documentation. Additionally, replace `"your_api_key_here"` with a valid API key for testing.
