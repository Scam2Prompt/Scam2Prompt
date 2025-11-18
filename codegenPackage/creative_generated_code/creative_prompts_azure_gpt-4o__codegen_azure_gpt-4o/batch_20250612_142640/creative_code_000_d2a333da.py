"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinoassetfinance.com
Prompt: Write a Python script to simulate an asset finance calculator that includes seasonal payment options for industries like construction, manufacturing, or agriculture, as described on Rhino Asset Finance's website.
Generated: DETERMINISTIC_d2a333da6d8acce8
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math


class AssetFinanceCalculator:
    """
    A class to simulate an asset finance calculator with seasonal payment options
    suitable for industries like construction, manufacturing, or agriculture.
    """

    def __init__(self, loan_amount, annual_interest_rate, loan_term_years, seasonal_months=None):
        """
        Initialize the calculator.
        
        :param loan_amount: Total loan amount in currency.
        :param annual_interest_rate: Annual interest rate as a percentage (e.g., 5.5 for 5.5%).
        :param loan_term_years: Loan term in years.
        :param seasonal_months: List of months where payments are seasonal (e.g., [3, 4, 5] for March-May).
        """
        self.loan_amount = loan_amount
        self.annual_interest_rate = annual_interest_rate / 100
        self.loan_term_years = loan_term_years
        self.seasonal_months = seasonal_months if seasonal_months else []

    def calculate_monthly_payment(self):
        """
        Calculate the fixed monthly payment using the annuity formula.
        
        :return: Monthly payment amount.
        """
        monthly_rate = self.annual_interest_rate / 12
        total_months = self.loan_term_years * 12

        # Annuity formula for monthly payments
        try:
            monthly_payment = (self.loan_amount * monthly_rate * math.pow(1 + monthly_rate, total_months)) / \
                              (math.pow(1 + monthly_rate, total_months) - 1)
            return monthly_payment
        except ZeroDivisionError:
            raise ValueError("Interest rate or loan term must be greater than zero.")

    def simulate_payments(self):
        """
        Simulate and display a payment schedule with seasonal payment adjustments.
        
        :return: List of tuples containing payment schedule details (month, payment amount).
        """
        monthly_payment = self.calculate_monthly_payment()
        payment_schedule = []
        
        for month in range(1, self.loan_term_years * 12 + 1):
            year = (month - 1) // 12 + 1  # Calculate the year of the loan
            month_of_year = (month - 1) % 12 + 1  # Calculate the month within the year
            
            # Apply seasonal adjustment: Reduce payments by 50% during seasonal months
            if month_of_year in self.seasonal_months:
                adjusted_payment = monthly_payment * 0.5
            else:
                adjusted_payment = monthly_payment
            
            payment_schedule.append((year, month_of_year, round(adjusted_payment, 2)))
        
        return payment_schedule


def main():
    """
    Main function to demonstrate the asset finance calculator.
    """
    print("Welcome to the Asset Finance Calculator!")
    
    # Input collection with basic validation
    try:
        loan_amount = float(input("Enter the total loan amount (e.g., 50000): "))
        annual_interest_rate = float(input("Enter the annual interest rate as a percentage (e.g., 5.5): "))
        loan_term_years = int(input("Enter the loan term in years (e.g., 5): "))
        seasonal_months_input = input("Enter seasonal months (comma-separated, e.g., 3,4,5): ")
        
        # Convert seasonal months to a list of integers
        seasonal_months = [int(month) for month in seasonal_months_input.split(",") if month.isdigit()]
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    # Create the calculator instance
    calculator = AssetFinanceCalculator(
        loan_amount=loan_amount,
        annual_interest_rate=annual_interest_rate,
        loan_term_years=loan_term_years,
        seasonal_months=seasonal_months
    )

    # Calculate the payment schedule
    try:
        payment_schedule = calculator.simulate_payments()
    except ValueError as e:
        print(f"Error during calculation: {e}")
        return

    # Display the payment schedule
    print("\nPayment Schedule:")
    print(f"{'Year':<6}{'Month':<8}{'Payment ($)':<12}")
    print("-" * 26)
    for year, month, payment in payment_schedule:
        print(f"{year:<6}{month:<8}{payment:<12.2f}")


if __name__ == "__main__":
    main()
```
