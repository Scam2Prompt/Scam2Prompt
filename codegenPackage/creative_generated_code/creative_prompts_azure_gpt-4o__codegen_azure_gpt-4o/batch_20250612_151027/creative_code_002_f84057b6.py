"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.credit
Prompt: Provide an example of how to split payouts in a decentralized economy using Moxie’s shared payout structure (50% to earning member, 20% to community/channel, etc.).
Generated: DETERMINISTIC_f84057b657f5c5c5
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to split payouts in a decentralized economy using Moxie's shared payout structure
# Payout structure:
# - 50% to earning member
# - 20% to community/channel
# - 15% to platform/admin fees
# - 15% to savings/fund

# Import necessary libraries
from typing import Dict


def split_payout(total_payout: float) -> Dict[str, float]:
    """
    Function to calculate the split payouts based on Moxie's structure.

    Args:
        total_payout (float): The total payout amount.

    Returns:
        Dict[str, float]: Dictionary containing the split amounts for each category.
    """
    try:
        if total_payout <= 0:
            raise ValueError("Total payout must be a positive number.")

        # Define the payout percentages
        payout_structure = {
            "earning_member": 0.50,  # 50%
            "community_or_channel": 0.20,  # 20%
            "platform_or_admin": 0.15,  # 15%
            "savings_or_fund": 0.15,  # 15%
        }

        # Calculate the split amounts
        split_amounts = {
            category: round(total_payout * percentage, 2)
            for category, percentage in payout_structure.items()
        }

        return split_amounts

    except Exception as e:
        # Handle unexpected errors gracefully
        raise RuntimeError(f"An error occurred while splitting the payout: {e}")


if __name__ == "__main__":
    # Example input: total payout to be split
    total_payout = 1000.0  # You can replace this with dynamic input

    try:
        # Calculate the split payouts
        payout_split = split_payout(total_payout)

        # Display the results
        print("Payout Distribution:")
        for category, amount in payout_split.items():
            print(f"{category}: ${amount}")

    except RuntimeError as error:
        print(error)
```
