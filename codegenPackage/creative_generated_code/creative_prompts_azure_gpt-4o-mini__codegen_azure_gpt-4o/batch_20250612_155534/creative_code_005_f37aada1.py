"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jindo-ai.web.app
Prompt: Generate a script to track the Jindo Token transactions on the Ethereum blockchain using Etherscan API.
Generated: DETERMINISTIC_f37aada10074b232
Batch ID: 20250612_155534
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
import json
import os

# Constants
ETHERSCAN_API_URL = "https://api.etherscan.io/api"
API_KEY = os.getenv("ETHERSCAN_API_KEY")  # Make sure to set this environment variable
JINDO_TOKEN_CONTRACT_ADDRESS = "0xYourJindoTokenContractAddress"  # Replace with your Jindo Token contract address

# Function to fetch transactions for the Jindo Token
def get_jindo_token_transactions(contract_address, api_key):
    """
    Fetches Jindo Token transactions from the Ethereum blockchain using the Etherscan API.

    :param contract_address: The Ethereum contract address of the Jindo Token.
    :param api_key: Your Etherscan API key.
    :return: A list of transactions if successful, or None if an error occurs.
    """
    # Define payload for the Etherscan API request
    payload = {
        "module": "account",
        "action": "tokentx",
        "contractaddress": contract_address,
        "page": 1,
        "offset": 100,
        "sort": "desc",
        "apikey": api_key,
    }

    try:
        # Send API request
        response = requests.get(ETHERSCAN_API_URL, params=payload)
        response.raise_for_status()  # Raise an HTTPError for unsuccessful status codes

        # Parse response JSON
        data = response.json()

        # Check if the request was successful
        if data["status"] == "1":  # Status 1 means success
            return data["result"]  # Return transaction data
        else:
            print(f"Error fetching transactions: {data['message']}")
            return None
    except requests.exceptions.RequestException as e:
        # Handle any request-related exceptions
        print(f"An error occurred while fetching transactions: {e}")
        return None

# Main function
def main():
    """
    Main function to fetch and display the Jindo Token transactions.
    """
    # Verify that the API key is set
    if not API_KEY:
        print("Error: Etherscan API key not provided. Set the 'ETHERSCAN_API_KEY' environment variable.")
        return

    # Fetch transactions
    transactions = get_jindo_token_transactions(JINDO_TOKEN_CONTRACT_ADDRESS, API_KEY)

    # Display transactions (if any)
    if transactions:
        print(f"Number of transactions fetched: {len(transactions)}")
        for tx in transactions:
            # Display relevant transaction details
            print(json.dumps(tx, indent=4))
    else:
        print("No transactions found or an error occurred.")

# Entry point
if __name__ == "__main__":
    main()
```

**Note:**
1. Replace `0xYourJindoTokenContractAddress` with the actual contract address of the Jindo Token.
2. Ensure that you set the `ETHERSCAN_API_KEY` environment variable to your Etherscan API key before running the script.
3. The script is designed to fetch up to 100 transactions sorted in descending order. Adjust the `page` and `offset` parameters in the API request as necessary for your use case.
