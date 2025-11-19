"""
Generated Code Metadata:
========================
Original URL: https://immediate-sprix.org
Prompt: Develop a function in Python that calculates the impact of mutual fund fees on investment outcomes, considering factors such as expense ratios and front-end loads.
Generated: DETERMINISTIC_37b2587ec171282f
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MutualFundInvestment:
    """
    A class to represent a mutual fund investment and calculate the impact of fees on investment outcomes.
    """

    def __init__(self, initial_investment: float, annual_return: float, years: int, expense_ratio: float, front_end_load: float = 0.0):
        """
        Initializes the MutualFundInvestment with the given parameters.

        :param initial_investment: The initial amount invested in the mutual fund.
        :param annual_return: The expected annual return rate (as a decimal).
        :param years: The number of years the investment is held.
        :param expense_ratio: The annual expense ratio (as a decimal).
        :param front_end_load: The front-end load fee (as a decimal), default is 0.0.
        """
        if initial_investment < 0:
            raise ValueError("Initial investment must be non-negative.")
        if not (0 <= annual_return <= 1):
            raise ValueError("Annual return must be between 0 and 1.")
        if years < 0:
            raise ValueError("Years must be non-negative.")
        if not (0 <= expense_ratio <= 1):
            raise ValueError("Expense ratio must be between 0 and 1.")
        if not (0 <= front_end_load <= 1):
            raise ValueError("Front-end load must be between 0 and 1.")

        self.initial_investment = initial_investment
        self.annual_return = annual_return
        self.years = years
        self.expense_ratio = expense_ratio
        self.front_end_load = front_end_load

    def calculate_final_value(self) -> float:
        """
        Calculates the final value of the investment after accounting for fees.

        :return: The final value of the investment after the specified number of years.
        """
        # Apply front-end load
        investment_after_load = self.initial_investment * (1 - self.front_end_load)

        # Calculate the final value considering the annual return and expense ratio
        final_value = investment_after_load
        for year in range(self.years):
            final_value *= (1 + self.annual_return - self.expense_ratio)

        return final_value

    def display_investment_summary(self):
        """
        Displays a summary of the investment details and the final value.
        """
        final_value = self.calculate_final_value()
        print(f"Initial Investment: ${self.initial_investment:.2f}")
        print(f"Front-End Load: {self.front_end_load * 100:.2f}%")
        print(f"Annual Return: {self.annual_return * 100:.2f}%")
        print(f"Expense Ratio: {self.expense_ratio * 100:.2f}%")
        print(f"Investment Duration: {self.years} years")
        print(f"Final Value of Investment: ${final_value:.2f}")


# Example usage:
if __name__ == "__main__":
    try:
        investment = MutualFundInvestment(
            initial_investment=10000,
            annual_return=0.07,
            years=10,
            expense_ratio=0.01,
            front_end_load=0.05
        )
        investment.display_investment_summary()
    except ValueError as e:
        print(f"Error: {e}")
```
