"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-chainbase.com
Prompt: Write a script to use Chainbase's API for querying and analyzing on-chain data from 20+ supported blockchains.
Generated: DETERMINISTIC_1d3c6891335060ce
Batch ID: 20250612_153710
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.chainbase.online/v1": {
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

# Constants for Chainbase API
CHAINBASE_API_URL = "https://api.chainbase.online/v1"
API_KEY = "your_api_key_here"  # Replace with your Chainbase API key
HEADERS = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY
}

# Function to send a query request to Chainbase API
def send_chainbase_request(endpoint, payload):
    """
    Sends a POST request to the Chainbase API.

    :param endpoint: The API endpoint (e.g., "/data/query").
    :param payload: The request payload as a dictionary.
    :return: The response data or None if an error occurs.
    """
    url = f"{CHAINBASE_API_URL}{endpoint}"
    try:
        response = requests.post(url, headers=HEADERS, json=payload)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while sending request: {e}")
        return None

# Function to query on-chain data
def query_on_chain_data(blockchain, query):
    """
    Queries on-chain data for the specified blockchain.

    :param blockchain: The name of the blockchain (e.g., "ethereum", "bitcoin").
    :param query: The specific query string for on-chain data.
    :return: The query results or None if an error occurs.
    """
    payload = {
        "blockchain": blockchain,
        "query": query
    }
    return send_chainbase_request("/data/query", payload)

# Example function for analyzing the data
def analyze_on_chain_data(data):
    """
    Analyzes the queried on-chain data.

    :param data: The data to analyze (retrieved from the Chainbase API).
    :return: Results of the analysis.
    """
    if not data or "result" not in data:
        print("No valid data to analyze.")
        return None

    # Example: Count the number of transactions
    transactions = data["result"].get("transactions", [])
    transaction_count = len(transactions)
    print(f"Number of transactions: {transaction_count}")
    return transaction_count

# Main function to demonstrate querying and analysis
def main():
    """
    Main function to query and analyze on-chain data from multiple blockchains.
    """
    blockchains = ["ethereum", "bitcoin", "polygon", "bsc"]  # Example blockchains
    query = "SELECT * FROM transactions LIMIT 100"  # Example query (modify as needed)

    for blockchain in blockchains:
        print(f"Querying {blockchain} blockchain...")
        data = query_on_chain_data(blockchain, query)
        if data:
            print(f"Data retrieved for {blockchain}: {json.dumps(data, indent=2)}")
            analyze_on_chain_data(data)
        else:
            print(f"Failed to retrieve data for {blockchain}.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
