"""
Generated Code Metadata:
========================
Original URL: https://apcapitalin.com
Prompt: Create a function to calculate the total deposit, total payments, and duration for various investment plans (Basic, Silver, Gold, Platinum) as outlined by Apex Capital Investment.
Generated: DETERMINISTIC_1c7b4bb2f4d68868
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentPlanCalculator:
    """
    A class to calculate investment metrics for different plans offered by Apex Capital Investment.
    Supported plans: Basic, Silver, Gold, Platinum.
    """
    
    def __init__(self):
        self.plans = {
            'Basic': {
                'min_deposit': 1000,
                'max_deposit': 5000,
                'daily_interest': 0.02,  # 2%
                'duration_days': 30
            },
            'Silver': {
                'min_deposit': 5001,
                'max_deposit': 15000,
                'daily_interest': 0.025,  # 2.5%
                'duration_days': 45
            },
            'Gold': {
                'min_deposit': 15001,
                'max_deposit': 50000,
                'daily_interest': 0.03,  # 3%
                'duration_days': 60
            },
            'Platinum': {
                'min_deposit': 50001,
                'max_deposit': 100000,
                'daily_interest': 0.035,  # 3.5%
                'duration_days': 90
            }
        }
    
    def calculate_investment(self, plan_name: str, deposit_amount: float) -> dict:
        """
        Calculate investment metrics for the specified plan and deposit amount.
        
        Args:
            plan_name: Name of the investment plan (Basic, Silver, Gold, Platinum)
            deposit_amount: Amount to be deposited
            
        Returns:
            Dictionary containing:
                - total_deposit
                - total_payments
                - duration_days
                - daily_interest
                - plan_name
            
        Raises:
            ValueError: If plan_name is invalid or deposit_amount is out of range
        """
        if plan_name not in self.plans:
            raise ValueError(f"Invalid plan name. Available plans: {list(self.plans.keys())}")
        
        plan = self.plans[plan_name]
        
        if not (plan['min_deposit'] <= deposit_amount <= plan['max_deposit']):
            raise ValueError(
                f"Deposit amount for {plan_name} plan must be between "
                f"{plan['min_deposit']} and {plan['max_deposit']}"
            )
        
        total_payments = deposit_amount * (1 + plan['daily_interest'] * plan['duration_days'])
        
        return {
            'plan_name': plan_name,
            'total_deposit': deposit_amount,
            'total_payments': round(total_payments, 2),
            'duration_days': plan['duration_days'],
            'daily_interest': plan['daily_interest']
        }
    
    def get_plan_details(self, plan_name: str) -> dict:
        """
        Get details about a specific investment plan.
        
        Args:
            plan_name: Name of the investment plan
            
        Returns:
            Dictionary containing plan details
            
        Raises:
            ValueError: If plan_name is invalid
        """
        if plan_name not in self.plans:
            raise ValueError(f"Invalid plan name. Available plans: {list(self.plans.keys())}")
        
        return self.plans[plan_name]
    
    def get_all_plans(self) -> list:
        """
        Get a list of all available investment plans.
        
        Returns:
            List of plan names
        """
        return list(self.plans.keys())


# Example usage
if __name__ == "__main__":
    try:
        calculator = InvestmentPlanCalculator()
        
        # Calculate investment for Basic plan
        result = calculator.calculate_investment('Basic', 3000)
        print(f"Basic Plan Results: {result}")
        
        # Get details of Gold plan
        gold_details = calculator.get_plan_details('Gold')
        print(f"Gold Plan Details: {gold_details}")
        
        # List all available plans
        all_plans = calculator.get_all_plans()
        print(f"Available Plans: {all_plans}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
