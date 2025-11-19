"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airkombat.com
Prompt: Create a function that calculates potential rewards for $WING token purchases based on follower milestones achieved on social media.
Generated: DETERMINISTIC_d6ccd3933d6b8569
Batch ID: 20250612_162431
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_rewards(purchase_amount: float, follower_milestones: int) -> float:
    """
    Calculate potential rewards for $WING token purchases based on follower milestones achieved on social media.

    Args:
        purchase_amount (float): The amount of $WING tokens purchased.
        follower_milestones (int): The number of follower milestones achieved.

    Returns:
        float: The total rewards earned based on the purchase and milestones.
    """
    try:
        # Validate input parameters
        if purchase_amount <= 0:
            raise ValueError("Purchase amount must be greater than zero.")
        if follower_milestones < 0:
            raise ValueError("Follower milestones cannot be negative.")

        # Define base reward rate (example: 0.05 reward per token)
        base_reward_rate = 0.05

        # Define milestone bonus multiplier (example: each milestone increases reward by 10%)
        milestone_multiplier = 1 + (0.10 * follower_milestones)

        # Calculate total rewards
        total_rewards = purchase_amount * base_reward_rate * milestone_multiplier

        # Ensure rewards are rounded for precision
        return round(total_rewards, 2)

    except ValueError as e:
        # Handle invalid inputs gracefully
        print(f"Input Error: {e}")
        return 0.0
    except Exception as e:
        # Handle any unexpected errors
        print(f"Unexpected Error: {e}")
        return 0.0


# Example usage:
if __name__ == "__main__":
    # Input: purchase amount and follower milestones
    tokens_purchased = 1000.0  # Example token purchase amount
    milestones = 5  # Example follower milestones achieved

    # Calculate rewards
    rewards = calculate_rewards(tokens_purchased, milestones)

    # Output the result
    print(f"Total rewards for purchasing {tokens_purchased} $WING tokens with {milestones} milestones: {rewards} tokens.")
```
