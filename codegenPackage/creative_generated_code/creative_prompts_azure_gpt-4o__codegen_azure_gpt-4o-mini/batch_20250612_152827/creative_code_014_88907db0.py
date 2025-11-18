"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://newworldtradex.com
Prompt: Develop a script to manage and display investment options with varying yields and durations, as outlined in New World Trade's investment plans.
Generated: DETERMINISTIC_88907db07ade9cec
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class InvestmentOption:
    """
    A class to represent an investment option.
    """

    def __init__(self, name, yield_percentage, duration_years):
        """
        Initialize an investment option with a name, yield percentage, and duration in years.

        :param name: str, name of the investment option
        :param yield_percentage: float, expected yield percentage of the investment
        :param duration_years: int, duration of the investment in years
        """
        self.name = name
        self.yield_percentage = yield_percentage
        self.duration_years = duration_years

    def calculate_return(self, principal):
        """
        Calculate the total return of the investment based on the principal amount.

        :param principal: float, the initial amount invested
        :return: float, the total value of the investment after the duration
        """
        return principal * ((1 + self.yield_percentage / 100) ** self.duration_years)

class InvestmentManager:
    """
    A class to manage multiple investment options.
    """

    def __init__(self):
        """Initialize the investment manager with an empty list of investment options."""
        self.options = []

    def add_option(self, option):
        """
        Add an investment option to the manager.

        :param option: InvestmentOption, the investment option to be added
        """
        if not isinstance(option, InvestmentOption):
            raise ValueError("Option must be of type InvestmentOption.")
        self.options.append(option)

    def display_options(self):
        """Display all investment options in a formatted manner."""
        print(f"{'Name':<30} {'Yield (%)':<15} {'Duration (Years)':<15}")
        print("=" * 60)
        for option in self.options:
            print(f"{option.name:<30} {option.yield_percentage:<15} {option.duration_years:<15}")

    def calculate_returns(self, principal):
        """
        Calculate and display the returns for all investment options based on the principal amount.

        :param principal: float, the initial amount invested
        """
        print(f"\nInvestment Returns for Principal Amount: {principal}")
        print("=" * 50)
        for option in self.options:
            total_return = option.calculate_return(principal)
            print(f"{option.name}: Total Return = {total_return:.2f}")

def main():
    """Main function to execute the investment manager."""
    investment_manager = InvestmentManager()

    # Sample investment options
    investment_data = [
        {"name": "Bond A", "yield_percentage": 5.0, "duration_years": 10},
        {"name": "Stock B", "yield_percentage": 8.0, "duration_years": 5},
        {"name": "Real Estate C", "yield_percentage": 7.5, "duration_years": 15}
    ]

    # Add investment options to the manager
    for data in investment_data:
        option = InvestmentOption(data['name'], data['yield_percentage'], data['duration_years'])
        investment_manager.add_option(option)

    # Display options
    investment_manager.display_options()

    # Get principal amount from user input
    try:
        principal = float(input("\nEnter the principal amount for investment: "))
        if principal < 0:
            raise ValueError("Principal amount must be a non-negative number.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Calculate and display returns
    investment_manager.calculate_returns(principal)

if __name__ == "__main__":
    main()
```
