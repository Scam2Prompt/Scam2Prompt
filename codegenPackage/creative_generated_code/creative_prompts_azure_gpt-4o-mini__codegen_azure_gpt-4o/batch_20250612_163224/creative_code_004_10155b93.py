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
import math

class MorphoBorrowingCostCalculator:
    """
    A class to calculate borrowing costs on Morpho's lending platform.
    """

    def __init__(self, collateral_amount, collateral_rate, borrow_amount, borrow_rate):
        """
        Initialize the calculator with necessary parameters.

        :param collateral_amount: The amount of collateral provided (in USD).
        :param collateral_rate: The interest rate earned on the collateral (in % per year).
        :param borrow_amount: The amount borrowed (in USD).
        :param borrow_rate: The interest rate paid on the borrowed amount (in % per year).
        """
        self.collateral_amount = collateral_amount
        self.collateral_rate = collateral_rate
        self.borrow_amount = borrow_amount
        self.borrow_rate = borrow_rate

    def calculate_borrowing_cost(self):
        """
        Calculate and return the net borrowing cost per year.

        :return: Net borrowing cost per year (in USD).
        :raises ValueError: If input values are invalid.
        """
        # Validate inputs
        if self.collateral_amount < 0 or self.borrow_amount < 0:
            raise ValueError("Collateral and borrow amounts must be non-negative.")
        if self.collateral_rate < 0 or self.borrow_rate < 0:
            raise ValueError("Interest rates must be non-negative.")

        # Calculate the interest earned on collateral
        collateral_interest = (self.collateral_amount * self.collateral_rate) / 100

        # Calculate the interest paid on the borrowed amount
        borrow_interest = (self.borrow_amount * self.borrow_rate) / 100

        # Net borrowing cost is the interest paid minus the interest earned
        net_borrowing_cost = borrow_interest - collateral_interest
        return net_borrowing_cost


def main():
    """
    Main function to demonstrate the borrowing cost calculation.
    """
    try:
        # Example inputs
        collateral_amount = 10000  # USD
        collateral_rate = 2.5      # % per year
        borrow_amount = 5000       # USD
        borrow_rate = 6.0          # % per year

        # Create the calculator instance
        calculator = MorphoBorrowingCostCalculator(
            collateral_amount, collateral_rate, borrow_amount, borrow_rate
        )

        # Calculate borrowing cost
        borrowing_cost = calculator.calculate_borrowing_cost()
        print(f"The net borrowing cost per year is: ${borrowing_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
