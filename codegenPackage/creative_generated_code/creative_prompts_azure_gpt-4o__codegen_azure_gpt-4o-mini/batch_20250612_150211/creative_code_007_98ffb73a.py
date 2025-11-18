"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autodigitaltrade.com.easyprofitabletrading.com
Prompt: Create a script to manage investment plans and calculate insured returns, referencing the insurance coverage and safety measures mentioned on Autodigitaltrade.
Generated: DETERMINISTIC_98ffb73a4795bf93
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
    """
    A class to manage investment plans and calculate insured returns.
    """
    
    def __init__(self, initial_investment, annual_rate, years, insurance_coverage):
        """
        Initializes the investment plan with the provided parameters.

        :param initial_investment: The initial amount invested
        :param annual_rate: The annual return rate (as a decimal)
        :param years: The number of years the investment will be held
        :param insurance_coverage: The insurance coverage amount
        """
        if initial_investment < 0:
            raise ValueError("Initial investment must be a non-negative number.")
        if not (0 <= annual_rate <= 1):
            raise ValueError("Annual rate must be between 0 and 1.")
        if years < 0:
            raise ValueError("Years must be a non-negative integer.")
        if insurance_coverage < 0:
            raise ValueError("Insurance coverage must be a non-negative number.")

        self.initial_investment = initial_investment
        self.annual_rate = annual_rate
        self.years = years
        self.insurance_coverage = insurance_coverage

    def calculate_final_amount(self):
        """
        Calculate the final amount after the investment period.

        :return: Final amount after interest is applied
        """
        final_amount = self.initial_investment * (1 + self.annual_rate) ** self.years
        return final_amount

    def calculate_insured_return(self):
        """
        Calculate the insured return based on the final amount and insurance coverage.

        :return: Insured return amount
        """
        final_amount = self.calculate_final_amount()
        insured_return = min(final_amount, self.insurance_coverage)
        return insured_return

    def display_investment_summary(self):
        """
        Display a summary of the investment plan, including final amount and insured return.
        """
        final_amount = self.calculate_final_amount()
        insured_return = self.calculate_insured_return()

        summary = (
            f"Initial Investment: ${self.initial_investment:.2f}\n"
            f"Annual Rate: {self.annual_rate * 100:.2f}%\n"
            f"Investment Period: {self.years} years\n"
            f"Final Amount: ${final_amount:.2f}\n"
            f"Insurance Coverage: ${self.insurance_coverage:.2f}\n"
            f"Insured Return: ${insured_return:.2f}\n"
        )
        print(summary)


# Example of using the InvestmentPlan class
if __name__ == "__main__":
    try:
        investment = InvestmentPlan(
            initial_investment=10000,
            annual_rate=0.05,  # 5% annual return
            years=10,
            insurance_coverage=15000
        )
        investment.display_investment_summary()
    except ValueError as e:
        print(f"Error: {e}")
```
