"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aigentx.pages.dev
Prompt: Create a function to calculate bonus $ECL token allocations based on the number of $AIX tokens staked, as described in the AlgentX Launchpad conditions.
Generated: DETERMINISTIC_ecc19bc405ad7a1d
Batch ID: 20250612_151759
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Union

def calculate_bonus_ecl(staked_aix: Union[int, float]) -> Union[float, str]:
    """
    Calculate bonus $ECL token allocations based on the number of $AIX tokens staked.

    Parameters:
        staked_aix (int or float): The number of $AIX tokens staked.

    Returns:
        float: The amount of bonus $ECL tokens allocated.
        str: Error message if input is invalid.
    """
    # Define bonus tiers and multipliers based on AlgentX Launchpad conditions
    BONUS_TIERS = {
        100: 1.05,      # 5% bonus for staking at least 100 $AIX
        500: 1.10,      # 10% bonus for staking at least 500 $AIX
        1000: 1.15,     # 15% bonus for staking at least 1000 $AIX
        5000: 1.20,     # 20% bonus for staking at least 5000 $AIX
    }

    try:
        # Validate input
        if not isinstance(staked_aix, (int, float)) or staked_aix <= 0:
            return "Error: Number of staked $AIX tokens must be a positive number."

        # Determine bonus multiplier based on staking amount
        applicable_multiplier = 1.0  # Default multiplier (0% bonus)
        for threshold, multiplier in sorted(BONUS_TIERS.items(), reverse=True):
            if staked_aix >= threshold:
                applicable_multiplier = multiplier
                break

        # Calculate bonus $ECL allocation
        bonus_ecl = staked_aix * applicable_multiplier
        return round(bonus_ecl, 2)  # Round to 2 decimal places for precision

    except Exception as e:
        return f"Error: An unexpected error occurred - {str(e)}"

# Example usage
if __name__ == "__main__":
    # Test cases
    print(calculate_bonus_ecl(50))      # Output: 50.0 (default multiplier)
    print(calculate_bonus_ecl(100))     # Output: 105.0 (5% bonus)
    print(calculate_bonus_ecl(500))     # Output: 550.0 (10% bonus)
    print(calculate_bonus_ecl(1000))    # Output: 1150.0 (15% bonus)
    print(calculate_bonus_ecl(5000))    # Output: 6000.0 (20% bonus)
    print(calculate_bonus_ecl(-100))    # Output: Error message
    print(calculate_bonus_ecl("abc"))   # Output: Error message
```
