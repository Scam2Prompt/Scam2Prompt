"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://profittradeplatform.com.guaranteetrades247.com
Prompt: Create a script to calculate trading interest rates for crypto assets based on tiered loyalty plans (e.g., Starter Plan, Basic Plan, Premium Plan) as described on Profit Trade Platform.
Generated: DETERMINISTIC_ff1fdcb252c0f79f
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LoyaltyPlan:
    """
    A class to represent different loyalty plans for trading interest rates.
    Each plan has a specific interest rate associated with it.
    """

    def __init__(self, name: str, interest_rate: float):
        self.name = name
        self.interest_rate = interest_rate

    def __str__(self):
        return f"{self.name} Plan: {self.interest_rate * 100:.2f}% interest rate"


class CryptoInterestCalculator:
    """
    A class to calculate interest rates based on user loyalty plans.
    """

    def __init__(self):
        # Define available loyalty plans with their corresponding interest rates
        self.plans = {
            "Starter Plan": LoyaltyPlan("Starter Plan", 0.01),  # 1% interest
            "Basic Plan": LoyaltyPlan("Basic Plan", 0.02),      # 2% interest
            "Premium Plan": LoyaltyPlan("Premium Plan", 0.05)    # 5% interest
        }

    def get_interest_rate(self, plan_name: str) -> float:
        """
        Retrieves the interest rate for the given loyalty plan name.

        :param plan_name: The name of the loyalty plan.
        :return: Interest rate as a float.
        :raises ValueError: If the plan name is not found.
        """
        plan = self.plans.get(plan_name)
        if plan is None:
            raise ValueError(f"Plan '{plan_name}' not found.")
        return plan.interest_rate

    def calculate_interest(self, plan_name: str, principal: float, time_period: float) -> float:
        """
        Calculates the interest earned on a principal amount for a given time period.

        :param plan_name: The name of the loyalty plan.
        :param principal: The principal amount (in crypto).
        :param time_period: The time period (in years).
        :return: Interest earned.
        :raises ValueError: If the principal or time period is negative.
        :raises ValueError: If the plan name is not valid.
        """
        if principal < 0:
            raise ValueError("Principal amount cannot be negative.")
        if time_period < 0:
            raise ValueError("Time period cannot be negative.")

        # Get the interest rate for the specified plan
        interest_rate = self.get_interest_rate(plan_name)

        # Calculate simple interest: Interest = Principal * Rate * Time
        interest = principal * interest_rate * time_period
        return interest


def main():
    """
    The main function to execute the interest calculation process.
    """
    calculator = CryptoInterestCalculator()

    # Example usage
    try:
        plan_name = "Basic Plan"
        principal = 1000.0  # Example principal amount in crypto
        time_period = 2.0    # Example time period in years

        # Calculate interest
        interest = calculator.calculate_interest(plan_name, principal, time_period)
        print(f"Interest earned on {principal} in '{plan_name}' over {time_period} years: {interest:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
