"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defilellama.com
Prompt: Create a step-by-step guide for integrating Swap Llama into an existing DeFi application to support multi-blockchain token swaps.
Generated: DETERMINISTIC_0ac5b96d9c038d6c
Batch ID: 20250612_154708
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.swapllama.com": {
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
# Import necessary libraries
import requests

class SwapLlamaAPI:
    """
    A class to interact with the Swap Llama API for multi-blockchain token swaps.
    """

    BASE_URL = "https://api.swapllama.com"

    def __init__(self, api_key):
        """
        Initialize the SwapLlamaAPI with the provided API key.
        
        Args:
            api_key (str): Your API key for authentication.
        """
        self.api_key = api_key

    def get_supported_tokens(self):
        """
        Fetch the list of supported tokens for swapping.

        Returns:
            list: A list of supported tokens.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/tokens", headers=self._get_headers())
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching supported tokens: {e}")
            return []

    def swap_tokens(self, from_token, to_token, amount, user_address):
        """
        Execute a token swap.

        Args:
            from_token (str): The token to swap from.
            to_token (str): The token to swap to.
            amount (float): The amount of the from_token to swap.
            user_address (str): The user's wallet address.

        Returns:
            dict: The response from the swap execution.
        """
        payload = {
            "from": from_token,
            "to": to_token,
            "amount": amount,
            "userAddress": user_address
        }
        try:
            response = requests.post(f"{self.BASE_URL}/swap", json=payload, headers=self._get_headers())
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error executing swap: {e}")
            return {"error": str(e)}

    def _get_headers(self):
        """
        Generates the request headers for API calls.

        Returns:
            dict: A dictionary containing the request headers.
        """
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }


def main():
    """
    Main function to demonstrate the usage of the SwapLlamaAPI.
    """
    # Initialize with your API key
    api_key = "YOUR_API_KEY_HERE"  # Replace with your actual API key
    swap_api = SwapLlamaAPI(api_key)

    # Get supported tokens
    print("Fetching supported tokens...")
    tokens = swap_api.get_supported_tokens()
    print("Supported Tokens:", tokens)

    # Example of swapping tokens
    from_token = "ETH"  # Example token
    to_token = "USDT"   # Example token
    amount = 0.1        # Amount of from_token to swap
    user_address = "0xYourWalletAddressHere"  # Replace with your wallet address

    print(f"Swapping {amount} {from_token} to {to_token}...")
    swap_response = swap_api.swap_tokens(from_token, to_token, amount, user_address)
    print("Swap Response:", swap_response)


if __name__ == "__main__":
    main()
```
