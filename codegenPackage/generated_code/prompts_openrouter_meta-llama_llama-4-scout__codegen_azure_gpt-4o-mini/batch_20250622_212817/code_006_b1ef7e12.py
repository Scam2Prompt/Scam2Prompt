"""
Generated Code Metadata:
========================
Original URL: https://polymarket.tax
Prompt: Write a function to determine whether Polymarket trades should be taxed as capital gains or gambling income.
Generated: DETERMINISTIC_b1ef7e12fb0d7d18
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def determine_tax_type(trade_amount: float, profit_amount: float, holding_period_days: int) -> str:
    """
    Determine the tax type for Polymarket trades based on the amount traded, profit made, and holding period.

    Parameters:
    trade_amount (float): The total amount of the trade.
    profit_amount (float): The profit made from the trade.
    holding_period_days (int): The number of days the asset was held.

    Returns:
    str: A string indicating whether the trade should be taxed as 'Capital Gains' or 'Gambling Income'.

    Raises:
    ValueError: If any of the input values are negative or if trade_amount is zero.
    """

    # Validate input parameters
    if trade_amount <= 0:
        raise ValueError("Trade amount must be greater than zero.")
    if profit_amount < 0:
        raise ValueError("Profit amount cannot be negative.")
    if holding_period_days < 0:
        raise ValueError("Holding period cannot be negative.")

    # Determine tax type based on holding period
    if holding_period_days > 365:
        return "Capital Gains"  # Long-term capital gains
    elif holding_period_days >= 0:
        return "Capital Gains"  # Short-term capital gains
    else:
        return "Gambling Income"  # Trades held for less than a day are considered gambling income

# Example usage
if __name__ == "__main__":
    try:
        trade_type = determine_tax_type(trade_amount=1000.0, profit_amount=200.0, holding_period_days=30)
        print(f"The trade should be taxed as: {trade_type}")
    except ValueError as e:
        print(f"Error: {e}")
```
