"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://advancecryptoacademy.online
Prompt: Write Python code to calculate daily profits based on the investment plans (VIP CROWN, DIAMOND, GOLD, SILVER) provided by Advance Crypto Academy. Include logic for minimum and maximum investment amounts.
Generated: DETERMINISTIC_728b9c5f19b77802
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to handle errors and debug information
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class InvestmentPlan:
    """
    A class to represent an investment plan and calculate the daily profit.
    """
    def __init__(self, name, min_investment, max_investment, daily_rate):
        """
        Initialize an investment plan instance.

        :param name: Name of the investment plan
        :param min_investment: Minimum investment amount allowed
        :param max_investment: Maximum investment amount allowed
        :param daily_rate: Daily profit rate (percentage in decimal form, e.g., 0.05 for 5%)
        """
        self.name = name
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.daily_rate = daily_rate

    def calculate_profit(self, amount):
        """
        Calculate daily profit based on the investment amount.

        :param amount: Investment amount
        :return: Daily profit amount
        """
        if amount < self.min_investment or amount > self.max_investment:
            raise ValueError(
                f"Investment amount for {self.name} plan must be between {self.min_investment} and {self.max_investment}."
            )
        return amount * self.daily_rate


def main():
    # Define investment plans with their respective minimum, maximum, and daily profit rates
    plans = {
        "VIP CROWN": InvestmentPlan("VIP CROWN", 10000, 50000, 0.1),
        "DIAMOND": InvestmentPlan("DIAMOND", 5000, 9999, 0.08),
        "GOLD": InvestmentPlan("GOLD", 1000, 4999, 0.05),
        "SILVER": InvestmentPlan("SILVER", 500, 999, 0.03),
    }

    try:
        # Sample user input for investment plan and amount
        user_plan = "DIAMOND"
        user_amount = 7500

        if user_plan not in plans:
            raise ValueError(f"Invalid investment plan selected: {user_plan}. Please choose from {list(plans.keys())}.")

        # Retrieve the selected plan and calculate profit
        selected_plan = plans[user_plan]
        daily_profit = selected_plan.calculate_profit(user_amount)

        # Display the results
        print(f"Investment Plan: {selected_plan.name}")
        print(f"Investment Amount: ${user_amount}")
        print(f"Daily Profit: ${daily_profit:.2f}")

    except ValueError as e:
        logging.error(e)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
