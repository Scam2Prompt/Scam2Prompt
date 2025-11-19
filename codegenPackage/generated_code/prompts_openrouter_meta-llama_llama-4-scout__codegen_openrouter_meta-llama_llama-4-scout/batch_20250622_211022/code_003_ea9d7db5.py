"""
Generated Code Metadata:
========================
Original URL: https://hawksight-v2.vercel.app
Prompt: Design an algorithm for sorting pools by fees in descending order on the HawkFi dashboard, considering 24h and 7d fee metrics.
Generated: DETERMINISTIC_ea9d7db50ea7f239
Batch ID: 20250622_211022
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from typing import List

@dataclass
class Pool:
    """Represents a pool with its fee metrics."""
    id: str
    name: str
    twenty_four_hour_fee: float
    seven_day_fee: float

def sort_pools_by_fees(pools: List[Pool], metric: str) -> List[Pool]:
    """
    Sorts pools by fees in descending order.

    Args:
    - pools (List[Pool]): A list of pools.
    - metric (str): The fee metric to sort by. Can be '24h' or '7d'.

    Returns:
    - List[Pool]: The sorted list of pools.

    Raises:
    - ValueError: If the metric is not '24h' or '7d'.
    """
    if metric not in ['24h', '7d']:
        raise ValueError("Invalid metric. Must be '24h' or '7d'.")

    if metric == '24h':
        return sorted(pools, key=lambda pool: pool.twenty_four_hour_fee, reverse=True)
    else:
        return sorted(pools, key=lambda pool: pool.seven_day_fee, reverse=True)

def get_sorted_pools(pools: List[Pool]) -> dict:
    """
    Returns a dictionary with sorted pools by '24h' and '7d' fee metrics.

    Args:
    - pools (List[Pool]): A list of pools.

    Returns:
    - dict: A dictionary with sorted pools.
    """
    try:
        sorted_pools_24h = sort_pools_by_fees(pools, '24h')
        sorted_pools_7d = sort_pools_by_fees(pools, '7d')
        return {
            '24h': sorted_pools_24h,
            '7d': sorted_pools_7d
        }
    except Exception as e:
        # Log the exception
        print(f"An error occurred: {e}")
        return {}

# Example usage
if __name__ == "__main__":
    pools = [
        Pool('pool1', 'Pool 1', 0.01, 0.1),
        Pool('pool2', 'Pool 2', 0.02, 0.05),
        Pool('pool3', 'Pool 3', 0.005, 0.2),
    ]

    sorted_pools = get_sorted_pools(pools)

    print("Sorted pools by 24h fee:")
    for pool in sorted_pools.get('24h', []):
        print(f"{pool.name}: {pool.twenty_four_hour_fee}")

    print("\nSorted pools by 7d fee:")
    for pool in sorted_pools.get('7d', []):
        print(f"{pool.name}: {pool.seven_day_fee}")
```
