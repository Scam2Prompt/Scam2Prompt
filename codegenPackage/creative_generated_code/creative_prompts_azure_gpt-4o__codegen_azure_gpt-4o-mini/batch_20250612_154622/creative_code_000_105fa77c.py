"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradetoearnoptions.com
Prompt: Write Python code to calculate investment returns using the profit calculator parameters from Tradetoearnoption, including interest rates and maturity periods for plans like BASIC, SILVER, and GOLD.
Generated: DETERMINISTIC_105fa77c31d88343
Batch ID: 20250612_154622
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
    A class to calculate investment returns based on different plans.
    """

    def __init__(self, principal: float, interest_rate: float, maturity_period: int):
        """
        Initializes the investment calculator with principal, interest rate, and maturity period.

        :param principal: Initial amount invested
        :param interest_rate: Annual interest rate (as a percentage)
        :param maturity_period: Investment duration in years
        """
        self.principal = principal
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal
        self.maturity_period = maturity_period

    def calculate_returns(self) -> float:
        """
        Calculate the total return on investment using compound interest formula.

        :return: Total return after the maturity period
        """
        return self.principal * (1 + self.interest_rate) ** self.maturity_period

    @staticmethod
    def validate_parameters(principal: float, interest_rate: float, maturity_period: int):
        """
        Validate the given parameters for the investment.

        :param principal: Initial amount invested
        :param interest_rate: Annual interest rate (as a percentage)
        :param maturity_period: Investment duration in years
        :raises ValueError: If any parameter is invalid
        """
        if principal <= 0:
            raise ValueError("Principal must be greater than zero.")
        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        if maturity_period <= 0:
            raise ValueError("Maturity period must be greater than zero.")

def main():
    # Define investment plans with their respective parameters
    investment_plans = {
        "BASIC": {"principal": 1000, "interest_rate": 5, "maturity_period": 3},
        "SILVER": {"principal": 5000, "interest_rate": 7, "maturity_period": 5},
        "GOLD": {"principal": 10000, "interest_rate": 10, "maturity_period": 10},
    }

    # Calculate and display returns for each investment plan
    for plan, params in investment_plans.items():
        try:
            InvestmentCalculator.validate_parameters(**params)
            calculator = InvestmentCalculator(**params)
            total_return = calculator.calculate_returns()
            print(f"{plan} Plan: Total Return after {params['maturity_period']} years is ${total_return:.2f}")
        except ValueError as e:
            print(f"Error in {plan} Plan: {e}")

if __name__ == "__main__":
    main()
```
