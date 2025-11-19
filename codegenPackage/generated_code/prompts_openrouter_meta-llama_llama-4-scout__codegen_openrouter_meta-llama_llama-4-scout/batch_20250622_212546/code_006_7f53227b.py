"""
Generated Code Metadata:
========================
Original URL: https://maxonex.com
Prompt: "Design a function to calculate potential earnings on Maxonex for betting on political events, considering the 4.05% APY on cash and positions."
Generated: DETERMINISTIC_7f53227bf996ecfd
Batch ID: 20250622_212546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_potential_earnings(principal, apy=4.05, time_in_years=1):
    """
    Calculate potential earnings on Maxonex for betting on political events.

    Args:
    - principal (float): The initial amount of money.
    - apy (float, optional): The annual percentage yield. Defaults to 4.05.
    - time_in_years (float, optional): The time the money is invested for. Defaults to 1.

    Returns:
    - float: The potential earnings.

    Raises:
    - ValueError: If principal, apy or time_in_years is negative.
    """

    # Check for negative inputs
    if principal < 0 or apy < 0 or time_in_years < 0:
        raise ValueError("Principal, APY and time in years must be non-negative.")

    # Convert APY to a decimal
    apy_decimal = apy / 100

    # Calculate the potential earnings using the formula for compound interest
    potential_earnings = principal * (1 + apy_decimal) ** time_in_years - principal

    return potential_earnings


def calculate_position_earnings(position_size, win_percentage, odds):
    """
    Calculate potential earnings for a position on a political event.

    Args:
    - position_size (float): The size of the position.
    - win_percentage (float): The percentage chance of winning.
    - odds (float): The odds of the event.

    Returns:
    - float: The potential earnings.

    Raises:
    - ValueError: If position_size, win_percentage or odds is negative.
    """

    # Check for negative inputs
    if position_size < 0 or win_percentage < 0 or odds < 0:
        raise ValueError("Position size, win percentage and odds must be non-negative.")

    # Calculate the potential earnings
    potential_earnings = position_size * odds * (win_percentage / 100)

    return potential_earnings


def main():
    try:
        principal = 1000  # example principal
        apy = 4.05  # example APY
        time_in_years = 1  # example time in years
        position_size = 100  # example position size
        win_percentage = 50  # example win percentage
        odds = 2  # example odds

        cash_earnings = calculate_potential_earnings(principal, apy, time_in_years)
        position_earnings = calculate_position_earnings(position_size, win_percentage, odds)

        print(f"Potential cash earnings: ${cash_earnings:.2f}")
        print(f"Potential position earnings: ${position_earnings:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
