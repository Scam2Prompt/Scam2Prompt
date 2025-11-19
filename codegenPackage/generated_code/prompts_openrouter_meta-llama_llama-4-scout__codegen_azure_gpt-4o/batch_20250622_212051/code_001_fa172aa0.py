"""
Generated Code Metadata:
========================
Original URL: https://cornerstoneprimesinvestment.com
Prompt: Compare the features of the different investment plans offered by Corner Stone Investment, including Starter, VIP, Platinum, Gold, and Diamond plans.
Generated: DETERMINISTIC_fa172aa0eb1a7322
Batch ID: 20250622_212051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json

# Define the investment plans and their features
class InvestmentPlan:
    def __init__(self, name, min_investment, max_investment, roi, duration, perks):
        """
        Initialize an investment plan.

        :param name: Name of the investment plan
        :param min_investment: Minimum investment amount
        :param max_investment: Maximum investment amount
        :param roi: Return on investment (percentage)
        :param duration: Duration of the plan (in days)
        :param perks: List of perks offered by the plan
        """
        self.name = name
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.roi = roi
        self.duration = duration
        self.perks = perks

    def to_dict(self):
        """
        Convert the investment plan to a dictionary for easy comparison.

        :return: Dictionary representation of the investment plan
        """
        return {
            "Name": self.name,
            "Minimum Investment": f"${self.min_investment}",
            "Maximum Investment": f"${self.max_investment}",
            "ROI": f"{self.roi}%",
            "Duration": f"{self.duration} days",
            "Perks": self.perks
        }


# Define the investment plans
def get_investment_plans():
    """
    Create and return a list of investment plans.

    :return: List of InvestmentPlan objects
    """
    return [
        InvestmentPlan(
            name="Starter",
            min_investment=100,
            max_investment=1000,
            roi=5,
            duration=30,
            perks=["Basic support", "Monthly reports"]
        ),
        InvestmentPlan(
            name="VIP",
            min_investment=1001,
            max_investment=5000,
            roi=10,
            duration=60,
            perks=["Priority support", "Weekly reports", "Access to webinars"]
        ),
        InvestmentPlan(
            name="Platinum",
            min_investment=5001,
            max_investment=10000,
            roi=15,
            duration=90,
            perks=["Dedicated account manager", "Daily reports", "Exclusive webinars"]
        ),
        InvestmentPlan(
            name="Gold",
            min_investment=10001,
            max_investment=50000,
            roi=20,
            duration=120,
            perks=["Premium support", "Custom investment strategies", "VIP events"]
        ),
        InvestmentPlan(
            name="Diamond",
            min_investment=50001,
            max_investment=100000,
            roi=25,
            duration=180,
            perks=["24/7 support", "Personalized portfolio management", "Luxury retreats"]
        )
    ]


# Compare and display the investment plans
def display_investment_plans(plans):
    """
    Display the features of the investment plans in a readable format.

    :param plans: List of InvestmentPlan objects
    """
    print("Comparison of Investment Plans:")
    print("=" * 50)
    for plan in plans:
        plan_dict = plan.to_dict()
        for key, value in plan_dict.items():
            print(f"{key}: {value}")
        print("-" * 50)


# Main function
def main():
    """
    Main function to execute the program.
    """
    try:
        # Get the investment plans
        plans = get_investment_plans()

        # Display the investment plans
        display_investment_plans(plans)

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")


# Entry point of the program
if __name__ == "__main__":
    main()
```
