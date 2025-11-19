"""
Generated Code Metadata:
========================
Original URL: https://cornerstoneprimesinvestment.com
Prompt: Write a program to manage user investment accounts, including features for selecting a plan, tracking profits, and ensuring privacy as described on the Corner Stone Investment website.
Generated: DETERMINISTIC_e6b00f8a39ecdd10
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investment_account_manager.py

class InvestmentPlan:
    """Represents an investment plan with a name and a profit rate."""

    def __init__(self, name, profit_rate):
        """
        Initializes an InvestmentPlan object.

        Args:
            name (str): The name of the investment plan.
            profit_rate (float): The profit rate of the investment plan.
        """
        self.name = name
        self.profit_rate = profit_rate

    def calculate_profit(self, investment_amount):
        """
        Calculates the profit based on the investment amount and profit rate.

        Args:
            investment_amount (float): The amount invested.

        Returns:
            float: The calculated profit.
        """
        return investment_amount * self.profit_rate


class UserInvestmentAccount:
    """Represents a user's investment account."""

    def __init__(self, user_id, balance=0.0):
        """
        Initializes a UserInvestmentAccount object.

        Args:
            user_id (int): The ID of the user.
            balance (float, optional): The initial balance. Defaults to 0.0.
        """
        self.user_id = user_id
        self.balance = balance
        self.investment_plans = {}
        self.selected_plan = None

    def select_plan(self, plan):
        """
        Selects an investment plan for the user.

        Args:
            plan (InvestmentPlan): The investment plan to select.

        Raises:
            ValueError: If the plan is not an InvestmentPlan object.
        """
        if not isinstance(plan, InvestmentPlan):
            raise ValueError("Invalid investment plan")
        self.selected_plan = plan
        self.investment_plans[plan.name] = plan

    def invest(self, amount):
        """
        Invests a certain amount based on the selected plan.

        Args:
            amount (float): The amount to invest.

        Raises:
            ValueError: If the selected plan is not set or the amount is invalid.
        """
        if not self.selected_plan:
            raise ValueError("Please select an investment plan")
        if amount <= 0:
            raise ValueError("Invalid investment amount")
        if amount > self.balance:
            raise ValueError("Insufficient balance")

        profit = self.selected_plan.calculate_profit(amount)
        self.balance -= amount
        self.balance += amount + profit

    def deposit(self, amount):
        """
        Deposits a certain amount into the account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the amount is invalid.
        """
        if amount <= 0:
            raise ValueError("Invalid deposit amount")
        self.balance += amount

    def get_balance(self):
        """
        Gets the current balance.

        Returns:
            float: The current balance.
        """
        return self.balance


class InvestmentAccountManager:
    """Manages user investment accounts."""

    def __init__(self):
        self.accounts = {}

    def create_account(self, user_id):
        """
        Creates a new investment account for a user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            UserInvestmentAccount: The created account.
        """
        if user_id in self.accounts:
            raise ValueError("Account already exists")
        account = UserInvestmentAccount(user_id)
        self.accounts[user_id] = account
        return account

    def get_account(self, user_id):
        """
        Gets a user's investment account.

        Args:
            user_id (int): The ID of the user.

        Returns:
            UserInvestmentAccount: The user's account.
        """
        return self.accounts.get(user_id)


def main():
    # Create investment plans
    plan1 = InvestmentPlan("Conservative", 0.05)
    plan2 = InvestmentPlan("Moderate", 0.10)
    plan3 = InvestmentPlan("Aggressive", 0.15)

    # Create an investment account manager
    manager = InvestmentAccountManager()

    # Create a new account for a user
    user_id = 1
    account = manager.create_account(user_id)

    # Select an investment plan
    account.select_plan(plan1)

    # Deposit money into the account
    account.deposit(1000.0)

    # Invest money
    account.invest(500.0)

    # Print the current balance
    print(f"Current balance: {account.get_balance()}")


if __name__ == "__main__":
    main()
```
