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
def calculate_total_return(investment_amount):
    """
    Calculate the total return for the "Trump Card" investment plan.
    
    The plan offers a daily return of 17% for 31 cycles.
    
    Parameters:
    investment_amount (float): The initial amount to invest.
    
    Returns:
    float: The total return after 31 cycles.
    
    Raises:
    ValueError: If the investment amount is less than 100 or greater than 10000.
    """
    
    # Define constants
    DAILY_RETURN_RATE = 0.17  # 17% daily return
    CYCLES = 31                # Number of cycles

    # Validate investment amount
    if investment_amount < 100:
        raise ValueError("Investment amount must be at least $100.")
    elif investment_amount > 10000:
        raise ValueError("Investment amount must not exceed $10,000.")
    
    # Calculate total return after 31 cycles
    total_return = investment_amount * ((1 + DAILY_RETURN_RATE) ** CYCLES)
    
    return total_return

# Example usage
if __name__ == "__main__":
    try:
        # Set initial investment
        investment = 1000  # Example investment amount
        total = calculate_total_return(investment)
        print(f"Total return after 31 cycles: ${total:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
