"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aphatradespro.com
Prompt: Create a function that calculates potential ROI for the various investment plans offered by Aphatradespro, such as Spot Futures and Infinity Grid Bot.
Generated: DETERMINISTIC_0111d3bb7a5e14a8
Batch ID: 20250612_160446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python Code to Calculate Potential ROI for Investment Plans

def calculate_roi(investment_plan, initial_investment, duration_months, monthly_rate_of_return):
    """
    Calculate the potential ROI for various investment plans.

    Parameters:
        investment_plan (str): The name of the investment plan (e.g., "Spot Futures", "Infinity Grid Bot").
        initial_investment (float): The initial amount invested.
        duration_months (int): The investment duration in months.
        monthly_rate_of_return (float): The expected monthly rate of return as a percentage (e.g., 5 for 5%).

    Returns:
        dict: A dictionary containing the investment plan name and the potential ROI.
    """
    try:
        # Input validation
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than 0.")
        if duration_months <= 0:
            raise ValueError("Duration must be greater than 0 months.")
        if monthly_rate_of_return < 0:
            raise ValueError("Rate of return must be a non-negative value.")

        # Calculate ROI using compound interest formula
        total_value = initial_investment * ((1 + monthly_rate_of_return / 100) ** duration_months)
        roi = total_value - initial_investment

        # Return results in a structured format
        return {
            "Investment Plan": investment_plan,
            "Initial Investment": initial_investment,
            "Duration (Months)": duration_months,
            "Monthly Rate of Return (%)": monthly_rate_of_return,
            "Potential ROI": round(roi, 2),
            "Total Value": round(total_value, 2)
        }
    except ValueError as e:
        return {"Error": str(e)}
    except Exception as e:
        return {"Error": f"An unexpected error occurred: {str(e)}"}

# Example Usage
if __name__ == "__main__":
    # Example investment plans
    investment_plans = [
        {"plan_name": "Spot Futures", "initial_investment": 1000, "duration_months": 12, "monthly_rate_of_return": 5},
        {"plan_name": "Infinity Grid Bot", "initial_investment": 500, "duration_months": 6, "monthly_rate_of_return": 3}
    ]

    # Calculate ROI for each plan
    for plan in investment_plans:
        result = calculate_roi(
            investment_plan=plan["plan_name"],
            initial_investment=plan["initial_investment"],
            duration_months=plan["duration_months"],
            monthly_rate_of_return=plan["monthly_rate_of_return"]
        )
        print(result)
```
