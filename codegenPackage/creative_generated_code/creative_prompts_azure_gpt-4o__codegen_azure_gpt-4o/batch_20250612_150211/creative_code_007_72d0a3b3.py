"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://goldenfundinvestment.com
Prompt: Generate a script to automate the calculation of daily returns for multiple investment plans, including minimum and maximum deposit limits, as described on goldenfundinvestment.com.
Generated: DETERMINISTIC_72d0a3b33b9e26af
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

# Constants for investment plan limits (you can adjust these values as per the plans on goldenfundinvestment.com)
INVESTMENT_PLANS = {
    "Plan A": {"min_deposit": 100, "max_deposit": 1000, "daily_return_rate": 0.01},  # 1% daily return
    "Plan B": {"min_deposit": 1001, "max_deposit": 5000, "daily_return_rate": 0.015}, # 1.5% daily return
    "Plan C": {"min_deposit": 5001, "max_deposit": 10000, "daily_return_rate": 0.02}, # 2% daily return
}

# Function to validate deposit against plan limits
def validate_deposit(plan_name, deposit):
    plan = INVESTMENT_PLANS.get(plan_name)
    if not plan:
        raise ValueError(f"Invalid plan name: {plan_name}")
    if deposit < plan["min_deposit"] or deposit > plan["max_deposit"]:
        raise ValueError(
            f"Deposit amount ${deposit} is out of range for {plan_name} "
            f"(Min: ${plan['min_deposit']}, Max: ${plan['max_deposit']})"
        )

# Function to calculate daily return based on plan and deposit
def calculate_daily_return(plan_name, deposit):
    validate_deposit(plan_name, deposit)
    plan = INVESTMENT_PLANS[plan_name]
    return deposit * plan["daily_return_rate"]

# Main function for processing multiple investments
def process_investments(investment_data):
    """
    Processes a list of investments and calculates daily returns for each.
    
    Args:
        investment_data (list): List of dictionaries containing investment details.
                                Each dictionary should have keys: 'plan_name' and 'deposit'.
    
    Returns:
        pd.DataFrame: A DataFrame with investment details and calculated daily returns.
    """
    results = []

    for investment in investment_data:
        try:
            plan_name = investment["plan_name"]
            deposit = investment["deposit"]
            daily_return = calculate_daily_return(plan_name, deposit)
            results.append({
                "Plan Name": plan_name,
                "Deposit": deposit,
                "Daily Return": round(daily_return, 2),
            })
        except ValueError as e:
            # Log error and append to results with error message
            results.append({
                "Plan Name": investment.get("plan_name", "Unknown"),
                "Deposit": investment.get("deposit", "Unknown"),
                "Error": str(e),
            })

    # Create a DataFrame for better display and analysis
    return pd.DataFrame(results)

# Example usage
if __name__ == "__main__":
    # Define sample investment data
    investments = [
        {"plan_name": "Plan A", "deposit": 500},
        {"plan_name": "Plan B", "deposit": 1500},
        {"plan_name": "Plan C", "deposit": 8000},
        {"plan_name": "Plan A", "deposit": 1200},  # Invalid deposit (out of range)
        {"plan_name": "Plan D", "deposit": 3000},  # Invalid plan name
    ]

    # Process investments and display results
    results_df = process_investments(investments)
    print(results_df)
```
