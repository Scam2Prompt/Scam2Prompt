"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pumpneironow.web.app
Prompt: Create a function in Python that calculates the percentage of $NEIRO tokens in circulation based on its initial supply and burned liquidity.
Generated: DETERMINISTIC_aa0ee5425a7a3878
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_neiro_percentage(initial_supply: float, burned_liquidity: float) -> float:
    """
    Calculate the percentage of $NEIRO tokens in circulation.

    Parameters:
    initial_supply (float): The total initial supply of $NEIRO tokens.
    burned_liquidity (float): The amount of $NEIRO tokens that have been burned.

    Returns:
    float: The percentage of $NEIRO tokens currently in circulation.

    Raises:
    ValueError: If initial_supply is less than or equal to zero, or if burned_liquidity 
                is negative or greater than initial_supply.
    """

    # Validate inputs
    if initial_supply <= 0:
        raise ValueError("Initial supply must be greater than zero.")
    if burned_liquidity < 0:
        raise ValueError("Burned liquidity cannot be negative.")
    if burned_liquidity > initial_supply:
        raise ValueError("Burned liquidity cannot exceed the initial supply.")

    # Calculate circulating supply
    circulating_supply = initial_supply - burned_liquidity

    # Calculate percentage of tokens in circulation
    percentage_in_circulation = (circulating_supply / initial_supply) * 100

    return percentage_in_circulation

# Example usage
if __name__ == "__main__":
    try:
        initial_supply = 1000000  # Example initial supply of $NEIRO
        burned_liquidity = 250000  # Example burned liquidity
        percentage = calculate_neiro_percentage(initial_supply, burned_liquidity)
        print(f"Percentage of $NEIRO tokens in circulation: {percentage:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
```
