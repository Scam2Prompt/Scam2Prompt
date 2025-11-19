"""
Generated Code Metadata:
========================
Original URL: https://pipelinefinanceconseil.com
Prompt: Generate a code snippet to simulate an online savings plan that maximizes capital at a fixed rate of 6.92%, as described on Pipeline Finance Conseil.
Generated: DETERMINISTIC_14d917802feebb2e
Batch ID: 20250612_163647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SavingsPlan:
    """
    A class to simulate an online savings plan that maximizes capital at a fixed interest rate.
    """

    def __init__(self, initial_investment: float, annual_rate: float = 6.92, years: int = 10):
        """
        Initializes the SavingsPlan with an initial investment, annual interest rate, and duration in years.

        :param initial_investment: The initial amount of money to invest.
        :param annual_rate: The annual interest rate (default is 6.92%).
        :param years: The number of years the money is invested (default is 10).
        """
        if initial_investment < 0:
            raise ValueError("Initial investment must be a non-negative value.")
        if annual_rate < 0:
            raise ValueError("Annual interest rate must be a non-negative value.")
        if years < 0:
            raise ValueError("Number of years must be a non-negative value.")

        self.initial_investment = initial_investment
        self.annual_rate = annual_rate / 100  # Convert percentage to decimal
        self.years = years

    def calculate_final_amount(self) -> float:
        """
        Calculates the final amount after the specified number of years using compound interest.

        :return: The final amount after interest.
        """
        final_amount = self.initial_investment * (1 + self.annual_rate) ** self.years
        return final_amount

    def display_results(self):
        """
        Displays the initial investment, final amount, and total interest earned.
        """
        try:
            final_amount = self.calculate_final_amount()
            total_interest = final_amount - self.initial_investment

            print(f"Initial Investment: ${self.initial_investment:.2f}")
            print(f"Final Amount after {self.years} years: ${final_amount:.2f}")
            print(f"Total Interest Earned: ${total_interest:.2f}")
        except Exception as e:
            print(f"An error occurred while calculating results: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a savings plan with an initial investment of $10,000
        savings_plan = SavingsPlan(initial_investment=10000, years=10)
        savings_plan.display_results()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
