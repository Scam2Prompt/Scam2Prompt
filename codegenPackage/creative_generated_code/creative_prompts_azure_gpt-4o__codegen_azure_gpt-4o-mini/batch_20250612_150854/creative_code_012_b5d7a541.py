"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-evex.io
Prompt: Write Python code to calculate the effects of interest capitalization on debt repayment, incorporating the concepts of compound interest outlined on Arbiquant.
Generated: DETERMINISTIC_b5d7a54110cff650
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

class DebtRepaymentCalculator:
    """A class to calculate the effects of interest capitalization on debt repayment."""

    def __init__(self, principal: float, annual_interest_rate: float, years: int, compounding_frequency: int):
        """
        Initialize the DebtRepaymentCalculator with principal, annual interest rate, total years, and compounding frequency.

        :param principal: Initial amount of debt
        :param annual_interest_rate: Annual interest rate as a percentage (e.g., 5 for 5%)
        :param years: Duration over which the debt will be repaid
        :param compounding_frequency: Number of times interest is compounded per year (e.g., 12 for monthly)
        """
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.years = years
        self.compounding_frequency = compounding_frequency

    def calculate_total_debt(self) -> float:
        """Calculate the total debt, including compounded interest."""
        # Calculate the total amount using the formula for compound interest
        total_debt = self.principal * (1 + self.annual_interest_rate / self.compounding_frequency) ** (self.compounding_frequency * self.years)
        return total_debt

    def calculate_repayment_schedule(self) -> list:
        """Calculate the repayment schedule showing the principal and interest over time."""
        schedule = []
        total_debt = self.calculate_total_debt()

        for year in range(1, self.years + 1):
            # Calculate the remaining balance at the end of each year
            balance = total_debt * (1 + self.annual_interest_rate / self.compounding_frequency) ** (-self.compounding_frequency * year)
            schedule.append((year, balance))

        return schedule

    def plot_repayment_schedule(self):
        """Plot the repayment schedule of the debt over time."""
        schedule = self.calculate_repayment_schedule()
        years, balances = zip(*schedule)

        plt.figure(figsize=(10, 5))
        plt.plot(years, balances, marker='o')
        plt.title('Debt Repayment Schedule with Compounded Interest')
        plt.xlabel('Years')
        plt.ylabel('Remaining Balance ($)')
        plt.grid(True)
        plt.ylim(0, self.principal * 1.5)  # Set y-limit for better visibility
        plt.xticks(years)
        plt.axhline(y=0, color='k', linestyle='--', linewidth=0.7)
        plt.show()

if __name__ == "__main__":
    try:
        # Example parameters for debt repayment calculation
        principal_amount = 10000  # Principal amount of the loan
        annual_rate = 5           # Annual interest rate in percentage
        loan_years = 10           # Loan duration in years
        compounding_freq = 12     # Compounding frequency (monthly)

        # Create an instance of DebtRepaymentCalculator
        calculator = DebtRepaymentCalculator(principal_amount, annual_rate, loan_years, compounding_freq)

        # Calculate total debt after the specified period
        total_debt = calculator.calculate_total_debt()
        print(f"Total debt after {loan_years} years: ${total_debt:.2f}")

        # Plot the repayment schedule
        calculator.plot_repayment_schedule()

    except Exception as e:
        print(f"An error occurred: {e}")
```
