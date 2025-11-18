"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinexchainltd.com
Prompt: Generate code to calculate daily earnings based on the trading plans offered by Coinex Chain Trading Company Ltd, including the ROOKIE PLAN and MASTER PLAN.
Generated: DETERMINISTIC_38552f6c1b643d57
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradingPlan:
    """
    Base class for trading plans. This class defines the interface and common 
    functionalities of trading plans.
    """
    def __init__(self, name, daily_rate):
        """
        Initializes a TradingPlan instance.
        
        :param name: Name of the trading plan
        :param daily_rate: Daily return rate as a decimal (e.g., 0.05 for 5%)
        """
        self.name = name
        self.daily_rate = daily_rate

    def calculate_daily_earnings(self, investment_amount):
        """
        Calculates the daily earnings based on the investment amount.
        
        :param investment_amount: The amount invested in the trading plan
        :return: Daily earnings calculated from the investment
        """
        if investment_amount < 0:
            raise ValueError("Investment amount must be non-negative.")
        return investment_amount * self.daily_rate


class RookiePlan(TradingPlan):
    """
    Class representing the ROOKIE PLAN with specific daily earning rate.
    """
    def __init__(self):
        super().__init__("Rookie Plan", 0.02)  # 2% daily rate


class MasterPlan(TradingPlan):
    """
    Class representing the MASTER PLAN with specific daily earning rate.
    """
    def __init__(self):
        super().__init__("Master Plan", 0.05)  # 5% daily rate


def main():
    """
    Main function to demonstrate the calculation of daily earnings from different trading plans.
    """
    # Investment amounts for testing
    investment_amounts = [1000, 5000, 10000]

    # Instantiate trading plans
    rookie_plan = RookiePlan()
    master_plan = MasterPlan()

    # Output daily earnings for each plan
    for amount in investment_amounts:
        try:
            rookie_earnings = rookie_plan.calculate_daily_earnings(amount)
            master_earnings = master_plan.calculate_daily_earnings(amount)
            print(f"Investment: ${amount:.2f} -> Rookie Earnings: ${rookie_earnings:.2f}, Master Earnings: ${master_earnings:.2f}")
        except ValueError as e:
            print(f"Error calculating earnings for amount ${amount}: {e}")


if __name__ == "__main__":
    main()
```
