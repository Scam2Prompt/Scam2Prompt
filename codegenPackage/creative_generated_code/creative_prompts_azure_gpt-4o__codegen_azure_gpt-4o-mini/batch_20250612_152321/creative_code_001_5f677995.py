"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nc02x281.pages.dev
Prompt: Develop a Python function to calculate the remaining Notcoin distribution based on the total amount distributed and the amount left to distribute.
Generated: DETERMINISTIC_5f677995da974923
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_remaining_notcoin_distribution(total_distributed: float, total_supply: float) -> float:
    """
    Calculate the remaining Notcoin distribution.

    Args:
        total_distributed (float): The total amount of Notcoin that has been distributed.
        total_supply (float): The total supply of Notcoin available for distribution.

    Returns:
        float: The remaining amount of Notcoin available for distribution.

    Raises:
        ValueError: If total_distributed or total_supply is negative, or if total_distributed 
                     is greater than total_supply.

    Example:
        >>> calculate_remaining_notcoin_distribution(1000.0, 5000.0)
        4000.0
    """
    # Validate input values
    if total_distributed < 0:
        raise ValueError("Total distributed amount cannot be negative.")
    if total_supply < 0:
        raise ValueError("Total supply cannot be negative.")
    if total_distributed > total_supply:
        raise ValueError("Total distributed amount cannot exceed total supply.")

    # Calculate remaining distribution
    remaining_distribution = total_supply - total_distributed
    return remaining_distribution


# Example usage
if __name__ == "__main__":
    try:
        remaining = calculate_remaining_notcoin_distribution(1000.0, 5000.0)
        print(f"Remaining Notcoin distribution: {remaining:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
