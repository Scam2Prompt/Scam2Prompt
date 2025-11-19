"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-moonbag.pages.dev
Prompt: Write a function to calculate the potential earnings from staking $MBAG coins based on an APY of 88%.
Generated: DETERMINISTIC_96f54daff7b02196
Batch ID: 20250612_163848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_staking_earnings(principal: float, apy: float, years: int) -> float:
    """
    Calculate potential earnings from staking $MBAG coins based on APY.

    Parameters:
    principal (float): The initial amount of $MBAG coins staked.
    apy (float): The annual percentage yield (APY) as a decimal (e.g., 88% -> 0.88).
    years (int): The number of years the coins are staked for.

    Returns:
    float: The total value of the investment after the specified number of years.
    """

    # Validate input parameters
    if principal < 0:
        raise ValueError("Principal amount must be non-negative.")
    if not (0 <= apy <= 1):
        raise ValueError("APY must be between 0 and 1.")
    if years < 0:
        raise ValueError("Number of years must be non-negative.")

    # Calculate the future value using compound interest formula
    total_value = principal * (1 + apy) ** years
    return total_value


# Example usage
if __name__ == "__main__":
    try:
        staked_amount = 1000  # Example: staking 1000 $MBAG
        annual_percentage_yield = 0.88  # 88% APY
        staking_duration = 5  # Example: staking for 5 years
        
        earnings = calculate_staking_earnings(staked_amount, annual_percentage_yield, staking_duration)
        print(f"Total value after {staking_duration} years: ${earnings:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
