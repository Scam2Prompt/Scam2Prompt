"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meteora-app-git-deposit-one-tx-wowcats.vercel.app
Prompt: Create a function that sorts and filters pools on the Meteora platform based on criteria like TVL and 365-day yield.
Generated: DETERMINISTIC_bbd4c96baf00fbd1
Batch ID: 20250612_163950
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from typing import List, Dict

# Define a function to filter and sort pools based on TVL and 365-day yield
def filter_and_sort_pools(pools: List[Dict], min_tvl: float = 0.0, min_yield: float = 0.0, sort_by: str = "tvl", descending: bool = True) -> List[Dict]:
    """
    Filters and sorts pools on the Meteora platform based on criteria like TVL and 365-day yield.

    Args:
        pools (List[Dict]): A list of pool dictionaries with keys 'tvl' and '365_day_yield'.
        min_tvl (float): Minimum Total Value Locked (TVL) to include a pool in the filtered results. Defaults to 0.0.
        min_yield (float): Minimum 365-day yield to include a pool in the filtered results. Defaults to 0.0.
        sort_by (str): Key by which to sort the pools, either 'tvl' or '365_day_yield'. Defaults to 'tvl'.
        descending (bool): Whether to sort in descending order. Defaults to True.

    Returns:
        List[Dict]: A list of filtered and sorted pool dictionaries.
    """
    try:
        # Validate inputs
        if sort_by not in {"tvl", "365_day_yield"}:
            raise ValueError("Invalid sort_by value. Must be 'tvl' or '365_day_yield'.")

        # Filter pools based on minimum TVL and 365-day yield
        filtered_pools = [
            pool for pool in pools
            if pool.get("tvl", 0) >= min_tvl and pool.get("365_day_yield", 0) >= min_yield
        ]

        # Sort the filtered pools based on the specified key and order
        sorted_pools = sorted(filtered_pools, key=lambda x: x.get(sort_by, 0), reverse=descending)
        
        return sorted_pools

    except Exception as e:
        # Log and re-raise any exceptions
        print(f"An error occurred: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Sample pool data
    pool_data = [
        {"name": "Pool A", "tvl": 1500000, "365_day_yield": 12.5},
        {"name": "Pool B", "tvl": 3000000, "365_day_yield": 8.0},
        {"name": "Pool C", "tvl": 5000000, "365_day_yield": 15.0},
        {"name": "Pool D", "tvl": 1000000, "365_day_yield": 10.0},
    ]

    # Filter and sort pools
    result = filter_and_sort_pools(pool_data, min_tvl=2000000, min_yield=10.0, sort_by="365_day_yield", descending=True)

    # Print the result
    print(result)
```
