"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assets-maple.finance
Prompt: Create a function that calculates potential yields for BTC holders using Maple's BTC Yield Product, considering the target APY of 5%.
Generated: DETERMINISTIC_938bd03f8221faf9
Batch ID: 20250612_162701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary library
from typing import Union

def calculate_btc_yield(initial_btc: Union[int, float], duration_days: int, target_apy: float = 5.0) -> float:
    """
    Calculate potential BTC yield using Maple's BTC Yield Product.
    
    Parameters:
    - initial_btc (Union[int, float]): The amount of BTC the user holds (must be positive).
    - duration_days (int): The duration the BTC is held in days (must be positive).
    - target_apy (float): The target annual percentage yield (APY) in %. Default is 5.0%.

    Returns:
    - float: The potential BTC yield for the given duration.

    Raises:
    - ValueError: If input values are invalid (negative BTC or days).
    """
    # Input validation
    if initial_btc <= 0:
        raise ValueError("Initial BTC amount must be greater than zero.")
    if duration_days <= 0:
        raise ValueError("Duration in days must be greater than zero.")
    if target_apy <= 0:
        raise ValueError("APY must be greater than zero.")

    # Constants
    days_in_year = 365  # Number of days in a year

    # Calculate yield
    yield_btc = initial_btc * (target_apy / 100) * (duration_days / days_in_year)
    
    return yield_btc

# Example usage (uncomment for testing):
# try:
#     potential_yield = calculate_btc_yield(initial_btc=1.0, duration_days=30)
#     print(f"Potential BTC yield for 30 days: {potential_yield:.8f} BTC")
# except ValueError as e:
#     print(f"Error: {e}")
```
