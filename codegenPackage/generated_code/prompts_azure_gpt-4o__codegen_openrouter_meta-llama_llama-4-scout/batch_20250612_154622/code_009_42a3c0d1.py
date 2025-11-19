"""
Generated Code Metadata:
========================
Original URL: https://syncexperttrade.com
Prompt: Write a Python script to automate investment planning based on SyncExpertTrade's account tiers (Bronze, Silver, Gold, Premium) and their respective profit margins.
Generated: DETERMINISTIC_42a3c0d16c6af8e3
Batch ID: 20250612_154622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investment_planner.py

class InvestmentPlanner:
    """
    Automates investment planning based on SyncExpertTrade's account tiers.
    """

    def __init__(self):
        # Define account tiers and their respective profit margins
        self.account_tiers = {
            "Bronze": 0.02,  # 2% profit margin
            "Silver": 0.05,  # 5% profit margin
            "Gold": 0.10,    # 10% profit margin
            "Premium": 0.20  # 20% profit margin
        }

    def calculate_investment(self, account_tier, investment_amount):
        """
        Calculates the profit based on the account tier and investment amount.

        Args:
            account_tier (str): The account tier (Bronze, Silver, Gold, Premium)
            investment_amount (float): The investment amount

        Returns:
            float: The calculated profit
        """
        if account_tier not in self.account_tiers:
            raise ValueError("Invalid account tier")

        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero")

        profit_margin = self.account_tiers[account_tier]
        profit = investment_amount * profit_margin
        return profit

    def plan_investment(self, account_tier, investment_amount, risk_tolerance):
        """
        Generates an investment plan based on the account tier, investment amount, and risk tolerance.

        Args:
            account_tier (str): The account tier (Bronze, Silver, Gold, Premium)
            investment_amount (float): The investment amount
            risk_tolerance (str): The risk tolerance (Low, Medium, High)

        Returns:
            dict: The investment plan
        """
        try:
            profit = self.calculate_investment(account_tier, investment_amount)
            investment_plan = {
                "account_tier": account_tier,
                "investment_amount": investment_amount,
                "risk_tolerance": risk_tolerance,
                "profit": profit
            }
            return investment_plan
        except ValueError as e:
            print(f"Error: {e}")
            return None


def main():
    planner = InvestmentPlanner()

    # Example usage
    account_tier = "Gold"
    investment_amount = 10000.0
    risk_tolerance = "Medium"

    investment_plan = planner.plan_investment(account_tier, investment_amount, risk_tolerance)

    if investment_plan:
        print("Investment Plan:")
        for key, value in investment_plan.items():
            print(f"{key.capitalize().replace('_', ' ')}: {value}")


if __name__ == "__main__":
    main()
```
