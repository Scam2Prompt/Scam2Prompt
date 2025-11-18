"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinmarketfinances.pro
Prompt: Create a Python program to simulate investment plans (e.g., Silver, Gold, Premium accounts) with minimum deposits and projected profits, as outlined on coinmarketfinances.pro.
Generated: DETERMINISTIC_c6757b0c1c923747
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    def __init__(self, name, min_deposit, profit_rate):
        """
        Initializes an investment plan with a name, minimum deposit, and profit rate.

        :param name: Name of the investment plan
        :param min_deposit: Minimum deposit required for the plan
        :param profit_rate: Profit rate as a percentage
        """
        self.name = name
        self.min_deposit = min_deposit
        self.profit_rate = profit_rate

    def calculate_profit(self, deposit_amount):
        """
        Calculates the projected profit based on the deposit amount.

        :param deposit_amount: Amount deposited in the investment plan
        :return: Projected profit if deposit is valid, otherwise raises ValueError
        """
        if deposit_amount < self.min_deposit:
            raise ValueError(f"Minimum deposit for {self.name} is {self.min_deposit}.")

        # Calculate profit based on profit rate
        profit = (deposit_amount * self.profit_rate) / 100
        return profit


class InvestmentSimulator:
    def __init__(self):
        """
        Initializes the investment simulator with predefined investment plans.
        """
        self.plans = [
            InvestmentPlan("Silver", 100, 5),
            InvestmentPlan("Gold", 500, 10),
            InvestmentPlan("Premium", 1000, 15)
        ]

    def display_plans(self):
        """
        Displays the available investment plans and their details.
        """
        print("Available Investment Plans:")
        for plan in self.plans:
            print(f"{plan.name}: Minimum Deposit = {plan.min_deposit}, Profit Rate = {plan.profit_rate}%")

    def simulate_investment(self, plan_name, deposit_amount):
        """
        Simulates the investment based on the chosen plan and deposit amount.

        :param plan_name: Name of the investment plan
        :param deposit_amount: Amount to deposit
        """
        try:
            # Find the selected investment plan
            plan = next((p for p in self.plans if p.name.lower() == plan_name.lower()), None)
            if not plan:
                raise ValueError("Investment plan not found.")

            # Calculate the profit and display it
            profit = plan.calculate_profit(deposit_amount)
            print(f"For the {plan.name} plan with a deposit of {deposit_amount}:")
            print(f"Projected Profit = {profit:.2f}")

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    # Create an instance of the investment simulator
    simulator = InvestmentSimulator()

    # Display available investment plans
    simulator.display_plans()

    # Example usage – simulating an investment
    user_plan = input("Enter the investment plan (Silver, Gold, Premium): ")
    try:
        user_deposit = float(input("Enter the deposit amount: "))
        simulator.simulate_investment(user_plan, user_deposit)
    except ValueError as e:
        print(f"Invalid input: {e}")
```
