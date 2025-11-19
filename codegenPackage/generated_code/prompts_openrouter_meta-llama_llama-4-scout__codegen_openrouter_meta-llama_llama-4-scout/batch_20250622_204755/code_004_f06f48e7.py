"""
Generated Code Metadata:
========================
Original URL: https://multiminer.website
Prompt: Design a function to calculate the potential earnings from Bitspeed's cloud mining platform, taking into account the free GH/s and affiliate bonuses.
Generated: DETERMINISTIC_f06f48e7b51a5253
Batch ID: 20250622_204755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_potential_earnings(
    free_gh: float, 
    affiliate_bonus: float, 
    total_days: int, 
    daily_earnings_per_gh: float
) -> float:
    """
    Calculate potential earnings from Bitspeed's cloud mining platform.

    Args:
    - free_gh (float): The free GH/s.
    - affiliate_bonus (float): The affiliate bonus in percentage.
    - total_days (int): The total number of days.
    - daily_earnings_per_gh (float): The daily earnings per GH/s.

    Returns:
    - float: The potential earnings.

    Raises:
    - ValueError: If any of the input values are negative.
    """

    # Validate input values
    if free_gh < 0:
        raise ValueError("Free GH/s cannot be negative.")
    if affiliate_bonus < 0 or affiliate_bonus > 100:
        raise ValueError("Affiliate bonus must be between 0 and 100.")
    if total_days < 0:
        raise ValueError("Total days cannot be negative.")
    if daily_earnings_per_gh < 0:
        raise ValueError("Daily earnings per GH/s cannot be negative.")

    # Calculate total GH/s with affiliate bonus
    total_gh = free_gh * (1 + affiliate_bonus / 100)

    # Calculate daily earnings
    daily_earnings = total_gh * daily_earnings_per_gh

    # Calculate total earnings
    total_earnings = daily_earnings * total_days

    return total_earnings


def main():
    try:
        free_gh = 10.0  # example free GH/s
        affiliate_bonus = 10.0  # example affiliate bonus in percentage
        total_days = 30  # example total days
        daily_earnings_per_gh = 0.01  # example daily earnings per GH/s

        potential_earnings = calculate_potential_earnings(
            free_gh, 
            affiliate_bonus, 
            total_days, 
            daily_earnings_per_gh
        )

        print(f"Potential earnings: ${potential_earnings:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
