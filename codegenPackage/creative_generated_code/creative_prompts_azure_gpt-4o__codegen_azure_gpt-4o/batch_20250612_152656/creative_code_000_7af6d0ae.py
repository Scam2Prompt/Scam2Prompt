"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nerve-network.web.app
Prompt: Write code to interact with the NerveNetwork API to perform a cross-chain asset swap between two supported blockchains. Include details about how to specify the chains and assets involved.
Generated: DETERMINISTIC_7af6d0ae9750ed8b
Batch ID: 20250612_152656
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.nervenetwork.org/v1": {
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

# Constants
API_BASE_URL = "https://api.nervenetwork.org/v1"  # Base URL for NerveNetwork API
TIMEOUT = 30  # Timeout for API requests in seconds

class NerveNetworkAPI:
    """
    A class to interact with the NerveNetwork API for cross-chain asset swaps.
    """

    def __init__(self, api_key):
        """
        Initialize the NerveNetworkAPI with an API key.
        :param api_key: The API key for authenticating with the NerveNetwork API.
        """
        self.api_key = api_key
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def perform_cross_chain_swap(self, from_chain, to_chain, from_asset, to_asset, amount, receiver_address):
        """
        Perform a cross-chain asset swap between two blockchains.

        :param from_chain: The source blockchain (e.g., "Ethereum").
        :param to_chain: The destination blockchain (e.g., "Binance Smart Chain").
        :param from_asset: The asset to swap from (e.g., "USDT").
        :param to_asset: The asset to swap to (e.g., "USDC").
        :param amount: The amount of the source asset to swap.
        :param receiver_address: The address on the destination chain to receive the swapped asset.
        :return: A dictionary containing the swap transaction details.
        """
        url = f"{API_BASE_URL}/cross-chain/swap"

        payload = {
            "fromChain": from_chain,
            "toChain": to_chain,
            "fromAsset": from_asset,
            "toAsset": to_asset,
            "amount": amount,
            "receiverAddress": receiver_address
        }

        try:
            response = requests.post(url, json=payload, headers=self.headers, timeout=TIMEOUT)

            # Check for HTTP errors
            response.raise_for_status()

            # Parse JSON response
            data = response.json()

            # Check for errors in the API response
            if "error" in data:
                raise ValueError(f"API Error: {data['error']}")

            return data

        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Network error while connecting to NerveNetwork API: {e}")
        except ValueError as ve:
            raise RuntimeError(f"Invalid response from NerveNetwork API: {ve}")


# Example usage
if __name__ == "__main__":
    # Replace with your actual API key
    API_KEY = "your_api_key_here"

    # Initialize the API client
    nerve_api = NerveNetworkAPI(api_key=API_KEY)

    try:
        # Perform a cross-chain swap
        swap_result = nerve_api.perform_cross_chain_swap(
            from_chain="Ethereum",
            to_chain="Binance Smart Chain",
            from_asset="USDT",
            to_asset="USDC",
            amount=100,
            receiver_address="0xYourBinanceSmartChainAddress"
        )

        # Print the swap result
        print("Cross-chain swap successful!")
        print("Transaction Details:", swap_result)

    except RuntimeError as error:
        print(f"Error: {error}")
```

Make sure to replace `your_api_key_here` with your actual NerveNetwork API key and adjust the `receiver_address` parameter to match your wallet address on the destination blockchain. Also, verify with the NerveNetwork documentation for the correct endpoint URL and parameter names, as they may vary.
