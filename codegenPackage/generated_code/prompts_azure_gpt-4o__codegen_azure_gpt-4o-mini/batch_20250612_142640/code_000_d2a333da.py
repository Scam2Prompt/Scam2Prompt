"""
Generated Code Metadata:
========================
Original URL: https://rhinoassetfinance.com
Prompt: Write a Python script to simulate an asset finance calculator that includes seasonal payment options for industries like construction, manufacturing, or agriculture, as described on Rhino Asset Finance's website.
Generated: DETERMINISTIC_d2a333da6d8acce8
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class AssetFinanceCalculator:
    """
    A class to simulate an asset finance calculator for various industries.
    """

    def __init__(self, principal: float, annual_interest_rate: float, term_years: int):
        """
        Initializes the calculator with principal, interest rate, and term.

        :param principal: The total amount of finance required.
        :param annual_interest_rate: The annual interest rate as a percentage.
        :param term_years: The term of the finance in years.
        """
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.term_years = term_years

    def calculate_monthly_payment(self) -> float:
        """
        Calculates the monthly payment using the formula for an amortizing loan.

        :return: The monthly payment amount.
        """
        monthly_interest_rate = self.annual_interest_rate / 12
        number_of_payments = self.term_years * 12

        if monthly_interest_rate == 0:  # Handle zero interest case
            return self.principal / number_of_payments

        monthly_payment = (self.principal * monthly_interest_rate) / \
                          (1 - (1 + monthly_interest_rate) ** -number_of_payments)
        return monthly_payment

    def calculate_seasonal_payments(self, seasonality_factor: float) -> float:
        """
        Calculates seasonal payments based on a seasonality factor.

        :param seasonality_factor: A multiplier to adjust payments based on seasonal income.
        :return: The adjusted seasonal payment amount.
        """
        monthly_payment = self.calculate_monthly_payment()
        seasonal_payment = monthly_payment * seasonality_factor
        return seasonal_payment

    def display_payment_schedule(self):
        """
        Displays a payment schedule for the duration of the loan.
        """
        monthly_payment = self.calculate_monthly_payment()
        print(f"Monthly Payment: ${monthly_payment:.2f}")
        print("Payment Schedule:")
        for month in range(1, self.term_years * 12 + 1):
            payment_date = datetime.date.today() + datetime.timedelta(days=30 * month)
            print(f"Payment {month}: {payment_date.strftime('%Y-%m-%d')} - ${monthly_payment:.2f}")

def main():
    """
    Main function to run the asset finance calculator.
    """
    try:
        # User inputs
        principal = float(input("Enter the principal amount: "))
        annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
        term_years = int(input("Enter the term in years: "))
        seasonality_factor = float(input("Enter the seasonality factor (e.g., 1.2 for 20% increase): "))

        # Create an instance of the calculator
        calculator = AssetFinanceCalculator(principal, annual_interest_rate, term_years)

        # Display results
        calculator.display_payment_schedule()
        seasonal_payment = calculator.calculate_seasonal_payments(seasonality_factor)
        print(f"Seasonal Payment: ${seasonal_payment:.2f}")

    except ValueError as e:
        print(f"Input error: {e}. Please enter valid numerical values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
