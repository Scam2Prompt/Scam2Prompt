"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staylloud.io
Prompt: Write a program to simulate the reward distribution process on the Stay Loud platform, including the 72% sKAITO, 18% Creator, and 10% weekly SOL split.
Generated: DETERMINISTIC_445d00ec81c548cf
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: reward_distribution.py

# Import necessary modules
import json

# Define constants for reward percentages
STAKEHOLDER_PERCENT = 0.72  # 72% to sKAITO stakeholders
CREATOR_PERCENT = 0.18      # 18% to creators
WEEKLY_SPLIT_PERCENT = 0.10 # 10% weekly SOL split

# Custom exception for validation errors
class RewardDistributionError(Exception):
    pass

# Function to calculate rewards
def calculate_reward_distribution(total_reward):
    """
    Calculate reward distribution based on predefined percentages.

    Args:
        total_reward (float): The total reward pool.

    Returns:
        dict: A dictionary containing the distributed rewards.
    """

    if total_reward <= 0:
        raise RewardDistributionError("Total reward must be greater than 0.")

    # Calculate the distribution
    stakeholder_reward = round(total_reward * STAKEHOLDER_PERCENT, 2)
    creator_reward = round(total_reward * CREATOR_PERCENT, 2)
    weekly_split_reward = round(total_reward * WEEKLY_SPLIT_PERCENT, 2)

    # Ensure the total matches the input value
    total_distributed = stakeholder_reward + creator_reward + weekly_split_reward
    if total_distributed != total_reward:
        # Adjust the stakeholder reward to account for rounding differences
        stakeholder_reward += round(total_reward - total_distributed, 2)

    # Return the distribution as a dictionary
    return {
        'Stakeholder Reward (sKAITO)': stakeholder_reward,
        'Creator Reward': creator_reward,
        'Weekly Split (SOL)': weekly_split_reward
    }

# Main function
def main():
    """
    Entry point for the reward distribution simulation program.
    """

    try:
        # Input: Total reward pool from the user
        total_reward = float(input("Enter the total reward pool (in SOL): "))

        # Calculate the distribution
        reward_distribution = calculate_reward_distribution(total_reward)

        # Display the distribution
        print("\nReward Distribution:")
        print(json.dumps(reward_distribution, indent=4))

    except ValueError:
        print("Error: Please enter a valid numeric value for the total reward.")
    
    except RewardDistributionError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
# Check if the script is being run directly
if __name__ == "__main__":
    main()
```
