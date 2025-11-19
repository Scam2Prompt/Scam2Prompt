"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morpho.orgmorpho.org
Prompt: Create a function that calculates the borrowing costs on Morpho based on collateral and market rates, using their lending platform features.
Generated: DETERMINISTIC_10155b93a8bc09e6
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MorphoLending:
    """
    A class to represent the Morpho lending platform for calculating borrowing costs.
    """

    def __init__(self, collateral_amount: float, market_rate: float):
        """
        Initializes the MorphoLending instance with collateral amount and market rate.

        :param collateral_amount: Amount of collateral provided (in the base currency)
        :param market_rate: Current market interest rate (as a decimal, e.g. 0.05 for 5%)
        """
        self.collateral_amount = collateral_amount
        self.market_rate = market_rate

    def calculate_borrowing_costs(self, loan_amount: float, duration_days: int) -> float:
        """
        Calculates the borrowing costs based on collateral, market rates, and loan duration.

        :param loan_amount: Amount of loan being borrowed (in the base currency)
        :param duration_days: Duration of the loan in days
        :return: Total borrowing costs (in the base currency)
        :raises ValueError: If loan_amount or duration_days are non-positive
        """
        if loan_amount <= 0:
            raise ValueError("Loan amount must be greater than 0.")
        if duration_days <= 0:
            raise ValueError("Duration in days must be greater than 0.")

        # Calculate the daily borrowing cost
        daily_rate = self.market_rate / 365
        total_borrowing_cost = loan_amount * daily_rate * duration_days

        return total_borrowing_cost

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize with collateral amount and market rate
        lending_platform = MorphoLending(collateral_amount=1000.0, market_rate=0.05)

        # Calculate borrowing costs for a loan of 500.0 over 30 days
        loan_amount = 500.0
        duration_days = 30
        costs = lending_platform.calculate_borrowing_costs(loan_amount, duration_days)

        print(f"Borrowing costs for ${loan_amount} over {duration_days} days: ${costs:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
