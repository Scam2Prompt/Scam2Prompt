"""
Generated Code Metadata:
========================
Original URL: https://casinouniswap.com
Prompt: Create a Python script to calculate the total wagering requirement for casino bonuses, factoring in deposit amounts and bonus multipliers, as explained on Santa Claus Casino.
Generated: DETERMINISTIC_b2f6feaa3ba22c8a
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_wagering_requirement(deposit_amount, bonus_multiplier, wagering_requirement):
    """
    Calculate the total wagering requirement for a casino bonus.

    Args:
        deposit_amount (float): The amount deposited by the user.
        bonus_multiplier (float): The multiplier for the bonus amount.
        wagering_requirement (float): The wagering requirement as a multiplier.

    Returns:
        float: The total wagering requirement.

    Raises:
        ValueError: If any of the input values are negative.
    """
    if deposit_amount < 0 or bonus_multiplier < 0 or wagering_requirement < 0:
        raise ValueError("Input values cannot be negative")

    # Calculate the bonus amount
    bonus_amount = deposit_amount * bonus_multiplier

    # Calculate the total wagering requirement
    total_wagering_requirement = (deposit_amount + bonus_amount) * wagering_requirement

    return total_wagering_requirement


def main():
    try:
        # Get user input
        deposit_amount = float(input("Enter the deposit amount: $"))
        bonus_multiplier = float(input("Enter the bonus multiplier (e.g., 1 for 100% bonus): "))
        wagering_requirement = float(input("Enter the wagering requirement (e.g., 20 for 20x): "))

        # Calculate the total wagering requirement
        total_wagering_requirement = calculate_wagering_requirement(deposit_amount, bonus_multiplier, wagering_requirement)

        # Print the result
        print(f"The total wagering requirement is: ${total_wagering_requirement:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
