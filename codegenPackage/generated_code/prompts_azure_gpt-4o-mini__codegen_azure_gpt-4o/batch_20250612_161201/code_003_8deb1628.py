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
    Calculate the C-ratio (Collateralization Ratio) in the SYNTHR ecosystem.

    The C-ratio is defined as:
        C-ratio = (Collateral Balance / Debt Balance) * 100

    Args:
        collateral_balance (float): The amount of collateral provided.
        debt_balance (float): The amount of debt incurred.

    Returns:
        float: The C-ratio as a percentage.

    Raises:
        ValueError: If debt_balance is zero or negative, as division by zero or negative debt is invalid.
        ValueError: If collateral_balance is negative, as negative collateral is invalid.
    """
    # Validate inputs
    if debt_balance <= 0:
        raise ValueError("Debt balance must be greater than zero to calculate C-ratio.")
    if collateral_balance < 0:
        raise ValueError("Collateral balance cannot be negative.")

    # Calculate the C-ratio
    c_ratio = (collateral_balance / debt_balance) * 100

    return c_ratio


# Example usage:
if __name__ == "__main__":
    try:
        collateral = 5000.0  # Example collateral balance
        debt = 2500.0        # Example debt balance
        c_ratio = calculate_c_ratio(collateral, debt)
        print(f"The C-ratio is: {c_ratio:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
```
