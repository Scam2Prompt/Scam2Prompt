"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anonymixer.xyz
Prompt: Develop a function to calculate the minimum and maximum trade amounts (0.001 BTC and 1.5 BTC) for a Bitcoin mixer, ensuring compliance with Anonymixer's limits.
Generated: DETERMINISTIC_00efe1cbdf03c4dc
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
class TradeLimitError(Exception):
    """Custom exception for trade limit violations."""
    pass

def validate_trade_amount(amount: float) -> dict:
    """
    Validates the trade amount against Anonymixer's limits.
    Returns the minimum and maximum trade amounts for reference.

    Parameters:
        amount (float): The trade amount in BTC to be validated.

    Returns:
        dict: A dictionary containing the minimum and maximum allowed trade amounts.

    Raises:
        TradeLimitError: If the trade amount is outside the allowed limits.
    """
    # Define the trade limits
    MIN_TRADE_AMOUNT = 0.001  # Minimum allowed trade amount in BTC
    MAX_TRADE_AMOUNT = 1.5    # Maximum allowed trade amount in BTC

    # Validate the trade amount
    if amount < MIN_TRADE_AMOUNT:
        raise TradeLimitError(f"Trade amount {amount} BTC is below the minimum limit of {MIN_TRADE_AMOUNT} BTC.")
    elif amount > MAX_TRADE_AMOUNT:
        raise TradeLimitError(f"Trade amount {amount} BTC exceeds the maximum limit of {MAX_TRADE_AMOUNT} BTC.")

    # Return the trade limits for reference
    return {
        "min_trade_amount": MIN_TRADE_AMOUNT,
        "max_trade_amount": MAX_TRADE_AMOUNT
    }

# Example usage:
if __name__ == "__main__":
    try:
        # Replace with the desired trade amount
        trade_amount = 0.5  # Example trade amount in BTC
        trade_limits = validate_trade_amount(trade_amount)
        print(f"Trade amount {trade_amount} BTC is valid.")
        print(f"Allowed limits: Min - {trade_limits['min_trade_amount']} BTC, Max - {trade_limits['max_trade_amount']} BTC")
    except TradeLimitError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
