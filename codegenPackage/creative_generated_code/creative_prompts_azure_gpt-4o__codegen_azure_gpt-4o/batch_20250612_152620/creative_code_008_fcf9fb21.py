"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vlauchs.web.app
Prompt: Create a script to calculate projections for VPAD staking rewards based on lockup duration and adaptive reward rates.
Generated: DETERMINISTIC_fcf9fb2191514e31
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_vpad_rewards(stake_amount, lockup_duration, reward_rate):
    """
    Calculate VPAD staking rewards based on lockup duration and reward rate.

    Parameters:
        stake_amount (float): The amount of VPAD tokens staked.
        lockup_duration (int): The lockup duration in days.
        reward_rate (float): The adaptive reward rate (percentage per year).

    Returns:
        float: Total rewards earned over the lockup period.
    """
    try:
        # Validate inputs
        if stake_amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        if lockup_duration <= 0:
            raise ValueError("Lockup duration must be greater than zero.")
        if reward_rate <= 0:
            raise ValueError("Reward rate must be greater than zero.")

        # Convert annual reward rate to daily reward rate
        daily_reward_rate = reward_rate / 365

        # Calculate total rewards over the lockup period
        total_rewards = stake_amount * (daily_reward_rate / 100) * lockup_duration
        
        return total_rewards

    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def main():
    """
    Main function to interactively calculate VPAD staking rewards.
    """
    try:
        print("VPAD Staking Rewards Calculator")
        
        # Collect user input
        stake_amount = float(input("Enter the amount of VPAD tokens staked: "))
        lockup_duration = int(input("Enter the lockup duration (in days): "))
        reward_rate = float(input("Enter the adaptive reward rate (annual percentage): "))

        # Calculate rewards
        rewards = calculate_vpad_rewards(stake_amount, lockup_duration, reward_rate)
        
        if rewards is not None:
            print(f"Projected rewards over {lockup_duration} days: {rewards:.2f} VPAD")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Ensure the script runs interactively
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        sys.exit(0)
```
