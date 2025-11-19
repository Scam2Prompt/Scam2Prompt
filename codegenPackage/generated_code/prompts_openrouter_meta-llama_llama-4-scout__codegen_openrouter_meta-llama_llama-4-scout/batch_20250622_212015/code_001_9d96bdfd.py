"""
Generated Code Metadata:
========================
Original URL: https://landing-jackpotcow.pages.dev
Prompt: Write a Python code snippet to calculate the maximum bonus a player can receive from the 100% up to €500 first deposit bonus at Jackpot Cow Casino.
Generated: DETERMINISTIC_9d96bdfd0d255947
Batch ID: 20250622_212015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_max_bonus(deposit_amount: float) -> float:
    """
    Calculate the maximum bonus a player can receive from the 100% up to €500 first deposit bonus.

    Args:
        deposit_amount (float): The player's first deposit amount.

    Returns:
        float: The maximum bonus the player can receive.

    Raises:
        ValueError: If the deposit amount is negative.
    """

    # Check if deposit amount is negative
    if deposit_amount < 0:
        raise ValueError("Deposit amount cannot be negative.")

    # Define the maximum bonus cap
    max_bonus_cap = 500.0

    # Calculate the bonus as 100% of the deposit amount
    bonus = deposit_amount

    # Apply the maximum bonus cap
    bonus = min(bonus, max_bonus_cap)

    return bonus


def main():
    try:
        # Example usage
        deposit_amounts = [100.0, 500.0, 1000.0]

        for deposit_amount in deposit_amounts:
            max_bonus = calculate_max_bonus(deposit_amount)
            print(f"Deposit Amount: €{deposit_amount:.2f}, Maximum Bonus: €{max_bonus:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
