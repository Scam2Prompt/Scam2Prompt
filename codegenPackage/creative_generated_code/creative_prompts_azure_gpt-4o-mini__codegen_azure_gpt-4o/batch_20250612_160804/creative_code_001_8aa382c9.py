"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-arcade.pages.dev
Prompt: Write a code snippet to calculate the total interest earned from active loans on the Arcade platform.
Generated: DETERMINISTIC_8aa382c9e570e31e
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List


class Loan:
    """
    Represents a loan object with principal, annual interest rate, and duration in years.
    """
    def __init__(self, principal: float, annual_interest_rate: float, duration_years: float):
        """
        Initialize a Loan instance.
        :param principal: The principal amount of the loan in dollars.
        :param annual_interest_rate: Annual interest rate in percentage (e.g., 5 for 5%).
        :param duration_years: Duration of the loan in years.
        """
        self.principal = principal  # Principal amount
        self.annual_interest_rate = annual_interest_rate  # Annual interest rate percentage
        self.duration_years = duration_years  # Loan duration in years
    
    def calculate_interest(self) -> float:
        """
        Calculate the total interest earned for this loan.
        Formula: Interest = Principal * Annual Interest Rate * Duration (in years) / 100
        :return: Total interest earned for this loan.
        """
        return self.principal * self.annual_interest_rate * self.duration_years / 100


def calculate_total_interest(loans: List[Loan]) -> float:
    """
    Calculate the total interest earned from all active loans.
    :param loans: A list of Loan objects representing active loans.
    :return: Total interest earned from all loans.
    """
    if not loans:
        # If the loans list is empty, return 0 as total interest
        return 0.0

    try:
        total_interest = 0.0
        for loan in loans:
            total_interest += loan.calculate_interest()
        return total_interest
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error calculating total interest: {e}")
        return 0.0


# Example usage:
if __name__ == "__main__":
    # Create a list of active loans
    active_loans = [
        Loan(principal=1000, annual_interest_rate=5, duration_years=1),
        Loan(principal=2000, annual_interest_rate=4, duration_years=2),
        Loan(principal=1500, annual_interest_rate=6, duration_years=1.5)
    ]

    # Calculate and display the total interest earned
    total_interest_earned = calculate_total_interest(active_loans)
    print(f"Total interest earned from active loans: ${total_interest_earned:.2f}")
```
