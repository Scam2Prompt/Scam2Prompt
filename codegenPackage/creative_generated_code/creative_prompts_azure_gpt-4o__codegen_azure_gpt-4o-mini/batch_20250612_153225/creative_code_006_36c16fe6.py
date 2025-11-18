"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://batikenttofas.com
Prompt: Write a Python script to calculate monthly membership fees based on the pricing plans (Starter, Professional, Enterprise) provided on the Batıkent Tofaş Spor Klübü website.
Generated: DETERMINISTIC_36c16fe6fe3e5c88
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MembershipPlan:
    """Class to represent a membership plan with a name and monthly fee."""

    def __init__(self, name: str, monthly_fee: float):
        """Initialize a membership plan with a given name and monthly fee.

        Args:
            name (str): The name of the membership plan.
            monthly_fee (float): The monthly fee for the plan.
        """
        self.name = name
        self.monthly_fee = monthly_fee


class MembershipFeeCalculator:
    """Class to calculate the total membership fee based on selected plans and duration."""

    def __init__(self):
        """Initialize the membership fee calculator with predefined plans."""
        self.plans = {
            "Starter": MembershipPlan("Starter", 50.0),
            "Professional": MembershipPlan("Professional", 100.0),
            "Enterprise": MembershipPlan("Enterprise", 250.0),
        }

    def calculate_fee(self, plan_name: str, months: int) -> float:
        """Calculate the total membership fee for a selected plan and duration.

        Args:
            plan_name (str): The name of the membership plan.
            months (int): The number of months for the membership.

        Returns:
            float: The total fee for the selected plan and duration.

        Raises:
            ValueError: If the plan name is invalid or the number of months is not positive.
        """
        if plan_name not in self.plans:
            raise ValueError(f"Invalid plan name: {plan_name}. Available plans: {', '.join(self.plans.keys())}.")

        if months <= 0:
            raise ValueError("Number of months must be a positive integer.")

        plan = self.plans[plan_name]
        total_fee = plan.monthly_fee * months
        return total_fee


def main():
    """Main function to execute the membership fee calculation."""
    calculator = MembershipFeeCalculator()
    
    try:
        # Input from the user for the plan and duration
        plan_name = input("Enter the membership plan (Starter, Professional, Enterprise): ")
        months = int(input("Enter the number of months: "))

        # Calculate the fee and display the result
        total_fee = calculator.calculate_fee(plan_name, months)
        print(f"The total fee for the {plan_name} plan for {months} month(s) is: ${total_fee:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
