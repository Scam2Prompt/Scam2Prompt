"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerspluslimited.com
Prompt: Write a program to simulate the profit and principle return for the "VIP Leader Special Trading and NFTC Plan" offered by minerspluslimited.com, which provides 15% daily profit for 2 months with a minimum deposit of $200,000.
Generated: DETERMINISTIC_edcfddc84d2a15c6
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class VipLeaderSpecialTradingPlan:
    """
    A class to simulate the profit and principal return for the VIP Leader Special Trading and NFTC Plan.
    
    Attributes:
        initial_investment (float): The amount of money invested.
        daily_profit_rate (float): Daily profit rate as a decimal.
        total_days (int): Total duration of the investment in days.
    """

    def __init__(self, initial_investment: float):
        """
        Initializes the investment plan with the given initial investment.
        
        Args:
            initial_investment (float): The amount of money invested.
        
        Raises:
            ValueError: If the initial investment is less than the minimum deposit.
        """
        self.minimum_deposit = 200000.0
        self.daily_profit_rate = 0.15  # 15%
        self.total_days = 60  # 2 months

        if initial_investment < self.minimum_deposit:
            raise ValueError(f"Initial investment must be at least ${self.minimum_deposit:.2f}.")

        self.initial_investment = initial_investment

    def calculate_total_profit(self) -> float:
        """
        Calculates the total profit over the investment period.
        
        Returns:
            float: Total profit earned over the investment period.
        """
        total_profit = self.initial_investment * self.daily_profit_rate * self.total_days
        return total_profit

    def calculate_total_return(self) -> float:
        """
        Calculates the total return, including principal and profit.
        
        Returns:
            float: Total return after the investment period.
        """
        total_profit = self.calculate_total_profit()
        total_return = self.initial_investment + total_profit
        return total_return

    def display_investment_summary(self):
        """
        Displays a summary of the investment, including principal, total profit, and total return.
        """
        try:
            total_profit = self.calculate_total_profit()
            total_return = self.calculate_total_return()

            print(f"--- Investment Summary ---")
            print(f"Initial Investment: ${self.initial_investment:.2f}")
            print(f"Total Profit: ${total_profit:.2f}")
            print(f"Total Return: ${total_return:.2f}")
            print("-------------------------")
        except Exception as e:
            print("An error occurred while calculating the investment summary:", e)


if __name__ == "__main__":
    try:
        # Example usage
        investment_amount = 250000.0  # User-defined investment amount
        plan = VipLeaderSpecialTradingPlan(investment_amount)
        plan.display_investment_summary()
    except ValueError as ve:
        print("Value Error:", ve)
    except Exception as e:
        print("An unexpected error occurred:", e)
```
