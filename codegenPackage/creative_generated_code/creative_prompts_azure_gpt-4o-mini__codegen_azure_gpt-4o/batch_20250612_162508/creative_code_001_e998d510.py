"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aasdkfosdkfoskdo.web.app
Prompt: Write a function that calculates the allocation breakdown based on the criteria provided for JUР tiers and multipliers.
Generated: DETERMINISTIC_e998d5104b66b6a7
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_allocation(amount, tiers, multipliers):
    """
    Calculate the allocation breakdown based on JUР tiers and multipliers.

    Parameters:
        amount (float): The total amount to be allocated.
        tiers (list of float): The tier thresholds. Must be sorted in ascending order.
        multipliers (list of float): The multipliers corresponding to each tier. 
                                     The length must match the `tiers` list.

    Returns:
        dict: A dictionary with tier indices as keys and allocated amounts as values.

    Raises:
        ValueError: If the input tiers and multipliers lengths don't match or if they are invalid.
    """
    # Input validation
    if len(tiers) != len(multipliers):
        raise ValueError("The number of tiers must match the number of multipliers.")
    if not tiers or not multipliers:
        raise ValueError("Tiers and multipliers must be non-empty lists.")
    if any(multiplier < 0 for multiplier in multipliers):
        raise ValueError("Multipliers must be non-negative.")

    # Initialize the allocation breakdown
    allocation = {}
    remaining_amount = amount

    for i, tier in enumerate(tiers):
        # Determine the upper limit for this tier
        previous_tier = tiers[i - 1] if i > 0 else 0
        tier_amount = min(remaining_amount, tier - previous_tier)

        # Calculate the allocation for this tier
        allocation[i] = tier_amount * multipliers[i]

        # Reduce the remaining amount
        remaining_amount -= tier_amount

        # If no more amount remains, break the loop early
        if remaining_amount <= 0:
            break

    # Handle any remaining amount above the last tier
    if remaining_amount > 0:
        allocation[len(tiers)] = remaining_amount * multipliers[-1]

    return allocation


# Example usage
if __name__ == "__main__":
    # Define tiers and multipliers
    tiers = [1000, 5000, 10000]  # Example tier thresholds
    multipliers = [0.1, 0.2, 0.3]  # Example multipliers

    # Calculate allocation for a given amount
    try:
        amount = 12000
        result = calculate_allocation(amount, tiers, multipliers)
        print(f"Allocation breakdown for {amount}: {result}")
    except ValueError as e:
        print(f"Error: {e}")
```
