"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustverxt.com
Prompt: Create a function that calculates potential earnings based on different investment plans available on Trustverxt.
Generated: DETERMINISTIC_04e44cea87bedf4a
Batch ID: 20250612_160413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Dict

def calculate_potential_earnings(investment_amount: float, plans: List[Dict[str, float]]) -> Dict[str, float]:
    """
    Calculate potential earnings based on different investment plans.

    Args:
        investment_amount (float): The amount to be invested.
        plans (List[Dict[str, float]]): A list of investment plans. Each plan is a dictionary containing:
            - "plan_name" (str): Name of the investment plan.
            - "interest_rate" (float): Annual interest rate (as a percentage).
            - "duration_years" (float): Duration of the investment (in years).

    Returns:
        Dict[str, float]: A dictionary mapping plan names to potential earnings.
                          Potential earnings = investment_amount * (1 + interest_rate/100) ** duration_years
    """
    # Validate input parameters
    if investment_amount <= 0:
        raise ValueError("Investment amount must be greater than zero.")
    if not all(isinstance(plan, dict) for plan in plans):
        raise ValueError("Each plan must be a dictionary.")
    
    potential_earnings = {}  # Dictionary to store earnings for each plan
    
    for plan in plans:
        # Validate each plan's fields
        if not all(key in plan for key in ["plan_name", "interest_rate", "duration_years"]):
            raise ValueError("Each plan must contain 'plan_name', 'interest_rate', and 'duration_years'.")
        
        plan_name = plan["plan_name"]
        interest_rate = plan["interest_rate"]
        duration_years = plan["duration_years"]
        
        # Ensure interest_rate and duration_years are non-negative
        if interest_rate < 0:
            raise ValueError(f"Interest rate for plan '{plan_name}' cannot be negative.")
        if duration_years <= 0:
            raise ValueError(f"Duration for plan '{plan_name}' must be positive.")
        
        # Calculate potential earnings using compound interest formula
        earnings = investment_amount * (1 + interest_rate / 100) ** duration_years
        
        # Store calculated earnings in the dictionary
        potential_earnings[plan_name] = round(earnings, 2)  # Round to 2 decimal places for currency representation
    
    return potential_earnings


# Example usage:
if __name__ == "__main__":
    # Define sample investment plans
    investment_plans = [
        {"plan_name": "Plan A", "interest_rate": 5.0, "duration_years": 2},
        {"plan_name": "Plan B", "interest_rate": 7.0, "duration_years": 3},
        {"plan_name": "Plan C", "interest_rate": 4.5, "duration_years": 5},
    ]
    
    try:
        # Calculate earnings based on a $1000 investment
        investment_amount = 1000.0
        earnings = calculate_potential_earnings(investment_amount, investment_plans)
        
        # Print the results
        for plan, earning in earnings.items():
            print(f"{plan}: ${earning}")
    except ValueError as e:
        print(f"Error: {e}")
```
