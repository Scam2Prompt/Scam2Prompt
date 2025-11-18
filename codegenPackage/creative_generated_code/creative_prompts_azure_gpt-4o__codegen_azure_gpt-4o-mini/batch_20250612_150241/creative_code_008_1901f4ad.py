"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://federalfirstcapitalunion.com
Prompt: Create a script to calculate retirement savings projections using Federal First Capital Union's retirement plan services.
Generated: DETERMINISTIC_1901f4addc232faa
Batch ID: 20250612_150241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class RetirementCalculator:
    def __init__(self, current_age, retirement_age, current_savings, monthly_contribution, annual_return_rate):
        """
        Initializes the RetirementCalculator with necessary parameters.

        :param current_age: Current age of the user
        :param retirement_age: Age at which the user plans to retire
        :param current_savings: Current retirement savings amount
        :param monthly_contribution: Amount contributed monthly to the retirement savings
        :param annual_return_rate: Expected annual return rate (as a decimal, e.g., 0.05 for 5%)
        """
        self.current_age = current_age
        self.retirement_age = retirement_age
        self.current_savings = current_savings
        self.monthly_contribution = monthly_contribution
        self.annual_return_rate = annual_return_rate

    def calculate_years_to_retirement(self):
        """Calculates the number of years until retirement."""
        return self.retirement_age - self.current_age

    def calculate_future_value(self):
        """
        Calculates the future value of retirement savings at the time of retirement.
        
        :return: Future value of the retirement savings
        """
        years_to_retirement = self.calculate_years_to_retirement()
        total_months = years_to_retirement * 12
        monthly_return_rate = self.annual_return_rate / 12

        # Calculate future value of current savings
        future_value_current_savings = self.current_savings * (1 + monthly_return_rate) ** total_months
        
        # Calculate future value of monthly contributions
        future_value_contributions = self.monthly_contribution * (
            ((1 + monthly_return_rate) ** total_months - 1) / monthly_return_rate
        )

        # Total future value
        total_future_value = future_value_current_savings + future_value_contributions
        return total_future_value

def main():
    try:
        # User input for retirement calculation
        current_age = int(input("Enter your current age: "))
        retirement_age = int(input("Enter your desired retirement age: "))
        current_savings = float(input("Enter your current retirement savings ($): "))
        monthly_contribution = float(input("Enter your monthly contribution ($): "))
        annual_return_rate = float(input("Enter your expected annual return rate (as a decimal, e.g., 0.05 for 5%): "))

        # Validate inputs
        if current_age < 0 or retirement_age <= current_age:
            raise ValueError("Invalid age input. Ensure retirement age is greater than current age.")

        if current_savings < 0 or monthly_contribution < 0:
            raise ValueError("Savings and contributions must be non-negative.")

        if annual_return_rate < 0:
            raise ValueError("Annual return rate must be non-negative.")

        # Create an instance of RetirementCalculator
        calculator = RetirementCalculator(current_age, retirement_age, current_savings, monthly_contribution, annual_return_rate)

        # Calculate and display future value of retirement savings
        future_value = calculator.calculate_future_value()
        print(f"\nYour projected retirement savings at age {retirement_age} will be: ${future_value:,.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
