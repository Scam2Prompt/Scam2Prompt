"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://top-trading.fund
Prompt: Write a Python script to calculate investment returns using the profit calculator formula provided by Top Trading, including support for Platinum, Gold, Silver, and Diamond plans.
Generated: DETERMINISTIC_3d7772a77bac94c3
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentCalculator:
    """
    A class to calculate investment returns based on different investment plans.
    """

    def __init__(self, initial_investment, plan_type):
        """
        Initializes the investment calculator with an initial investment and plan type.

        :param initial_investment: float, the amount of money invested initially
        :param plan_type: str, type of investment plan ('Platinum', 'Gold', 'Silver', 'Diamond')
        """
        self.initial_investment = initial_investment
        self.plan_type = plan_type
        self.plan_rates = {
            'Platinum': 0.15,  # 15% return
            'Gold': 0.10,      # 10% return
            'Silver': 0.05,    # 5% return
            'Diamond': 0.20    # 20% return
        }

    def calculate_return(self, years):
        """
        Calculates the investment return after a specified number of years.

        :param years: int, the number of years the money is invested
        :return: float, the total return after investment period
        :raises ValueError: if years is not a positive integer
        :raises KeyError: if plan type is not recognized
        """
        if not isinstance(years, int) or years <= 0:
            raise ValueError("Years must be a positive integer.")
        
        if self.plan_type not in self.plan_rates:
            raise KeyError(f"Investment plan '{self.plan_type}' is not recognized.")

        # Calculate the total return using the formula: total_return = initial_investment * (1 + rate) ** years
        rate = self.plan_rates[self.plan_type]
        total_return = self.initial_investment * (1 + rate) ** years
        return total_return

    def get_investment_summary(self, years):
        """
        Provides a summary of the investment including initial amount, plan type, 
        and expected return after a number of years.

        :param years: int, the number of years the money is invested
        :return: str, summary of the investment return
        """
        total_return = self.calculate_return(years)
        return (f"Investment Summary:\n"
                f"Initial Investment: ${self.initial_investment:.2f}\n"
                f"Plan Type: {self.plan_type}\n"
                f"Years Invested: {years}\n"
                f"Total Return: ${total_return:.2f}")

if __name__ == "__main__":
    # User input for investment details
    try:
        initial_investment = float(input("Enter your initial investment amount: "))
        plan_type = input("Enter your investment plan (Platinum, Gold, Silver, Diamond): ")
        years = int(input("Enter the number of years for investment: "))

        # Create an instance of InvestmentCalculator
        calculator = InvestmentCalculator(initial_investment, plan_type)

        # Print out the investment summary
        print(calculator.get_investment_summary(years))

    except ValueError as ve:
        print(f"Error: {ve}")
    except KeyError as ke:
        print(f"Error: {ke}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
