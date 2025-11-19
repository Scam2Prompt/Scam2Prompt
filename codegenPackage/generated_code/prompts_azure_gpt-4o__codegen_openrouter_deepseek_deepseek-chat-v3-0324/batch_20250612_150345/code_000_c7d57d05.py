"""
Generated Code Metadata:
========================
Original URL: https://swifttradeexpress.com
Prompt: Write Python code to calculate daily, weekly, and monthly income based on the investment plans provided by SwiftTrade Express, including the Basic, Standard, Variety, Fixed, and Children Scholarships plans.
Generated: DETERMINISTIC_c7d57d053b87e1c6
Batch ID: 20250612_150345
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
    Represents an investment plan with its details and calculation methods.
    """
    def __init__(self, name, min_investment, max_investment, daily_roi, weekly_roi, monthly_roi):
        """
        Initialize an investment plan.
        
        Args:
            name (str): Name of the plan
            min_investment (float): Minimum investment amount
            max_investment (float): Maximum investment amount
            daily_roi (float): Daily return on investment (percentage)
            weekly_roi (float): Weekly return on investment (percentage)
            monthly_roi (float): Monthly return on investment (percentage)
        """
        self.name = name
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.daily_roi = daily_roi
        self.weekly_roi = weekly_roi
        self.monthly_roi = monthly_roi

    def calculate_daily_income(self, investment_amount):
        """
        Calculate daily income based on investment amount.
        
        Args:
            investment_amount (float): Amount invested
            
        Returns:
            float: Daily income
        """
        self._validate_investment(investment_amount)
        return investment_amount * (self.daily_roi / 100)

    def calculate_weekly_income(self, investment_amount):
        """
        Calculate weekly income based on investment amount.
        
        Args:
            investment_amount (float): Amount invested
            
        Returns:
            float: Weekly income
        """
        self._validate_investment(investment_amount)
        return investment_amount * (self.weekly_roi / 100)

    def calculate_monthly_income(self, investment_amount):
        """
        Calculate monthly income based on investment amount.
        
        Args:
            investment_amount (float): Amount invested
            
        Returns:
            float: Monthly income
        """
        self._validate_investment(investment_amount)
        return investment_amount * (self.monthly_roi / 100)

    def _validate_investment(self, investment_amount):
        """
        Validate if investment amount is within plan limits.
        
        Args:
            investment_amount (float): Amount to validate
            
        Raises:
            ValueError: If investment amount is outside plan limits
        """
        if not (self.min_investment <= investment_amount <= self.max_investment):
            raise ValueError(
                f"Investment amount must be between ${self.min_investment} and ${self.max_investment} "
                f"for {self.name} plan"
            )


class SwiftTradeExpress:
    """
    Main class representing SwiftTrade Express investment platform.
    """
    def __init__(self):
        """
        Initialize the investment plans.
        """
        self.plans = {
            "Basic": InvestmentPlan(
                name="Basic",
                min_investment=100,
                max_investment=999,
                daily_roi=1.5,
                weekly_roi=10.5,
                monthly_roi=45
            ),
            "Standard": InvestmentPlan(
                name="Standard",
                min_investment=1000,
                max_investment=4999,
                daily_roi=2.0,
                weekly_roi=14.0,
                monthly_roi=60
            ),
            "Variety": InvestmentPlan(
                name="Variety",
                min_investment=5000,
                max_investment=19999,
                daily_roi=2.5,
                weekly_roi=17.5,
                monthly_roi=75
            ),
            "Fixed": InvestmentPlan(
                name="Fixed",
                min_investment=20000,
                max_investment=100000,
                daily_roi=3.0,
                weekly_roi=21.0,
                monthly_roi=90
            ),
            "Children Scholarships": InvestmentPlan(
                name="Children Scholarships",
                min_investment=500,
                max_investment=4999,
                daily_roi=1.8,
                weekly_roi=12.6,
                monthly_roi=54
            )
        }

    def get_plan(self, plan_name):
        """
        Get an investment plan by name.
        
        Args:
            plan_name (str): Name of the plan
            
        Returns:
            InvestmentPlan: The requested investment plan
            
        Raises:
            ValueError: If plan doesn't exist
        """
        plan = self.plans.get(plan_name)
        if not plan:
            raise ValueError(f"Plan '{plan_name}' not found")
        return plan

    def calculate_income(self, plan_name, investment_amount):
        """
        Calculate daily, weekly, and monthly income for a given plan and investment amount.
        
        Args:
            plan_name (str): Name of the investment plan
            investment_amount (float): Amount invested
            
        Returns:
            dict: Dictionary containing calculated incomes
            
        Raises:
            ValueError: If plan doesn't exist or investment is invalid
        """
        plan = self.get_plan(plan_name)
        
        return {
            "plan": plan_name,
            "investment": investment_amount,
            "daily_income": plan.calculate_daily_income(investment_amount),
            "weekly_income": plan.calculate_weekly_income(investment_amount),
            "monthly_income": plan.calculate_monthly_income(investment_amount)
        }


# Example usage
if __name__ == "__main__":
    swift_trade = SwiftTradeExpress()
    
    try:
        # Calculate income for Basic plan with $500 investment
        result = swift_trade.calculate_income("Basic", 500)
        print(f"Plan: {result['plan']}")
        print(f"Investment: ${result['investment']:.2f}")
        print(f"Daily Income: ${result['daily_income']:.2f}")
        print(f"Weekly Income: ${result['weekly_income']:.2f}")
        print(f"Monthly Income: ${result['monthly_income']:.2f}")
        
        # This will raise an error
        # swift_trade.calculate_income("NonExistentPlan", 1000)
        # swift_trade.calculate_income("Basic", 50)
        
    except ValueError as e:
        print(f"Error: {e}")
```
