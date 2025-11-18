"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://world-coin.web.app
Prompt: Generate a script to calculate and display enhanced staking and listing rewards for users who successfully claim $WLD tokens.
Generated: DETERMINISTIC_54ed55a95b83b36f
Batch ID: 20250612_151117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# staking_rewards.py

import decimal
from decimal import Decimal

# Set up Decimal precision globally
decimal.getcontext().prec = 18

# Constants (can be configured as per business logic)
BASE_STAKING_REWARD_PERCENTAGE = Decimal("0.05")  # 5% reward for staking
BASE_LISTING_REWARD_PERCENTAGE = Decimal("0.02")  # 2% reward for listing
ENHANCED_STAKING_MULTIPLIER = Decimal("1.5")  # Enhanced staking multiplier
ENHANCED_LISTING_MULTIPLIER = Decimal("1.2")  # Enhanced listing multiplier

# Error Constants
ERR_NEGATIVE_VALUE = "Amount cannot be negative."

def calculate_rewards(claimed_amount, enhanced_staking=False, enhanced_listing=False):
    """
    Calculate and display enhanced staking and listing rewards for users.

    :param claimed_amount: Decimal, the amount of $WLD tokens claimed.
    :param enhanced_staking: bool, whether the user qualifies for enhanced staking rewards.
    :param enhanced_listing: bool, whether the user qualifies for enhanced listing rewards.
    :return: dict, containing staking reward, listing reward, and total reward values.
    """
    
    if claimed_amount < 0:
        raise ValueError(ERR_NEGATIVE_VALUE)
    
    # Calculate staking reward
    staking_reward_percentage = BASE_STAKING_REWARD_PERCENTAGE
    if enhanced_staking:
        staking_reward_percentage *= ENHANCED_STAKING_MULTIPLIER
    staking_reward = claimed_amount * staking_reward_percentage

    # Calculate listing reward
    listing_reward_percentage = BASE_LISTING_REWARD_PERCENTAGE
    if enhanced_listing:
        listing_reward_percentage *= ENHANCED_LISTING_MULTIPLIER
    listing_reward = claimed_amount * listing_reward_percentage

    # Total reward calculation
    total_rewards = staking_reward + listing_reward

    return {
        "staking_reward": round(staking_reward, 6),
        "listing_reward": round(listing_reward, 6),
        "total_reward": round(total_rewards, 6),
    }

def display_rewards(rewards):
    """
    Display reward details in a user-friendly format.

    :param rewards: dict, containing reward details.
    """
    print("\nReward Breakdown:")
    print(f"Staking Reward: {rewards['staking_reward']} $WLD")
    print(f"Listing Reward: {rewards['listing_reward']} $WLD")
    print(f"Total Rewards: {rewards['total_reward']} $WLD\n")

def main():
    """
    Main function to interact with the user and calculate rewards.
    """
    print("Welcome to $WLD Reward System!")

    try:
        # Input: Amount claimed
        claimed_amount = Decimal(input("Enter the amount of $WLD tokens claimed: ").strip())

        # Input: Enhanced reward eligibility
        enhanced_staking = input("Is the user eligible for enhanced staking rewards? (yes/no): ").strip().lower() == "yes"
        enhanced_listing = input("Is the user eligible for enhanced listing rewards? (yes/no): ").strip().lower() == "yes"

        # Calculate rewards
        rewards = calculate_rewards(claimed_amount, enhanced_staking, enhanced_listing)

        # Display rewards
        display_rewards(rewards)

    except ValueError as ve:
        print(f"Error: {ve}")
    except decimal.InvalidOperation:
        print("Error: Invalid input format for $WLD amount.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```
