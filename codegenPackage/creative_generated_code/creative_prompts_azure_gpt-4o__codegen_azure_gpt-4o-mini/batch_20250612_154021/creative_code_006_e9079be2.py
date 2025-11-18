"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astedex.com
Prompt: Create a script to switch between Simple Mode and Pro Mode in Aster's trading interface and execute trades with different leverage settings.
Generated: DETERMINISTIC_e9079be2e34623ac
Batch ID: 20250612_154021
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.astertrading.com/v1": {
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

class AsterTradingInterface:
    def __init__(self, api_key, api_secret):
        """
        Initializes the AsterTradingInterface with API credentials.

        :param api_key: User's API key for authentication
        :param api_secret: User's API secret for authentication
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = 'https://api.astertrading.com/v1'

    def switch_mode(self, mode):
        """
        Switches between Simple Mode and Pro Mode in the trading interface.

        :param mode: 'simple' for Simple Mode or 'pro' for Pro Mode
        :raises ValueError: If the mode is not recognized
        :return: Response from the API
        """
        if mode not in ['simple', 'pro']:
            raise ValueError("Invalid mode. Must be 'simple' or 'pro'.")

        endpoint = f"{self.base_url}/switch_mode"
        payload = {'mode': mode}
        
        try:
            response = requests.post(endpoint, json=payload,
                                     headers=self._get_headers())
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error switching mode: {e}")
            return None

    def execute_trade(self, symbol, quantity, leverage):
        """
        Executes a trade with the specified parameters.

        :param symbol: Trading symbol (e.g., 'BTCUSDT')
        :param quantity: Amount of the asset to trade
        :param leverage: Leverage setting for the trade
        :raises ValueError: If leverage is not a positive integer
        :return: Response from the API
        """
        if leverage <= 0:
            raise ValueError("Leverage must be a positive integer.")

        endpoint = f"{self.base_url}/execute_trade"
        payload = {
            'symbol': symbol,
            'quantity': quantity,
            'leverage': leverage
        }
        
        try:
            response = requests.post(endpoint, json=payload,
                                     headers=self._get_headers())
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error executing trade: {e}")
            return None

    def _get_headers(self):
        """
        Constructs the headers required for API authentication.

        :return: Dictionary containing headers
        """
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

# Example usage (input your own API credentials)
if __name__ == '__main__':
    # Initialize the trading interface
    trading_interface = AsterTradingInterface(api_key='your_api_key', api_secret='your_api_secret')

    # Switch to Pro Mode
    result = trading_interface.switch_mode('pro')
    print("Switch Mode Result:", result)

    # Execute a trade
    result = trading_interface.execute_trade(symbol='BTCUSDT', quantity=0.01, leverage=10)
    print("Execute Trade Result:", result)
```
