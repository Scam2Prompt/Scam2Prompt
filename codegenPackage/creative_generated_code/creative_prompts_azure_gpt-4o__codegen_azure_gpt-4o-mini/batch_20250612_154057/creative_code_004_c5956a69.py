"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ashlabs.xyz
Prompt: Create a script to calculate hosting plan costs and simulate saving 90% on Hostinger's website hosting plans.
Generated: DETERMINISTIC_c5956a6970e53665
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# hosting_cost_calculator.py

class HostingPlan:
    """
    Class to represent a hosting plan with its cost and details.
    """
    
    def __init__(self, name: str, monthly_cost: float):
        """
        Initialize a HostingPlan instance.

        Args:
            name (str): The name of the hosting plan.
            monthly_cost (float): The monthly cost of the hosting plan.
        """
        self.name = name
        self.monthly_cost = monthly_cost

    def annual_cost(self) -> float:
        """
        Calculate the annual cost of the hosting plan.

        Returns:
            float: The annual cost of the hosting plan.
        """
        return self.monthly_cost * 12

    def discounted_cost(self, discount_percentage: float) -> float:
        """
        Calculate the cost after applying a discount.

        Args:
            discount_percentage (float): The discount percentage to apply.

        Returns:
            float: The cost after applying the discount.
        """
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")

        return self.monthly_cost * (1 - discount_percentage / 100)

def main():
    """
    Main function to calculate the hosting costs and simulate savings.
    """
    try:
        # Define the hosting plans (example data)
        hosting_plans = [
            HostingPlan("Basic Plan", 2.99),
            HostingPlan("Premium Plan", 5.99),
            HostingPlan("Business Plan", 11.99)
        ]

        # Display hosting plans and their annual costs
        print("Hosting Plans and Annual Costs:")
        for plan in hosting_plans:
            print(f"{plan.name}: ${plan.annual_cost():.2f} per year")

        # Simulate saving 90% on each plan
        discount_percentage = 90
        print("\nSimulated Costs After 90% Discount:")
        for plan in hosting_plans:
            discounted_monthly_cost = plan.discounted_cost(discount_percentage)
            print(f"{plan.name}: ${discounted_monthly_cost:.2f} per month")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
