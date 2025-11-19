"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syncexperttrade.com
Prompt: Create a function that calculates potential profits based on the investment plans (Bronze, Silver, Gold, Premium) offered by SyncExpertTrade.
Generated: DETERMINISTIC_fb175a6858d5130b
Batch ID: 20250612_160413
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
    Class to represent an investment plan with associated profit calculations.
    """
    
    def __init__(self, plan_name, investment_amount, duration_months):
        """
        Initializes the InvestmentPlan with a name, investment amount, and duration.
        
        :param plan_name: Name of the investment plan (Bronze, Silver, Gold, Premium)
        :param investment_amount: Amount of money invested
        :param duration_months: Duration of the investment in months
        """
        self.plan_name = plan_name
        self.investment_amount = investment_amount
        self.duration_months = duration_months

    def calculate_profit(self):
        """
        Calculates potential profit based on the investment plan.
        
        :return: Calculated profit amount
        :raises ValueError: If an invalid plan name is provided
        """
        # Define profit rates for each plan
        profit_rates = {
            "Bronze": 0.05,  # 5% profit
            "Silver": 0.1,   # 10% profit
            "Gold": 0.15,    # 15% profit
            "Premium": 0.2   # 20% profit
        }

        try:
            # Validate the investment plan name
            if self.plan_name not in profit_rates:
                raise ValueError(f"Invalid plan name: {self.plan_name}. "
                                 "Must be one of: Bronze, Silver, Gold, Premium.")
            
            # Calculate profit
            profit_rate = profit_rates[self.plan_name]
            profit = self.investment_amount * profit_rate * self.duration_months
            
            return profit
            
        except Exception as e:
            print(f"Error calculating profit: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Create an instance of InvestmentPlan
    plan = InvestmentPlan("Gold", 1000, 12)
    # Calculate and print the profit
    profit = plan.calculate_profit()
    
    if profit is not None:
        print(f"The potential profit for your {plan.plan_name} plan is: ${profit:.2f}")
```
