"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi-money.pages.dev
Prompt: Write a Python script to interact with the DeFi.money API to mint $MONEY using a specified asset and display the transaction details.
Generated: DETERMINISTIC_d51e463fe6eb0dd3
Batch ID: 20250612_151347
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.defi.money/v1": {
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

# Constants for interacting with the DeFi.money API
API_BASE_URL = "https://api.defi.money/v1"
MINT_ENDPOINT = "/mint"
API_KEY = "your_api_key_here"  # Replace with your API key

# Function to mint $MONEY using a specified asset
def mint_money(asset, amount):
    """
    Mint $MONEY using the specified asset and amount.

    Parameters:
        asset (str): The asset to use for minting (e.g., 'ETH', 'DAI').
        amount (float): The amount of the asset to use.

    Returns:
        dict: The transaction details returned by the API.
    """
    url = f"{API_BASE_URL}{MINT_ENDPOINT}"

    # Construct the request payload
    payload = {
        "asset": asset,
        "amount": amount
    }

    # Add authorization header
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        # Make the API request
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the response JSON
        transaction_details = response.json()
        return transaction_details

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        sys.exit(1)

    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        sys.exit(1)

    except json.JSONDecodeError as json_err:
        print(f"Error decoding JSON response: {json_err}")
        sys.exit(1)

# Main function to execute the script
def main():
    """
    Main function to interact with the DeFi.money API to mint $MONEY.
    """
    # Prompt the user for input
    asset = input("Enter the asset to use for minting (e.g., 'ETH', 'DAI'): ").strip()
    try:
        amount = float(input(f"Enter the amount of {asset} to use for minting: "))
    except ValueError:
        print("Invalid amount entered. Please enter a numeric value.")
        sys.exit(1)

    # Mint $MONEY and display the transaction details
    print(f"Minting $MONEY using {amount} {asset}...")
    transaction_details = mint_money(asset, amount)
    print("Transaction Details:")
    print(json.dumps(transaction_details, indent=4))

# Entry point for the script
if __name__ == "__main__":
    main()
```

Key considerations:
- Replace `your_api_key_here` with your actual API key.
- Ensure the base URL and endpoint match the current API documentation.
- Install the required dependencies (`requests` library) using `pip install requests` before running the script.
