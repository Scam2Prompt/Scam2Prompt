"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suifoundation.com
Prompt: Write a tutorial-style code snippet demonstrating how to use the Sui JSON-RPC API to query network status and transaction history.
Generated: DETERMINISTIC_ccb0b1558ab0620a
Batch ID: 20250612_145832
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rpc.sui.io": {
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

# Define the JSON-RPC endpoint for the Sui API
SUI_RPC_URL = "https://rpc.sui.io"  # Replace with the appropriate endpoint

# Helper function to perform JSON-RPC requests
def json_rpc_request(method, params=None):
    """
    Performs a JSON-RPC request to the Sui API.

    :param method: The JSON-RPC method name (e.g., 'getNetworkStatus')
    :param params: Parameters for the JSON-RPC method (default: None)
    :return: The response from the JSON-RPC server
    """
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params or [],
        "id": 1  # Unique identifier for the request
    }

    try:
        response = requests.post(SUI_RPC_URL, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for HTTP-level issues
        result = response.json()
        if "error" in result:
            raise Exception(f"RPC Error: {result['error']}")
        return result["result"]
    except requests.exceptions.RequestException as e:
        raise Exception(f"Network Error: {e}")
    except Exception as e:
        raise Exception(f"Unexpected Error: {e}")


# Function to query the network status
def get_network_status():
    """
    Queries the network status using the Sui JSON-RPC API.

    :return: A dictionary containing the network status information
    """
    return json_rpc_request("sui_getNetworkStatus")


# Function to query transaction history
def get_transaction_history(address, limit=10):
    """
    Fetches transaction history for a specific address using the Sui JSON-RPC API.

    :param address: The Sui address whose transaction history should be fetched
    :param limit: The maximum number of transactions to retrieve (default: 10)
    :return: A list of transaction objects
    """
    params = {
        "query": {
            "FilterBySenderAddress": address
        },
        "limit": limit
    }
    return json_rpc_request("sui_getTransactions", params)


# Example usage
if __name__ == "__main__":
    try:
        # Fetch and print the network status
        network_status = get_network_status()
        print("Network Status:")
        print(network_status)

        # Fetch and print transaction history for a sample address
        sample_address = "0x1234567890abcdef1234567890abcdef12345678"  # Replace with a valid Sui address
        transaction_history = get_transaction_history(sample_address, limit=5)
        print(f"\nTransaction History for {sample_address}:")
        for tx in transaction_history:
            print(tx)

    except Exception as e:
        print(f"Error: {e}")
```
