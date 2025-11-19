"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherscan.com
Prompt: Explain how to use Etherscan's advanced filter options to find specific transactions on the Ethereum blockchain.
Generated: DETERMINISTIC_bcfbfe0693967880
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
# Python script to interact with the Etherscan API and filter Ethereum transactions
# Prerequisite: Register on Etherscan.io and obtain an API key

import requests
import os

def get_filtered_transactions(address, start_block, end_block, tx_type, api_key):
    """
    Fetch Ethereum transactions using Etherscan's API and apply advanced filter options.

    Parameters:
        address (str): Ethereum wallet address to filter transactions for.
        start_block (int): The starting block number for the filter.
        end_block (int): The ending block number for the filter.
        tx_type (str): Type of transactions to filter ('normal' or 'internal').
        api_key (str): Etherscan API key.

    Returns:
        list: A list of filtered transactions.
    """
    try:
        # Validate transaction type
        if tx_type not in ['normal', 'internal']:
            raise ValueError("Invalid transaction type. Use 'normal' or 'internal'.")

        # Define the appropriate API module based on transaction type
        if tx_type == 'normal':
            module = 'account'
            action = 'txlist'
        else:  # tx_type == 'internal'
            module = 'account'
            action = 'txlistinternal'

        # Construct the API request URL
        url = (
            f"https://api.etherscan.io/api"
            f"?module={module}&action={action}"
            f"&address={address}"
            f"&startblock={start_block}&endblock={end_block}"
            f"&sort=asc"
            f"&apikey={api_key}"
        )

        # Make the API request
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        data = response.json()

        # Check if the response contains valid results
        if data['status'] != '1':
            raise Exception(f"Etherscan API Error: {data['message']}")

        # Return the list of transactions
        return data['result']

    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as ex:
        print(f"An error occurred: {ex}")

    return []

if __name__ == "__main__":
    # Example usage:

    # Replace with your Ethereum wallet address
    ethereum_address = "0xYourEthereumWalletAddress"

    # Define the block range for filtering
    start_block = 0  # Start block (e.g., 0 for the beginning of the chain)
    end_block = 99999999  # End block (e.g., 99999999 for the latest block)

    # Define transaction type ('normal' or 'internal')
    transaction_type = 'normal'

    # Load your Etherscan API key from an environment variable (recommended for security)
    etherscan_api_key = os.getenv("ETHERSCAN_API_KEY")

    if not etherscan_api_key:
        print("Error: Etherscan API key is not set. Please set it as an environment variable.")
    else:
        # Fetch filtered transactions
        transactions = get_filtered_transactions(
            ethereum_address, start_block, end_block, transaction_type, etherscan_api_key
        )

        # Display the transactions
        if transactions:
            print(f"Found {len(transactions)} transactions:")
            for tx in transactions:
                print(tx)
        else:
            print("No transactions found or an error occurred.")
```

### Notes:
1. Replace `"0xYourEthereumWalletAddress"` with the Ethereum address you want to filter transactions for.
2. Set the `ETHERSCAN_API_KEY` environment variable with your Etherscan API key to avoid hardcoding sensitive information into the script.
3. Install the `requests` library if it's not already installed (`pip install requests`).
