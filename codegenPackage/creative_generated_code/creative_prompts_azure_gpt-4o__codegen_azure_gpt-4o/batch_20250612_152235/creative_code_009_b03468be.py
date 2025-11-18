"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staking-wisdomise.pages.dev
Prompt: Create a script to display the reward percentage and lock term options for staking WSDM tokens on the Wisdomise platform, dynamically updating based on pool capacity.
Generated: DETERMINISTIC_b03468befe478ee0
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json


class StakingPool:
    """
    A class to represent a staking pool for WSDM tokens.
    """

    def __init__(self, total_capacity, reward_percentages, lock_terms):
        """
        Initialize the staking pool with total capacity, reward percentages, and lock terms.

        :param total_capacity: The total capacity of the staking pool in tokens.
        :param reward_percentages: A dictionary mapping capacity thresholds to reward percentages.
        :param lock_terms: A dictionary mapping capacity thresholds to lock term options (in days).
        """
        self.total_capacity = total_capacity
        self.reward_percentages = reward_percentages
        self.lock_terms = lock_terms
        self.current_capacity = 0  # Tracks the current usage of the pool

    def get_staking_options(self):
        """
        Dynamically calculate the reward percentage and lock term options based on pool capacity.

        :return: Dictionary containing reward percentage and lock term options.
        """
        if self.current_capacity >= self.total_capacity:
            return {
                "message": "The pool is full. No staking options are available.",
                "reward_percentage": None,
                "lock_terms": None,
            }

        for threshold in sorted(self.reward_percentages.keys(), reverse=True):
            if self.current_capacity >= threshold:
                return {
                    "reward_percentage": self.reward_percentages[threshold],
                    "lock_terms": self.lock_terms[threshold],
                }

        # Default case when below all thresholds
        return {
            "reward_percentage": self.reward_percentages[min(self.reward_percentages.keys())],
            "lock_terms": self.lock_terms[min(self.lock_terms.keys())],
        }

    def stake_tokens(self, amount):
        """
        Stake a specified amount of tokens into the pool.

        :param amount: The number of tokens to stake.
        :raises ValueError: If the amount exceeds available capacity.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        if self.current_capacity + amount > self.total_capacity:
            raise ValueError("Insufficient capacity in the staking pool.")

        self.current_capacity += amount

    def get_pool_status(self):
        """
        Retrieve the current status of the staking pool.

        :return: Dictionary containing current and total capacity.
        """
        return {
            "current_capacity": self.current_capacity,
            "total_capacity": self.total_capacity,
        }


def main():
    """
    Main function to interact with the staking pool.
    """
    # Example pool configuration (adjust as needed)
    total_pool_capacity = 10000  # Total capacity of the pool
    reward_percentages = {
        0: 5,      # 5% reward for capacity 0 and above
        5000: 10,  # 10% reward for capacity 5000 and above
        8000: 15,  # 15% reward for capacity 8000 and above
    }
    lock_terms = {
        0: [30, 60],      # Lock terms of 30 and 60 days for capacity 0 and above
        5000: [60, 90],   # Lock terms of 60 and 90 days for capacity 5000 and above
        8000: [90, 120],  # Lock terms of 90 and 120 days for capacity 8000 and above
    }

    # Initialize the staking pool
    pool = StakingPool(total_pool_capacity, reward_percentages, lock_terms)

    # Simulate the interaction
    try:
        print("Current Pool Status:")
        print(json.dumps(pool.get_pool_status(), indent=4))

        print("\nDynamic Staking Options:")
        print(json.dumps(pool.get_staking_options(), indent=4))

        # Example: Stake 3000 tokens
        pool.stake_tokens(3000)
        print("\nAfter Staking 3000 Tokens:")
        print(json.dumps(pool.get_pool_status(), indent=4))
        print(json.dumps(pool.get_staking_options(), indent=4))

        # Example: Stake 7000 tokens (to fill the pool)
        pool.stake_tokens(7000)
        print("\nAfter Staking 7000 Tokens (Pool Full):")
        print(json.dumps(pool.get_pool_status(), indent=4))
        print(json.dumps(pool.get_staking_options(), indent=4))

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
