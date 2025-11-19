"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pipelinefinanceconseil.com
Prompt: Generate a code snippet to simulate an online savings plan that maximizes capital at a fixed rate of 6.92%, as described on Pipeline Finance Conseil.
Generated: DETERMINISTIC_14d917802feebb2e
Batch ID: 20250612_163647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SavingsPlan:
    """
    A class to simulate an online savings plan that maximizes capital 
    at a fixed interest rate of 6.92%.
    """

    def __init__(self, initial_investment, monthly_contribution, years):
        """
        Initializes the SavingsPlan with initial investment, monthly contribution, and investment duration.

        :param initial_investment: The starting amount of money to invest.
        :param monthly_contribution: The amount of money to contribute each month.
        :param years: The duration of the investment in years.
        """
        if initial_investment < 0 or monthly_contribution < 0 or years < 0:
            raise ValueError("Initial investment, monthly contribution, and years must be non-negative.")

        self.initial_investment = initial_investment
        self.monthly_contribution = monthly_contribution
        self.years = years
        self.interest_rate = 0.0692  # Fixed interest rate of 6.92%

    def calculate_final_amount(self):
        """
        Calculate the final amount in the savings plan after the specified number of years.

        :return: The final amount after interest and contributions.
        """
        months = self.years * 12
        final_amount = self.initial_investment

        for month in range(months):
            # Interest calculation for the current balance
            final_amount *= (1 + self.interest_rate / 12)
            # Add the monthly contribution
            final_amount += self.monthly_contribution

        return final_amount

    def display_summary(self):
        """
        Display a summary of the savings plan, including the initial investment, 
        total contributions, and final amount.
        """
        total_contributions = self.initial_investment + (self.monthly_contribution * self.years * 12)
        final_amount = self.calculate_final_amount()

        print("Savings Plan Summary:")
        print(f"Initial Investment: ${self.initial_investment:.2f}")
        print(f"Monthly Contribution: ${self.monthly_contribution:.2f}")
        print(f"Investment Duration: {self.years} years")
        print(f"Total Contributions: ${total_contributions:.2f}")
        print(f"Final Amount after {self.years} years: ${final_amount:.2f}")


if __name__ == "__main__":
    try:
        # Example usage
        initial_investment = 10000  # Initial investment of $10,000
        monthly_contribution = 500   # Monthly contribution of $500
        years = 10                   # Investment duration of 10 years

        plan = SavingsPlan(initial_investment, monthly_contribution, years)
        plan.display_summary()

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
