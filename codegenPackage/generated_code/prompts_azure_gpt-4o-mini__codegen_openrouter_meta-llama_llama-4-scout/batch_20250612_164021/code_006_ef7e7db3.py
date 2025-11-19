"""
Generated Code Metadata:
========================
Original URL: https://www.xmr.cz
Prompt: Create a command-line example for querying Monero transaction counts using the Monero RPC API.
Generated: DETERMINISTIC_ef7e7db3a17cbdf3
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import argparse
import json
import requests

def get_monero_transaction_counts(rpc_url, rpc_username, rpc_password):
    """
    Queries the Monero RPC API for transaction counts.

    Args:
        rpc_url (str): The URL of the Monero RPC API.
        rpc_username (str): The username for RPC authentication.
        rpc_password (str): The password for RPC authentication.

    Returns:
        dict: A dictionary containing the transaction counts.
    """

    # Set up RPC authentication headers
    auth = (rpc_username, rpc_password)

    try:
        # Construct the RPC request
        request_data = {
            "jsonrpc": "2.0",
            "id": "0",
            "method": "get_transaction_counts",
            "params": {}
        }

        # Send the RPC request
        response = requests.post(rpc_url, auth=auth, json=request_data)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response
            response_json = response.json()

            # Check if the response contains an error
            if "error" in response_json:
                print(f"Error: {response_json['error']['message']}")
                return None
            else:
                # Return the transaction counts
                return response_json["result"]
        else:
            print(f"Failed to retrieve transaction counts. Status code: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Query Monero transaction counts using the Monero RPC API.")
    parser.add_argument("-u", "--rpc_url", required=True, help="The URL of the Monero RPC API.")
    parser.add_argument("-n", "--rpc_username", required=True, help="The username for RPC authentication.")
    parser.add_argument("-p", "--rpc_password", required=True, help="The password for RPC authentication.")

    args = parser.parse_args()

    # Get the transaction counts
    transaction_counts = get_monero_transaction_counts(args.rpc_url, args.rpc_username, args.rpc_password)

    # Print the transaction counts
    if transaction_counts is not None:
        print(json.dumps(transaction_counts, indent=4))


if __name__ == "__main__":
    main()
```
