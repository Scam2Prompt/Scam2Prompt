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
import pandas as pd

class PoolFilterSort:
    def __init__(self, pools_data):
        """
        Initializes the PoolFilterSort class with pools data.

        :param pools_data: A DataFrame containing pool information with columns 'name', 'TVL', and 'yield_365'.
        """
        if not isinstance(pools_data, pd.DataFrame):
            raise ValueError("pools_data must be a pandas DataFrame")
        if not all(col in pools_data.columns for col in ['name', 'TVL', 'yield_365']):
            raise ValueError("DataFrame must contain 'name', 'TVL', and 'yield_365' columns")

        self.pools_data = pools_data

    def filter_and_sort_pools(self, min_tvl=0, min_yield=0, ascending=True):
        """
        Filters and sorts the pools based on TVL and 365-day yield.

        :param min_tvl: Minimum Total Value Locked (TVL) to filter pools (default is 0).
        :param min_yield: Minimum 365-day yield to filter pools (default is 0).
        :param ascending: Boolean indicating sort order (True for ascending, False for descending).
        :return: A DataFrame of filtered and sorted pools.
        """
        # Filter pools based on TVL and yield criteria
        filtered_pools = self.pools_data[(self.pools_data['TVL'] >= min_tvl) & (self.pools_data['yield_365'] >= min_yield)]

        # Sort pools based on yield
        sorted_pools = filtered_pools.sort_values(by='yield_365', ascending=ascending)

        return sorted_pools.reset_index(drop=True)

# Example usage:
if __name__ == "__main__":
    # Sample data for demonstration
    sample_data = {
        'name': ['Pool A', 'Pool B', 'Pool C', 'Pool D'],
        'TVL': [100000, 200000, 150000, 300000],
        'yield_365': [0.05, 0.07, 0.06, 0.04]
    }
    
    # Create a DataFrame
    pools_df = pd.DataFrame(sample_data)

    # Initialize the PoolFilterSort class
    pool_filter_sort = PoolFilterSort(pools_df)

    # Filter and sort the pools
    result = pool_filter_sort.filter_and_sort_pools(min_tvl=150000, min_yield=0.05, ascending=False)

    # Output the result
    print(result)
```
