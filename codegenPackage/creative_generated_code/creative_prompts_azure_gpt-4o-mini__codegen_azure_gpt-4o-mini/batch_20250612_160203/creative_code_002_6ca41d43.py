"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://epiccoin-miners.ltd
Prompt: Generate a code snippet that simulates the growth of capital in an investment account based on the investment plans provided by epiccoin-miners.ltd, including calculations for different deposit amounts.
Generated: DETERMINISTIC_6ca41d43065be841
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentAccount:
    """
    A class to simulate the growth of capital in an investment account.

    Attributes:
    ----------
    principal : float
        The initial amount of money invested.
    annual_rate : float
        The annual interest rate (as a decimal).
    years : int
        The number of years the money is invested for.

    Methods:
    -------
    calculate_growth():
        Calculates the future value of the investment.
    """

    def __init__(self, principal: float, annual_rate: float, years: int):
        """
        Initializes the InvestmentAccount with principal, annual_rate, and years.

        Parameters:
        ----------
        principal : float
            Initial investment amount.
        annual_rate : float
            Annual interest rate (as a decimal).
        years : int
            Duration of investment in years.
        """
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")
        if not (0 <= annual_rate <= 1):
            raise ValueError("Annual rate must be between 0 and 1.")
        if years < 0:
            raise ValueError("Years must be non-negative.")

        self.principal = principal
        self.annual_rate = annual_rate
        self.years = years

    def calculate_growth(self) -> float:
        """
        Calculates the future value of the investment using compound interest formula.

        Returns:
        -------
        float
            The future value of the investment after the specified number of years.
        """
        future_value = self.principal * (1 + self.annual_rate) ** self.years
        return future_value


def main():
    """
    Main function to demonstrate investment growth calculation.
    """
    try:
        # Example parameters for the investment account
        principal_amount = 1000.0  # Initial investment
        annual_interest_rate = 0.05  # 5% annual interest
        investment_duration = 10  # Invest for 10 years

        # Create an instance of InvestmentAccount
        investment_account = InvestmentAccount(principal_amount, annual_interest_rate, investment_duration)

        # Calculate future value
        future_value = investment_account.calculate_growth()

        # Display the result
        print(f"Future value of the investment: ${future_value:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
