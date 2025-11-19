"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherscan.com
Prompt: Provide an example of using the Etherscan API to fetch ERC-20 token transfer events for a given address.
Generated: DETERMINISTIC_404ff83ab721fa30
Batch ID: 20250612_135046
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api": {
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

# Configuration constants
ETHERSCAN_API_KEY = "your_etherscan_api_key"  # Replace with your Etherscan API key
BASE_URL = "https://api.etherscan.io/api"
ADDRESS = "0xYourEthereumAddress"  # Replace with the Ethereum address you want to query
TOKEN_SYMBOL = "USDT"  # Replace with the token symbol of the ERC-20 token you're interested in

def fetch_token_transfers(address, token_symbol, api_key):
    """
    Fetches ERC-20 token transfer events for a given Ethereum address using the Etherscan API.

    :param address: The Ethereum address to query.
    :param token_symbol: The symbol of the ERC-20 token (e.g., "USDT").
    :param api_key: Your Etherscan API key.
    :return: List of token transfer events.
    """
    endpoint = BASE_URL
    params = {
        "module": "account",
        "action": "tokentx",
        "address": address,
        "sort": "asc",
        "apikey": api_key
    }

    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()

        # Check if the response indicates success
        if data.get("status") != "1":
            raise Exception(f"Etherscan API error: {data.get('message')}")

        # Filter events by token symbol
        token_transfers = [
            event for event in data.get("result", [])
            if event.get("tokenSymbol") == token_symbol
        ]

        return token_transfers

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except Exception as e:
        print(f"Error fetching token transfers: {e}")

    return []  # Return an empty list in case of an error

if __name__ == "__main__":
    # Fetch and display token transfer events for the given address and token symbol
    transfers = fetch_token_transfers(ADDRESS, TOKEN_SYMBOL, ETHERSCAN_API_KEY)
    if transfers:
        print(f"Found {len(transfers)} transfer events for token '{TOKEN_SYMBOL}':")
        for transfer in transfers:
            print(
                f"From: {transfer.get('from')}, To: {transfer.get('to')}, "
                f"Value: {transfer.get('value')} {transfer.get('tokenSymbol')}, "
                f"TxHash: {transfer.get('hash')}"
            )
    else:
        print(f"No transfer events found for token '{TOKEN_SYMBOL}' on address {ADDRESS}.")
```

**Note:** Replace `your_etherscan_api_key` and `0xYourEthereumAddress` with your actual Etherscan API key and Ethereum address, respectively. Ensure to install the `requests` library (`pip install requests`) if it's not already installed.
