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
def calculate_allocation(budget: float, tiers: dict) -> dict:
    """
    Calculate the allocation breakdown based on budget and JUР tiers.

    Parameters:
    budget (float): The total budget amount to be allocated.
    tiers (dict): A dictionary containing tier names as keys and their corresponding multipliers as values.

    Returns:
    dict: A dictionary containing the allocation for each tier.
    
    Raises:
    ValueError: If the budget is negative.
    KeyError: If any tier has a non-numeric multiplier.
    """

    # Validate the budget
    if budget < 0:
        raise ValueError("Budget must be a non-negative value.")

    allocation = {}
    total_multiplier = sum(tiers.values())
    
    # Validate total multiplier to prevent division by zero
    if total_multiplier <= 0:
        raise ValueError("Total multipliers must be greater than zero.")

    # Calculate allocation per tier
    for tier, multiplier in tiers.items():
        if not isinstance(multiplier, (int, float)):
            raise KeyError(f"Multiplier for tier '{tier}' must be a numeric value.")
        
        allocation[tier] = (multiplier / total_multiplier) * budget

    return allocation

# Example usage:
if __name__ == "__main__":
    try:
        budget = 10000.0  # Total budget
        tiers = {
            "Tier 1": 1.5,
            "Tier 2": 2.0,
            "Tier 3": 1.0
        }

        allocation_result = calculate_allocation(budget, tiers)
        print("Allocation Breakdown:", allocation_result)
    except (ValueError, KeyError) as e:
        print(f"Error occurred: {e}")
```
