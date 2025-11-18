"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supermining.website
Prompt: Generate code to calculate Bitcoin earnings based on the earning rates provided by SuperMining's investment plans (e.g., Micro, Mega, Giga, Tera), and display daily and minute-based profits.
Generated: DETERMINISTIC_6da27e96a8c7e753
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BitcoinEarningsCalculator:
    """
    A class to calculate Bitcoin earnings based on investment plans.
    """

    # Investment plans with their respective earning rates (in percentage).
    INVESTMENT_PLANS = {
        'Micro': 0.1,  # Daily earning percentage for Micro plan
        'Mega': 0.3,   # Daily earning percentage for Mega plan
        'Giga': 0.5,   # Daily earning percentage for Giga plan
        'Tera': 1.0    # Daily earning percentage for Tera plan
    }

    def __init__(self, investment_amount: float, plan: str):
        """
        Initializes the BitcoinEarningsCalculator with the investment amount and plan.
        
        :param investment_amount: The amount of investment in Bitcoin.
        :param plan: The investment plan ('Micro', 'Mega', 'Giga', 'Tera').
        """
        self.investment_amount = investment_amount
        self.plan = plan

        # Validate the investment plan
        if plan not in self.INVESTMENT_PLANS:
            raise ValueError("Invalid investment plan. Choose from: Micro, Mega, Giga, Tera")

    def daily_profit(self) -> float:
        """
        Calculates the daily profit based on the investment amount and selected plan.
        
        :return: Daily profit in Bitcoin.
        """
        rate = self.INVESTMENT_PLANS[self.plan]
        daily_profit = self.investment_amount * (rate / 100)
        return daily_profit

    def minute_profit(self) -> float:
        """
        Calculates the profit per minute based on the daily profit.
        
        :return: Profit in Bitcoin per minute.
        """
        daily_profit = self.daily_profit()
        minute_profit = daily_profit / (24 * 60)  # 1440 minutes in a day
        return minute_profit

    def display_profits(self):
        """
        Displays the daily and minute-based profits.
        """
        try:
            daily = self.daily_profit()
            minute = self.minute_profit()
            print(f"Investment Plan: {self.plan}")
            print(f"Investment Amount: {self.investment_amount} BTC")
            print(f"Daily Profit: {daily:.8f} BTC")
            print(f"Minute Profit: {minute:.8f} BTC")
        except Exception as e:
            print(f"An error occurred: {e}")


# Example of usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with a specific investment amount and plan
        investment_amount = 1.0  # Example investment amount in BTC
        plan = 'Giga'  # Example plan

        calculator = BitcoinEarningsCalculator(investment_amount, plan)
        calculator.display_profits()
    except Exception as e:
        print(f"An error occurred during initialization: {e}")
```
