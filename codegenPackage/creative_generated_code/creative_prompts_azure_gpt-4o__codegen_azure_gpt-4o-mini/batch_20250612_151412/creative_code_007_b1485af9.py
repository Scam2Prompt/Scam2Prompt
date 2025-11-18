"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.klar.com.mx
Prompt: Generate code to calculate GAT Nominal and GAT Real for Klar's investment products, incorporating inflation adjustments.
Generated: DETERMINISTIC_b1485af9f08eca33
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentProduct:
    """
    A class to represent an investment product and calculate its GAT Nominal and GAT Real values.
    """

    def __init__(self, initial_investment: float, annual_return_rate: float, years: int, inflation_rate: float):
        """
        Initializes an InvestmentProduct instance.

        :param initial_investment: The initial amount invested.
        :param annual_return_rate: The expected annual return rate (as a decimal).
        :param years: The number of years the investment is held.
        :param inflation_rate: The expected annual inflation rate (as a decimal).
        """
        self.initial_investment = initial_investment
        self.annual_return_rate = annual_return_rate
        self.years = years
        self.inflation_rate = inflation_rate

    def calculate_gat_nominal(self) -> float:
        """
        Calculate the GAT Nominal (Gross Annualized Total) based on the initial investment and annual return rate.

        :return: The GAT Nominal value.
        """
        try:
            final_amount = self.initial_investment * (1 + self.annual_return_rate) ** self.years
            gat_nominal = final_amount - self.initial_investment
            return gat_nominal
        except Exception as e:
            print(f"Error calculating GAT Nominal: {e}")
            return 0.0

    def calculate_gat_real(self) -> float:
        """
        Calculate the GAT Real (adjusted for inflation) based on the GAT Nominal.

        :return: The GAT Real value.
        """
        try:
            gat_nominal = self.calculate_gat_nominal()
            real_value = gat_nominal / ((1 + self.inflation_rate) ** self.years)
            return real_value
        except Exception as e:
            print(f"Error calculating GAT Real: {e}")
            return 0.0

    def display_results(self):
        """
        Display the calculated GAT Nominal and GAT Real values.
        """
        gat_nominal = self.calculate_gat_nominal()
        gat_real = self.calculate_gat_real()
        
        print(f"GAT Nominal: {gat_nominal:.2f}")
        print(f"GAT Real: {gat_real:.2f}")


# Example usage
if __name__ == "__main__":
    # Define investment parameters
    initial_investment = 10000  # Initial investment amount
    annual_return_rate = 0.05    # Expected annual return rate of 5%
    years = 10                    # Investment duration in years
    inflation_rate = 0.02        # Expected inflation rate of 2%

    # Create an instance of InvestmentProduct
    investment = InvestmentProduct(initial_investment, annual_return_rate, years, inflation_rate)

    # Display the GAT Nominal and GAT Real
    investment.display_results()
```
