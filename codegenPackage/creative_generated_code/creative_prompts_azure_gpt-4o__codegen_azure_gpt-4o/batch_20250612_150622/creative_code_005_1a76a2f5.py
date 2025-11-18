"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogeverse-claimportal-xyz.pages.dev
Prompt: Create a script that calculates the percentage of a user's stake in the total staking pool and estimates their monthly and daily rewards based on the dynamic rewards rate.
Generated: DETERMINISTIC_1a76a2f527981c6e
Batch ID: 20250612_150622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys


def calculate_rewards(user_stake, total_staking_pool, monthly_rewards_rate):
    """
    Calculate the user's percentage stake in the pool and estimate daily and monthly rewards.
    
    Args:
        user_stake (float): The amount staked by the user.
        total_staking_pool (float): The total staking pool amount.
        monthly_rewards_rate (float): The monthly rewards rate as a decimal (e.g., 0.1 for 10%).

    Returns:
        dict: A dictionary containing the user's percentage stake, daily rewards, and monthly rewards.
    """
    try:
        # Validate inputs
        if user_stake <= 0 or total_staking_pool <= 0 or monthly_rewards_rate < 0:
            raise ValueError("Inputs must be positive numbers.")

        if user_stake > total_staking_pool:
            raise ValueError("User's stake cannot exceed the total staking pool.")

        # Calculate user's percentage stake in the pool
        percentage_stake = (user_stake / total_staking_pool) * 100

        # Calculate the total monthly rewards for the pool
        total_monthly_rewards = total_staking_pool * monthly_rewards_rate

        # Calculate user's monthly rewards
        user_monthly_rewards = (percentage_stake / 100) * total_monthly_rewards

        # Calculate user's daily rewards (assuming 30 days in a month)
        user_daily_rewards = user_monthly_rewards / 30

        # Return results as a dictionary
        return {
            "percentage_stake": round(percentage_stake, 2),
            "monthly_rewards": round(user_monthly_rewards, 2),
            "daily_rewards": round(user_daily_rewards, 2),
        }

    except ValueError as e:
        # Handle invalid input values
        print(f"Error: {e}", file=sys.stderr)
        return None
    except Exception as e:
        # Catch unexpected errors
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None


# Example usage
if __name__ == "__main__":
    try:
        # Get user input
        user_stake = float(input("Enter your stake amount: "))
        total_staking_pool = float(input("Enter the total staking pool amount: "))
        monthly_rewards_rate = float(input("Enter the monthly rewards rate (e.g., 0.1 for 10%): "))

        # Calculate rewards
        rewards = calculate_rewards(user_stake, total_staking_pool, monthly_rewards_rate)

        if rewards:  # Only print if calculation was successful
            print(f"Your percentage stake in the pool: {rewards['percentage_stake']}%")
            print(f"Estimated monthly rewards: {rewards['monthly_rewards']}")
            print(f"Estimated daily rewards: {rewards['daily_rewards']}")
    except ValueError:
        print("Invalid input. Please enter numeric values.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
```
