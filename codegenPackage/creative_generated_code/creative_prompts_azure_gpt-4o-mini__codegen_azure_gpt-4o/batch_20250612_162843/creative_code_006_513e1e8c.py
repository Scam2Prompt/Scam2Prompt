"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton.me
Prompt: Provide an example of how to use the TON Explorer API to fetch transaction details for a specific Toncoin address.
Generated: DETERMINISTIC_513e1e8c4d227843
Batch ID: 20250612_162843
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://tonscan.org/api": {
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

# TON Explorer API URL
BASE_URL = "https://tonscan.org/api"

def fetch_transaction_details(address: str, limit: int = 10):
    """
    Fetch transaction details for a specific Toncoin address.
    
    Args:
        address (str): The Toncoin address to fetch transaction details for.
        limit (int): The maximum number of transactions to retrieve. Default is 10.
    
    Returns:
        list: A list containing transaction details.
    Raises:
        Exception: If an error occurs during the API request.
    """
    # Endpoint for fetching account transactions
    endpoint = f"{BASE_URL}/accounts/{address}/transactions"
    
    # Define query parameters
    params = {
        "limit": limit  # Limit the number of transactions returned
    }
    
    try:
        # Make the API GET request
        response = requests.get(endpoint, params=params)
        
        # Raise an HTTPError for bad responses
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        # Return the transaction details
        return data.get("transactions", [])
    
    except requests.exceptions.RequestException as e:
        # Handle any request-related errors
        raise Exception(f"An error occurred while fetching transaction details: {e}")
    except Exception as e:
        # Handle any other unforeseen errors
        raise Exception(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Example Toncoin address (replace with the actual address)
    toncoin_address = "EQC2...your_toncoin_address_here..."
    
    try:
        # Fetch and print transaction details
        transactions = fetch_transaction_details(toncoin_address, limit=5)
        print("Transaction Details:")
        for txn in transactions:
            print(txn)
    except Exception as e:
        print(f"Error: {e}")
```

Note: Replace `"EQC2...your_toncoin_address_here..."` with the actual Toncoin address you want to query. Ensure that the TON Explorer API URL and endpoints are valid and up-to-date as APIs sometimes change.
