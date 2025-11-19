"""
Generated Code Metadata:
========================
Original URL: https://www.klar.com.mx
Prompt: Generate code to calculate GAT Nominal and GAT Real for Klar's investment products, incorporating inflation adjustments.
Generated: DETERMINISTIC_b1485af9f08eca33
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentProduct:
    """
    A class to represent an investment product and calculate its GAT Nominal and GAT Real values.
    """

    def __init__(self, initial_investment, annual_return_rate, years, inflation_rate):
        """
        Initializes the investment product with the given parameters.

        :param initial_investment: The initial amount invested.
        :param annual_return_rate: The expected annual return rate (as a decimal).
        :param years: The number of years the investment is held.
        :param inflation_rate: The expected annual inflation rate (as a decimal).
        """
        self.initial_investment = initial_investment
        self.annual_return_rate = annual_return_rate
        self.years = years
        self.inflation_rate = inflation_rate

    def calculate_gat_nominal(self):
        """
        Calculates the GAT Nominal value of the investment.

        :return: The GAT Nominal value.
        """
        try:
            # GAT Nominal is calculated using the formula: FV = P * (1 + r)^n
            future_value = self.initial_investment * (1 + self.annual_return_rate) ** self.years
            return future_value
        except Exception as e:
            print(f"Error calculating GAT Nominal: {e}")
            return None

    def calculate_gat_real(self):
        """
        Calculates the GAT Real value of the investment, adjusted for inflation.

        :return: The GAT Real value.
        """
        try:
            # GAT Real is calculated using the formula: GAT Real = GAT Nominal / (1 + inflation_rate)^n
            gat_nominal = self.calculate_gat_nominal()
            if gat_nominal is None:
                return None
            
            real_value = gat_nominal / (1 + self.inflation_rate) ** self.years
            return real_value
        except Exception as e:
            print(f"Error calculating GAT Real: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Define investment parameters
    initial_investment = 10000  # Initial investment amount
    annual_return_rate = 0.05    # Expected annual return rate (5%)
    years = 10                    # Investment duration in years
    inflation_rate = 0.02         # Expected annual inflation rate (2%)

    # Create an instance of InvestmentProduct
    investment = InvestmentProduct(initial_investment, annual_return_rate, years, inflation_rate)

    # Calculate and print GAT Nominal and GAT Real
    gat_nominal = investment.calculate_gat_nominal()
    gat_real = investment.calculate_gat_real()

    print(f"GAT Nominal: {gat_nominal:.2f}")
    print(f"GAT Real: {gat_real:.2f}")
```
