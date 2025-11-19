"""
Generated Code Metadata:
========================
Original URL: https://worldcoin.org.hk
Prompt: "Compare the pricing plans of Stellar Hong Kong's AI API platform, including the differences between the 初級計劃, 高級計劃, 無限計劃, and 定制計劃."
Generated: DETERMINISTIC_ce675f2f1bf3bb28
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pricing_plans_comparator.py

class PricingPlan:
    """Represents a pricing plan with its characteristics."""

    def __init__(self, name, description, requests_per_day, 
                 data_storage, support, price):
        """
        Initializes a PricingPlan object.

        Args:
            name (str): The name of the plan.
            description (str): A brief description of the plan.
            requests_per_day (int): The number of API requests allowed per day.
            data_storage (str): The amount of data storage provided.
            support (str): The level of support offered.
            price (float): The price of the plan.
        """
        self.name = name
        self.description = description
        self.requests_per_day = requests_per_day
        self.data_storage = data_storage
        self.support = support
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.description}"


class PricingPlansComparator:
    """Compares pricing plans of Stellar Hong Kong's AI API platform."""

    def __init__(self):
        # Define pricing plans
        self.plans = {
            "初級計劃": PricingPlan(
                "初級計劃", "Basic plan for small projects", 
                1000, "100MB", "Email support", 100.0
            ),
            "高級計劃": PricingPlan(
                "高級計劃", "Advanced plan for growing businesses", 
                5000, "1GB", "Phone and email support", 500.0
            ),
            "無限計劃": PricingPlan(
                "無限計劃", "Unlimited plan for large enterprises", 
                float('inf'), "10GB", "Dedicated support", 2000.0
            ),
            "定制計劃": PricingPlan(
                "定制計劃", "Custom plan for specific needs", 
                float('inf'), "Custom", "Dedicated support", 0.0
            ),
        }

    def compare_plans(self):
        """Prints a comparison of the pricing plans."""
        print("Pricing Plans Comparison:")
        print("-------------------------")
        for plan_name, plan in self.plans.items():
            print(f"Plan: {plan_name}")
            print(f"Description: {plan.description}")
            print(f"Requests per day: {plan.requests_per_day}")
            print(f"Data storage: {plan.data_storage}")
            print(f"Support: {plan.support}")
            print(f"Price: ${plan.price:.2f}")
            print("-------------------------")

    def get_plan(self, plan_name):
        """Gets a pricing plan by name.

        Args:
            plan_name (str): The name of the plan.

        Returns:
            PricingPlan: The pricing plan object, or None if not found.
        """
        return self.plans.get(plan_name)

    def calculate_price_difference(self, plan_name1, plan_name2):
        """Calculates the price difference between two plans.

        Args:
            plan_name1 (str): The name of the first plan.
            plan_name2 (str): The name of the second plan.

        Returns:
            float: The price difference between the two plans.
        """
        plan1 = self.get_plan(plan_name1)
        plan2 = self.get_plan(plan_name2)
        if plan1 is None or plan2 is None:
            raise ValueError("One or both plans not found")
        return plan2.price - plan1.price


def main():
    comparator = PricingPlansComparator()
    comparator.compare_plans()

    # Example usage: calculate price difference
    plan_name1 = "初級計劃"
    plan_name2 = "高級計劃"
    try:
        price_diff = comparator.calculate_price_difference(plan_name1, plan_name2)
        print(f"Price difference between {plan_name1} and {plan_name2}: ${price_diff:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
