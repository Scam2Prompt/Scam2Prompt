"""
Generated Code Metadata:
========================
Original URL: https://financeimpactpro.com
Prompt: Write Python code to calculate daily profits for the investment plans offered by Finance Impact Pro, including Basic, Silver, Gold, and Ultimate plans, based on their guaranteed profit percentages and durations.
Generated: DETERMINISTIC_f1ba9f71017b351a
Batch ID: 20250612_154601
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
    Represents an investment plan with its properties and profit calculation logic.
    """
    
    def __init__(self, name: str, min_investment: float, max_investment: float, 
                 daily_profit_percent: float, duration_days: int):
        """
        Initialize an investment plan.
        
        Args:
            name: Name of the plan
            min_investment: Minimum investment amount
            max_investment: Maximum investment amount
            daily_profit_percent: Daily profit percentage (as decimal)
            duration_days: Duration of the plan in days
        """
        self.name = name
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.daily_profit_percent = daily_profit_percent
        self.duration_days = duration_days
    
    def calculate_daily_profit(self, investment_amount: float) -> float:
        """
        Calculate daily profit for a given investment amount.
        
        Args:
            investment_amount: Amount invested
            
        Returns:
            Daily profit amount
            
        Raises:
            ValueError: If investment amount is outside plan limits
        """
        if not (self.min_investment <= investment_amount <= self.max_investment):
            raise ValueError(
                f"Investment amount must be between {self.min_investment} and {self.max_investment}"
            )
        return investment_amount * self.daily_profit_percent
    
    def calculate_total_profit(self, investment_amount: float) -> float:
        """
        Calculate total profit over the plan duration.
        
        Args:
            investment_amount: Amount invested
            
        Returns:
            Total profit amount
        """
        daily_profit = self.calculate_daily_profit(investment_amount)
        return daily_profit * self.duration_days


class FinanceImpactPro:
    """
    Main class representing Finance Impact Pro investment plans and calculations.
    """
    
    def __init__(self):
        """
        Initialize all available investment plans.
        """
        self.plans = {
            'Basic': InvestmentPlan(
                name='Basic',
                min_investment=100.0,
                max_investment=999.0,
                daily_profit_percent=0.01,  # 1%
                duration_days=30
            ),
            'Silver': InvestmentPlan(
                name='Silver',
                min_investment=1000.0,
                max_investment=4999.0,
                daily_profit_percent=0.015,  # 1.5%
                duration_days=45
            ),
            'Gold': InvestmentPlan(
                name='Gold',
                min_investment=5000.0,
                max_investment=19999.0,
                daily_profit_percent=0.02,  # 2%
                duration_days=60
            ),
            'Ultimate': InvestmentPlan(
                name='Ultimate',
                min_investment=20000.0,
                max_investment=100000.0,
                daily_profit_percent=0.025,  # 2.5%
                duration_days=90
            )
        }
    
    def get_plan(self, plan_name: str) -> InvestmentPlan:
        """
        Get an investment plan by name.
        
        Args:
            plan_name: Name of the plan to retrieve
            
        Returns:
            The requested InvestmentPlan object
            
        Raises:
            ValueError: If plan name is invalid
        """
        if plan_name not in self.plans:
            raise ValueError(f"Invalid plan name. Available plans: {list(self.plans.keys())}")
        return self.plans[plan_name]
    
    def calculate_daily_profit(self, plan_name: str, investment_amount: float) -> float:
        """
        Calculate daily profit for a given plan and investment amount.
        
        Args:
            plan_name: Name of the investment plan
            investment_amount: Amount invested
            
        Returns:
            Daily profit amount
        """
        plan = self.get_plan(plan_name)
        return plan.calculate_daily_profit(investment_amount)
    
    def calculate_total_profit(self, plan_name: str, investment_amount: float) -> float:
        """
        Calculate total profit for a given plan and investment amount.
        
        Args:
            plan_name: Name of the investment plan
            investment_amount: Amount invested
            
        Returns:
            Total profit amount over plan duration
        """
        plan = self.get_plan(plan_name)
        return plan.calculate_total_profit(investment_amount)
    
    def generate_profit_report(self, plan_name: str, investment_amount: float) -> dict:
        """
        Generate a comprehensive profit report for an investment.
        
        Args:
            plan_name: Name of the investment plan
            investment_amount: Amount invested
            
        Returns:
            Dictionary containing all relevant profit information
        """
        plan = self.get_plan(plan_name)
        daily_profit = plan.calculate_daily_profit(investment_amount)
        total_profit = plan.calculate_total_profit(investment_amount)
        
        return {
            'plan_name': plan.name,
            'investment_amount': investment_amount,
            'daily_profit': round(daily_profit, 2),
            'total_profit': round(total_profit, 2),
            'duration_days': plan.duration_days,
            'daily_profit_percent': plan.daily_profit_percent * 100,
            'total_return': round(investment_amount + total_profit, 2)
        }


# Example usage
if __name__ == "__main__":
    finance_impact = FinanceImpactPro()
    
    try:
        # Calculate for Basic plan
        report = finance_impact.generate_profit_report('Basic', 500.0)
        print("Profit Report:")
        for key, value in report.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
        
        # Calculate for Gold plan
        daily_profit = finance_impact.calculate_daily_profit('Gold', 10000.0)
        print(f"\nGold Plan Daily Profit: ${daily_profit:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
