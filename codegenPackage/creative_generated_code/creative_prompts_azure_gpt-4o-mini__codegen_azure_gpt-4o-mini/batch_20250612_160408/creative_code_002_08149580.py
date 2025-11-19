"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ctradeinvestments.com
Prompt: Create a function that calculates potential earnings based on the investment plans provided by Crypto Trade Investments, including the hourly profit rates for different plans.
Generated: DETERMINISTIC_08149580dfad2c8f
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_potential_earnings(investment_amount, plan_type, hours=24):
    """
    Calculate potential earnings based on the investment plan type and amount.
    
    Parameters:
        investment_amount (float): The amount of money invested.
        plan_type (str): The type of investment plan ('basic', 'standard', 'premium').
        hours (int, optional): The number of hours the investment is held. Defaults to 24 hours.
        
    Returns:
        float: The potential earnings after the specified hours.
        
    Raises:
        ValueError: If the investment amount is negative or if the plan type is invalid.
    """
    
    # Define profit rates for each investment plan (hourly)
    PLAN_RATES = {
        'basic': 0.01,    # 1% hourly
        'standard': 0.02,  # 2% hourly
        'premium': 0.05    # 5% hourly
    }
    
    # Validate investment amount
    if investment_amount < 0:
        raise ValueError("Investment amount must be a non-negative value.")
    
    # Validate plan type
    if plan_type not in PLAN_RATES:
        raise ValueError("Invalid plan type. Choose from 'basic', 'standard', or 'premium'.")
    
    # Calculate potential earnings
    hourly_rate = PLAN_RATES[plan_type]
    potential_earnings = investment_amount * (1 + hourly_rate) ** hours - investment_amount
    
    return potential_earnings

# Example usage
if __name__ == "__main__":
    try:
        investment = 1000  # Example investment amount
        plan = 'premium'    # Example plan type
        hours = 48          # Example duration
        
        earnings = calculate_potential_earnings(investment, plan, hours)
        print(f"Potential earnings from the {plan} plan after {hours} hours: ${earnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
