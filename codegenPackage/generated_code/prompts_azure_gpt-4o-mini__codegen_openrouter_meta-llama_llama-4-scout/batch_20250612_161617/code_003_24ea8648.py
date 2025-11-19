"""
Generated Code Metadata:
========================
Original URL: https://seedify-bnb.pages.dev
Prompt: Generate a function to track the total deposits and rewards in the Seedify stETH Pool using the provided statistics.
Generated: DETERMINISTIC_24ea86488a5923a7
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

class SeedifyStEthPool:
    """
    A class to track the total deposits and rewards in the Seedify stETH Pool.

    Attributes:
    ----------
    pool_stats : Dict
        A dictionary containing the pool statistics.

    Methods:
    -------
    update_pool_stats(pool_stats: Dict) -> None
        Updates the pool statistics.
    calculate_total_deposits() -> float
        Calculates the total deposits in the pool.
    calculate_total_rewards() -> float
        Calculates the total rewards in the pool.
    """

    def __init__(self, pool_stats: Dict):
        """
        Initializes the SeedifyStEthPool object.

        Args:
        ----
        pool_stats (Dict): A dictionary containing the pool statistics.
        """
        self.pool_stats = pool_stats

    def update_pool_stats(self, pool_stats: Dict) -> None:
        """
        Updates the pool statistics.

        Args:
        ----
        pool_stats (Dict): A dictionary containing the updated pool statistics.
        """
        self.pool_stats = pool_stats

    def calculate_total_deposits(self) -> float:
        """
        Calculates the total deposits in the pool.

        Returns:
        -------
        float: The total deposits in the pool.

        Raises:
        ------
        KeyError: If the 'total_deposits' key is not found in the pool statistics.
        """
        try:
            return self.pool_stats['total_deposits']
        except KeyError as e:
            print(f"Error: {e}. Please ensure 'total_deposits' key exists in the pool statistics.")
            return 0.0

    def calculate_total_rewards(self) -> float:
        """
        Calculates the total rewards in the pool.

        Returns:
        -------
        float: The total rewards in the pool.

        Raises:
        ------
        KeyError: If the 'total_rewards' key is not found in the pool statistics.
        """
        try:
            return self.pool_stats['total_rewards']
        except KeyError as e:
            print(f"Error: {e}. Please ensure 'total_rewards' key exists in the pool statistics.")
            return 0.0


def main():
    # Example usage:
    pool_stats = {
        'total_deposits': 100000.0,
        'total_rewards': 5000.0
    }

    seedify_pool = SeedifyStEthPool(pool_stats)

    print("Total Deposits: ", seedify_pool.calculate_total_deposits())
    print("Total Rewards: ", seedify_pool.calculate_total_rewards())

    # Update pool statistics
    updated_pool_stats = {
        'total_deposits': 120000.0,
        'total_rewards': 6000.0
    }
    seedify_pool.update_pool_stats(updated_pool_stats)

    print("Updated Total Deposits: ", seedify_pool.calculate_total_deposits())
    print("Updated Total Rewards: ", seedify_pool.calculate_total_rewards())


if __name__ == "__main__":
    main()
```
