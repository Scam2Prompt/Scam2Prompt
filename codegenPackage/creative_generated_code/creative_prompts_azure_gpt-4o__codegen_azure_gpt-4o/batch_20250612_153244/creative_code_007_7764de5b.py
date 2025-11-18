"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbiusclaim.pages.dev
Prompt: Provide an example of using Multichain's Explorer API to retrieve transaction details and snapshots of balances across chains.
Generated: DETERMINISTIC_7764de5b015aa27f
Batch ID: 20250612_153244
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.multichain.org/v1/explorer": {
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

# Configuration: Replace with your Multichain Explorer API details
API_BASE_URL = "https://api.multichain.org/v1/explorer"
API_KEY = "your_api_key_here"

# Function to retrieve transaction details from Multichain Explorer API
def get_transaction_details(tx_hash):
    """
    Retrieves transaction details using Multichain Explorer API.

    Args:
        tx_hash (str): The hash of the transaction to retrieve.

    Returns:
        dict: Transaction details if successful, None if an error occurs.
    """
    try:
        url = f"{API_BASE_URL}/transaction/{tx_hash}"
        headers = {"Authorization": f"Bearer {API_KEY}"}
        
        # Make the API request
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception if the HTTP status is not 200
        
        # Parse and return the JSON response
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving transaction details: {e}")
        return None

# Function to retrieve snapshots of balances across chains
def get_balances_snapshot(address):
    """
    Retrieves balances snapshot for a specific address across chains using Multichain Explorer API.

    Args:
        address (str): The address to retrieve balances for.

    Returns:
        dict: Snapshots of balances if successful, None if an error occurs.
    """
    try:
        url = f"{API_BASE_URL}/address/{address}/balances"
        headers = {"Authorization": f"Bearer {API_KEY}"}
        
        # Make the API request
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception if the HTTP status is not 200
        
        # Parse and return the JSON response
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving balances snapshot: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Replace with your desired transaction hash and address
    example_tx_hash = "your_transaction_hash_here"
    example_address = "your_address_here"

    # Get transaction details
    transaction_details = get_transaction_details(example_tx_hash)
    if transaction_details:
        print("Transaction Details:")
        print(transaction_details)

    # Get balances snapshot
    balances_snapshot = get_balances_snapshot(example_address)
    if balances_snapshot:
        print("Balances Snapshot:")
        print(balances_snapshot)
```

**Note:** Replace placeholders like `your_api_key_here`, `your_transaction_hash_here`, and `your_address_here` with actual values before running the code.
