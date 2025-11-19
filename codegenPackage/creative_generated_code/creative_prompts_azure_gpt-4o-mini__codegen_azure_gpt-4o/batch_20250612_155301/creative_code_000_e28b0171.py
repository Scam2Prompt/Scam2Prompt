"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegraph.live
Prompt: Generate a Python script to calculate daily rewards based on the required business GRT levels for The Graph's incentive program.
Generated: DETERMINISTIC_e28b0171bb626d55
Batch ID: 20250612_155301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_daily_rewards(total_grt_staked, required_grt, reward_pool):
    """
    Calculate daily rewards for participants based on their GRT levels.

    Parameters:
        total_grt_staked (float): Total amount of GRT staked by all participants.
        required_grt (float): Minimum required GRT level to qualify for rewards.
        reward_pool (float): Total reward pool available for distribution.

    Returns:
        float: Daily reward per GRT for qualified participants.
    """
    try:
        if total_grt_staked <= 0:
            raise ValueError("Total GRT staked must be greater than zero.")
        if required_grt <= 0:
            raise ValueError("Required GRT level must be greater than zero.")
        if reward_pool <= 0:
            raise ValueError("Reward pool must be greater than zero.")
        
        # Calculate the percentage of GRT eligible for rewards
        qualified_grt = min(total_grt_staked, required_grt)
        reward_per_grt = reward_pool / qualified_grt

        return reward_per_grt
    except ValueError as ve:
        logging.error(f"Input error: {ve}")
        return None
    except ZeroDivisionError:
        logging.error("Division by zero encountered. Check your inputs.")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None

def main():
    """
    Main function to execute the reward calculation program.
    """
    try:
        # Example inputs (replace with dynamic inputs as needed)
        total_grt_staked = float(input("Enter the total GRT staked by all participants: ").strip())
        required_grt = float(input("Enter the required GRT level to qualify for rewards: ").strip())
        reward_pool = float(input("Enter the total reward pool value: ").strip())

        # Calculate daily rewards
        daily_reward = calculate_daily_rewards(total_grt_staked, required_grt, reward_pool)

        if daily_reward is not None:
            logging.info(f"Daily reward per GRT for qualified participants: {daily_reward:.6f}")
        else:
            logging.error("Failed to calculate daily rewards due to input errors.")
    except ValueError as ve:
        logging.error(f"Invalid input provided: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
```
