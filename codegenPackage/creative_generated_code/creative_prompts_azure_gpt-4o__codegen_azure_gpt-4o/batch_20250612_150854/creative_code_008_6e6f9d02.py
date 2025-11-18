"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediategains.org
Prompt: Write a program that simulates portfolio growth using ImmediateGains' investment strategies, including risk management techniques to minimize market volatility.
Generated: DETERMINISTIC_6e6f9d02e08efb99
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class InvestmentPortfolio:
    """
    A class to simulate portfolio growth using ImmediateGains' investment strategies
    with risk management techniques to minimize market volatility.
    """

    def __init__(self, initial_balance: float, risk_tolerance: str):
        """
        Initialize the portfolio with an initial balance and risk tolerance.

        :param initial_balance: Initial amount of money in the portfolio.
        :param risk_tolerance: Risk tolerance level ('low', 'medium', 'high').
        """
        self.balance = initial_balance
        if risk_tolerance not in ['low', 'medium', 'high']:
            raise ValueError("Risk tolerance must be 'low', 'medium', or 'high'.")
        self.risk_tolerance = risk_tolerance

    def simulate_growth(self, years: int):
        """
        Simulate portfolio growth over a given number of years.

        :param years: Number of years to simulate.
        :return: Final portfolio balance after simulation.
        """
        for year in range(1, years + 1):
            # Calculate annual return based on risk tolerance
            annual_return = self._generate_annual_return()

            # Apply annual return to the current balance
            self.balance *= (1 + annual_return)

            print(f"Year {year}: Annual Return = {annual_return:.2%}, Balance = ${self.balance:.2f}")

            # Risk management: Reduce exposure if balance exceeds a threshold
            self._apply_risk_management()

        return self.balance

    def _generate_annual_return(self) -> float:
        """
        Generate an annual return based on the risk tolerance.

        :return: Annual return percentage as a decimal.
        """
        if self.risk_tolerance == 'low':
            return random.uniform(0.02, 0.05)  # Low risk: 2% to 5% annual return
        elif self.risk_tolerance == 'medium':
            return random.uniform(0.03, 0.10)  # Medium risk: 3% to 10% annual return
        elif self.risk_tolerance == 'high':
            return random.uniform(-0.05, 0.15)  # High risk: -5% (loss) to 15% annual return

    def _apply_risk_management(self):
        """
        Apply risk management techniques to minimize volatility and secure profits.
        """
        # Example risk management strategy: When balance exceeds $1M, lower risk tolerance
        if self.balance > 1_000_000:
            print("Risk Management Triggered: Lowering risk tolerance.")
            self.risk_tolerance = 'low'

# Main program
def main():
    try:
        # Initialize portfolio with $100,000 and medium risk tolerance
        initial_balance = 100_000
        risk_tolerance = 'medium'

        portfolio = InvestmentPortfolio(initial_balance, risk_tolerance)

        # Simulate growth for 10 years
        final_balance = portfolio.simulate_growth(years=10)

        print(f"\nFinal Portfolio Balance: ${final_balance:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
