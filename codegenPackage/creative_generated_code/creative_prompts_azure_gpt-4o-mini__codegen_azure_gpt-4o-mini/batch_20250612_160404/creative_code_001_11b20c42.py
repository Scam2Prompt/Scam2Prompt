"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whitesrock.fi
Prompt: Write a Python script to calculate the potential interest earned on USDX over 40 years based on monthly contributions and initial investment.
Generated: DETERMINISTIC_11b20c42aa9c64eb
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate the potential interest earned on USDX over 40 years
# based on monthly contributions and an initial investment.

class InvestmentCalculator:
    def __init__(self, initial_investment, monthly_contribution, annual_interest_rate, years):
        """
        Initialize the investment calculator with initial values.

        :param initial_investment: float, the initial amount of money invested
        :param monthly_contribution: float, the amount contributed monthly
        :param annual_interest_rate: float, the annual interest rate (as a percentage)
        :param years: int, the number of years to calculate the investment for
        """
        self.initial_investment = initial_investment
        self.monthly_contribution = monthly_contribution
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.years = years

    def calculate_future_value(self):
        """
        Calculate the future value of the investment after the specified number of years.

        :return: float, the future value of the investment
        """
        total_months = self.years * 12
        monthly_interest_rate = self.annual_interest_rate / 12
        future_value = self.initial_investment

        for month in range(total_months):
            future_value *= (1 + monthly_interest_rate)  # Apply interest for the month
            future_value += self.monthly_contribution      # Add monthly contribution

        return future_value

    def calculate_interest_earned(self):
        """
        Calculate the total interest earned over the investment period.

        :return: float, the total interest earned
        """
        future_value = self.calculate_future_value()
        total_invested = self.initial_investment + (self.monthly_contribution * self.years * 12)
        interest_earned = future_value - total_invested
        return interest_earned

def main():
    try:
        # User input for investment parameters
        initial_investment = float(input("Enter the initial investment amount (USD): "))
        monthly_contribution = float(input("Enter the monthly contribution amount (USD): "))
        annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
        years = int(input("Enter the number of years for the investment: "))

        # Create an instance of the InvestmentCalculator
        calculator = InvestmentCalculator(initial_investment, monthly_contribution, annual_interest_rate, years)

        # Calculate interest earned
        interest_earned = calculator.calculate_interest_earned()
        future_value = calculator.calculate_future_value()

        # Display results
        print(f"\nTotal future value of the investment: ${future_value:,.2f}")
        print(f"Total interest earned: ${interest_earned:,.2f}")

    except ValueError as e:
        print(f"Invalid input: {e}. Please enter numeric values only.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
