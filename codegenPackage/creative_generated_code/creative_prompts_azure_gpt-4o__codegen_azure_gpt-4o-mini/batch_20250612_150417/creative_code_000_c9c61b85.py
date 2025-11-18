"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://longtradegroup.com
Prompt: Write Python code to calculate daily profits for a cryptocurrency staking plan based on the LongTradeGroup USD Plan, which offers 0.2% daily profit for 100 days. Include functionality to handle minimum and maximum investment limits ($25-$250).
Generated: DETERMINISTIC_c9c61b85b9f5dea1
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingPlan:
    """
    A class to represent a cryptocurrency staking plan.

    Attributes
    ----------
    min_investment : float
        The minimum investment amount.
    max_investment : float
        The maximum investment amount.
    daily_profit_rate : float
        Daily profit rate as a decimal.
    duration_days : int
        The duration of the staking plan in days.

    Methods
    -------
    calculate_daily_profit(investment):
        Calculates the daily profit based on the investment amount.
    """

    def __init__(self, min_investment=25.0, max_investment=250.0, daily_profit_rate=0.002, duration_days=100):
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.daily_profit_rate = daily_profit_rate
        self.duration_days = duration_days

    def calculate_daily_profit(self, investment):
        """
        Calculates the daily profit based on the investment amount.

        Parameters
        ----------
        investment : float
            The amount of money invested.

        Returns
        -------
        float
            The calculated daily profit.

        Raises
        ------
        ValueError
            If investment is less than min_investment or greater than max_investment.
        """
        if investment < self.min_investment:
            raise ValueError(f"Investment must be at least ${self.min_investment:.2f}.")
        if investment > self.max_investment:
            raise ValueError(f"Investment must not exceed ${self.max_investment:.2f}.")

        daily_profit = investment * self.daily_profit_rate
        return daily_profit

def main():
    """
    Main function to run the staking plan calculation.
    """
    try:
        # Get user input for investment amount
        investment = float(input("Enter your investment amount ($25 - $250): "))
        
        # Create an instance of the StakingPlan
        staking_plan = StakingPlan()
        
        # Calculate daily profit
        daily_profit = staking_plan.calculate_daily_profit(investment)
        
        # Display the result
        print(f"Daily Profit for an investment of ${investment:.2f}: ${daily_profit:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
