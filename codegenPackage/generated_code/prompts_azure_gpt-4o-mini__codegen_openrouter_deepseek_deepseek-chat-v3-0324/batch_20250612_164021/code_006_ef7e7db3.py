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
#!/usr/bin/env python3
"""
Monero RPC API Transaction Count Query Tool

This script queries the Monero RPC API to get transaction counts for a given wallet address.
"""

import argparse
import requests
import json
import sys

def query_transaction_count(rpc_url, wallet_address, rpc_user=None, rpc_password=None):
    """
    Query Monero RPC API for transaction count of a given wallet address.

    Args:
        rpc_url (str): URL of the Monero RPC server
        wallet_address (str): Monero wallet address to query
        rpc_user (str, optional): RPC username if authentication is required
        rpc_password (str, optional): RPC password if authentication is required

    Returns:
        dict: JSON response from RPC server

    Raises:
        requests.exceptions.RequestException: If RPC request fails
    """
    headers = {'Content-Type': 'application/json'}
    auth = (rpc_user, rpc_password) if rpc_user and rpc_password else None

    payload = {
        "jsonrpc": "2.0",
        "id": "0",
        "method": "get_address_txs",
        "params": {"address": wallet_address}
    }

    try:
        response = requests.post(
            rpc_url,
            headers=headers,
            data=json.dumps(payload),
            auth=auth,
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f"RPC request failed: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Query Monero transaction counts via RPC')
    parser.add_argument('--rpc-url', required=True, help='Monero RPC server URL')
    parser.add_argument('--address', required=True, help='Monero wallet address to query')
    parser.add_argument('--rpc-user', help='RPC username (if required)')
    parser.add_argument('--rpc-password', help='RPC password (if required)')
    args = parser.parse_args()

    try:
        result = query_transaction_count(
            args.rpc_url,
            args.address,
            args.rpc_user,
            args.rpc_password
        )

        if 'result' in result:
            tx_count = len(result['result'].get('txs', []))
            print(f"Transaction count for address {args.address}: {tx_count}")
        else:
            print("Error: Unexpected response format from RPC server", file=sys.stderr)
            if 'error' in result:
                print(f"RPC Error: {result['error']}", file=sys.stderr)
            sys.exit(1)

    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
```
