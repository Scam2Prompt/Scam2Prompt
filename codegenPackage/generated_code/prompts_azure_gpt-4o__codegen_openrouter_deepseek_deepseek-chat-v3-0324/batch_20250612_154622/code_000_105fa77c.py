"""
Generated Code Metadata:
========================
Original URL: https://tradetoearnoptions.com
Prompt: Write Python code to calculate investment returns using the profit calculator parameters from Tradetoearnoption, including interest rates and maturity periods for plans like BASIC, SILVER, and GOLD.
Generated: DETERMINISTIC_105fa77c31d88343
Batch ID: 20250612_154622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from enum import Enum
from typing import Dict, Optional, Union

class PlanType(Enum):
    """Enum representing the available investment plans."""
    BASIC = "BASIC"
    SILVER = "SILVER"
    GOLD = "GOLD"

class InvestmentCalculator:
    """
    A class to calculate investment returns based on different plans.
    
    Attributes:
        plan_rates (Dict[PlanType, Dict[str, Union[float, int]]]): A dictionary containing
            the interest rates and maturity periods for each plan.
    """
    
    def __init__(self):
        """Initialize the calculator with predefined plan parameters."""
        self.plan_rates = {
            PlanType.BASIC: {
                "interest_rate": 0.05,  # 5% per period
                "maturity_period": 30   # 30 days
            },
            PlanType.SILVER: {
                "interest_rate": 0.07,  # 7% per period
                "maturity_period": 60   # 60 days
            },
            PlanType.GOLD: {
                "interest_rate": 0.10,  # 10% per period
                "maturity_period": 90   # 90 days
            }
        }
    
    def calculate_return(
        self,
        principal: float,
        plan: PlanType,
        days_invested: Optional[int] = None
    ) -> float:
        """
        Calculate the investment return based on the plan and investment duration.
        
        Args:
            principal: The initial investment amount.
            plan: The investment plan (BASIC, SILVER, GOLD).
            days_invested: Optional; if provided, calculates return for the exact days.
                          If not provided, uses the plan's maturity period.
        
        Returns:
            The total return (principal + interest).
        
        Raises:
            ValueError: If principal is negative or days_invested is invalid.
        """
        if principal < 0:
            raise ValueError("Principal amount cannot be negative.")
        
        plan_params = self.plan_rates.get(plan)
        if not plan_params:
            raise ValueError(f"Invalid plan type: {plan}")
        
        interest_rate = plan_params["interest_rate"]
        maturity_period = plan_params["maturity_period"]
        
        if days_invested is None:
            days_invested = maturity_period
        elif days_invested <= 0:
            raise ValueError("Days invested must be a positive integer.")
        
        # Calculate the number of full periods and remaining days
        full_periods = days_invested // maturity_period
        remaining_days = days_invested % maturity_period
        
        # Calculate return for full periods
        total_return = principal * (1 + interest_rate) ** full_periods
        
        # Calculate return for remaining days (pro-rated)
        if remaining_days > 0:
            prorated_rate = interest_rate * (remaining_days / maturity_period)
            total_return *= (1 + prorated_rate)
        
        return round(total_return, 2)

# Example usage
if __name__ == "__main__":
    calculator = InvestmentCalculator()
    
    try:
        principal = 1000.0
        plan = PlanType.GOLD
        days = 90
        
        total_return = calculator.calculate_return(principal, plan, days)
        print(f"Invested: ${principal}, Plan: {plan.value}, Days: {days}")
        print(f"Total Return: ${total_return}")
    except ValueError as e:
        print(f"Error: {e}")
```
