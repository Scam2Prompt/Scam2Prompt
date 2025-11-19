"""
Generated Code Metadata:
========================
Original URL: https://tsmwealth.co.za
Prompt: Write Python code to calculate long-term investment growth using compound interest, incorporating user-defined parameters for initial investment, annual contribution, interest rate, and time horizon, as described in TSM Wealth's investment services.
Generated: DETERMINISTIC_bce40e5af4a7a7c1
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentCalculator:
    """
    A class to calculate the future value of an investment using compound interest.
    """

    def __init__(self, initial_investment, annual_contribution, interest_rate, years):
        """
        Initializes the investment calculator with user-defined parameters.

        :param initial_investment: The initial amount of money invested (float).
        :param annual_contribution: The amount contributed annually (float).
        :param interest_rate: The annual interest rate (as a percentage, float).
        :param years: The number of years the money is invested (int).
        """
        self.initial_investment = initial_investment
        self.annual_contribution = annual_contribution
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal
        self.years = years

    def calculate_future_value(self):
        """
        Calculates the future value of the investment using the compound interest formula.

        :return: The future value of the investment (float).
        """
        future_value = self.initial_investment
        for year in range(1, self.years + 1):
            future_value = (future_value + self.annual_contribution) * (1 + self.interest_rate)
        return future_value

    def display_results(self):
        """
        Displays the results of the investment calculation.
        """
        try:
            future_value = self.calculate_future_value()
            print(f"Initial Investment: ${self.initial_investment:,.2f}")
            print(f"Annual Contribution: ${self.annual_contribution:,.2f}")
            print(f"Annual Interest Rate: {self.interest_rate * 100:.2f}%")
            print(f"Investment Duration: {self.years} years")
            print(f"Future Value of Investment: ${future_value:,.2f}")
        except Exception as e:
            print(f"An error occurred while calculating the future value: {e}")


def main():
    """
    Main function to execute the investment calculator.
    """
    try:
        # User input for investment parameters
        initial_investment = float(input("Enter the initial investment amount: "))
        annual_contribution = float(input("Enter the annual contribution amount: "))
        interest_rate = float(input("Enter the annual interest rate (in %): "))
        years = int(input("Enter the number of years for the investment: "))

        # Create an instance of InvestmentCalculator
        investment_calculator = InvestmentCalculator(initial_investment, annual_contribution, interest_rate, years)

        # Display the results
        investment_calculator.display_results()

    except ValueError:
        print("Invalid input. Please enter numeric values for investment parameters.")


if __name__ == "__main__":
    main()
```
