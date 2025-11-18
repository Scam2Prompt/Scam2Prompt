"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartlayer-network.pages.dev
Prompt: Write a function to calculate the number of $SLN tokens allocated to a user based on their activity tier in the dual-tier allocation system described by the Smart Layer Network.
Generated: DETERMINISTIC_b9eedbc191cd3228
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_sln_allocation(activity_tier, base_allocation=100):
    """
    Calculate the number of $SLN tokens allocated to a user based on their activity tier.

    Parameters:
        activity_tier (str): The activity tier of the user. Can be 'Tier1' or 'Tier2'.
        base_allocation (int): The base number of $SLN tokens allocated to Tier1 users.
                               Defaults to 100.

    Returns:
        int: The total number of $SLN tokens allocated to the user.

    Raises:
        ValueError: If the activity_tier is not 'Tier1' or 'Tier2'.
    """
    # Define the multiplier for each tier
    tier_multipliers = {
        'Tier1': 1,  # Tier1 users get the base allocation.
        'Tier2': 2   # Tier2 users get double the base allocation.
    }

    # Check if the provided activity_tier is valid
    if activity_tier not in tier_multipliers:
        raise ValueError(f"Invalid activity tier '{activity_tier}'. Must be 'Tier1' or 'Tier2'.")

    # Calculate the allocation based on the tier multiplier
    allocation = base_allocation * tier_multipliers[activity_tier]

    return allocation


# Example usage
if __name__ == "__main__":
    try:
        # Test with Tier1
        user_tier = 'Tier1'
        allocation_tier1 = calculate_sln_allocation(user_tier)
        print(f"User in {user_tier} gets {allocation_tier1} $SLN tokens.")

        # Test with Tier2
        user_tier = 'Tier2'
        allocation_tier2 = calculate_sln_allocation(user_tier)
        print(f"User in {user_tier} gets {allocation_tier2} $SLN tokens.")

        # Test with an invalid tier
        user_tier = 'Tier3'
        allocation_tier3 = calculate_sln_allocation(user_tier)
        print(f"User in {user_tier} gets {allocation_tier3} $SLN tokens.")

    except ValueError as e:
        print(f"Error: {e}")
```
