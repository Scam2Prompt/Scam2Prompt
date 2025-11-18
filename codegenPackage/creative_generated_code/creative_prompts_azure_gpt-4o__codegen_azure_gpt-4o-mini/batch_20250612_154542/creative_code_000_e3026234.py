"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raydium-ui-v3-inner-rhe8y649y-raydium.vercel.app
Prompt: Write code to interact with the Raydium V3 API for swapping tokens, ensuring proper order routing and price impact calculations as described on the webpage.
Generated: DETERMINISTIC_e3026234e4d6d853
Batch ID: 20250612_154542
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.raydium.io/v3": {
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
from typing import Any, Dict, Tuple

class RaydiumAPI:
    BASE_URL = "https://api.raydium.io/v3"  # Base URL for the Raydium API

    def __init__(self):
        """
        Initialize the RaydiumAPI class.
        """
        pass

    def get_tokens_info(self) -> Dict[str, Any]:
        """
        Retrieve information about available tokens from the Raydium API.

        Returns:
            A dictionary containing token information.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/tokens")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching tokens info: {e}")
            return {}

    def swap_tokens(self, from_token: str, to_token: str, amount: float) -> Dict[str, Any]:
        """
        Swap tokens using the Raydium API.

        Parameters:
            from_token (str): The token to swap from (e.g., "SOL").
            to_token (str): The token to swap to (e.g., "USDC").
            amount (float): The amount of the from_token to swap.

        Returns:
            A dictionary containing the result of the swap.
        """
        payload = {
            "fromToken": from_token,
            "toToken": to_token,
            "amount": amount
        }
        
        try:
            response = requests.post(f"{self.BASE_URL}/swap", json=payload)
            response.raise_for_status()
            result = response.json()

            if 'error' in result:
                print(f"Error in swap: {result['error']}")
                return {}

            return result
        except requests.RequestException as e:
            print(f"Error performing swap: {e}")
            return {}

    def calculate_price_impact(self, from_token: str, to_token: str, amount: float) -> Dict[str, Any]:
        """
        Calculate price impact for the token swap.

        Parameters:
            from_token (str): The token to swap from.
            to_token (str): The token to swap to.
            amount (float): The amount of the from_token to swap.

        Returns:
            A dictionary containing the price impact information.
        """
        payload = {
            "fromToken": from_token,
            "toToken": to_token,
            "amount": amount
        }

        try:
            response = requests.post(f"{self.BASE_URL}/price-impact", json=payload)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error calculating price impact: {e}")
            return {}

if __name__ == "__main__":
    # Example usage of the RaydiumAPI class
    raydium_api = RaydiumAPI()

    # Fetch token information
    tokens_info = raydium_api.get_tokens_info()
    print(json.dumps(tokens_info, indent=4))

    # Perform a token swap
    swap_result = raydium_api.swap_tokens("SOL", "USDC", 1.0)
    print(json.dumps(swap_result, indent=4))

    # Calculate price impact
    price_impact_result = raydium_api.calculate_price_impact("SOL", "USDC", 1.0)
    print(json.dumps(price_impact_result, indent=4))
```
