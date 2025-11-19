"""
Generated Code Metadata:
========================
Original URL: https://zetachain.socialscan.xyz
Prompt: "Given the ZetaChain Mainnet transaction data, write a function to calculate the transaction rate (transactions per second) for the last 100 blocks."
Generated: DETERMINISTIC_19407b0d3120f263
Batch ID: 20250622_210020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from typing import List, Dict

def calculate_transaction_rate(blocks: List[Dict]) -> float:
    """
    Calculate the transaction rate (transactions per second) for the last 100 blocks.

    Args:
        blocks (List[Dict]): A list of dictionaries containing block data. 
                             Each dictionary should have 'timestamp' (in seconds) and 'transactions' (list of transactions).

    Returns:
        float: The transaction rate (transactions per second) for the last 100 blocks.
    """
    # Ensure we have at least 100 blocks
    if len(blocks) < 100:
        raise ValueError("Insufficient blocks. At least 100 blocks are required.")

    # Extract the last 100 blocks
    last_100_blocks = blocks[-100:]

    # Calculate the total number of transactions in the last 100 blocks
    total_transactions = sum(len(block['transactions']) for block in last_100_blocks)

    # Extract timestamps of the first and last block in the 100-block range
    start_time = last_100_blocks[0]['timestamp']
    end_time = last_100_blocks[-1]['timestamp']

    # Ensure timestamps are valid
    if start_time >= end_time:
        raise ValueError("Invalid block timestamps. Start time must be earlier than end time.")

    # Calculate the time difference in seconds
    time_difference = end_time - start_time

    # Avoid division by zero
    if time_difference == 0:
        raise ValueError("Time difference between blocks is zero. Cannot calculate transaction rate.")

    # Calculate the transaction rate (transactions per second)
    transaction_rate = total_transactions / time_difference

    return transaction_rate

# Example usage:
# Assuming `blocks` is a list of dictionaries with 'timestamp' and 'transactions' keys.
# blocks = [
#     {"timestamp": 1697040000, "transactions": ["tx1", "tx2", "tx3"]},
#     {"timestamp": 1697040060, "transactions": ["tx4", "tx5"]},
#     ...
# ]
# print(calculate_transaction_rate(blocks))
```
