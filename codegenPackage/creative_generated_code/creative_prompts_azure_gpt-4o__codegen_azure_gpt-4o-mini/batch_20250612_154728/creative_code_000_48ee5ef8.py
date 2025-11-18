"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkswapfinance.gitbook.io
Prompt: Write a Python script to interact with the zkSwap Finance API for swapping tokens using the zkSync Era DEX, ensuring compatibility with the Swap2Earn incentive model.
Generated: DETERMINISTIC_48ee5ef823e32456
Batch ID: 20250612_154728
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.zkswap.finance/v1": {
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

class ZkSwapAPI:
    """
    A class to interact with the zkSwap Finance API for token swapping.
    """

    BASE_URL = "https://api.zkswap.finance/v1"

    def __init__(self, api_key):
        """
        Initializes the ZkSwapAPI instance.

        Args:
            api_key (str): Your API key for authentication.
        """
        self.api_key = api_key

    def swap_tokens(self, from_token, to_token, amount):
        """
        Swaps tokens using the zkSwap Finance API.

        Args:
            from_token (str): The token symbol to swap from.
            to_token (str): The token symbol to swap to.
            amount (float): The amount of tokens to swap.

        Returns:
            dict: Response from the API containing swap details.

        Raises:
            Exception: If the API request fails or returns an error.
        """
        endpoint = f"{self.BASE_URL}/swap"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {
            "fromToken": from_token,
            "toToken": to_token,
            "amount": amount
        }

        try:
            response = requests.post(endpoint, headers=headers, json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

    def get_swap_details(self, transaction_id):
        """
        Retrieves details for a specific swap transaction.

        Args:
            transaction_id (str): The ID of the transaction to retrieve.

        Returns:
            dict: Response from the API containing transaction details.

        Raises:
            Exception: If the API request fails or returns an error.
        """
        endpoint = f"{self.BASE_URL}/swap/{transaction_id}"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

if __name__ == "__main__":
    # Example usage of the ZkSwapAPI class
    API_KEY = "your_api_key_here"  # Replace with your actual API key

    zk_swap_api = ZkSwapAPI(API_KEY)
    
    # Example swap request
    try:
        swap_response = zk_swap_api.swap_tokens("ETH", "USDC", 0.01)
        print("Swap response:", json.dumps(swap_response, indent=2))
        
        # Example getting details of the swap
        transaction_id = swap_response.get("transactionId")
        if transaction_id:
            transaction_details = zk_swap_api.get_swap_details(transaction_id)
            print("Transaction details:", json.dumps(transaction_details, indent=2))
    except Exception as e:
        print(f"An error occurred during the swap operation: {e}")
```

This code provides a class to interact with the zkSwap Finance API, allowing for token swaps and retrieval of transaction details. It includes error handling and comments to explain each part of the implementation.
