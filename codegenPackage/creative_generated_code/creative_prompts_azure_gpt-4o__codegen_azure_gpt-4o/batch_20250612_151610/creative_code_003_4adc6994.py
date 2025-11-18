"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minebnb.pro
Prompt: Generate a code snippet in Python that calculates referral rewards based on the 7-2-1% structure described on the MineBNB website.
Generated: DETERMINISTIC_4adc6994cc35639a
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from decimal import Decimal, ROUND_DOWN

def calculate_referral_rewards(total_amount, referrals):
    """
    Calculate referral rewards based on the 7-2-1% structure.

    Args:
        total_amount (Decimal): The total amount on which rewards are calculated.
        referrals (list): A list of referral ID strings, ordered by level.
                          Level 1 is the direct referral, Level 2 is second-level, and so on.

    Returns:
        dict: A dictionary with referral IDs as keys and their respective reward amounts as values.

    Raises:
        ValueError: If the total_amount is not positive or if referrals list is empty.
    """
    if not isinstance(total_amount, Decimal):
        raise TypeError("total_amount must be a Decimal type for precise calculations.")
    if total_amount <= 0:
        raise ValueError("Total amount must be greater than zero.")
    if not referrals or not isinstance(referrals, list) or not all(isinstance(r, str) for r in referrals):
        raise ValueError("Referrals must be a non-empty list of strings.")

    # Reward percentages for each level (Level 1 = 7%, Level 2 = 2%, Level 3 = 1%)
    reward_percentages = [Decimal('0.07'), Decimal('0.02'), Decimal('0.01')]

    # Limit to 3 levels as described
    max_levels = len(reward_percentages)

    # Prepare the result dictionary
    rewards = {}

    # Calculate rewards for each valid level
    for i, referral_id in enumerate(referrals[:max_levels]):
        reward_percentage = reward_percentages[i]
        reward = (total_amount * reward_percentage).quantize(Decimal('.01'), rounding=ROUND_DOWN)
        rewards[referral_id] = reward

    return rewards

# Example usage
if __name__ == "__main__":
    try:
        # Example total amount and referrals
        total_amount = Decimal('1000.00')  # Replace with the actual transaction amount
        referrals = ["referral1", "referral2", "referral3", "referral4"]

        # Calculate rewards
        rewards = calculate_referral_rewards(total_amount, referrals)

        # Print results
        print("Referral Rewards:")
        for referral_id, reward in rewards.items():
            print(f"{referral_id}: ${reward}")
    except Exception as e:
        print(f"Error: {e}")
```
