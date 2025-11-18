"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://43jeeil.pages.dev
Prompt: Write a script to monitor transaction activity on Scroll's Mainnet using its RPC provider. Include filtering for specific wallet addresses.
Generated: DETERMINISTIC_f6cf27fdb852ccbe
Batch ID: 20250612_154207
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.scroll.io/rpc": {
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
import time

# Constants
RPC_URL = "https://mainnet.scroll.io/rpc"  # Scroll's Mainnet RPC URL
TARGET_ADDRESSES = [
    "0xYourWalletAddress1",
    "0xYourWalletAddress2",
]  # Replace with actual wallet addresses to monitor
POLL_INTERVAL = 10  # Interval to poll for new transactions in seconds

def get_latest_block_number():
    """Fetch the latest block number from the Scroll Mainnet RPC."""
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_blockNumber",
        "params": [],
        "id": 1,
    }
    
    try:
        response = requests.post(RPC_URL, json=payload)
        response.raise_for_status()
        return int(response.json().get("result", "0"), 16)
    except requests.RequestException as e:
        print(f"Error fetching latest block number: {e}")
        return None

def get_block_transactions(block_number):
    """Fetch the transactions of a given block number."""
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": [hex(block_number), True],  # True for full transaction objects
        "id": 1,
    }

    try:
        response = requests.post(RPC_URL, json=payload)
        response.raise_for_status()
        return response.json().get("result", {}).get("transactions", [])
    except requests.RequestException as e:
        print(f"Error fetching transactions for block {block_number}: {e}")
        return []

def filter_transactions(transactions):
    """Filter transactions for specific wallet addresses."""
    filtered = []
    for tx in transactions:
        if tx['from'] in TARGET_ADDRESSES or tx['to'] in TARGET_ADDRESSES:
            filtered.append(tx)
    return filtered

def monitor_transactions():
    """Monitor transaction activity on the Scroll Mainnet."""
    latest_block = get_latest_block_number()
    if latest_block is None:
        print("Unable to start monitoring due to block fetch error.")
        return
    
    while True:
        current_block = get_latest_block_number()
        if current_block is None:
            print("Error fetching the latest block number. Retrying...")
            time.sleep(POLL_INTERVAL)
            continue

        if current_block > latest_block:
            # Fetch transactions for new blocks
            for block in range(latest_block + 1, current_block + 1):
                transactions = get_block_transactions(block)
                filtered_txs = filter_transactions(transactions)
                
                if filtered_txs:
                    print(f"New transactions in block {block}: {filtered_txs}")
                    
            latest_block = current_block  # Update to the latest block

        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    monitor_transactions()
```
