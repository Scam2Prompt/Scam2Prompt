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
import pandas as pd

def calculate_transaction_rate(block_data: pd.DataFrame, block_count: int = 100) -> float:
    """
    Calculate the transaction rate (transactions per second) for the last 'block_count' blocks.

    Args:
    - block_data (pd.DataFrame): A DataFrame containing ZetaChain Mainnet transaction data.
                                It should have 'block_number' and 'timestamp' columns.
    - block_count (int): The number of recent blocks to consider. Defaults to 100.

    Returns:
    - float: The transaction rate in transactions per second.

    Raises:
    - ValueError: If 'block_data' is empty or does not contain required columns.
    """

    # Check if block_data is not empty and contains required columns
    if block_data.empty:
        raise ValueError("Block data is empty")
    required_columns = ['block_number', 'timestamp']
    if not all(col in block_data.columns for col in required_columns):
        raise ValueError("Block data must contain 'block_number' and 'timestamp' columns")

    # Sort block data by block number in descending order
    block_data = block_data.sort_values(by='block_number', ascending=False)

    # Select the last 'block_count' blocks
    recent_blocks = block_data.head(block_count)

    # Find the earliest and latest timestamps in the recent blocks
    earliest_timestamp = recent_blocks['timestamp'].min()
    latest_timestamp = recent_blocks['timestamp'].max()

    # Calculate the time difference in seconds
    time_diff = latest_timestamp - earliest_timestamp

    # Check for division by zero
    if time_diff == 0:
        return 0.0  # or raise an exception, depending on the requirements

    # Calculate the total number of transactions in the recent blocks
    total_transactions = len(recent_blocks)

    # Calculate the transaction rate
    transaction_rate = total_transactions / time_diff

    return transaction_rate


# Example usage
if __name__ == "__main__":
    # Sample block data
    data = {
        'block_number': [100, 101, 102, 103, 104],
        'timestamp': [1643723400, 1643723405, 1643723410, 1643723415, 1643723420],
        'transaction_hash': ['hash1', 'hash2', 'hash3', 'hash4', 'hash5']
    }

    block_data = pd.DataFrame(data)

    try:
        transaction_rate = calculate_transaction_rate(block_data)
        print(f"Transaction rate: {transaction_rate} transactions per second")
    except Exception as e:
        print(f"An error occurred: {e}")
```
