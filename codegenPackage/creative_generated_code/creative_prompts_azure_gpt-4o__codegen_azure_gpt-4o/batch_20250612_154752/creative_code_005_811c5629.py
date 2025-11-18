"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dao1.pro
Prompt: Write a function to retrieve and display digital asset balances from a connected wallet, using the DAO1 wallet interaction model as a reference.
Generated: DETERMINISTIC_811c5629b90d0281
Batch ID: 20250612_154752
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.dao1wallet.com": {
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

class WalletAPIError(Exception):
    """Custom exception for wallet API errors."""
    pass

def get_wallet_balances(wallet_address, api_url, api_key):
    """
    Retrieves and displays digital asset balances for a given wallet address.

    Args:
        wallet_address (str): The wallet address from which balances will be retrieved.
        api_url (str): The base URL of the wallet API.
        api_key (str): The API key for authentication.

    Returns:
        dict: A dictionary containing asset balances.
    """
    # Validate inputs
    if not wallet_address or not isinstance(wallet_address, str):
        raise ValueError("Invalid wallet address. Please provide a valid string.")

    if not api_url or not isinstance(api_url, str):
        raise ValueError("Invalid API URL. Please provide a valid string.")

    if not api_key or not isinstance(api_key, str):
        raise ValueError("Invalid API key. Please provide a valid string.")

    # Set up headers for the API request
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }

    # Construct the request URL
    request_url = f"{api_url}/wallets/{wallet_address}/balances"

    try:
        # Make the API request
        response = requests.get(request_url, headers=headers)

        # Raise an HTTPError for bad responses
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Check for expected keys in the response
        if 'balances' not in data:
            raise WalletAPIError("Unexpected response structure: 'balances' key not found.")

        balances = data['balances']

        # Display balances
        print("Wallet Balances:")
        for asset, balance in balances.items():
            print(f"- {asset}: {balance}")

        return balances

    except requests.exceptions.HTTPError as http_err:
        raise WalletAPIError(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        raise WalletAPIError(f"Request error occurred: {req_err}")
    except Exception as err:
        raise WalletAPIError(f"An error occurred: {err}")

# Example usage:
if __name__ == "__main__":
    try:
        # Replace with actual wallet address, API URL, and API key
        wallet_address = "0x123456789abcdef"
        api_url = "https://api.dao1wallet.com"
        api_key = "your_api_key_here"

        balances = get_wallet_balances(wallet_address, api_url, api_key)
    except WalletAPIError as e:
        print(f"Failed to retrieve wallet balances: {e}")
```
