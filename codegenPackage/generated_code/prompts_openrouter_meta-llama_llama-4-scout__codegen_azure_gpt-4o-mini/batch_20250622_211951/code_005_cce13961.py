"""
Generated Code Metadata:
========================
Original URL: https://megapromining.live
Prompt: Develop a basic investment plan algorithm that could be used on a platform like Megapromining, taking into account daily payouts and profit percentages.
Generated: DETERMINISTIC_cce1396165d47ded
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentPlan:
    """
    A class to represent an investment plan for a platform like Megapromining.
    
    Attributes:
        initial_investment (float): The initial amount of money invested.
        daily_payout_percentage (float): The daily payout percentage.
        investment_duration (int): The duration of the investment in days.
    """

    def __init__(self, initial_investment: float, daily_payout_percentage: float, investment_duration: int):
        """
        Initializes the InvestmentPlan with the given parameters.

        Args:
            initial_investment (float): The initial amount of money invested.
            daily_payout_percentage (float): The daily payout percentage.
            investment_duration (int): The duration of the investment in days.

        Raises:
            ValueError: If any of the parameters are invalid.
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if not (0 < daily_payout_percentage < 100):
            raise ValueError("Daily payout percentage must be between 0 and 100.")
        if investment_duration <= 0:
            raise ValueError("Investment duration must be greater than zero.")

        self.initial_investment = initial_investment
        self.daily_payout_percentage = daily_payout_percentage
        self.investment_duration = investment_duration

    def calculate_total_payout(self) -> float:
        """
        Calculates the total payout after the investment duration.

        Returns:
            float: The total payout after the investment duration.
        """
        total_payout = 0.0
        daily_payout = self.initial_investment * (self.daily_payout_percentage / 100)

        for day in range(1, self.investment_duration + 1):
            total_payout += daily_payout
            print(f"Day {day}: Daily Payout = {daily_payout:.2f}, Total Payout = {total_payout:.2f}")

        return total_payout

    def calculate_total_return(self) -> float:
        """
        Calculates the total return including the initial investment.

        Returns:
            float: The total return after the investment duration.
        """
        total_payout = self.calculate_total_payout()
        total_return = self.initial_investment + total_payout
        return total_return

    def display_investment_summary(self):
        """
        Displays a summary of the investment plan.
        """
        print("Investment Summary:")
        print(f"Initial Investment: ${self.initial_investment:.2f}")
        print(f"Daily Payout Percentage: {self.daily_payout_percentage:.2f}%")
        print(f"Investment Duration: {self.investment_duration} days")
        print(f"Total Payout: ${self.calculate_total_payout():.2f}")
        print(f"Total Return: ${self.calculate_total_return():.2f}")


# Example usage
if __name__ == "__main__":
    try:
        investment_plan = InvestmentPlan(initial_investment=1000.0, daily_payout_percentage=5.0, investment_duration=30)
        investment_plan.display_investment_summary()
    except ValueError as e:
        print(f"Error: {e}")
```
