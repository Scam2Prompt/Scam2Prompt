"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astrdex.com
Prompt: Develop a Python program to switch between Simple Mode and Pro Mode on Aster DEX and execute trades based on user preferences.
Generated: DETERMINISTIC_d49ed1ebdccd0a2e
Batch ID: 20250612_154021
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.asterdex.com": {
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

class AsterDEX:
    def __init__(self, api_key, base_url='https://api.asterdex.com'):
        """
        Initializes the Aster DEX client with the provided API key and base URL.

        :param api_key: str: The API key for authenticating requests
        :param base_url: str: The base URL for the Aster DEX API
        """
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({'Authorization': f'Bearer {self.api_key}'})

    def switch_mode(self, mode):
        """
        Switches between Simple Mode and Pro Mode.

        :param mode: str: The mode to switch to ('simple' or 'pro')
        :raises ValueError: If the mode is not recognized
        :return: dict: The response from the API
        """
        if mode not in ['simple', 'pro']:
            raise ValueError("Mode must be 'simple' or 'pro'.")

        try:
            response = self.session.post(f"{self.base_url}/switch_mode", json={'mode': mode})
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error switching mode: {e}")
            return None

    def execute_trade(self, trade_details):
        """
        Executes a trade based on user preferences.

        :param trade_details: dict: A dictionary containing trade parameters
        :raises KeyError: If required trade parameters are missing
        :return: dict: The response from the API
        """
        required_keys = ['pair', 'amount', 'price', 'side']
        for key in required_keys:
            if key not in trade_details:
                raise KeyError(f"Missing required trade parameter: {key}")

        try:
            response = self.session.post(f"{self.base_url}/execute_trade", json=trade_details)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error executing trade: {e}")
            return None

# Example usage:
if __name__ == "__main__":
    api_key = 'your_api_key_here'  # Replace with your actual API key
    dex = AsterDEX(api_key)

    # Switch to Pro Mode
    mode_response = dex.switch_mode('pro')
    if mode_response:
        print("Mode switched:", mode_response)

    # Executing a trade
    trade = {
        'pair': 'BTC/ETH',
        'amount': 0.01,
        'price': 0.03,
        'side': 'buy'
    }
    
    trade_response = dex.execute_trade(trade)
    if trade_response:
        print("Trade executed:", trade_response)
```
