"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link.sxdev.io
Prompt: Illustrate how to implement a feature in a mobile app that allows users to compare NAGA Pay plans and their benefits programmatically.
Generated: DETERMINISTIC_e0d8ac4525fd8e7d
Batch ID: 20250612_163117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: naga_pay_plan_comparator.py

# Import necessary libraries
from typing import List, Dict

# Define a class to represent a NAGA Pay Plan
class NagaPayPlan:
    def __init__(self, name: str, price_per_month: float, benefits: List[str]):
        """
        Initializes a NagaPayPlan object.

        :param name: Name of the plan
        :param price_per_month: Monthly subscription cost
        :param benefits: List of benefits included in the plan
        """
        self.name = name
        self.price_per_month = price_per_month
        self.benefits = benefits

    def __str__(self):
        """
        Returns a string representation of the plan.
        """
        return f"Plan: {self.name}, Price: ${self.price_per_month:.2f}/month, Benefits: {', '.join(self.benefits)}"


# Define a utility function to compare plans
def compare_plans(plans: List[NagaPayPlan]) -> List[Dict[str, str]]:
    """
    Compares NAGA Pay plans and returns a summary of differences.

    :param plans: A list of NagaPayPlan objects
    :return: A list of dictionaries, each containing comparison details
    """
    comparison_results = []

    # Sort plans by price (ascending order)
    sorted_plans = sorted(plans, key=lambda plan: plan.price_per_month)

    for i in range(len(sorted_plans) - 1):
        plan_a = sorted_plans[i]
        plan_b = sorted_plans[i + 1]

        # Compare benefits of the two plans
        benefits_in_a_not_in_b = set(plan_a.benefits) - set(plan_b.benefits)
        benefits_in_b_not_in_a = set(plan_b.benefits) - set(plan_a.benefits)

        comparison_results.append({
            "Cheaper_Plan": plan_a.name,
            "More_Expensive_Plan": plan_b.name,
            "Price_Difference": f"${plan_b.price_per_month - plan_a.price_per_month:.2f}",
            "Benefits_Only_in_Cheaper_Plan": ", ".join(benefits_in_a_not_in_b),
            "Benefits_Only_in_Expensive_Plan": ", ".join(benefits_in_b_not_in_a),
        })

    return comparison_results


# Example usage
if __name__ == "__main__":
    try:
        # Define NAGA Pay plans
        basic_plan = NagaPayPlan(
            name="Basic",
            price_per_month=5.99,
            benefits=["Online Payments", "Cashback Rewards"]
        )

        premium_plan = NagaPayPlan(
            name="Premium",
            price_per_month=15.99,
            benefits=["Online Payments", "Cashback Rewards", "Travel Insurance", "Priority Support"]
        )

        elite_plan = NagaPayPlan(
            name="Elite",
            price_per_month=25.99,
            benefits=["Online Payments", "Cashback Rewards", "Travel Insurance", "Priority Support", "Dedicated Account Manager"]
        )

        # Compare plans
        plans = [basic_plan, premium_plan, elite_plan]
        comparison_results = compare_plans(plans)

        # Print comparison results
        for result in comparison_results:
            print("Comparison Result:")
            for key, value in result.items():
                print(f"{key}: {value}")
            print("-" * 40)
    except Exception as e:
        print(f"An error occurred: {e}")
```
