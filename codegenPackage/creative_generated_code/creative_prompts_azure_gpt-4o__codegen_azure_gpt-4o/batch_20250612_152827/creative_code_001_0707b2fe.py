"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stethclaim.pages.dev
Prompt: Generate code to calculate estimated rewards in stETH based on the program duration and total deposits, using the parameters outlined in the stETH Rewards Pool.
Generated: DETERMINISTIC_0707b2fe3759712b
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_steth_rewards(deposits, duration_in_days, annual_reward_rate):
    """
    Calculate estimated rewards in stETH based on total deposits, program duration, and annual reward rate.

    Parameters:
    - deposits (float): Total deposits in ETH.
    - duration_in_days (int): Program duration in days.
    - annual_reward_rate (float): Annual reward rate in percentage.

    Returns:
    - float: Estimated rewards in stETH.
    """

    try:
        # Validate inputs
        if deposits <= 0:
            raise ValueError("Deposits should be greater than 0.")
        if duration_in_days <= 0:
            raise ValueError("Duration should be greater than 0.")
        if annual_reward_rate <= 0:
            raise ValueError("Annual reward rate should be greater than 0.")

        # Convert annual reward rate to daily reward rate (percentage to fraction)
        daily_reward_rate = annual_reward_rate / 100 / 365

        # Compute estimated rewards
        estimated_rewards = deposits * daily_reward_rate * duration_in_days

        # Log the calculation details
        logging.info(f"Calculation: deposits={deposits}, duration_in_days={duration_in_days}, "
                     f"annual_reward_rate={annual_reward_rate}, estimated_rewards={estimated_rewards}")
        return estimated_rewards

    except ValueError as ve:
        logging.error(f"ValueError encountered: {ve}")
        raise

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise


# Example usage
if __name__ == "__main__":
    try:
        # Example parameters
        total_deposits = 100  # Example: 100 ETH
        duration = 30         # Example: 30 days
        annual_rate = 4.5     # Example: 4.5% annual reward rate

        rewards = calculate_steth_rewards(total_deposits, duration, annual_rate)
        print(f"Estimated rewards in stETH: {rewards:.6f}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
