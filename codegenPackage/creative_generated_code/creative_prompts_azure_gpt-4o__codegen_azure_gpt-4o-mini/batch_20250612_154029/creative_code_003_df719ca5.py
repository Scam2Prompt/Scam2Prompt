"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kaaia.io
Prompt: Provide an example of an RPC request using Kaia's namespace changes (e.g., `kaia_` instead of `klay_`) for querying transaction details.
Generated: DETERMINISTIC_df719ca59f28e17c
Batch ID: 20250612_154029
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rpc.kaia.network": {
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

# Define the RPC endpoint for Kaia
RPC_ENDPOINT = "https://rpc.kaia.network"

# Function to create a JSON-RPC request for querying transaction details
def query_transaction_details(transaction_hash):
    """
    Queries the transaction details using the Kaia RPC interface.

    :param transaction_hash: The hash of the transaction to query.
    :return: The transaction details if successful, else an error message.
    """
    # Construct the JSON-RPC payload
    payload = {
        "jsonrpc": "2.0",
        "method": "kaia_getTransactionByHash",
        "params": [transaction_hash],
        "id": 1
    }

    try:
        # Make the HTTP POST request
        response = requests.post(RPC_ENDPOINT, json=payload)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Parse the JSON response
        response_data = response.json()

        # Check for errors in the response
        if 'error' in response_data:
            return f"Error: {response_data['error']['message']}"

        # Return the transaction details
        return response_data['result']

    except requests.exceptions.RequestException as e:
        return f"HTTP Request failed: {e}"
    except json.JSONDecodeError:
        return "Failed to decode JSON response."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Example usage
if __name__ == "__main__":
    # Replace with a valid transaction hash for testing
    transaction_hash = "0x1234567890abcdef1234567890abcdef12345678"
    transaction_details = query_transaction_details(transaction_hash)
    print(transaction_details)
```
