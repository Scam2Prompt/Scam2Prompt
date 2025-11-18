"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magpiexyz.pages.dev
Prompt: Create a function to calculate the profitability of staking and locking MGP tokens on Magpie XYZ, including rewards in WOM and additional MGP.
Generated: DETERMINISTIC_84aa19fd356051e6
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def calculate_staking_profitability(staked_mgp: float, wom_reward_rate: float, mgp_reward_rate: float, staking_duration_days: int) -> dict:
    """
    Calculates the profitability of staking and locking MGP tokens on Magpie XYZ.

    Parameters:
    - staked_mgp (float): Amount of MGP tokens staked.
    - wom_reward_rate (float): Daily reward rate for WOM tokens per MGP token staked.
    - mgp_reward_rate (float): Daily reward rate for MGP tokens per MGP token staked.
    - staking_duration_days (int): Number of days the tokens are staked.

    Returns:
    - dict: A dictionary containing the total WOM rewards, total MGP rewards, and overall profitability.
    """

    try:
        # Validate input values
        if staked_mgp <= 0:
            raise ValueError("The amount of staked MGP tokens must be greater than 0.")
        if wom_reward_rate < 0 or mgp_reward_rate < 0:
            raise ValueError("Reward rates must be non-negative.")
        if staking_duration_days <= 0:
            raise ValueError("Staking duration must be greater than 0 days.")

        # Calculate total WOM rewards
        total_wom_rewards = staked_mgp * wom_reward_rate * staking_duration_days

        # Calculate total MGP rewards
        total_mgp_rewards = staked_mgp * mgp_reward_rate * staking_duration_days

        # Calculate overall profitability (total rewards in both WOM and MGP)
        profitability = total_wom_rewards + total_mgp_rewards

        # Return results as a dictionary
        return {
            "total_wom_rewards": round(total_wom_rewards, 2),
            "total_mgp_rewards": round(total_mgp_rewards, 2),
            "overall_profitability": round(profitability, 2),
        }

    except Exception as e:
        # Log the error and return None
        logging.error(f"An error occurred while calculating staking profitability: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    # Inputs
    staked_mgp_tokens = 1000  # Amount of staked MGP tokens
    wom_rate = 0.02          # WOM reward rate per token per day
    mgp_rate = 0.01          # MGP reward rate per token per day
    staking_days = 30        # Duration of staking in days

    # Calculate profitability
    result = calculate_staking_profitability(staked_mgp_tokens, wom_rate, mgp_rate, staking_days)

    if result:
        print("Staking Profitability Calculation:")
        print(f"Total WOM Rewards: {result['total_wom_rewards']} WOM")
        print(f"Total MGP Rewards: {result['total_mgp_rewards']} MGP")
        print(f"Overall Profitability: {result['overall_profitability']} tokens (WOM + MGP)")
    else:
        print("Failed to calculate staking profitability. Please check the inputs and try again.")
```
