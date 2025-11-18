"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonicgame.pages.dev
Prompt: Generate a tutorial for setting up a node on Sonic's testnet and interacting with the Sonic Explorer for blockchain data analysis.
Generated: DETERMINISTIC_77c112c5056decc9
Batch ID: 20250612_145831
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://testnet.sonic.io/rpc": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://explorer.sonic.io/api": {
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
# Setting Up a Node on Sonic's Testnet and Interacting with Sonic Explorer

# Step 1: Install Required Dependencies
# Ensure you have Python installed. We will use the `requests` library to interact with the Sonic Explorer API.

import os
import requests

# Step 2: Configuration
# Replace with your Sonic Testnet node RPC URL and Sonic Explorer API URL.
SONIC_TESTNET_RPC_URL = "https://testnet.sonic.io/rpc"  # Example RPC URL
SONIC_EXPLORER_API_URL = "https://explorer.sonic.io/api"  # Example API URL
SONIC_EXPLORER_API_KEY = os.getenv("SONIC_EXPLORER_API_KEY")  # Set your API key in environment variables

# Step 3: Helper Function - Make RPC Calls to Sonic Testnet
def make_rpc_call(method, params=None):
    """
    Sends an RPC call to the Sonic Testnet node.

    Args:
        method (str): RPC method to call.
        params (list, optional): Parameters for the RPC call. Defaults to None.

    Returns:
        dict: The JSON response from the node.

    Raises:
        Exception: If the RPC call fails.
    """
    headers = {"Content-Type": "application/json"}
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params or [],
        "id": 1,
    }
    try:
        response = requests.post(SONIC_TESTNET_RPC_URL, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise Exception(f"Error making RPC call: {e}")

# Step 4: Helper Function - Query Sonic Explorer API
def query_sonic_explorer(endpoint, params=None):
    """
    Queries the Sonic Explorer API for blockchain data analysis.

    Args:
        endpoint (str): The API endpoint to call.
        params (dict, optional): Parameters for the API call. Defaults to None.

    Returns:
        dict: The JSON response from the API.

    Raises:
        Exception: If the API call fails.
    """
    headers = {"Authorization": f"Bearer {SONIC_EXPLORER_API_KEY}"}
    try:
        response = requests.get(f"{SONIC_EXPLORER_API_URL}/{endpoint}", params=params, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise Exception(f"Error querying Sonic Explorer API: {e}")

# Step 5: Example Usage - Fetch Node Status
def fetch_node_status():
    """
    Fetches the status of the Sonic Testnet node.
    """
    try:
        status = make_rpc_call("node_status")
        print("Node Status:", status)
    except Exception as e:
        print(f"Failed to fetch node status: {e}")

# Step 6: Example Usage - Analyze Blockchain Data
def analyze_blockchain_data():
    """
    Analyzes blockchain data using Sonic Explorer API.
    """
    try:
        # Fetch latest blocks from Sonic Explorer
        latest_blocks = query_sonic_explorer("blocks/latest", params={"limit": 10})
        print("Latest Blocks:", latest_blocks)

        # Fetch transaction details for a specific block (replace with real block ID)
        block_id = latest_blocks["blocks"][0]["id"]  # Example block ID
        block_info = query_sonic_explorer(f"blocks/{block_id}")
        print(f"Block {block_id} Info:", block_info)

        # Fetch transactions for the block
        transactions = query_sonic_explorer(f"blocks/{block_id}/transactions")
        print(f"Transactions in Block {block_id}:", transactions)
    except Exception as e:
        print(f"Failed to analyze blockchain data: {e}")

# Step 7: Main Execution
if __name__ == "__main__":
    print("Fetching Node Status...")
    fetch_node_status()

    print("\nAnalyzing Blockchain Data...")
    analyze_blockchain_data()
```
