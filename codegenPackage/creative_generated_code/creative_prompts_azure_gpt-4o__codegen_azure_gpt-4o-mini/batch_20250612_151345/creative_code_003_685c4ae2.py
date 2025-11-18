"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegaincapital.com
Prompt: Create a script to calculate investment profits using The Gain Capital's investment calculator, incorporating plan-specific parameters like monthly returns and capital back options.
Generated: DETERMINISTIC_685c4ae2ad3086f5
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class InvestmentCalculator:
    def __init__(self, initial_investment, monthly_return_rate, investment_duration_months, capital_back_option):
        """
        Initializes the InvestmentCalculator with parameters for calculation.

        :param initial_investment: The initial amount invested (float).
        :param monthly_return_rate: The monthly return rate as a percentage (float).
        :param investment_duration_months: The total duration of the investment in months (int).
        :param capital_back_option: Flag to indicate if capital is returned at the end (bool).
        """
        self.initial_investment = initial_investment
        self.monthly_return_rate = monthly_return_rate / 100  # Convert percentage to decimal
        self.investment_duration_months = investment_duration_months
        self.capital_back_option = capital_back_option

    def calculate_profit(self):
        """
        Calculates the total profit from the investment.

        :return: Total profit (float).
        """
        total_profit = 0.0
        current_investment = self.initial_investment
        
        for month in range(self.investment_duration_months):
            monthly_profit = current_investment * self.monthly_return_rate
            total_profit += monthly_profit
            current_investment += monthly_profit  # Reinvest profits

        if self.capital_back_option:
            total_profit += self.initial_investment  # Add initial investment back

        return total_profit

def main():
    """
    Main function to run the investment calculator.
    """
    try:
        # User input for investment parameters
        initial_investment = float(input("Enter the initial investment amount: "))
        monthly_return_rate = float(input("Enter the monthly return rate (in %): "))
        investment_duration_months = int(input("Enter the investment duration (in months): "))
        capital_back_option = input("Return capital at the end? (yes/no): ").strip().lower() == 'yes'

        # Create an instance of the InvestmentCalculator
        calculator = InvestmentCalculator(initial_investment, monthly_return_rate, investment_duration_months, capital_back_option)

        # Calculate total profit
        total_profit = calculator.calculate_profit()

        # Output the result
        print(f"Total profit after {investment_duration_months} months: ${total_profit:.2f}")

    except ValueError as e:
        print(f"Input error: {e}. Please enter valid numeric values.")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
