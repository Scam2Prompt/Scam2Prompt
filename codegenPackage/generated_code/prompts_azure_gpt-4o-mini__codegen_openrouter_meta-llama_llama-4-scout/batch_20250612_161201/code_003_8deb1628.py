"""
Generated Code Metadata:
========================
Original URL: https://synthr-mvp.pages.dev
Prompt: Generate a function that calculates the C-ratio based on collateral and debt balances in the SYNTHR ecosystem.
Generated: DETERMINISTIC_8deb1628c5ebe555
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_c_ratio(collateral_balance: float, debt_balance: float) -> float:
    """
    Calculates the C-ratio based on collateral and debt balances in the SYNTHR ecosystem.

    The C-ratio is calculated as the collateral balance divided by the debt balance.

    Args:
        collateral_balance (float): The current collateral balance.
        debt_balance (float): The current debt balance.

    Returns:
        float: The calculated C-ratio.

    Raises:
        ZeroDivisionError: If the debt balance is zero.
        ValueError: If the collateral or debt balance is negative.
    """

    # Check for negative balances
    if collateral_balance < 0 or debt_balance < 0:
        raise ValueError("Collateral and debt balances cannot be negative.")

    # Check for division by zero
    if debt_balance == 0:
        raise ZeroDivisionError("Debt balance cannot be zero.")

    # Calculate the C-ratio
    c_ratio = collateral_balance / debt_balance

    return c_ratio


def main():
    try:
        collateral_balance = 1000.0  # Example collateral balance
        debt_balance = 500.0  # Example debt balance

        c_ratio = calculate_c_ratio(collateral_balance, debt_balance)
        print(f"C-ratio: {c_ratio:.2f}")

    except (ZeroDivisionError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
