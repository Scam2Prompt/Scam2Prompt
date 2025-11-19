"""
Generated Code Metadata:
========================
Original URL: https://thegaincapital.com
Prompt: "Compare the features of Gain Capital's investment plans, including Silver Demat, Gold Demat, Diamond Demat, and Platinum Demat, and recommend the best plan for a beginner investor."
Generated: DETERMINISTIC_ce66521666b7ac9f
Batch ID: 20250622_204755
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
    """

    def __init__(self, name, features, risk_level, fees):
        """
        Initializes an InvestmentPlan instance.

        :param name: Name of the investment plan
        :param features: List of features of the investment plan
        :param risk_level: Risk level associated with the investment plan
        :param fees: Fees associated with the investment plan
        """
        self.name = name
        self.features = features
        self.risk_level = risk_level
        self.fees = fees

    def __str__(self):
        """
        Returns a string representation of the investment plan.
        """
        return f"{self.name} - Risk Level: {self.risk_level}, Fees: {self.fees}, Features: {', '.join(self.features)}"


def compare_investment_plans(plans):
    """
    Compares investment plans and recommends the best plan for a beginner investor.

    :param plans: List of InvestmentPlan instances
    :return: Recommended investment plan for beginners
    """
    try:
        # Filter plans suitable for beginners (low risk and reasonable fees)
        beginner_friendly_plans = [
            plan for plan in plans if plan.risk_level == 'Low' and plan.fees <= 100
        ]

        if not beginner_friendly_plans:
            raise ValueError("No suitable investment plans found for beginners.")

        # Sort plans by fees (lower fees are better)
        recommended_plan = min(beginner_friendly_plans, key=lambda x: x.fees)
        return recommended_plan

    except Exception as e:
        print(f"Error during comparison: {e}")
        return None


# Define investment plans
silver_demat = InvestmentPlan(
    name="Silver Demat",
    features=["Basic trading", "Low fees", "Limited research"],
    risk_level="Low",
    fees=50
)

gold_demat = InvestmentPlan(
    name="Gold Demat",
    features=["Advanced trading", "Moderate fees", "Research tools"],
    risk_level="Medium",
    fees=150
)

diamond_demat = InvestmentPlan(
    name="Diamond Demat",
    features=["Premium trading", "High fees", "Comprehensive research"],
    risk_level="High",
    fees=300
)

platinum_demat = InvestmentPlan(
    name="Platinum Demat",
    features=["Exclusive trading", "Very high fees", "Expert research"],
    risk_level="Very High",
    fees=500
)

# List of all investment plans
investment_plans = [silver_demat, gold_demat, diamond_demat, platinum_demat]

# Compare plans and get recommendation
recommended_plan = compare_investment_plans(investment_plans)

# Output the recommended plan
if recommended_plan:
    print("Recommended Investment Plan for Beginners:")
    print(recommended_plan)
else:
    print("No suitable investment plan found.")
```
