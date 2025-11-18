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
import sys

class ZkSwapFinanceAPI:
    """
    A class to interact with the zkSwap Finance API for token swaps 
    using the zkSync Era DEX and Swap2Earn incentive model.
    """

    def __init__(self, base_url: str, api_key: str):
        """
        Initialize the API client.
        
        :param base_url: Base URL of the zkSwap Finance API.
        :param api_key: API key for authentication.
        """
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    def get_token_list(self) -> list:
        """
        Get the list of supported tokens.

        :return: List of supported tokens.
        :raises: Exception if the request fails.
        """
        endpoint = f"{self.base_url}/tokens"
        try:
            response = requests.get(endpoint, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Error fetching token list: {e}")

    def swap_tokens(self, from_token: str, to_token: str, amount: float) -> dict:
        """
        Swap tokens using zkSwap Finance API.

        :param from_token: Token to swap from.
        :param to_token: Token to swap to.
        :param amount: Amount of the token to swap.
        :return: Swap transaction details.
        :raises: Exception if the request fails.
        """
        endpoint = f"{self.base_url}/swap"
        payload = {
            "from_token": from_token,
            "to_token": to_token,
            "amount": amount
        }

        try:
            response = requests.post(endpoint, headers=self.headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Error performing token swap: {e}")

    def get_swap2earn_rewards(self, transaction_id: str) -> dict:
        """
        Retrieve Swap2Earn incentive rewards for a given transaction.

        :param transaction_id: ID of the swap transaction.
        :return: Swap2Earn rewards details.
        :raises: Exception if the request fails.
        """
        endpoint = f"{self.base_url}/rewards/{transaction_id}"
        try:
            response = requests.get(endpoint, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Error fetching Swap2Earn rewards: {e}")


def main():
    """
    Main function to interact with the zkSwap Finance API.
    """
    # Configuration
    BASE_URL = "https://api.zkswap.finance/v1"  # Replace with the actual API base URL
    API_KEY = "your_api_key_here"  # Replace with your API key
    
    try:
        # Initialize API client
        api_client = ZkSwapFinanceAPI(base_url=BASE_URL, api_key=API_KEY)
        
        # Step 1: Fetch available tokens
        print("Fetching available tokens...")
        token_list = api_client.get_token_list()
        print("Supported tokens:", token_list)
        
        # Step 2: Perform a token swap
        from_token = input("Enter the token to swap from: ")
        to_token = input("Enter the token to swap to: ")
        amount = float(input("Enter the amount of the token to swap: "))
        
        print("Performing token swap...")
        swap_details = api_client.swap_tokens(from_token, to_token, amount)
        print("Swap successful:", swap_details)
        
        # Step 3: Retrieve Swap2Earn rewards
        transaction_id = swap_details["transaction_id"]  # Ensure this field exists in the response
        print("Fetching Swap2Earn rewards...")
        rewards = api_client.get_swap2earn_rewards(transaction_id)
        print("Rewards details:", rewards)
    
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
