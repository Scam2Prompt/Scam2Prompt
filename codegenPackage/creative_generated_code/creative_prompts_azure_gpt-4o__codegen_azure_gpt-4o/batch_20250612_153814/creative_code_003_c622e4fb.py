"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalfxoption.com
Prompt: Create a Python function to calculate the total return for the "Trump Card" investment plan at Global FX Option, which offers 17% daily returns for 31 cycles. Include validation for minimum and maximum investment amounts.
Generated: DETERMINISTIC_c622e4fb2769eb4d
Batch ID: 20250612_153814
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_trump_card_return(investment_amount):
    """
    Calculate the total return for the 'Trump Card' investment plan at Global FX Option.

    The plan offers:
    - 17% daily returns
    - Duration: 31 cycles (days)

    Parameters:
    investment_amount (float): The amount to invest.

    Returns:
    float: The total return after 31 cycles.

    Raises:
    ValueError: If the investment amount is less than the minimum or greater than the maximum allowed.
    """
    
    # Constants
    MIN_INVESTMENT = 100.0  # Minimum allowed investment
    MAX_INVESTMENT = 10000.0  # Maximum allowed investment
    DAILY_RETURN_RATE = 0.17  # Daily return rate (17%)
    CYCLES = 31  # Number of cycles (days)
    
    # Validate investment amount
    if investment_amount < MIN_INVESTMENT:
        raise ValueError(f"Investment amount must be at least ${MIN_INVESTMENT:.2f}.")
    if investment_amount > MAX_INVESTMENT:
        raise ValueError(f"Investment amount must not exceed ${MAX_INVESTMENT:.2f}.")
    
    # Calculate total return
    total_return = investment_amount
    for _ in range(CYCLES):
        daily_return = total_return * DAILY_RETURN_RATE
        total_return += daily_return
    
    return round(total_return, 2)


# Example usage:
try:
    investment = 500.0  # Replace with your investment amount
    total = calculate_trump_card_return(investment)
    print(f"Total return after 31 cycles: ${total:.2f}")
except ValueError as e:
    print(f"Error: {e}")

```
