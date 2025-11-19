"""
Generated Code Metadata:
========================
Original URL: https://crptominer.com
Prompt: Generate a Python script that calculates potential returns based on the investment plans offered by CrptoMiner, including the Starter, Gold, Standard, and Platinum plans.
Generated: DETERMINISTIC_c9ef82c862425339
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# crypto_miner_investment_calculator.py

class CryptoMinerInvestmentPlan:
    def __init__(self, name, investment_amount, daily_return_rate, contract_duration_days):
        """
        Initialize a CryptoMiner investment plan.

        Args:
        - name (str): Name of the plan.
        - investment_amount (float): Initial investment amount.
        - daily_return_rate (float): Daily return rate as a decimal.
        - contract_duration_days (int): Contract duration in days.
        """
        self.name = name
        self.investment_amount = investment_amount
        self.daily_return_rate = daily_return_rate
        self.contract_duration_days = contract_duration_days

    def calculate_total_return(self):
        """
        Calculate the total return based on the investment plan.

        Returns:
        - float: Total return.
        """
        total_return = self.investment_amount * (1 + self.daily_return_rate) ** self.contract_duration_days
        return total_return

    def calculate_daily_returns(self):
        """
        Calculate daily returns for the contract duration.

        Returns:
        - list[float]: Daily returns.
        """
        daily_returns = [self.investment_amount * (1 + self.daily_return_rate) ** day for day in range(1, self.contract_duration_days + 1)]
        return daily_returns


class CryptoMiner:
    def __init__(self):
        """
        Initialize CryptoMiner with available investment plans.
        """
        self.plans = {
            "Starter": CryptoMinerInvestmentPlan("Starter", 100, 0.01, 30),
            "Gold": CryptoMinerInvestmentPlan("Gold", 500, 0.02, 60),
            "Standard": CryptoMinerInvestmentPlan("Standard", 1000, 0.03, 90),
            "Platinum": CryptoMinerInvestmentPlan("Platinum", 5000, 0.05, 180),
        }

    def get_plan(self, plan_name):
        """
        Get a specific investment plan by name.

        Args:
        - plan_name (str): Name of the plan.

        Returns:
        - CryptoMinerInvestmentPlan: Investment plan.

        Raises:
        - ValueError: If the plan does not exist.
        """
        try:
            return self.plans[plan_name]
        except KeyError:
            raise ValueError(f"Invalid plan name: {plan_name}")

    def list_plans(self):
        """
        List available investment plans.

        Returns:
        - dict[str, CryptoMinerInvestmentPlan]: Available plans.
        """
        return self.plans


def main():
    crypto_miner = CryptoMiner()

    print("Available plans:")
    for plan_name, plan in crypto_miner.list_plans().items():
        print(f"- {plan_name}")

    plan_name = input("Enter the plan name: ")
    try:
        plan = crypto_miner.get_plan(plan_name)
        total_return = plan.calculate_total_return()
        daily_returns = plan.calculate_daily_returns()

        print(f"\nPlan: {plan.name}")
        print(f"Total Return: ${total_return:.2f}")
        print("Daily Returns:")
        for day, daily_return in enumerate(daily_returns, start=1):
            print(f"Day {day}: ${daily_return:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
