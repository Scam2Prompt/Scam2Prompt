"""
Generated Code Metadata:
========================
Original URL: https://bitinvestcoin.com
Prompt: Write Python code to simulate the investment plans offered by BitInvestCoin, including calculations for percentage profit and fixed profit based on the plan duration and investment amount.
Generated: DETERMINISTIC_c7fb7cda431b2840
Batch ID: 20250612_150211
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
    A class to represent an investment plan offered by BitInvestCoin.
    
    Attributes:
        name (str): The name of the investment plan.
        duration_days (int): The duration of the plan in days.
        min_amount (float): The minimum investment amount for the plan.
        max_amount (float): The maximum investment amount for the plan.
        profit_type (str): The type of profit ('percentage' or 'fixed').
        profit_value (float): The value of profit (percentage or fixed amount).
    """
    
    def __init__(self, name, duration_days, min_amount, max_amount, profit_type, profit_value):
        """
        Initialize the InvestmentPlan with the given parameters.
        
        Args:
            name (str): The name of the investment plan.
            duration_days (int): The duration of the plan in days.
            min_amount (float): The minimum investment amount for the plan.
            max_amount (float): The maximum investment amount for the plan.
            profit_type (str): The type of profit ('percentage' or 'fixed').
            profit_value (float): The value of profit (percentage or fixed amount).
        """
        self.name = name
        self.duration_days = duration_days
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.profit_type = profit_type
        self.profit_value = profit_value
    
    def calculate_profit(self, investment_amount):
        """
        Calculate the profit based on the investment amount and plan type.
        
        Args:
            investment_amount (float): The amount invested in the plan.
            
        Returns:
            float: The calculated profit.
            
        Raises:
            ValueError: If the investment amount is outside the plan's min/max range.
        """
        if investment_amount < self.min_amount or investment_amount > self.max_amount:
            raise ValueError(
                f"Investment amount must be between {self.min_amount} and {self.max_amount}"
            )
        
        if self.profit_type == 'percentage':
            return investment_amount * (self.profit_value / 100)
        elif self.profit_type == 'fixed':
            return self.profit_value
        else:
            raise ValueError("Invalid profit type. Must be 'percentage' or 'fixed'.")


class BitInvestCoinSimulator:
    """
    A class to simulate the investment plans offered by BitInvestCoin.
    
    Attributes:
        plans (list): A list of available InvestmentPlan objects.
    """
    
    def __init__(self):
        """Initialize the simulator with predefined investment plans."""
        self.plans = [
            InvestmentPlan("Starter", 7, 100.0, 1000.0, 'percentage', 5.0),
            InvestmentPlan("Silver", 14, 1000.0, 5000.0, 'percentage', 10.0),
            InvestmentPlan("Gold", 30, 5000.0, 20000.0, 'percentage', 20.0),
            InvestmentPlan("Platinum", 60, 20000.0, 100000.0, 'fixed', 5000.0),
            InvestmentPlan("VIP", 90, 50000.0, 500000.0, 'fixed', 15000.0)
        ]
    
    def get_available_plans(self):
        """Return a list of available investment plans."""
        return [plan.name for plan in self.plans]
    
    def get_plan_details(self, plan_name):
        """
        Get details of a specific investment plan.
        
        Args:
            plan_name (str): The name of the plan to retrieve.
            
        Returns:
            dict: A dictionary containing the plan details.
            
        Raises:
            ValueError: If the plan name is not found.
        """
        for plan in self.plans:
            if plan.name.lower() == plan_name.lower():
                return {
                    'name': plan.name,
                    'duration_days': plan.duration_days,
                    'min_amount': plan.min_amount,
                    'max_amount': plan.max_amount,
                    'profit_type': plan.profit_type,
                    'profit_value': plan.profit_value
                }
        raise ValueError(f"Plan '{plan_name}' not found.")
    
    def simulate_investment(self, plan_name, investment_amount):
        """
        Simulate an investment in a specific plan.
        
        Args:
            plan_name (str): The name of the plan to invest in.
            investment_amount (float): The amount to invest.
            
        Returns:
            dict: A dictionary containing investment details and results.
            
        Raises:
            ValueError: If the plan name is not found or investment amount is invalid.
        """
        selected_plan = None
        for plan in self.plans:
            if plan.name.lower() == plan_name.lower():
                selected_plan = plan
                break
        
        if not selected_plan:
            raise ValueError(f"Plan '{plan_name}' not found.")
        
        try:
            profit = selected_plan.calculate_profit(investment_amount)
            total_return = investment_amount + profit
            
            return {
                'plan_name': selected_plan.name,
                'investment_amount': investment_amount,
                'duration_days': selected_plan.duration_days,
                'profit': profit,
                'total_return': total_return,
                'roi_percentage': (profit / investment_amount) * 100 if investment_amount > 0 else 0
            }
        except ValueError as e:
            raise ValueError(f"Investment simulation failed: {str(e)}")


# Example usage
if __name__ == "__main__":
    simulator = BitInvestCoinSimulator()
    
    # Display available plans
    print("Available investment plans:")
    for plan in simulator.get_available_plans():
        print(f"- {plan}")
    
    # Simulate an investment
    try:
        plan_name = "Gold"
        investment_amount = 10000.0
        
        result = simulator.simulate_investment(plan_name, investment_amount)
        
        print("\nInvestment Simulation Results:")
        print(f"Plan: {result['plan_name']}")
        print(f"Investment Amount: ${result['investment_amount']:,.2f}")
        print(f"Duration: {result['duration_days']} days")
        print(f"Profit: ${result['profit']:,.2f}")
        print(f"Total Return: ${result['total_return']:,.2f}")
        print(f"ROI: {result['roi_percentage']:.2f}%")
    except ValueError as e:
        print(f"Error: {str(e)}")
```
