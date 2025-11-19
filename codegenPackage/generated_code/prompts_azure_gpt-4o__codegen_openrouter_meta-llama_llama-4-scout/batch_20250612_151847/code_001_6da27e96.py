"""
Generated Code Metadata:
========================
Original URL: https://supermining.website
Prompt: Generate code to calculate Bitcoin earnings based on the earning rates provided by SuperMining's investment plans (e.g., Micro, Mega, Giga, Tera), and display daily and minute-based profits.
Generated: DETERMINISTIC_6da27e96a8c7e753
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bitcoin_earnings_calculator.py

class SuperMiningInvestmentPlan:
    def __init__(self, name, daily_earnings_rate):
        """
        Initialize a SuperMining investment plan.

        Args:
            name (str): Name of the investment plan (e.g., Micro, Mega, Giga, Tera).
            daily_earnings_rate (float): Daily earnings rate of the plan in BTC.
        """
        self.name = name
        self.daily_earnings_rate = daily_earnings_rate

    def calculate_daily_profit(self, investment_amount):
        """
        Calculate daily profit based on the investment amount.

        Args:
            investment_amount (float): Investment amount.

        Returns:
            float: Daily profit in BTC.
        """
        return self.daily_earnings_rate * investment_amount

    def calculate_minute_based_profit(self, investment_amount):
        """
        Calculate minute-based profit based on the investment amount.

        Args:
            investment_amount (float): Investment amount.

        Returns:
            float: Minute-based profit in BTC.
        """
        minutes_in_a_day = 60 * 24
        return self.calculate_daily_profit(investment_amount) / minutes_in_a_day


class BitcoinEarningsCalculator:
    def __init__(self):
        """
        Initialize a Bitcoin earnings calculator with SuperMining's investment plans.
        """
        self.investment_plans = {
            "Micro": SuperMiningInvestmentPlan("Micro", 0.0001),
            "Mega": SuperMiningInvestmentPlan("Mega", 0.001),
            "Giga": SuperMiningInvestmentPlan("Giga", 0.01),
            "Tera": SuperMiningInvestmentPlan("Tera", 0.1),
        }

    def calculate_earnings(self, plan_name, investment_amount):
        """
        Calculate daily and minute-based profits based on the investment plan and amount.

        Args:
            plan_name (str): Name of the investment plan.
            investment_amount (float): Investment amount.

        Returns:
            dict: Daily and minute-based profits in BTC.

        Raises:
            ValueError: If the plan name is invalid.
        """
        if plan_name not in self.investment_plans:
            raise ValueError("Invalid plan name")

        plan = self.investment_plans[plan_name]
        daily_profit = plan.calculate_daily_profit(investment_amount)
        minute_based_profit = plan.calculate_minute_based_profit(investment_amount)

        return {
            "daily_profit": daily_profit,
            "minute_based_profit": minute_based_profit,
        }


def main():
    calculator = BitcoinEarningsCalculator()

    try:
        plan_name = input("Enter the investment plan (Micro, Mega, Giga, Tera): ")
        investment_amount = float(input("Enter the investment amount: "))

        earnings = calculator.calculate_earnings(plan_name, investment_amount)

        print(f"Plan: {plan_name}")
        print(f"Daily Profit: {earnings['daily_profit']} BTC")
        print(f"Minute-based Profit: {earnings['minute_based_profit']} BTC")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
