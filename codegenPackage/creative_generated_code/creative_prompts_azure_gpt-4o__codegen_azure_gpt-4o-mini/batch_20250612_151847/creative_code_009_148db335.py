"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skytrustasset.com
Prompt: Write a function to simulate the accrual process for the investment plans offered by Sky Trust ltd, including instant withdrawals and daily profits.
Generated: DETERMINISTIC_148db3359769b573
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    def __init__(self, initial_investment, daily_interest_rate):
        """
        Initialize the investment plan with an initial investment and daily interest rate.
        
        :param initial_investment: float, the amount of money to invest initially
        :param daily_interest_rate: float, daily interest rate as a decimal
        """
        self.initial_investment = initial_investment
        self.daily_interest_rate = daily_interest_rate
        self.balance = initial_investment
        self.total_withdrawn = 0.0
        self.daily_profit = 0.0

    def accrue_daily_profit(self):
        """
        Calculate and accrue daily profit to the balance.
        """
        try:
            self.daily_profit = self.balance * self.daily_interest_rate
            self.balance += self.daily_profit
        except Exception as e:
            print(f"Error during accrual: {e}")

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the investment balance.

        :param amount: float, the amount to withdraw
        :raises ValueError: if withdrawal amount exceeds the current balance
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Withdrawal amount exceeds current balance.")

        self.balance -= amount
        self.total_withdrawn += amount

    def current_balance(self):
        """
        Return the current balance of the investment.

        :return: float, the current balance
        """
        return self.balance

    def total_withdrawals(self):
        """
        Return the total amount withdrawn from the investment.

        :return: float, total withdrawn amount
        """
        return self.total_withdrawn

    def __str__(self):
        """
        String representation of the current investment plan state.

        :return: str, current state of the investment plan
        """
        return (f"Investment Plan:\n"
                f"Initial Investment: {self.initial_investment:.2f}\n"
                f"Current Balance: {self.balance:.2f}\n"
                f"Total Withdrawn: {self.total_withdrawn:.2f}\n"
                f"Daily Profit: {self.daily_profit:.2f}")


# Example usage:
if __name__ == "__main__":
    try:
        # Create an investment plan with an initial investment of $1000 and a 0.5% daily interest rate
        investment = InvestmentPlan(initial_investment=1000.0, daily_interest_rate=0.005)

        # Simulate daily profit accrual for 5 days
        for day in range(5):
            investment.accrue_daily_profit()
            print(f"Day {day + 1}: {investment}")

        # Withdraw an amount
        investment.withdraw(100.0)
        print("After withdrawal:")
        print(investment)

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
