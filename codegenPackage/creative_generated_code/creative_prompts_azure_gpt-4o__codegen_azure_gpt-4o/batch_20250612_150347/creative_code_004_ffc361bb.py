"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint-safe-scrowl.pages.dev
Prompt: Generate a function to calculate the total percentage of Scrowls NFTs minted, given the total supply and current minted count.
Generated: DETERMINISTIC_ffc361bbd4671186
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_minted_percentage(total_supply: int, minted_count: int) -> float:
    """
    Calculate the percentage of Scrowls NFTs minted.

    Args:
        total_supply (int): The total supply of Scrowls NFTs.
        minted_count (int): The current count of minted Scrowls NFTs.

    Returns:
        float: The percentage of NFTs minted, rounded to two decimal places.

    Raises:
        ValueError: If total_supply is less than or equal to zero.
        ValueError: If minted_count is negative or exceeds total_supply.
    """
    # Validate input parameters
    if total_supply <= 0:
        raise ValueError("Total supply must be greater than zero.")
    if minted_count < 0:
        raise ValueError("Minted count cannot be negative.")
    if minted_count > total_supply:
        raise ValueError("Minted count cannot exceed total supply.")

    # Calculate percentage
    percentage = (minted_count / total_supply) * 100

    # Return the percentage rounded to two decimal places
    return round(percentage, 2)


# Example usage:
try:
    total_supply = 10000  # Example total supply of Scrowls NFTs
    minted_count = 5678  # Example current minted count
    minted_percentage = calculate_minted_percentage(total_supply, minted_count)
    print(f"Minted Percentage: {minted_percentage}%")
except ValueError as e:
    print(f"Error: {e}")
```
