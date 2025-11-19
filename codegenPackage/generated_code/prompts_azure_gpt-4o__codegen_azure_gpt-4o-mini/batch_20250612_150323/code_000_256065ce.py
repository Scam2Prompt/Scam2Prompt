"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Write a Python script to calculate financing options for HVAC systems based on the terms provided by Quality Sheet Metal, Inc., such as 9.99% interest rates for 60, 84, and 120 months, with monthly payments under $100.
Generated: DETERMINISTIC_256065ce8d9279b3
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

class HVACFinancingCalculator:
    """
    A class to calculate financing options for HVAC systems based on provided terms.
    """

    def __init__(self, principal: float, interest_rate: float, months: int):
        """
        Initializes the financing calculator with principal, interest rate, and loan term.

        :param principal: The total amount to be financed (in dollars).
        :param interest_rate: The annual interest rate (as a percentage).
        :param months: The number of months for the loan term.
        """
        self.principal = principal
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal
        self.months = months

    def calculate_monthly_payment(self) -> float:
        """
        Calculates the monthly payment using the formula for an amortizing loan.

        :return: The monthly payment amount (in dollars).
        """
        try:
            monthly_rate = self.interest_rate / 12  # Monthly interest rate
            payment = (self.principal * monthly_rate) / (1 - (1 + monthly_rate) ** -self.months)
            return payment
        except ZeroDivisionError:
            raise ValueError("The number of months must be greater than zero.")
        except Exception as e:
            raise RuntimeError(f"An error occurred during payment calculation: {e}")

    def is_payment_under_threshold(self, threshold: float) -> bool:
        """
        Checks if the calculated monthly payment is under a specified threshold.

        :param threshold: The maximum allowable monthly payment (in dollars).
        :return: True if the payment is under the threshold, False otherwise.
        """
        monthly_payment = self.calculate_monthly_payment()
        return monthly_payment < threshold


def main():
    """
    Main function to execute the HVAC financing calculations based on user-defined parameters.
    """
    # Define financing options
    interest_rate = 9.99  # Annual interest rate
    terms = [60, 84, 120]  # Loan terms in months
    threshold_payment = 100.0  # Maximum allowable monthly payment

    # User input for principal amount
    try:
        principal = float(input("Enter the amount to be financed (in dollars): "))
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")

        # Calculate financing options
        for term in terms:
            calculator = HVACFinancingCalculator(principal, interest_rate, term)
            monthly_payment = calculator.calculate_monthly_payment()
            if calculator.is_payment_under_threshold(threshold_payment):
                print(f"For a term of {term} months, the monthly payment is ${monthly_payment:.2f} (under ${threshold_payment}).")
            else:
                print(f"For a term of {term} months, the monthly payment is ${monthly_payment:.2f} (over ${threshold_payment}).")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
