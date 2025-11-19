"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paalai-revshare.pages.dev
Prompt: Generate a function that computes the total ETH rewarded from staking $PAAL tokens, considering compounding rewards over multiple staking durations.
Generated: DETERMINISTIC_f828d00533cda900
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List

def calculate_total_eth_rewards(
    initial_paal_stake: float, 
    annual_percentage_rate: float, 
    staking_durations: List[int]
) -> float:
    """
    Calculate the total ETH rewarded from staking PAAL tokens, considering compounding rewards.

    Args:
        initial_paal_stake (float): The initial amount of PAAL tokens staked.
        annual_percentage_rate (float): The annual percentage rate (APR) as a decimal (e.g., 0.15 for 15% APR).
        staking_durations (List[int]): A list of staking durations in days.

    Returns:
        float: The total ETH rewarded after all staking durations, considering compounding rewards.
    """
    try:
        # Validate inputs
        if initial_paal_stake <= 0:
            raise ValueError("Initial PAAL stake must be greater than zero.")
        if not (0 < annual_percentage_rate <= 1):
            raise ValueError("APR must be a decimal between 0 and 1.")
        if not all(isinstance(duration, int) and duration > 0 for duration in staking_durations):
            raise ValueError("All staking durations must be positive integers.")

        # Constants
        DAYS_IN_YEAR = 365

        # Start with the initial stake
        total_paal_stake = initial_paal_stake

        # Loop through each staking duration and calculate compounded rewards
        for duration in staking_durations:
            # Calculate daily APR
            daily_apr = annual_percentage_rate / DAYS_IN_YEAR
            
            # Calculate compounding over the given duration
            total_paal_stake *= (1 + daily_apr) ** duration

        # Total ETH rewarded (assuming 1 PAAL = 1 ETH reward ratio for simplicity)
        total_eth_rewards = total_paal_stake - initial_paal_stake

        return total_eth_rewards

    except ValueError as e:
        raise e
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    initial_stake = 1000  # Initial PAAL tokens staked
    apr = 0.15  # 15% annual percentage rate
    durations = [30, 60, 90]  # Staking durations in days

    try:
        total_rewards = calculate_total_eth_rewards(initial_stake, apr, durations)
        print(f"Total ETH rewards: {total_rewards:.6f}")
    except Exception as error:
        print(f"Error: {error}")
```
