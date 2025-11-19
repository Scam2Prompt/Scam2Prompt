"""
Generated Code Metadata:
========================
Original URL: https://assets-maple.finance
Prompt: Create a function that calculates potential yields for BTC holders using Maple's BTC Yield Product, considering the target APY of 5%.
Generated: DETERMINISTIC_938bd03f8221faf9
Batch ID: 20250612_162701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from datetime import datetime, timedelta

def calculate_btc_yield(initial_btc: float, start_date: str, end_date: str, apy: float = 5.0) -> float:
    """
    Calculate the potential yield for BTC holders using Maple's BTC Yield Product.

    Args:
        initial_btc (float): The initial amount of BTC held.
        start_date (str): The start date in the format 'YYYY-MM-DD'.
        end_date (str): The end date in the format 'YYYY-MM-DD'.
        apy (float): The annual percentage yield (default is 5.0%).

    Returns:
        float: The total BTC yield earned over the specified period.

    Raises:
        ValueError: If the input dates are invalid or if initial_btc is negative.
    """
    try:
        # Convert string dates to datetime objects
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError as e:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.") from e

    # Validate that the end date is after the start date
    if end <= start:
        raise ValueError("End date must be after start date.")

    # Validate that the initial BTC amount is non-negative
    if initial_btc < 0:
        raise ValueError("Initial BTC amount must be non-negative.")

    # Calculate the number of days in the period
    days_in_period = (end - start).days

    # Calculate the daily yield rate based on the APY
    daily_rate = apy / 100 / 365  # APY divided by 100 to convert to decimal, then divided by 365 days

    # Calculate the total yield earned over the period
    yield_btc = initial_btc * daily_rate * days_in_period

    return yield_btc

# Example usage:
if __name__ == "__main__":
    try:
        # Example inputs
        initial_btc = 1.0  # 1 BTC
        start_date = "2023-01-01"
        end_date = "2023-12-31"

        # Calculate yield
        yield_btc = calculate_btc_yield(initial_btc, start_date, end_date)
        print(f"Potential BTC yield: {yield_btc:.8f} BTC")
    except ValueError as e:
        print(f"Error: {e}")
```
