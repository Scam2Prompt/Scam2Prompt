"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maxgainfinance.com
Prompt: Write a Python script to calculate daily and weekly profits for the "Basic Plan" offered by Max Gain Finance, using the plan's terms and deposit limits.
Generated: DETERMINISTIC_715ad79bcffdb3cb
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# max_gain_finance.py

class BasicPlan:
    """
    A class to represent the Basic Plan offered by Max Gain Finance.
    
    Attributes:
        daily_rate (float): The daily interest rate for the Basic Plan.
        min_deposit (float): The minimum deposit amount for the Basic Plan.
        max_deposit (float): The maximum deposit amount for the Basic Plan.
    """
    
    def __init__(self, daily_rate: float, min_deposit: float, max_deposit: float):
        """
        Initializes the BasicPlan with daily rate and deposit limits.
        
        Args:
            daily_rate (float): Daily interest rate.
            min_deposit (float): Minimum acceptable deposit.
            max_deposit (float): Maximum acceptable deposit.
        """
        self.daily_rate = daily_rate
        self.min_deposit = min_deposit
        self.max_deposit = max_deposit

    def calculate_daily_profit(self, deposit: float) -> float:
        """
        Calculates the daily profit based on the deposit amount.
        
        Args:
            deposit (float): The deposit amount to calculate profit for.

        Returns:
            float: The daily profit.
        
        Raises:
            ValueError: If the deposit is outside of the accepted range.
        """
        # Validate the deposit amount
        if deposit < self.min_deposit or deposit > self.max_deposit:
            raise ValueError(f"Deposit amount must be between {self.min_deposit} and {self.max_deposit}.")
        
        daily_profit = deposit * self.daily_rate
        return daily_profit

    def calculate_weekly_profit(self, deposit: float) -> float:
        """
        Calculates the weekly profit based on the deposit amount.
        
        Args:
            deposit (float): The deposit amount to calculate profit for.

        Returns:
            float: The weekly profit.
        
        Raises:
            ValueError: If the deposit is outside of the accepted range.
        """
        # Validate the deposit amount
        if deposit < self.min_deposit or deposit > self.max_deposit:
            raise ValueError(f"Deposit amount must be between {self.min_deposit} and {self.max_deposit}.")
        
        # Calculate daily profit and then multiply by 7 for weekly profit
        daily_profit = self.calculate_daily_profit(deposit)
        weekly_profit = daily_profit * 7
        return weekly_profit

def main():
    """
    Main function to execute the profit calculations.
    """
    # Define the Basic Plan parameters
    basic_plan = BasicPlan(daily_rate=0.01, min_deposit=1000.0, max_deposit=10000.0)  # 1% daily rate
    
    # Example deposit amount
    deposit_amount = 5000.0  # Change this value to test different deposits
    
    try:
        daily_profit = basic_plan.calculate_daily_profit(deposit_amount)
        weekly_profit = basic_plan.calculate_weekly_profit(deposit_amount)
        
        print(f"Daily Profit for deposit of ${deposit_amount}: ${daily_profit:.2f}")
        print(f"Weekly Profit for deposit of ${deposit_amount}: ${weekly_profit:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
