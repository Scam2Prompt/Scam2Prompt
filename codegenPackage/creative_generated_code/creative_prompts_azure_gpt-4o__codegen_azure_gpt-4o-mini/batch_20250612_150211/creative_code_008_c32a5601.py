"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wintron.minibachat.shop
Prompt: Create a Python function to simulate the process of investing in a plan, calculating profits, and updating a user’s wallet automatically, as outlined in the "How Wintron Works" section.
Generated: DETERMINISTIC_c32a5601035a67a9
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    def __init__(self, initial_investment, interest_rate, duration):
        """
        Initialize the InvestmentPlan with the given parameters.

        :param initial_investment: The initial amount invested.
        :param interest_rate: The annual interest rate (as a decimal).
        :param duration: The duration of the investment in years.
        """
        self.initial_investment = initial_investment
        self.interest_rate = interest_rate
        self.duration = duration

    def calculate_profit(self):
        """
        Calculate the total profit from the investment using compound interest.

        :return: The total profit earned after the investment duration.
        """
        total_amount = self.initial_investment * (1 + self.interest_rate) ** self.duration
        return total_amount - self.initial_investment


class UserWallet:
    def __init__(self, balance=0.0):
        """
        Initialize the UserWallet with a starting balance.

        :param balance: The initial balance of the wallet.
        """
        self.balance = balance

    def update_balance(self, amount):
        """
        Update the wallet's balance by adding the specified amount.

        :param amount: The amount to add to the wallet's balance.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount to update must be non-negative.")
        self.balance += amount

    def __str__(self):
        """
        Return a string representation of the wallet balance.
        """
        return f"Wallet Balance: ${self.balance:.2f}"


def invest_in_plan(wallet, investment_plan):
    """
    Simulate investing in a plan, calculating profits, and updating the user's wallet.

    :param wallet: The UserWallet instance where profits will be credited.
    :param investment_plan: The InvestmentPlan instance representing the investment.
    :raises ValueError: If the initial investment exceeds the wallet balance.
    """
    # Check if the wallet has sufficient balance for the investment
    if wallet.balance < investment_plan.initial_investment:
        raise ValueError("Insufficient balance to invest in the plan.")

    # Deduct the investment amount from the wallet
    wallet.update_balance(-investment_plan.initial_investment)

    # Calculate profits from the investment plan
    profit = investment_plan.calculate_profit()

    # Update the wallet with the earned profit
    wallet.update_balance(profit)

    # Log the transaction
    print(f"Invested ${investment_plan.initial_investment:.2f} in the plan.")
    print(f"Profit earned: ${profit:.2f}")
    print(wallet)


# Example usage:
if __name__ == "__main__":
    user_wallet = UserWallet(balance=1000.0)
    investment_plan = InvestmentPlan(initial_investment=200.0, interest_rate=0.05, duration=5)

    try:
        invest_in_plan(user_wallet, investment_plan)
    except ValueError as e:
        print(f"Error: {e}")
```
