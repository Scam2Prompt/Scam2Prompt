"""
Generated Code Metadata:
========================
Original URL: https://immediatexport.co
Prompt: Generate a code snippet that demonstrates how to create a simple investment calculator, taking into account factors like inflation, interest rates, and risk tolerance, as discussed in the Starlight Stakemarket content.
Generated: DETERMINISTIC_9032d67318460e21
Batch ID: 20250622_211310
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
    A simple investment calculator that estimates the future value of an investment
    based on initial investment amount, annual interest rate, inflation rate, and
    investment duration in years.
    """

    def __init__(self, principal: float, annual_interest_rate: float, 
                 inflation_rate: float, years: int, risk_tolerance: str):
        """
        Initializes the InvestmentCalculator with the given parameters.

        :param principal: Initial investment amount (float)
        :param annual_interest_rate: Annual interest rate as a percentage (float)
        :param inflation_rate: Annual inflation rate as a percentage (float)
        :param years: Number of years to invest (int)
        :param risk_tolerance: Risk tolerance level (str)
        """
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.inflation_rate = inflation_rate / 100  # Convert percentage to decimal
        self.years = years
        self.risk_tolerance = risk_tolerance

    def calculate_future_value(self) -> float:
        """
        Calculates the future value of the investment after accounting for interest and inflation.

        :return: Future value of the investment (float)
        """
        try:
            # Calculate future value using the formula: FV = P * (1 + r)^n
            future_value = self.principal * (1 + self.annual_interest_rate) ** self.years
            return future_value
        except Exception as e:
            print(f"Error calculating future value: {e}")
            return 0.0

    def adjust_for_inflation(self, future_value: float) -> float:
        """
        Adjusts the future value for inflation to determine the real value of the investment.

        :param future_value: Future value of the investment (float)
        :return: Real value of the investment after inflation (float)
        """
        try:
            # Calculate real value using the formula: Real Value = FV / (1 + inflation_rate)^n
            real_value = future_value / (1 + self.inflation_rate) ** self.years
            return real_value
        except Exception as e:
            print(f"Error adjusting for inflation: {e}")
            return 0.0

    def display_investment_summary(self):
        """
        Displays a summary of the investment calculation including future value and real value.
        """
        future_value = self.calculate_future_value()
        real_value = self.adjust_for_inflation(future_value)

        print(f"Investment Summary:")
        print(f"Initial Investment: ${self.principal:.2f}")
        print(f"Annual Interest Rate: {self.annual_interest_rate * 100:.2f}%")
        print(f"Inflation Rate: {self.inflation_rate * 100:.2f}%")
        print(f"Investment Duration: {self.years} years")
        print(f"Risk Tolerance: {self.risk_tolerance}")
        print(f"Future Value: ${future_value:.2f}")
        print(f"Real Value after Inflation: ${real_value:.2f}")


# Example usage
if __name__ == "__main__":
    # Create an instance of InvestmentCalculator
    investment_calculator = InvestmentCalculator(
        principal=10000,  # Initial investment amount
        annual_interest_rate=5,  # Annual interest rate in percentage
        inflation_rate=2,  # Annual inflation rate in percentage
        years=10,  # Investment duration in years
        risk_tolerance='Moderate'  # Risk tolerance level
    )

    # Display the investment summary
    investment_calculator.display_investment_summary()
```
