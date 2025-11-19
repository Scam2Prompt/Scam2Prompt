"""
Generated Code Metadata:
========================
Original URL: https://metamaskcoins.com
Prompt: Write Python code to calculate the expected profit for a cryptocurrency investment based on Meta Mask Coins' trading plans (e.g., Silver, Gold, Diamond) using the given trade duration and profit percentages.
Generated: DETERMINISTIC_3a1d4f32c9f45427
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MetaMaskCoinInvestment:
    """
    A class to calculate expected profit for MetaMask Coins' trading plans.
    """
    
    def __init__(self):
        """
        Initialize the trading plans with their respective profit percentages.
        """
        self.trading_plans = {
            'Silver': {'daily': 0.02, 'weekly': 0.15, 'monthly': 0.65},
            'Gold': {'daily': 0.03, 'weekly': 0.20, 'monthly': 0.85},
            'Diamond': {'daily': 0.05, 'weekly': 0.35, 'monthly': 1.50}
        }
    
    def calculate_profit(self, plan: str, duration: str, investment: float) -> float:
        """
        Calculate the expected profit based on the selected plan, duration, and investment amount.
        
        Args:
            plan (str): The trading plan (Silver, Gold, Diamond)
            duration (str): The investment duration (daily, weekly, monthly)
            investment (float): The initial investment amount
            
        Returns:
            float: The expected profit
            
        Raises:
            ValueError: If the plan or duration is invalid
        """
        try:
            plan_data = self.trading_plans[plan]
        except KeyError:
            raise ValueError(f"Invalid plan. Available plans: {list(self.trading_plans.keys())}")
        
        try:
            profit_percentage = plan_data[duration]
        except KeyError:
            raise ValueError(f"Invalid duration. Available durations: {list(plan_data.keys())}")
        
        if investment <= 0:
            raise ValueError("Investment amount must be positive")
            
        return investment * profit_percentage


# Example usage
if __name__ == "__main__":
    calculator = MetaMaskCoinInvestment()
    
    try:
        plan = "Gold"
        duration = "weekly"
        investment = 1000.0
        
        profit = calculator.calculate_profit(plan, duration, investment)
        print(f"Expected profit for {plan} plan ({duration}): ${profit:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
