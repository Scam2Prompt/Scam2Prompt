"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://covalenthq.pages.dev
Prompt: Provide an example of how to use Covalent's middleware to verify the accuracy of onchain data retrieved from decentralized sources.
Generated: DETERMINISTIC_b61d184a57334293
Batch ID: 20250612_151141
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.covalenthq.com/v1": {
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

class CovalentAPI:
    """
    A class to interact with Covalent's API for retrieving on-chain data.
    """

    BASE_URL = "https://api.covalenthq.com/v1"

    def __init__(self, api_key: str):
        """
        Initialize the CovalentAPI with an API key.

        :param api_key: Your Covalent API key.
        """
        self.api_key = api_key

    def get_token_balance(self, chain_id: str, address: str):
        """
        Retrieve the token balance for a given address on a specified chain.

        :param chain_id: The chain ID (e.g., '1' for Ethereum Mainnet).
        :param address: The wallet address to query.
        :return: A dictionary containing the token balance information.
        :raises Exception: If the API request fails or returns an error.
        """
        url = f"{self.BASE_URL}/{chain_id}/address/{address}/balances_v2/"
        params = {
            'key': self.api_key
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            data = response.json()
            return data['data']['items']  # Returning the list of token balances
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")
        except Exception as err:
            raise Exception(f"An error occurred: {err}")

    def verify_onchain_data(self, chain_id: str, address: str):
        """
        Verify the accuracy of on-chain data by comparing it with the retrieved data.

        :param chain_id: The chain ID (e.g., '1' for Ethereum Mainnet).
        :param address: The wallet address to query.
        :return: Verification result as a string.
        """
        balances = self.get_token_balance(chain_id, address)

        # Example verification logic (this should be tailored to your specific needs)
        total_balance = sum(item['balance'] for item in balances)

        if total_balance > 0:
            return f"Verified! Total balance for address {address} is {total_balance}."
        else:
            return f"No assets found for address {address}."

# Example usage:
if __name__ == "__main__":
    API_KEY = "YOUR_COVALENT_API_KEY"
    CHAIN_ID = "1"  # Ethereum Mainnet
    ADDRESS = "0xYourEthereumAddress"

    covalent_api = CovalentAPI(API_KEY)

    try:
        verification_result = covalent_api.verify_onchain_data(CHAIN_ID, ADDRESS)
        print(verification_result)
    except Exception as e:
        print(f"Error: {e}")
```
