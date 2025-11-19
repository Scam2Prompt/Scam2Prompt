"""
Generated Code Metadata:
========================
Original URL: https://bitplusinvestment.com
Prompt: Develop a Python script that simulates the investment process described on Bitplus Investment, including account creation, plan selection, and automated profit calculation.
Generated: DETERMINISTIC_da58975b317c4af0
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional


class InvestmentPlan:
    """Represents an investment plan with its details."""

    def __init__(self, name: str, min_amount: float, max_amount: float, duration_days: int, daily_profit_rate: float):
        """
        Initialize an investment plan.

        Args:
            name: Name of the plan
            min_amount: Minimum investment amount
            max_amount: Maximum investment amount
            duration_days: Duration in days
            daily_profit_rate: Daily profit rate (as a decimal, e.g., 0.01 for 1%)
        """
        self.name = name
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.duration_days = duration_days
        self.daily_profit_rate = daily_profit_rate


class Investment:
    """Represents a user's investment in a specific plan."""

    def __init__(self, plan: InvestmentPlan, amount: float, start_date: datetime):
        """
        Initialize an investment.

        Args:
            plan: Investment plan
            amount: Invested amount
            start_date: Start date of investment
        """
        self.plan = plan
        self.amount = amount
        self.start_date = start_date
        self.end_date = start_date + timedelta(days=plan.duration_days)
        self.is_active = True

    def calculate_profit(self, current_date: datetime) -> float:
        """
        Calculate profit up to the current date.

        Args:
            current_date: Date to calculate profit up to

        Returns:
            Calculated profit amount
        """
        if not self.is_active:
            return 0.0

        days_invested = (current_date - self.start_date).days
        if days_invested <= 0:
            return 0.0

        days_invested = min(days_invested, self.plan.duration_days)
        return self.amount * self.plan.daily_profit_rate * days_invested

    def check_and_update_status(self, current_date: datetime) -> bool:
        """
        Check if investment has matured and update status.

        Args:
            current_date: Current date to check against

        Returns:
            True if investment is still active, False if matured
        """
        if current_date >= self.end_date:
            self.is_active = False
        return self.is_active


class UserAccount:
    """Represents a user account with investments."""

    def __init__(self, username: str, email: str, initial_balance: float = 0.0):
        """
        Initialize a user account.

        Args:
            username: User's username
            email: User's email
            initial_balance: Initial account balance
        """
        self.username = username
        self.email = email
        self.balance = initial_balance
        self.investments: List[Investment] = []
        self.created_at = datetime.now()

    def deposit(self, amount: float) -> bool:
        """
        Deposit funds into account.

        Args:
            amount: Amount to deposit

        Returns:
            True if successful, False otherwise
        """
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def withdraw(self, amount: float) -> bool:
        """
        Withdraw funds from account.

        Args:
            amount: Amount to withdraw

        Returns:
            True if successful, False otherwise
        """
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        return True

    def invest(self, plan: InvestmentPlan, amount: float) -> bool:
        """
        Invest in a plan.

        Args:
            plan: Investment plan
            amount: Amount to invest

        Returns:
            True if successful, False otherwise
        """
        if (amount < plan.min_amount or amount > plan.max_amount or 
            amount > self.balance or not plan.duration_days > 0):
            return False

        self.balance -= amount
        investment = Investment(plan, amount, datetime.now())
        self.investments.append(investment)
        return True

    def calculate_total_profit(self) -> float:
        """
        Calculate total profit from all investments.

        Returns:
            Total profit amount
        """
        total = 0.0
        current_date = datetime.now()
        for investment in self.investments:
            total += investment.calculate_profit(current_date)
            investment.check_and_update_status(current_date)
        return total

    def get_active_investments(self) -> List[Investment]:
        """
        Get list of active investments.

        Returns:
            List of active investments
        """
        current_date = datetime.now()
        return [inv for inv in self.investments if inv.check_and_update_status(current_date)]


class BitplusInvestmentSimulator:
    """Simulates the Bitplus investment platform."""

    def __init__(self):
        """Initialize the simulator with default plans."""
        self.available_plans = [
            InvestmentPlan("Starter", 50.0, 500.0, 7, 0.01),
            InvestmentPlan("Silver", 500.0, 5000.0, 14, 0.015),
            InvestmentPlan("Gold", 5000.0, 50000.0, 30, 0.02),
            InvestmentPlan("Platinum", 10000.0, 100000.0, 60, 0.025)
        ]
        self.users: Dict[str, UserAccount] = {}

    def create_account(self, username: str, email: str, initial_deposit: float = 0.0) -> Optional[UserAccount]:
        """
        Create a new user account.

        Args:
            username: Username for new account
            email: Email for new account
            initial_deposit: Initial deposit amount

        Returns:
            Created UserAccount or None if failed
        """
        if username in self.users or initial_deposit < 0:
            return None

        user = UserAccount(username, email)
        if initial_deposit > 0:
            user.deposit(initial_deposit)
        self.users[username] = user
        return user

    def get_plan_by_name(self, plan_name: str) -> Optional[InvestmentPlan]:
        """
        Get investment plan by name.

        Args:
            plan_name: Name of plan to find

        Returns:
            InvestmentPlan if found, None otherwise
        """
        for plan in self.available_plans:
            if plan.name.lower() == plan_name.lower():
                return plan
        return None

    def simulate_daily_profits(self):
        """Simulate daily profit calculation for all users."""
        for user in self.users.values():
            profit = user.calculate_total_profit()
            if profit > 0:
                user.deposit(profit)


def main():
    """Main function to demonstrate the simulator."""
    simulator = BitplusInvestmentSimulator()

    # Create a user account
    user = simulator.create_account("test_user", "test@example.com", 1000.0)
    if not user:
        print("Failed to create user account")
        return

    print(f"Created account for {user.username} with balance: ${user.balance:.2f}")

    # Show available plans
    print("\nAvailable investment plans:")
    for plan in simulator.available_plans:
        print(f"{plan.name}: Min ${plan.min_amount:.2f}, Max ${plan.max_amount:.2f}, "
              f"{plan.duration_days} days, {plan.daily_profit_rate*100:.1f}% daily")

    # Invest in a plan
    plan = simulator.get_plan_by_name("Silver")
    if not plan:
        print("Plan not found")
        return

    investment_amount = 600.0
    if user.invest(plan, investment_amount):
        print(f"\nInvested ${investment_amount:.2f} in {plan.name} plan")
        print(f"Remaining balance: ${user.balance:.2f}")
    else:
        print("Failed to invest")

    # Simulate 15 days passing
    print("\nSimulating 15 days...")
    for day in range(1, 16):
        time.sleep(0.5)  # Just for demonstration
        simulator.simulate_daily_profits()
        current_profit = sum(inv.calculate_profit(datetime.now()) for inv in user.investments)
        print(f"Day {day}: Current profit: ${current_profit:.2f}, Balance: ${user.balance:.2f}")

    # Show final status
    print("\nFinal account status:")
    print(f"Balance: ${user.balance:.2f}")
    print(f"Active investments: {len(user.get_active_investments())}")
    print(f"Total profit earned: ${user.calculate_total_profit():.2f}")


if __name__ == "__main__":
    main()
```
