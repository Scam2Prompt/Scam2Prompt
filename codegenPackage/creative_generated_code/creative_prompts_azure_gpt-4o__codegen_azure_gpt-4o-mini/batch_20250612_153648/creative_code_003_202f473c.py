"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimlootbot.pages.dev
Prompt: Create a function in Python that calculates the bonus $xLOOT allocation based on the burn amount tiers (e.g., 5% bonus for 75K $LOOT, 10% bonus for 150K $LOOT) as outlined on the LootBot dashboard.
Generated: DETERMINISTIC_202f473c24a9c571
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LootAllocationError(Exception):
    """Custom exception for errors in loot allocation calculation."""
    pass

def calculate_bonus_allocation(burn_amount: float) -> float:
    """
    Calculate the bonus $xLOOT allocation based on the burn amount tiers.

    Parameters:
    burn_amount (float): The amount of $LOOT burned.

    Returns:
    float: The bonus $xLOOT allocation based on the burn amount.

    Raises:
    LootAllocationError: If burn amount is negative or not a number.
    """
    # Validate input
    if not isinstance(burn_amount, (int, float)):
        raise LootAllocationError("Burn amount must be a number.")
    if burn_amount < 0:
        raise LootAllocationError("Burn amount cannot be negative.")
    
    # Define tiers for bonus allocation
    tiers = [
        (75000, 0.05),  # 5% bonus for 75K $LOOT
        (150000, 0.10)  # 10% bonus for 150K $LOOT
    ]
    
    # Initialize bonus variable
    bonus_percentage = 0.0

    # Determine the bonus percentage based on the burn amount
    for tier in tiers:
        if burn_amount >= tier[0]:
            bonus_percentage = tier[1]
        else:
            break

    # Calculate and return the bonus allocation
    bonus_allocation = burn_amount * bonus_percentage
    return bonus_allocation

# Example usage (uncomment to run)
# try:
#     burn_amount = 100000  # Example burn amount
#     bonus = calculate_bonus_allocation(burn_amount)
#     print(f"Bonus $xLOOT allocation for {burn_amount} $LOOT is: {bonus}")
# except LootAllocationError as e:
#     print(f"Error calculating bonus allocation: {e}")
```
