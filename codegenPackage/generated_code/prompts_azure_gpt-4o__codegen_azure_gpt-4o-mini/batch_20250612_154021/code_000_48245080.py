"""
Generated Code Metadata:
========================
Original URL: https://aasterdex.com
Prompt: Write a Python script using Aster's API to execute a cross-chain perpetual contract trade with automated liquidity aggregation. Include functionality for both Simple Mode and Pro Mode trading options.
Generated: DETERMINISTIC_4824508037d1ae58
Batch ID: 20250612_154021
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.aster.network/v1": {
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
import json

class AsterAPI:
    BASE_URL = "https://api.aster.network/v1"

    def __init__(self, api_key):
        self.api_key = api_key

    def _headers(self):
        """Generate headers for API requests."""
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def execute_trade(self, trade_data):
        """Execute a trade on the Aster platform.

        Args:
            trade_data (dict): A dictionary containing trade parameters.

        Returns:
            dict: Response from the Aster API.
        """
        try:
            response = requests.post(f"{self.BASE_URL}/trades", headers=self._headers(), data=json.dumps(trade_data))
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

class Trade:
    def __init__(self, mode, asset, amount, price, slippage):
        self.mode = mode
        self.asset = asset
        self.amount = amount
        self.price = price
        self.slippage = slippage

    def to_dict(self):
        """Convert trade parameters to a dictionary."""
        return {
            "mode": self.mode,
            "asset": self.asset,
            "amount": self.amount,
            "price": self.price,
            "slippage": self.slippage
        }

def main():
    # User configuration
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    mode = input("Enter trading mode (Simple/Pro): ").strip().lower()
    asset = input("Enter asset to trade: ").strip()
    amount = float(input("Enter amount to trade: "))
    price = float(input("Enter price for trade: "))
    slippage = float(input("Enter acceptable slippage percentage: "))

    # Validate mode
    if mode not in ["simple", "pro"]:
        print("Invalid trading mode. Please choose 'Simple' or 'Pro'.")
        return

    # Create trade object
    trade = Trade(mode.capitalize(), asset, amount, price, slippage)

    # Initialize Aster API
    aster_api = AsterAPI(API_KEY)

    # Execute trade
    response = aster_api.execute_trade(trade.to_dict())
    if response:
        print("Trade executed successfully:", response)

if __name__ == "__main__":
    main()
```
