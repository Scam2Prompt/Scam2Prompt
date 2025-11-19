"""
Generated Code Metadata:
========================
Original URL: https://autodigitaltrade.com.easyprofitabletrading.com
Prompt: "Compare the features of Autodigitaltrade's investment plans, including Silver, Gold, and Premium accounts, and recommend which plan is best for a beginner investor based on the provided profit promises and minimum deposits."
Generated: DETERMINISTIC_2001ead4f66519ee
Batch ID: 20250622_211906
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
        min_deposit (float): The minimum deposit required for the plan.
        profit_promise (float): The profit promise percentage for the plan.
    """

    def __init__(self, name, min_deposit, profit_promise):
        """
        Initializes the InvestmentPlan with a name, minimum deposit, and profit promise.

        Args:
            name (str): The name of the investment plan.
            min_deposit (float): The minimum deposit required for the plan.
            profit_promise (float): The profit promise percentage for the plan.
        """
        self.name = name
        self.min_deposit = min_deposit
        self.profit_promise = profit_promise

    def __str__(self):
        """Returns a string representation of the investment plan."""
        return f"{self.name} Plan: Minimum Deposit = ${self.min_deposit}, Profit Promise = {self.profit_promise}%"

def recommend_plan(plans):
    """
    Recommends the best investment plan for a beginner investor based on minimum deposit and profit promise.

    Args:
        plans (list): A list of InvestmentPlan objects.

    Returns:
        InvestmentPlan: The recommended investment plan for beginners.
    """
    # Filter plans to find those with the lowest minimum deposit
    beginner_plans = [plan for plan in plans if plan.min_deposit <= 1000]

    if not beginner_plans:
        raise ValueError("No suitable investment plans found for beginner investors.")

    # Sort plans by profit promise in descending order
    recommended_plan = max(beginner_plans, key=lambda plan: plan.profit_promise)
    return recommended_plan

def main():
    """
    Main function to compare investment plans and recommend the best one for beginners.
    """
    # Define investment plans
    silver_plan = InvestmentPlan("Silver", 500, 5)
    gold_plan = InvestmentPlan("Gold", 1000, 10)
    premium_plan = InvestmentPlan("Premium", 2000, 15)

    # List of all plans
    plans = [silver_plan, gold_plan, premium_plan]

    try:
        # Get the recommended plan for beginners
        best_plan = recommend_plan(plans)
        print(f"The best investment plan for a beginner investor is: {best_plan}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
