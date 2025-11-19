"""
Generated Code Metadata:
========================
Original URL: https://metlifeinvests.com
Prompt: Generate a Python script that calculates daily profits based on investment plans from MET LIFE INVESTS, including the daily profit and total profit for each plan.
Generated: DETERMINISTIC_cf9433276afe3793
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Union

class METLifeInvestsProfitCalculator:
    """
    A class to calculate daily and total profits for investment plans from MET LIFE INVESTS.
    
    Attributes:
        plans (Dict[str, Dict[str, Union[float, int]]]): A dictionary containing investment plans.
    """
    
    def __init__(self, plans_config: Dict[str, Dict[str, Union[float, int]]] = None):
        """
        Initializes the profit calculator with investment plans.
        
        Args:
            plans_config (Dict[str, Dict[str, Union[float, int]]], optional): 
                A dictionary containing investment plans. Defaults to None.
                Example:
                {
                    "Plan A": {"daily_rate": 0.05, "duration_days": 30},
                    "Plan B": {"daily_rate": 0.07, "duration_days": 15}
                }
        """
        if plans_config is None:
            self.plans = {
                "Plan A": {"daily_rate": 0.05, "duration_days": 30},
                "Plan B": {"daily_rate": 0.07, "duration_days": 15},
                "Plan C": {"daily_rate": 0.10, "duration_days": 10}
            }
        else:
            self.plans = plans_config
    
    def calculate_daily_profit(self, plan_name: str, investment_amount: float) -> float:
        """
        Calculates the daily profit for a given investment plan.
        
        Args:
            plan_name (str): The name of the investment plan.
            investment_amount (float): The amount invested.
            
        Returns:
            float: The daily profit.
            
        Raises:
            ValueError: If the plan name is invalid or investment amount is non-positive.
        """
        if investment_amount <= 0:
            raise ValueError("Investment amount must be positive.")
        
        plan = self.plans.get(plan_name)
        if not plan:
            raise ValueError(f"Invalid plan name: {plan_name}. Available plans: {list(self.plans.keys())}")
        
        daily_rate = plan["daily_rate"]
        return investment_amount * daily_rate
    
    def calculate_total_profit(self, plan_name: str, investment_amount: float) -> float:
        """
        Calculates the total profit for a given investment plan over its duration.
        
        Args:
            plan_name (str): The name of the investment plan.
            investment_amount (float): The amount invested.
            
        Returns:
            float: The total profit over the plan's duration.
            
        Raises:
            ValueError: If the plan name is invalid or investment amount is non-positive.
        """
        if investment_amount <= 0:
            raise ValueError("Investment amount must be positive.")
        
        plan = self.plans.get(plan_name)
        if not plan:
            raise ValueError(f"Invalid plan name: {plan_name}. Available plans: {list(self.plans.keys())}")
        
        daily_rate = plan["daily_rate"]
        duration_days = plan["duration_days"]
        return investment_amount * daily_rate * duration_days
    
    def calculate_profits_for_all_plans(self, investment_amount: float) -> Dict[str, Dict[str, float]]:
        """
        Calculates daily and total profits for all available investment plans.
        
        Args:
            investment_amount (float): The amount invested.
            
        Returns:
            Dict[str, Dict[str, float]]: A dictionary containing daily and total profits for each plan.
            
        Raises:
            ValueError: If the investment amount is non-positive.
        """
        if investment_amount <= 0:
            raise ValueError("Investment amount must be positive.")
        
        results = {}
        for plan_name in self.plans:
            daily_profit = self.calculate_daily_profit(plan_name, investment_amount)
            total_profit = self.calculate_total_profit(plan_name, investment_amount)
            results[plan_name] = {
                "daily_profit": round(daily_profit, 2),
                "total_profit": round(total_profit, 2)
            }
        return results
    
    def save_results_to_json(self, results: Dict[str, Dict[str, float]], file_path: str) -> None:
        """
        Saves the profit calculation results to a JSON file.
        
        Args:
            results (Dict[str, Dict[str, float]]): The results to save.
            file_path (str): The path to the JSON file.
            
        Raises:
            IOError: If there is an issue writing to the file.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(results, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save results to {file_path}: {e}")


# Example usage
if __name__ == "__main__":
    try:
        calculator = METLifeInvestsProfitCalculator()
        investment_amount = 1000.0  # Example investment amount
        
        # Calculate profits for all plans
        results = calculator.calculate_profits_for_all_plans(investment_amount)
        print("Profit Calculations:")
        for plan, profits in results.items():
            print(f"{plan}: Daily Profit: ${profits['daily_profit']}, Total Profit: ${profits['total_profit']}")
        
        # Save results to JSON file
        calculator.save_results_to_json(results, "profit_calculations.json")
        print("Results saved to 'profit_calculations.json'")
    
    except ValueError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"Error: {e}")
```
