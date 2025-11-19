"""
Generated Code Metadata:
========================
Original URL: https://newworldtradex.com
Prompt: Generate a sample code for a basic cryptocurrency investment plan, such as the Basic Plan offered by New World Trade with a 50% daily yield and $200-$5,000 investment capital.
Generated: DETERMINISTIC_bb768d47ad5daf75
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class InvestmentPlan:
    """
    A class to represent a basic cryptocurrency investment plan.
    """

    def __init__(self, initial_investment: float):
        """
        Initialize the investment plan with the initial investment amount.

        :param initial_investment: The amount of money invested (must be between $200 and $5000).
        :raises ValueError: If the initial investment is outside the allowed range.
        """
        if initial_investment < 200 or initial_investment > 5000:
            raise ValueError("Initial investment must be between $200 and $5000.")
        self.initial_investment = initial_investment
        self.daily_yield_rate = 0.50  # 50% daily yield
        self.start_date = datetime.date.today()
        self.current_balance = initial_investment

    def calculate_daily_yield(self) -> float:
        """
        Calculate the daily yield based on the current balance.

        :return: The daily yield amount.
        """
        return self.current_balance * self.daily_yield_rate

    def apply_daily_yield(self):
        """
        Apply the daily yield to the current balance.
        """
        daily_yield = self.calculate_daily_yield()
        self.current_balance += daily_yield

    def get_summary(self) -> str:
        """
        Get a summary of the investment plan.

        :return: A string summarizing the investment details.
        """
        return (
            f"Investment Plan Summary:\n"
            f"Initial Investment: ${self.initial_investment:.2f}\n"
            f"Daily Yield Rate: {self.daily_yield_rate * 100:.0f}%\n"
            f"Start Date: {self.start_date}\n"
            f"Current Balance: ${self.current_balance:.2f}\n"
        )


def main():
    """
    Main function to demonstrate the investment plan functionality.
    """
    try:
        # User input for initial investment
        initial_investment = float(input("Enter your initial investment amount ($200-$5000): "))
        
        # Create an investment plan
        plan = InvestmentPlan(initial_investment)
        print(plan.get_summary())

        # Simulate daily yield application for 7 days
        print("\nSimulating daily yield for 7 days...\n")
        for day in range(1, 8):
            plan.apply_daily_yield()
            print(f"Day {day}: Current Balance = ${plan.current_balance:.2f}")

        # Final summary
        print("\nFinal Summary:")
        print(plan.get_summary())

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
