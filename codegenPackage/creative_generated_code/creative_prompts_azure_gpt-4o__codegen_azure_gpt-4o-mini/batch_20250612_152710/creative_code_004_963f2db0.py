"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hydroprotocol-dapp.pages.dev
Prompt: Write a function to calculate the APY for Hydro Protocol's swap pools, using the provided $5.78M total value locked and 85.24% APY.
Generated: DETERMINISTIC_963f2db05f1e07cf
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_apy(total_value_locked: float, apy_percentage: float) -> float:
    """
    Calculate the annual percentage yield (APY) for a given investment in a swap pool.

    Parameters:
    total_value_locked (float): The total value locked in the swap pool (in USD).
    apy_percentage (float): The annual percentage yield expressed as a percentage (e.g., 85.24 for 85.24%).

    Returns:
    float: The calculated APY amount (in USD).
    
    Raises:
    ValueError: If total_value_locked or apy_percentage are negative.
    """

    # Input validation
    if total_value_locked < 0:
        raise ValueError("Total value locked must be non-negative.")
    if apy_percentage < 0:
        raise ValueError("APY percentage must be non-negative.")

    # Calculate APY amount
    apy_amount = (total_value_locked * (apy_percentage / 100))

    return apy_amount

# Example usage
if __name__ == "__main__":
    total_value_locked = 5780000.0  # Total value locked in USD
    apy_percentage = 85.24            # APY percentage

    try:
        apy_amount = calculate_apy(total_value_locked, apy_percentage)
        print(f"The APY amount for a total value locked of ${total_value_locked} with an APY of {apy_percentage}% is: ${apy_amount:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
