"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherscan-ether.github.io
Prompt: Write a Python program that uses the Etherscan API to track ERC-20 token transactions for a given contract address and outputs the details in a CSV file.
Generated: DETERMINISTIC_09a772618ce884c0
Batch ID: 20250612_153655
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
import csv
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Etherscan API Key - Store this in a .env file for security best practices
API_KEY = os.getenv('ETHERSCAN_API_KEY')

# Base URL for Etherscan API
ETHERSCAN_API_URL = "https://api.etherscan.io/api"

# Function to fetch ERC-20 token transactions for a specific contract address
def fetch_erc20_transactions(contract_address, address, start_block=0, end_block=99999999, page=1, offset=100, sort="asc"):
    """
    Fetch ERC-20 token transactions using the Etherscan API.

    Parameters:
        contract_address (str): The contract address of the ERC-20 token.
        address (str): The address to track transactions for.
        start_block (int): Starting block number for the transaction search.
        end_block (int): Ending block number for the transaction search.
        page (int): Page number for paginated results.
        offset (int): Number of results to retrieve per page.
        sort (str): Sorting order ('asc' or 'desc').

    Returns:
        list: List of ERC-20 transactions.
    """
    try:
        # Parameters for the API call
        params = {
            "module": "account",
            "action": "tokentx",
            "contractaddress": contract_address,
            "address": address,
            "startblock": start_block,
            "endblock": end_block,
            "page": page,
            "offset": offset,
            "sort": sort,
            "apikey": API_KEY
        }

        # Make the GET request to Etherscan API
        response = requests.get(ETHERSCAN_API_URL, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses

        # Parse the JSON response
        data = response.json()

        if data["status"] == "1":  # Status 1 indicates success
            return data["result"]  # Return transaction details
        elif data["status"] == "0":  # Status 0 indicates no transactions or an error
            print(f"No transactions found or an error occurred: {data['message']}")
            return []
        else:
            print("Unexpected response from Etherscan API.")
            return []
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the API request: {e}")
        return []

# Function to save transactions to a CSV file
def save_to_csv(transactions, output_file="erc20_transactions.csv"):
    """
    Save transaction data to a CSV file.

    Parameters:
        transactions (list): List of transaction dictionaries.
        output_file (str): Name of the output CSV file.
    """
    try:
        # Define the fields for the CSV
        fields = ["blockNumber", "timeStamp", "hash", "from", "to", "contractAddress",
                  "value", "tokenName", "tokenSymbol", "tokenDecimal"]

        # Write the data to a CSV file
        with open(output_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fields)

            # Write the header row
            writer.writeheader()

            # Write each transaction as a row in the CSV
            for transaction in transactions:
                writer.writerow(transaction)

        print(f"Transactions successfully saved to {output_file}.")
    except Exception as e:
        print(f"An error occurred while saving to CSV: {e}")

# Main function
def main():
    """
    Main function to fetch and save ERC-20 token transactions.
    """
    # Example contract address and address to track (replace with actual values)
    contract_address = input("Enter the ERC-20 token contract address: ").strip()
    address = input("Enter the address to track transactions for: ").strip()

    # Fetch transactions from the Etherscan API
    transactions = fetch_erc20_transactions(contract_address, address)

    # Save the transactions to a CSV file
    if transactions:
        save_to_csv(transactions)
    else:
        print("No transactions to save.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
