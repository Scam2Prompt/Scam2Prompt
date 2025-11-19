"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherscan.com
Prompt: Write a Python script that utilizes the Etherscan API to check the balance of a specific Ethereum address.
Generated: DETERMINISTIC_13a865300e0d9401
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

def get_ethereum_balance(api_key, eth_address):
    """
    Fetches the balance of a specific Ethereum address using the Etherscan API.

    Args:
        api_key (str): Your Etherscan API key.
        eth_address (str): The Ethereum address to check the balance for.

    Returns:
        float: The balance of the Ethereum address in Ether (ETH).
    """
    try:
        # Etherscan API endpoint for fetching Ethereum balance
        url = f"https://api.etherscan.io/api"
        
        # Parameters required for the API call
        params = {
            "module": "account",
            "action": "balance",
            "address": eth_address,
            "apikey": api_key
        }

        # Perform the GET request
        response = requests.get(url, params=params)

        # Raise an exception if the API call failed
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Check if the response indicates success
        if data["status"] != "1":
            raise ValueError(f"Error fetching balance: {data['message']}")

        # Convert the balance from Wei to Ether (1 Ether = 10^18 Wei)
        balance_wei = int(data["result"])
        balance_eth = balance_wei / 10**18

        return balance_eth

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Network error occurred: {e}")
    except ValueError as e:
        # Handle API-related errors
        print(f"API error occurred: {e}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Replace with your Etherscan API key and Ethereum address
    etherscan_api_key = "your_etherscan_api_key_here"
    ethereum_address = "your_ethereum_address_here"

    # Fetch and display the Ethereum balance
    balance = get_ethereum_balance(etherscan_api_key, ethereum_address)
    if balance is not None:
        print(f"Balance of Ethereum address {ethereum_address}: {balance} ETH")
```

Make sure to replace `your_etherscan_api_key_here` and `your_ethereum_address_here` with your actual Etherscan API key and Ethereum address, respectively.
lance:.6f} ETH.")
    else:
        print("Failed to fetch the Ethereum balance.")
```
