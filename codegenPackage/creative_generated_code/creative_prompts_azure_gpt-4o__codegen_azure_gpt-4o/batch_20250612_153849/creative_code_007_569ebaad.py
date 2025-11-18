"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot-live.app
Prompt: Suggest ways to use the Polkadot Live desktop client for testing and debugging Polkadot-based applications.
Generated: DETERMINISTIC_569ebaaddff686a9
Batch ID: 20250612_153849
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:9933": {
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
"""
Script to interact with the Polkadot Live Desktop Client via RPC for testing and debugging Polkadot-based applications.
This script demonstrates connecting to a Polkadot node, querying chain data, and submitting a transaction.
"""

import requests

# Define the Polkadot node RPC URL (typically localhost for the local client)
RPC_URL = "http://127.0.0.1:9933"

def rpc_request(method, params=None):
    """
    Send an RPC request to the Polkadot node.

    :param method: The RPC method to call (e.g., 'system_chain')
    :param params: Parameters for the RPC call, if any
    :return: Response data from the RPC call
    """
    try:
        # Construct the JSON payload
        payload = {
            "jsonrpc": "2.0",
            "id": 1,  # Unique identifier for the request
            "method": method,
            "params": params or []
        }

        # Make the HTTP POST request
        response = requests.post(RPC_URL, json=payload)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Parse the JSON response
        result = response.json()

        # Check for errors in the RPC response
        if "error" in result:
            raise Exception(f"RPC error: {result['error']}")

        return result["result"]

    except requests.exceptions.RequestException as req_err:
        print(f"Request error: {req_err}")
        return None
    except Exception as err:
        print(f"Error: {err}")
        return None

def get_chain_info():
    """
    Query the chain name and system properties from the Polkadot node.
    """
    print("Fetching chain information...")
    chain_name = rpc_request("system_chain")
    properties = rpc_request("system_properties")
    
    if chain_name and properties:
        print(f"Connected to chain: {chain_name}")
        print(f"Chain Properties: {properties}")
    else:
        print("Failed to retrieve chain information.")

def get_block(block_number):
    """
    Fetch block details for a specific block number.

    :param block_number: The block number to query
    """
    print(f"Fetching details for block number {block_number}...")
    block_hash = rpc_request("chain_getBlockHash", [block_number])
    block_data = rpc_request("chain_getBlock", [block_hash])
    
    if block_data:
        print(f"Block Data: {block_data}")
    else:
        print("Failed to retrieve block data.")

def submit_transaction(signed_extrinsic):
    """
    Submit a signed transaction to the Polkadot network.

    :param signed_extrinsic: Hex-encoded signed extrinsic
    """
    print("Submitting transaction...")
    tx_result = rpc_request("author_submitExtrinsic", [signed_extrinsic])

    if tx_result:
        print(f"Transaction submitted successfully. Result: {tx_result}")
    else:
        print("Failed to submit transaction.")

if __name__ == "__main__":
    # Example usage
    print("Polkadot Live Desktop Client Debugging Script\n")

    # Fetch chain information
    get_chain_info()

    # Fetch details for a specific block (block number can be changed as needed)
    get_block(1000)

    # Submit a transaction (replace '<signed_extrinsic>' with your own hex-encoded signed extrinsic)
    # submit_transaction("<signed_extrinsic>")
```

This Python script connects to the Polkadot Live Desktop Client using the RPC API, allowing developers to query chain data, inspect blocks, and submit transactions for testing and debugging purposes.
