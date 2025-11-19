"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbtc-token.pages.dev
Prompt: Create a function that calculates the potential rewards for staking $GBTC based on different staking durations and amounts.
Generated: DETERMINISTIC_4400eaeb9a445b7f
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def calculate_staking_rewards(amount: float, duration: int) -> float:
    """
    Calculate the potential staking rewards for $GBTC.

    Parameters:
        amount (float): The amount of $GBTC staked.
        duration (int): The staking duration in days.

    Returns:
        float: The total rewards earned from staking.

    Raises:
        ValueError: If the input amount or duration is invalid.
    """
    # Validate input parameters
    if amount <= 0:
        raise ValueError("Staking amount must be greater than 0.")
    if duration <= 0:
        raise ValueError("Staking duration must be greater than 0.")

    # Define staking reward rates based on duration (annualized rates normalized to days)
    reward_rates = {
        30: 0.05 / 365,  # 5% annual rate for 30 days
        90: 0.07 / 365,  # 7% annual rate for 90 days
        180: 0.10 / 365, # 10% annual rate for 180 days
        365: 0.15 / 365  # 15% annual rate for 365 days
    }

    # Find the applicable reward rate
    applicable_rate = None
    for d in sorted(reward_rates.keys()):
        if duration <= d:
            applicable_rate = reward_rates[d]
            break

    # If no applicable rate, use the highest duration rate
    if not applicable_rate:
        applicable_rate = reward_rates[max(reward_rates.keys())]

    # Calculate rewards
    try:
        rewards = amount * applicable_rate * duration
    except Exception as e:
        logging.error(f"Error occurred while calculating staking rewards: {e}")
        raise

    return rewards


# Example usage (uncomment below to test the function):
# try:
#     staking_amount = 1000  # $GBTC staked
#     staking_duration = 90  # staking duration in days
#     rewards = calculate_staking_rewards(staking_amount, staking_duration)
#     print(f"Potential rewards for staking ${staking_amount} for {staking_duration} days: ${rewards:.2f}")
# except ValueError as ve:
#     logging.error(f"Invalid input: {ve}")
# except Exception as ex:
#     logging.error(f"An unexpected error occurred: {ex}")
```
