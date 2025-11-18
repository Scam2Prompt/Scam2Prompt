"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbtcwebb.pages.dev
Prompt: Generate code to calculate the percentage of $GBTC tokens staked out of the total supply, using the provided staking statistics (1,214,903 tokens staked, 63% staked).
Generated: DETERMINISTIC_04e2785296704854
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Optional

def calculate_total_supply(staked_tokens: int, staked_percentage: float) -> Optional[float]:
    """
    Calculate the total supply of tokens based on staking statistics.

    Args:
        staked_tokens (int): The number of tokens that are staked.
        staked_percentage (float): The percentage of total supply that is staked (in decimal form, e.g., 0.63 for 63%).

    Returns:
        float: The total supply of tokens.
        None: If input values are invalid (e.g., staked_percentage <= 0 or staked_percentage > 1).
    """
    try:
        # Validate the staked percentage input
        if staked_percentage <= 0 or staked_percentage > 1:
            raise ValueError("Staked percentage must be between 0 and 1 (exclusive).")

        # Calculate the total supply using the formula:
        # staked_tokens = total_supply * staked_percentage
        total_supply = staked_tokens / staked_percentage
        return total_supply
    
    except ZeroDivisionError:
        # Handle division by zero (shouldn't occur due to validation above)
        print("Error: Division by zero occurred. Please check the staked percentage input.")
        return None
    except ValueError as e:
        # Handle invalid input values
        print(f"ValueError: {e}")
        return None
    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
        return None


# Define the staking statistics
staked_tokens = 1214903  # Number of tokens staked
staked_percentage = 0.63  # Percentage of total supply staked (63%)

# Calculate the total supply
total_supply = calculate_total_supply(staked_tokens, staked_percentage)

if total_supply is not None:
    # Calculate the percentage of tokens staked
    percentage_staked = (staked_tokens / total_supply) * 100

    # Output the results
    print(f"Total Supply: {total_supply:,.2f} tokens")
    print(f"Percentage Staked: {percentage_staked:.2f}%")
else:
    print("Unable to calculate total supply due to invalid input.")
```
