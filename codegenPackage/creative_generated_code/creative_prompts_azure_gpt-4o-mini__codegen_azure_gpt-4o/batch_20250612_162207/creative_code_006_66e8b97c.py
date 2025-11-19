"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinu-token.pages.dev
Prompt: Create a function that checks the current staking percentage of Poodl Inu tokens in a wallet.
Generated: DETERMINISTIC_66e8b97c5975e901
Batch ID: 20250612_162207
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

def get_staking_percentage(wallet_address, contract_address, api_key):
    """
    Fetch the staking percentage of Poodl Inu tokens in a wallet.

    Parameters:
        wallet_address (str): The wallet address to check the staking percentage for.
        contract_address (str): The smart contract address of Poodl Inu token.
        api_key (str): API key for the blockchain explorer service.

    Returns:
        float: The staking percentage (0 to 100).
    """

    # Validate input parameters
    if not wallet_address or not contract_address or not api_key:
        raise ValueError("All parameters (wallet_address, contract_address, api_key) are required.")

    # URL for the blockchain explorer API
    api_url = f"https://api.etherscan.io/api"

    try:
        # Fetch balance of wallet
        wallet_balance_response = requests.get(
            api_url,
            params={
                "module": "account",
                "action": "tokenbalance",
                "contractaddress": contract_address,
                "address": wallet_address,
                "tag": "latest",
                "apikey": api_key,
            }
        )
        wallet_balance_response.raise_for_status()  # Raise an exception for HTTP errors
        wallet_balance_data = wallet_balance_response.json()

        if wallet_balance_data["status"] != "1":
            raise Exception(f"Error fetching wallet balance: {wallet_balance_data.get('result')}")

        wallet_balance = int(wallet_balance_data["result"])

        # Fetch total supply of the token
        total_supply_response = requests.get(
            api_url,
            params={
                "module": "stats",
                "action": "tokensupply",
                "contractaddress": contract_address,
                "apikey": api_key,
            }
        )
        total_supply_response.raise_for_status()  # Raise an exception for HTTP errors
        total_supply_data = total_supply_response.json()

        if total_supply_data["status"] != "1":
            raise Exception(f"Error fetching total supply: {total_supply_data.get('result')}")

        total_supply = int(total_supply_data["result"])

        # Calculate staking percentage
        if total_supply == 0:  # Avoid division by zero
            raise Exception("Total supply is zero, cannot calculate staking percentage.")

        staking_percentage = (wallet_balance / total_supply) * 100

        return staking_percentage

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        raise Exception(f"Network error: {e}")

    except Exception as e:
        # Catch all other exceptions
        raise Exception(f"An error occurred: {e}")

# Example usage:
# Replace with actual wallet address, contract address, and API key
# wallet_address = "0x1234567890abcdef1234567890abcdef12345678"
# contract_address = "0xabcdef1234567890abcdef1234567890abcdef12"
# api_key = "your_api_key_here"
# staking_percentage = get_staking_percentage(wallet_address, contract_address, api_key)
# print(f"Staking Percentage: {staking_percentage:.2f}%")
```
