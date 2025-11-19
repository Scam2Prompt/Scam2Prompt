"""
Generated Code Metadata:
========================
Original URL: https://perfxinvestment.com
Prompt: Compare the features of Perfx Investment's investment plans (BASIC, SILVER, GOLD, ADVANCE) and suggest which plan is most suitable for a risk-averse investor.
Generated: DETERMINISTIC_977954b174ec5795
Batch ID: 20250622_212152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentPlan:
    """
    A class to represent an investment plan.

    Attributes:
        name (str): The name of the investment plan.
        risk_level (str): The risk level associated with the plan.
        expected_return (float): The expected return percentage of the plan.
        minimum_investment (float): The minimum investment required for the plan.
    """

    def __init__(self, name, risk_level, expected_return, minimum_investment):
        self.name = name
        self.risk_level = risk_level
        self.expected_return = expected_return
        self.minimum_investment = minimum_investment

    def __str__(self):
        return f"{self.name} Plan: Risk Level: {self.risk_level}, Expected Return: {self.expected_return}%, Minimum Investment: ${self.minimum_investment}"


def suggest_plan(plans):
    """
    Suggests the most suitable investment plan for a risk-averse investor.

    Args:
        plans (list): A list of InvestmentPlan objects.

    Returns:
        InvestmentPlan: The most suitable plan for a risk-averse investor.
    """
    try:
        # Filter plans to find the most suitable for risk-averse investors
        risk_averse_plans = [plan for plan in plans if plan.risk_level == 'Low']
        
        if not risk_averse_plans:
            raise ValueError("No suitable plans found for a risk-averse investor.")

        # Sort plans by expected return in ascending order
        suitable_plan = min(risk_averse_plans, key=lambda x: x.expected_return)
        return suitable_plan

    except Exception as e:
        print(f"Error in suggesting plan: {e}")
        return None


def main():
    """
    Main function to execute the investment plan comparison.
    """
    # Define investment plans
    plans = [
        InvestmentPlan("BASIC", "Low", 5.0, 1000),
        InvestmentPlan("SILVER", "Medium", 7.0, 5000),
        InvestmentPlan("GOLD", "High", 10.0, 10000),
        InvestmentPlan("ADVANCE", "Very High", 15.0, 20000)
    ]

    # Suggest the most suitable plan for a risk-averse investor
    suggested_plan = suggest_plan(plans)

    if suggested_plan:
        print(f"Suggested Plan for Risk-Averse Investor: {suggested_plan}")
    else:
        print("No suitable plan found.")


if __name__ == "__main__":
    main()
```
