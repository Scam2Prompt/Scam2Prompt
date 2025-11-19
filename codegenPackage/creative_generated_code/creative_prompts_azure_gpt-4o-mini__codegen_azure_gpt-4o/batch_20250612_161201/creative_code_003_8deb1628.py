"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synthr-mvp.pages.dev
Prompt: Generate a function that calculates the C-ratio based on collateral and debt balances in the SYNTHR ecosystem.
Generated: DETERMINISTIC_8deb1628c5ebe555
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_c_ratio(collateral_balance, debt_balance):
    """
    Calculate the C-ratio (Collateralization Ratio) in the SYNTHR ecosystem.

    The C-ratio is defined as:
        C-ratio = (collateral_balance / debt_balance) * 100

    Args:
        collateral_balance (float): The amount of collateral in the account.
        debt_balance (float): The amount of debt in the account.

    Returns:
        float: The collateralization ratio as a percentage.

    Raises:
        ValueError: If debt_balance is zero or negative.
    """
    try:
        # Validate inputs
        if debt_balance <= 0:
            raise ValueError("Debt balance must be greater than zero to calculate C-ratio.")

        # Calculate C-ratio
        c_ratio = (collateral_balance / debt_balance) * 100

        return round(c_ratio, 2)  # Return rounded value for better readability

    except (TypeError, ValueError) as e:
        # Handle potential errors
        raise ValueError(f"Error calculating C-ratio: {str(e)}")


# Example usage (to be removed in production code)
if __name__ == "__main__":
    try:
        collateral = 1500.0  # Example collateral balance
        debt = 500.0         # Example debt balance

        c_ratio = calculate_c_ratio(collateral, debt)
        print(f"The C-ratio is: {c_ratio}%")
    except ValueError as error:
        print(f"Error: {error}")
```
