"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acextradex.ltd
Prompt: Write a Python function that calculates the potential earnings based on the investment plans offered by Acex Tradex, specifically for the Supersonic and Turbocharged plans.
Generated: DETERMINISTIC_57324218bcbd3fc5
Batch ID: 20250612_164236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_earnings(plan_name: str, initial_investment: float, duration_months: int) -> float:
    """
    Calculate the potential earnings based on Acex Tradex investment plans.

    Parameters:
    - plan_name (str): Name of the investment plan ("Supersonic" or "Turbocharged").
    - initial_investment (float): The amount invested in USD.
    - duration_months (int): Duration of the investment in months.

    Returns:
    - float: Total earnings (including initial investment) in USD.

    Raises:
    - ValueError: If the plan_name is invalid or if the initial_investment or 
                duration_months are non-positive values.
    """
    
    # Validate input parameters
    if initial_investment <= 0 or duration_months <= 0:
        raise ValueError("Initial investment and duration must both be positive values.")
    
    if plan_name not in ["Supersonic", "Turbocharged"]:
        raise ValueError("Invalid plan name. Available plans are 'Supersonic' and 'Turbocharged'.")
    
    # Define interest rates for each plan
    interest_rates = {
        "Supersonic": 0.05,  # 5% monthly growth
        "Turbocharged": 0.07  # 7% monthly growth
    }
    
    # Retrieve the appropriate interest rate
    monthly_interest_rate = interest_rates[plan_name]
    
    # Calculate total earnings using compound interest
    try:
        total_earnings = initial_investment * ((1 + monthly_interest_rate) ** duration_months)
    except OverflowError:
        raise OverflowError("Calculation resulted in excessively large earnings. Check inputs.")
    
    return round(total_earnings, 2)


# Example Usage:
if __name__ == "__main__":
    try:
        plan = "Supersonic"
        investment = 1000.0
        months = 12
        earnings = calculate_earnings(plan, investment, months)
        print(f"Total earnings for the {plan} plan: ${earnings}")
    except Exception as e:
        print(f"Error: {e}")
```
