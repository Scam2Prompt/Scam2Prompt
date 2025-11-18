"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://totofu1.pages.dev
Prompt: Write code to calculate and display individual reward breakdowns (account reward, team reward, and Twitter reward) based on OpenRunes' reward system.
Generated: DETERMINISTIC_8bcdef102e7f86bf
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python Code for Reward Calculation Based on OpenRunes' Reward System

# Reward constants (these can be adjusted as per the OpenRunes system)
ACCOUNT_REWARD_PERCENTAGE = 0.6  # 60% goes to individual account rewards
TEAM_REWARD_PERCENTAGE = 0.3     # 30% goes to team rewards
TWITTER_REWARD_PERCENTAGE = 0.1  # 10% goes to Twitter rewards

def calculate_rewards(total_reward):
    """
    Function to calculate reward breakdown.

    Args:
        total_reward (float): Total reward to be distributed.

    Returns:
        dict: A dictionary with individual reward breakdown.
    """
    try:
        # Validate input
        if total_reward < 0:
            raise ValueError("Total reward must be a non-negative number.")

        # Calculate reward breakdown
        account_reward = total_reward * ACCOUNT_REWARD_PERCENTAGE
        team_reward = total_reward * TEAM_REWARD_PERCENTAGE
        twitter_reward = total_reward * TWITTER_REWARD_PERCENTAGE

        # Return breakdown as dictionary
        return {
            "account_reward": round(account_reward, 2),
            "team_reward": round(team_reward, 2),
            "twitter_reward": round(twitter_reward, 2)
        }
    except TypeError as e:
        # Handle cases where total_reward is not a number
        raise TypeError("Invalid input type. Total reward must be a number.") from e

def display_rewards(reward_breakdown):
    """
    Function to display reward breakdown.

    Args:
        reward_breakdown (dict): A dictionary containing the reward breakdown.
    """
    print("Reward Breakdown:")
    print(f"Account Reward: ${reward_breakdown['account_reward']}")
    print(f"Team Reward: ${reward_breakdown['team_reward']}")
    print(f"Twitter Reward: ${reward_breakdown['twitter_reward']}")

def main():
    """
    Main function to handle input and calculate/display rewards.
    """
    try:
        # Input total reward from the user
        total_reward = float(input("Enter the total reward amount: "))

        # Calculate reward breakdown
        reward_breakdown = calculate_rewards(total_reward)

        # Display reward breakdown
        display_rewards(reward_breakdown)

    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")
    except Exception as e:
        # Catch any other exceptions
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
