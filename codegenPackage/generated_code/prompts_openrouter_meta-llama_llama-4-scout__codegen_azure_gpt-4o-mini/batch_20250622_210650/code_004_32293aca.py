"""
Generated Code Metadata:
========================
Original URL: https://tsmwealth.co.za
Prompt: Write a function to calculate the benefits of a long-term investment plan, taking into account factors such as interest rates, inflation, and compounding frequency, as described in TSM Wealth's investment services.
Generated: DETERMINISTIC_32293acaf253ec31
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentPlan:
    """
    A class to represent a long-term investment plan and calculate its benefits.
    """

    def __init__(self, principal: float, annual_rate: float, years: int, inflation_rate: float, compounding_frequency: int):
        """
        Initializes the investment plan with the given parameters.

        :param principal: Initial amount of money invested (float).
        :param annual_rate: Annual interest rate (as a decimal, e.g., 0.05 for 5%) (float).
        :param years: Number of years the money is invested (int).
        :param inflation_rate: Annual inflation rate (as a decimal, e.g., 0.02 for 2%) (float).
        :param compounding_frequency: Number of times interest is compounded per year (int).
        """
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")
        if not (0 <= annual_rate <= 1):
            raise ValueError("Annual interest rate must be between 0 and 1.")
        if years < 0:
            raise ValueError("Number of years must be non-negative.")
        if not (0 <= inflation_rate <= 1):
            raise ValueError("Inflation rate must be between 0 and 1.")
        if compounding_frequency <= 0:
            raise ValueError("Compounding frequency must be a positive integer.")

        self.principal = principal
        self.annual_rate = annual_rate
        self.years = years
        self.inflation_rate = inflation_rate
        self.compounding_frequency = compounding_frequency

    def calculate_future_value(self) -> float:
        """
        Calculates the future value of the investment after the specified number of years.

        :return: Future value of the investment (float).
        """
        # Future Value formula: FV = P * (1 + r/n)^(nt)
        future_value = self.principal * (1 + self.annual_rate / self.compounding_frequency) ** (self.compounding_frequency * self.years)
        return future_value

    def calculate_inflation_adjusted_value(self) -> float:
        """
        Calculates the inflation-adjusted future value of the investment.

        :return: Inflation-adjusted future value (float).
        """
        future_value = self.calculate_future_value()
        # Adjusting for inflation: Real Value = FV / (1 + inflation_rate)^years
        inflation_adjusted_value = future_value / ((1 + self.inflation_rate) ** self.years)
        return inflation_adjusted_value

    def calculate_benefits(self) -> dict:
        """
        Calculates the benefits of the investment plan, including future value and inflation-adjusted value.

        :return: A dictionary containing future value and inflation-adjusted value.
        """
        try:
            future_value = self.calculate_future_value()
            inflation_adjusted_value = self.calculate_inflation_adjusted_value()
            return {
                "Future Value": future_value,
                "Inflation Adjusted Value": inflation_adjusted_value
            }
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating benefits: {e}")


# Example usage:
if __name__ == "__main__":
    try:
        investment = InvestmentPlan(principal=10000, annual_rate=0.05, years=20, inflation_rate=0.02, compounding_frequency=12)
        benefits = investment.calculate_benefits()
        print("Investment Benefits:")
        print(f"Future Value: ${benefits['Future Value']:.2f}")
        print(f"Inflation Adjusted Value: ${benefits['Inflation Adjusted Value']:.2f}")
    except Exception as e:
        print(f"Error: {e}")
```
