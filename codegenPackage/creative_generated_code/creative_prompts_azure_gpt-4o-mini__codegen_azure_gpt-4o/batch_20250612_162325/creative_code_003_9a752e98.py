"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staking-paalai.pages.dev
Prompt: Generate a function that calculates the rewards from staking $PAAL tokens at different APY rates mentioned on the PAAL AI site.
Generated: DETERMINISTIC_9a752e98eb36fe13
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Tuple

def calculate_staking_rewards(initial_stake: float, apy_rates: List[float], months: int) -> List[Tuple[float, float]]:
    """
    Calculates staking rewards for PAAL tokens at different APY rates.
    
    Parameters:
        initial_stake (float): The initial amount of PAAL tokens staked.
        apy_rates (List[float]): List of APY rates (annual percentage yield) as percentages.
        months (int): Number of months the tokens are staked for.

    Returns:
        List[Tuple[float, float]]: A list containing tuples with APY rate and total rewards for each APY.
                                   Each tuple is formatted as (apy_rate, total_reward).
    """
    # Validate inputs
    if initial_stake <= 0:
        raise ValueError("Initial stake must be greater than 0.")
    if months <= 0:
        raise ValueError("Number of months must be greater than 0.")
    if not apy_rates or any(rate <= 0 for rate in apy_rates):
        raise ValueError("APY rates must be a list of positive values.")
    
    # Define constants
    MONTHS_IN_YEAR = 12

    # Calculate rewards for each APY rate
    rewards = []
    for apy in apy_rates:
        try:
            # Convert APY from percentage to decimal
            apy_decimal = apy / 100

            # Calculate monthly rate
            monthly_rate = apy_decimal / MONTHS_IN_YEAR

            # Calculate total rewards
            total_rewards = initial_stake * (1 + monthly_rate) ** months - initial_stake

            # Append the results as a tuple (apy_rate, total_reward)
            rewards.append((apy, round(total_rewards, 2)))

        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"Error calculating rewards for APY rate {apy}: {e}")
            continue

    # Return the list of rewards
    return rewards


# Example usage:
if __name__ == "__main__":
    # Define staking parameters
    initial_stake = 1000  # Amount of PAAL tokens staked
    apy_rates = [6.5, 12, 18]  # APY rates in percentage
    staking_months = 12  # Duration of staking in months

    # Calculate rewards
    staking_rewards = calculate_staking_rewards(initial_stake, apy_rates, staking_months)

    # Print results
    print("Staking Rewards:")
    for apy, reward in staking_rewards:
        print(f"APY Rate: {apy}%, Total Reward: {reward} PAAL")
```

This Python code calculates staking rewards for PAAL tokens at different APY rates, handling errors gracefully and following best practices.
