"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://premiertradeoptions.com
Prompt: Generate code to calculate ROI percentages for different investment plans (Starter, Silver, Gold, Platinum) based on the details provided by Premier Trade Options.
Generated: DETERMINISTIC_9e2e86b7b9e144f8
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to calculate ROI percentages for different investment plans offered by Premier Trade Options.
Plans: Starter, Silver, Gold, Platinum.
"""

# Define a function to calculate ROI
def calculate_roi(investment_plan, principal_amount, annual_rate, time_in_years):
    """
    Calculates the ROI (Return on Investment) percentage for a given plan.

    Args:
        investment_plan (str): Name of the investment plan (Starter, Silver, Gold, Platinum).
        principal_amount (float): The amount of money invested.
        annual_rate (float): Annual interest rate (in percentage) for the plan.
        time_in_years (int): Investment duration in years.

    Returns:
        float: ROI percentage.

    Raises:
        ValueError: If the investment plan is invalid or input values are negative.
    """
    # Validate inputs
    if principal_amount < 0 or annual_rate < 0 or time_in_years < 0:
        raise ValueError("Principal amount, annual rate, and time in years must be non-negative.")
    if investment_plan not in ["Starter", "Silver", "Gold", "Platinum"]:
        raise ValueError("Invalid investment plan. Choose from: Starter, Silver, Gold, Platinum.")
    
    # Calculate total return based on simple interest formula
    total_return = principal_amount * (annual_rate / 100) * time_in_years
    
    # Calculate ROI percentage
    roi_percentage = (total_return / principal_amount) * 100
    return roi_percentage

# Define a dictionary of investment plans and their annual rates
investment_plans = {
    "Starter": 5.0,   # 5% annual rate
    "Silver": 7.5,    # 7.5% annual rate
    "Gold": 10.0,     # 10% annual rate
    "Platinum": 12.5  # 12.5% annual rate
}

# Example usage
if __name__ == "__main__":
    try:
        # Example input data
        principal = 10000  # Principal amount in dollars
        duration = 3       # Time in years
        
        # Calculate ROI for each plan
        for plan, rate in investment_plans.items():
            roi = calculate_roi(plan, principal, rate, duration)
            print(f"Plan: {plan}, ROI Percentage: {roi:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
