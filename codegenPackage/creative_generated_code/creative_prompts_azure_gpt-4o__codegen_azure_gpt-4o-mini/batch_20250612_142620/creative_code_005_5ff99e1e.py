"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inceptiontrades.net
Prompt: Create a program to manage investment plans, including starter, enterprise, apex, partnership, and share plans, as outlined on the Inception Trades website.
Generated: DETERMINISTIC_5ff99e1e30376784
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """
    Base class for different investment plans.
    """

    def __init__(self, name, min_investment, max_investment, interest_rate):
        """
        Initialize an investment plan.

        :param name: The name of the investment plan.
        :param min_investment: Minimum investment amount for the plan.
        :param max_investment: Maximum investment amount for the plan.
        :param interest_rate: Interest rate applicable to the plan.
        """
        self.name = name
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.interest_rate = interest_rate

    def calculate_return(self, amount, duration):
        """
        Calculate the return on investment based on the amount and duration.

        :param amount: The amount invested.
        :param duration: Duration of the investment in years.
        :return: Total return after the specified duration.
        """
        if amount < self.min_investment or amount > self.max_investment:
            raise ValueError("Investment amount must be between min and max limits.")
        
        return amount * ((1 + self.interest_rate) ** duration)

    def __str__(self):
        return f"{self.name} Plan: Min ${self.min_investment}, Max ${self.max_investment}, Interest Rate {self.interest_rate * 100}%"


class StarterPlan(InvestmentPlan):
    def __init__(self):
        super().__init__(name="Starter", min_investment=100, max_investment=1000, interest_rate=0.05)


class EnterprisePlan(InvestmentPlan):
    def __init__(self):
        super().__init__(name="Enterprise", min_investment=1000, max_investment=10000, interest_rate=0.07)


class ApexPlan(InvestmentPlan):
    def __init__(self):
        super().__init__(name="Apex", min_investment=10000, max_investment=100000, interest_rate=0.1)


class PartnershipPlan(InvestmentPlan):
    def __init__(self):
        super().__init__(name="Partnership", min_investment=50000, max_investment=500000, interest_rate=0.12)


class SharePlan(InvestmentPlan):
    def __init__(self):
        super().__init__(name="Share", min_investment=200, max_investment=2000, interest_rate=0.04)


class InvestmentManager:
    """
    Class to manage investment plans and calculate returns.
    """

    def __init__(self):
        self.plans = {
            "starter": StarterPlan(),
            "enterprise": EnterprisePlan(),
            "apex": ApexPlan(),
            "partnership": PartnershipPlan(),
            "share": SharePlan(),
        }

    def get_plan(self, plan_name):
        """
        Retrieve an investment plan by name.

        :param plan_name: The name of the investment plan.
        :return: InvestmentPlan object if found, else None.
        """
        return self.plans.get(plan_name.lower())

    def calculate_investment_return(self, plan_name, amount, duration):
        """
        Calculate the return on investment for a specific plan.

        :param plan_name: Name of the investment plan.
        :param amount: Amount invested.
        :param duration: Duration of the investment in years.
        :return: Total return after the specified duration.
        """
        plan = self.get_plan(plan_name)
        if plan is None:
            raise ValueError("Investment plan not found.")

        return plan.calculate_return(amount, duration)


if __name__ == "__main__":
    # Example usage
    manager = InvestmentManager()
    
    try:
        plan_name = "Apex"
        amount = 15000  # Example investment amount
        duration = 5    # Example investment duration in years
        
        total_return = manager.calculate_investment_return(plan_name, amount, duration)
        print(f"Total return on {amount} in {plan_name} plan after {duration} years: ${total_return:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
