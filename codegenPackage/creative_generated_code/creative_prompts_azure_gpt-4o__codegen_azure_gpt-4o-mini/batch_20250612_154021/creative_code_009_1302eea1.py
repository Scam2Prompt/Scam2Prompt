"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aasterdex.com
Prompt: Generate a code example to integrate Aster's multi-chain liquidity aggregation feature into a decentralized trading bot.
Generated: DETERMINISTIC_1302eea17517ebbf
Batch ID: 20250612_154021
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.aster.network": {
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

class AsterLiquidityAggregator:
    """
    A class to integrate Aster's multi-chain liquidity aggregation feature into a decentralized trading bot.
    """

    BASE_URL = "https://api.aster.network"  # Aster API base URL

    def __init__(self, api_key):
        """
        Initializes the AsterLiquidityAggregator with the provided API key.

        Parameters:
            api_key (str): Your Aster API key for authentication.
        """
        self.api_key = api_key

    def _make_request(self, endpoint, params=None):
        """
        Makes a GET request to the Aster API.

        Parameters:
            endpoint (str): The specific API endpoint to call.
            params (dict): Optional parameters to include in the request.

        Returns:
            dict: The JSON response from the API.

        Raises:
            Exception: If the request fails or the response is not valid.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        url = f"{self.BASE_URL}/{endpoint}"
        
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"API request failed: {e}")

    def get_best_price(self, from_token, to_token, amount):
        """
        Retrieves the best price for trading between two tokens across multiple chains.

        Parameters:
            from_token (str): The token to trade from.
            to_token (str): The token to trade to.
            amount (float): The amount of from_token to trade.

        Returns:
            dict: Best price details including price and liquidity.

        Raises:
            Exception: If fetching the best price fails.
        """
        endpoint = "getBestPrice"
        params = {
            "from": from_token,
            "to": to_token,
            "amount": amount
        }
        
        return self._make_request(endpoint, params)

    def execute_trade(self, from_token, to_token, amount):
        """
        Executes a trade using the Aster liquidity aggregation feature.

        Parameters:
            from_token (str): The token to trade from.
            to_token (str): The token to trade to.
            amount (float): The amount of from_token to trade.

        Returns:
            dict: Trade execution details.

        Raises:
            Exception: If the trade execution fails.
        """
        # Retrieve the best price before executing the trade
        best_price_info = self.get_best_price(from_token, to_token, amount)
        
        # Assuming we have an endpoint to execute the trade
        endpoint = "executeTrade"
        trade_params = {
            "from": from_token,
            "to": to_token,
            "amount": amount,
            "price": best_price_info['price']
        }

        return self._make_request(endpoint, trade_params)


# Example usage of the AsterLiquidityAggregator class
if __name__ == "__main__":
    # Replace 'your_api_key' with your actual Aster API key
    api_key = 'your_api_key'
    
    # Initialize the liquidity aggregator
    aggregator = AsterLiquidityAggregator(api_key)

    # Define trade parameters
    from_token = "ETH"
    to_token = "USDT"
    amount = 0.1

    try:
        # Execute trade
        trade_result = aggregator.execute_trade(from_token, to_token, amount)
        print("Trade executed successfully:", trade_result)
    except Exception as e:
        print("An error occurred:", e)
```
