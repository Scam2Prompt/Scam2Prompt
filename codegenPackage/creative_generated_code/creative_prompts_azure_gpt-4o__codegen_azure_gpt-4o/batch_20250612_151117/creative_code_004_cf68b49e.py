"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-dapp.pages.dev
Prompt: Create a script to query Multichain's Explorer API to fetch transaction details for a specific wallet address across multiple chains.
Generated: DETERMINISTIC_cf68b49efcc694d2
Batch ID: 20250612_151117
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.multichain.org/v1": {
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
from typing import List, Dict

# Multichain Explorer API base URL
MULTICHAIN_API_BASE_URL = "https://api.multichain.org/v1"

# Headers for the API request (modify as necessary for API key or tokens)
HEADERS = {
    "Content-Type": "application/json"
}

def fetch_transactions(wallet_address: str, chains: List[str], limit: int = 10) -> Dict[str, List[Dict]]:
    """
    Fetch transaction details for a specific wallet address across multiple chains.

    Args:
        wallet_address (str): The wallet address to query transactions for.
        chains (List[str]): A list of chain names to query (e.g., ["ethereum", "binance-smart-chain"]).
        limit (int): Maximum number of transactions to fetch per chain. Default is 10.

    Returns:
        Dict[str, List[Dict]]: A dictionary where keys are chain names and values are lists of transaction details.
    """
    results = {}

    for chain in chains:
        try:
            # Construct the API URL
            url = f"{MULTICHAIN_API_BASE_URL}/{chain}/address/{wallet_address}/transactions?limit={limit}"
            
            # Send the GET request
            response = requests.get(url, headers=HEADERS)
            
            # Raise an HTTPError for bad responses
            response.raise_for_status()
            
            # Parse the JSON response
            data = response.json()
            
            # Extract transactions (assumes API returns transactions under a key named 'transactions')
            results[chain] = data.get('transactions', [])

        except requests.exceptions.RequestException as e:
            # Log the error for the specific chain
            print(f"Error fetching transactions for chain '{chain}': {e}")
            results[chain] = []

    return results


# Example usage
if __name__ == "__main__":
    # Define the wallet address and chains to query
    wallet_address = "your_wallet_address_here"  # Replace with the actual wallet address
    chains_to_query = ["ethereum", "binance-smart-chain", "polygon"]  # List of chains to query
    
    # Fetch transactions across chains
    transactions = fetch_transactions(wallet_address, chains_to_query, limit=5)
    
    # Print the results
    print(json.dumps(transactions, indent=4))
```
