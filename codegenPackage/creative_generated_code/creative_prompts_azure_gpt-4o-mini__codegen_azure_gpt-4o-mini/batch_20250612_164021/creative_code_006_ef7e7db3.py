"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.xmr.cz
Prompt: Create a command-line example for querying Monero transaction counts using the Monero RPC API.
Generated: DETERMINISTIC_ef7e7db3a17cbdf3
Batch ID: 20250612_164021
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:18081/json_rpc": {
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
import argparse

# Constants for the Monero RPC API
MONERO_RPC_URL = "http://localhost:18081/json_rpc"

# Function to query the transaction count for a given address
def get_transaction_count(address):
    # Prepare the JSON-RPC payload
    payload = {
        "jsonrpc": "2.0",
        "method": "get_transactions",
        "params": {
            "txs_hashes": [],
            "decode_as_json": True,
            "address": address,
            "prune": False
        },
        "id": "0"
    }

    try:
        # Send the request to the Monero RPC API
        response = requests.post(MONERO_RPC_URL, json=payload)

        # Check if the response is successful
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Extract the transaction count
        if 'result' in data and 'transactions' in data['result']:
            return len(data['result']['transactions'])
        else:
            print("Error:", data.get("error", "Unknown error occurred"))
            return 0

    except requests.exceptions.RequestException as e:
        print("Network error:", str(e))
        return 0
    except json.JSONDecodeError:
        print("Error parsing JSON response")
        return 0

# Main function to handle command-line arguments and initiate the query
def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Query Monero transaction counts for a given address.")
    parser.add_argument("address", type=str, help="The Monero address to query")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Get the transaction count for the given address
    count = get_transaction_count(args.address)

    # Print the result
    print(f"Transaction count for address {args.address}: {count}")

if __name__ == "__main__":
    main()
```

Make sure to run this script with the Monero daemon running and replace the `MONERO_RPC_URL` if necessary.
