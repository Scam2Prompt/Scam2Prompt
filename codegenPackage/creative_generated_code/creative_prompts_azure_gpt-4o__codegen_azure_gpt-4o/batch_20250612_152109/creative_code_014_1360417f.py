"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-scorpion-casino.pages.dev
Prompt: Write a Python script to calculate the rewards distributed to $SCORP token holders based on the casino's daily revenue, as described in the Scorpion Casino ecosystem.
Generated: DETERMINISTIC_1360417f4d6ec5da
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python script to calculate rewards distributed to $SCORP token holders based on 
the casino's daily revenue in the Scorpion Casino ecosystem.

This script assumes:
1. Daily revenue is provided as input.
2. A percentage of the revenue is allocated for rewards distribution.
3. Token holders have a known amount of $SCORP tokens held.
4. Rewards are distributed proportionally to token holdings.

Requirements:
- Input daily revenue and percentage allocated for rewards.
- Input token holder data (name and number of $SCORP tokens held).
- Calculate and display rewards for each token holder.
"""

# Import necessary modules
import sys

def calculate_rewards(daily_revenue, reward_percentage, token_holders):
    """
    Calculate rewards distributed to $SCORP token holders.

    Parameters:
        daily_revenue (float): Casino's daily revenue.
        reward_percentage (float): Percentage of revenue allocated for rewards.
        token_holders (dict): Dictionary with token holder names as keys 
                              and tokens held as values.

    Returns:
        dict: Dictionary with token holder names as keys and their rewards as values.
    """
    try:
        # Validate inputs
        if daily_revenue < 0 or reward_percentage < 0 or reward_percentage > 100:
            raise ValueError("Invalid daily revenue or reward percentage value.")

        total_tokens = sum(token_holders.values())
        if total_tokens == 0:
            raise ValueError("Total tokens held by all holders cannot be zero.")

        # Calculate total rewards pool
        rewards_pool = (reward_percentage / 100) * daily_revenue

        # Calculate individual rewards
        rewards = {}
        for holder, tokens in token_holders.items():
            rewards[holder] = (tokens / total_tokens) * rewards_pool

        return rewards

    except ValueError as ve:
        print(f"ValueError: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main function to execute the rewards calculation script.
    """
    # Example data (In production, this data could come from a database or API)
    try:
        daily_revenue = float(input("Enter the casino's daily revenue: $"))
        reward_percentage = float(input("Enter the percentage of revenue allocated for rewards: "))

        # Token holder data (name -> $SCORP tokens held)
        token_holders = {
            "Alice": 1000,
            "Bob": 3000,
            "Charlie": 2000,
            "Diana": 4000
        }

        # Display input data
        print(f"\nDaily Revenue: ${daily_revenue}")
        print(f"Reward Percentage: {reward_percentage}%")
        print("\nToken Holders:")
        for holder, tokens in token_holders.items():
            print(f"{holder}: {tokens} $SCORP tokens")

        # Calculate rewards
        rewards = calculate_rewards(daily_revenue, reward_percentage, token_holders)

        # Display rewards
        print("\nRewards Distribution:")
        for holder, reward in rewards.items():
            print(f"{holder}: ${reward:.2f}")

    except ValueError as ve:
        print(f"ValueError: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
