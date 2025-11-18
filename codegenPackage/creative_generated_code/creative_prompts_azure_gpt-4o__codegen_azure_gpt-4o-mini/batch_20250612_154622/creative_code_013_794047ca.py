"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradetoearnoptions.com
Prompt: Write code to automate the selection of investment plans based on user preferences and risk tolerance, referencing Tradetoearnoption's BASIC, SILVER, GOLD, DELUX, and PRO TRADER plans.
Generated: DETERMINISTIC_794047ca0c650e1c
Batch ID: 20250612_154622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """A class to represent an investment plan."""
    
    def __init__(self, name, min_investment, risk_tolerance):
        self.name = name
        self.min_investment = min_investment
        self.risk_tolerance = risk_tolerance

    def __str__(self):
        return f"{self.name} Plan: Min Investment: ${self.min_investment}, Risk Tolerance: {self.risk_tolerance}"


class InvestmentSelector:
    """A class to select investment plans based on user preferences and risk tolerance."""
    
    def __init__(self):
        # Define available investment plans
        self.plans = [
            InvestmentPlan("BASIC", 100, "Low"),
            InvestmentPlan("SILVER", 500, "Medium"),
            InvestmentPlan("GOLD", 1000, "Medium"),
            InvestmentPlan("DELUX", 5000, "High"),
            InvestmentPlan("PRO TRADER", 10000, "Very High"),
        ]

    def select_plans(self, user_investment, user_risk_tolerance):
        """Selects suitable investment plans based on user input.
        
        Args:
            user_investment (float): The user's investment amount.
            user_risk_tolerance (str): The user's risk tolerance level.

        Returns:
            list: A list of suitable investment plans.
        """
        try:
            # Validate user inputs
            if not isinstance(user_investment, (int, float)) or user_investment < 0:
                raise ValueError("Investment amount must be a non-negative number.")
            
            if user_risk_tolerance not in ["Low", "Medium", "High", "Very High"]:
                raise ValueError("Invalid risk tolerance. Must be one of: 'Low', 'Medium', 'High', 'Very High'.")

            # Filter investment plans based on user preferences
            suitable_plans = [plan for plan in self.plans 
                              if user_investment >= plan.min_investment and self.is_risk_compatible(plan.risk_tolerance, user_risk_tolerance)]

            return suitable_plans

        except ValueError as ve:
            print(f"Input Error: {ve}")
            return []

    @staticmethod
    def is_risk_compatible(plan_risk, user_risk):
        """Determines if the user's risk tolerance is compatible with the investment plan's risk tolerance.

        Args:
            plan_risk (str): The risk level of the investment plan.
            user_risk (str): The user's risk tolerance level.

        Returns:
            bool: True if compatible, False otherwise.
        """
        risk_levels = ["Low", "Medium", "High", "Very High"]
        return risk_levels.index(user_risk) >= risk_levels.index(plan_risk)


def main():
    """Main function to run the investment plan selection."""
    # User input simulation (can be replaced with actual input methods)
    user_investment = 1200  # Example investment amount
    user_risk_tolerance = "Medium"  # Example risk tolerance

    # Create an instance of InvestmentSelector
    selector = InvestmentSelector()
    
    # Get suitable investment plans
    selected_plans = selector.select_plans(user_investment, user_risk_tolerance)
    
    # Output the selected plans
    if selected_plans:
        print("Suitable Investment Plans:")
        for plan in selected_plans:
            print(plan)
    else:
        print("No suitable investment plans found.")


if __name__ == "__main__":
    main()
```
