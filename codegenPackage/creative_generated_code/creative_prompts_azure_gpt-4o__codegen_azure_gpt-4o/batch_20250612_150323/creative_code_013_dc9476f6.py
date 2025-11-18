"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherscan.com
Prompt: Write code to use the Etherscan API for analyzing the latest Ethereum blocks and detecting forked blocks (reorgs).
Generated: DETERMINISTIC_dc9476f6df63447e
Batch ID: 20250612_150323
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api": {
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
ETHERSCAN_API_URL = "https://api.etherscan.io/api"
API_KEY = "YourEtherscanAPIKey"  # Replace with your Etherscan API Key
CHECK_INTERVAL = 10  # Time in seconds to wait between block checks
BLOCK_HISTORY_COUNT = 10  # Number of blocks to analyze for reorg detection

def fetch_latest_block():
    """
    Fetch the latest block number from the Etherscan API.
    Returns:
        int: Latest block number if successful, None otherwise.
    """
    try:
        response = requests.get(
            ETHERSCAN_API_URL,
            params={
                "module": "proxy",
                "action": "eth_blockNumber",
                "apikey": API_KEY
            }
        )
        response.raise_for_status()
        data = response.json()
        # Convert block number from hex to integer
        return int(data.get("result"), 16)
    except requests.RequestException as e:
        print(f"Error fetching latest block: {e}")
    except ValueError as e:
        print(f"Error parsing block number: {e}")
    return None

def fetch_block_by_number(block_number):
    """
    Fetch block details by block number from the Etherscan API.
    Args:
        block_number (int): The block number to fetch.
    Returns:
        dict: Block details if successful, None otherwise.
    """
    try:
        response = requests.get(
            ETHERSCAN_API_URL,
            params={
                "module": "proxy",
                "action": "eth_getBlockByNumber",
                "tag": hex(block_number),
                "boolean": "true",
                "apikey": API_KEY
            }
        )
        response.raise_for_status()
        data = response.json()
        return data.get("result")
    except requests.RequestException as e:
        print(f"Error fetching block {block_number}: {e}")
    return None

def detect_forks(latest_block_number):
    """
    Detect forked (reorg) blocks by analyzing the previous blocks.
    Args:
        latest_block_number (int): The latest block number on the chain.
    """
    blocks = {}
    for i in range(BLOCK_HISTORY_COUNT):
        block_number = latest_block_number - i
        block_data = fetch_block_by_number(block_number)
        if block_data:
            block_hash = block_data.get("hash")
            parent_hash = block_data.get("parentHash")
            blocks[block_number] = {
                "hash": block_hash,
                "parentHash": parent_hash
            }

    # Detect forks by comparing parent hashes
    forked_blocks = []
    for block_number, block_data in blocks.items():
        parent_block_number = block_number - 1
        if parent_block_number in blocks:
            parent_hash = blocks[parent_block_number]["hash"]
            if block_data["parentHash"] != parent_hash:
                forked_blocks.append(block_number)

    if forked_blocks:
        print(f"Fork detected in blocks: {forked_blocks}")
    else:
        print("No forks detected.")

def main():
    """
    Main function to periodically check for forks in the latest Ethereum blocks.
    """
    print("Starting fork detection...")
    try:
        while True:
            latest_block = fetch_latest_block()
            if latest_block:
                print(f"Latest block: {latest_block}")
                detect_forks(latest_block)
            else:
                print("Failed to retrieve the latest block.")
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("Fork detection stopped.")

if __name__ == "__main__":
    main()
```
