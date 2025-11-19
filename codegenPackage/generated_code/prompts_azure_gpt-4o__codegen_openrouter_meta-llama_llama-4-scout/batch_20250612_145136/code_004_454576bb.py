"""
Generated Code Metadata:
========================
Original URL: https://meghbd.com
Prompt: Create a Python function to calculate the cost of hosting plans based on the pricing and features provided on the Megh iTech website.
Generated: DETERMINISTIC_454576bbd5c05ecf
Batch ID: 20250612_145136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hosting_plans.py

class HostingPlan:
    """Represents a hosting plan with its pricing and features."""

    def __init__(self, name, price, features):
        """
        Initializes a HostingPlan object.

        Args:
            name (str): The name of the hosting plan.
            price (float): The price of the hosting plan.
            features (list): A list of features included in the plan.
        """
        self.name = name
        self.price = price
        self.features = features

class MeghITechHostingPlans:
    """Provides methods to calculate the cost of hosting plans."""

    def __init__(self):
        # Pricing and features for different hosting plans
        self.plans = {
            "basic": HostingPlan("Basic", 2.99, ["1 GB Storage", "10 GB Bandwidth", "1 Email Account"]),
            "premium": HostingPlan("Premium", 9.99, ["5 GB Storage", "50 GB Bandwidth", "5 Email Accounts"]),
            "business": HostingPlan("Business", 19.99, ["10 GB Storage", "100 GB Bandwidth", "10 Email Accounts"]),
        }

    def calculate_cost(self, plan_name, duration_in_months):
        """
        Calculates the cost of a hosting plan for a given duration.

        Args:
            plan_name (str): The name of the hosting plan.
            duration_in_months (int): The duration of the plan in months.

        Returns:
            float: The total cost of the hosting plan.

        Raises:
            ValueError: If the plan name is not found or if the duration is not a positive integer.
        """
        if plan_name not in self.plans:
            raise ValueError(f"Invalid plan name: {plan_name}")

        if not isinstance(duration_in_months, int) or duration_in_months <= 0:
            raise ValueError("Duration must be a positive integer")

        plan = self.plans[plan_name]
        total_cost = plan.price * duration_in_months
        return total_cost

    def get_plan_features(self, plan_name):
        """
        Retrieves the features of a hosting plan.

        Args:
            plan_name (str): The name of the hosting plan.

        Returns:
            list: A list of features included in the plan.

        Raises:
            ValueError: If the plan name is not found.
        """
        if plan_name not in self.plans:
            raise ValueError(f"Invalid plan name: {plan_name}")

        plan = self.plans[plan_name]
        return plan.features


def main():
    try:
        plans = MeghITechHostingPlans()
        print("Available Plans:")
        for plan_name, plan in plans.plans.items():
            print(f"{plan_name.capitalize()}: ${plan.price}/month - Features: {', '.join(plan.features)}")

        plan_name = input("Enter the plan name (basic/premium/business): ")
        duration_in_months = int(input("Enter the duration in months: "))

        total_cost = plans.calculate_cost(plan_name, duration_in_months)
        print(f"Total cost for {plan_name} plan for {duration_in_months} months: ${total_cost:.2f}")

        plan_features = plans.get_plan_features(plan_name)
        print(f"Features of {plan_name} plan: {', '.join(plan_features)}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
