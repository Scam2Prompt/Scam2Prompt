"""
Generated Code Metadata:
========================
Original URL: https://ashlabs.xyz
Prompt: Create a script to calculate hosting plan costs and simulate saving 90% on Hostinger's website hosting plans.
Generated: DETERMINISTIC_c5956a6970e53665
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HostingPlan:
    """
    A class to represent a hosting plan with its cost and a method to calculate savings.
    """

    def __init__(self, name: str, monthly_cost: float):
        """
        Initializes a new HostingPlan instance.

        :param name: The name of the hosting plan.
        :param monthly_cost: The monthly cost of the hosting plan.
        """
        self.name = name
        self.monthly_cost = monthly_cost

    def calculate_savings(self, discount_percentage: float) -> float:
        """
        Calculates the savings based on the discount percentage.

        :param discount_percentage: The percentage of discount to apply.
        :return: The amount saved.
        """
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        
        savings = (self.monthly_cost * discount_percentage) / 100
        return savings

    def discounted_cost(self, discount_percentage: float) -> float:
        """
        Calculates the new cost after applying the discount.

        :param discount_percentage: The percentage of discount to apply.
        :return: The new monthly cost after discount.
        """
        savings = self.calculate_savings(discount_percentage)
        return self.monthly_cost - savings


def main():
    """
    Main function to simulate the hosting plan cost calculation and savings.
    """
    # Define the hosting plans with their monthly costs
    plans = [
        HostingPlan("Basic", 2.49),
        HostingPlan("Premium", 3.99),
        HostingPlan("Business", 7.99)
    ]

    # Define the discount percentage for savings simulation
    discount_percentage = 90

    print(f"{'Plan Name':<15} {'Original Cost':<15} {'Savings':<15} {'Discounted Cost':<15}")
    print("=" * 60)

    for plan in plans:
        try:
            original_cost = plan.monthly_cost
            savings = plan.calculate_savings(discount_percentage)
            discounted_cost = plan.discounted_cost(discount_percentage)

            print(f"{plan.name:<15} {original_cost:<15.2f} {savings:<15.2f} {discounted_cost:<15.2f}")
        except ValueError as e:
            print(f"Error calculating for {plan.name}: {e}")


if __name__ == "__main__":
    main()
```
