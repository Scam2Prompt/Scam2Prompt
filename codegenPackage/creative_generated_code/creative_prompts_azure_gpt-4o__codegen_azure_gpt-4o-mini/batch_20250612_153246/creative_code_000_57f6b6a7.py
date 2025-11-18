"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lenderlibrary.ca
Prompt: Write a Python script that calculates mortgage ratios for 1 to 4 rental units based on guidelines provided by Dominion Lending's "Biblio-Hypothécaire" portal. Include options for variable-to-fixed mortgage conversion.
Generated: DETERMINISTIC_57f6b6a73a8039e6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class MortgageCalculator:
    def __init__(self, purchase_price, down_payment, interest_rate, amortization_period, rental_income, variable_to_fixed=False):
        """
        Initialize the MortgageCalculator with necessary parameters.
        
        :param purchase_price: Total price of the property
        :param down_payment: Down payment amount
        :param interest_rate: Annual interest rate (as a percentage)
        :param amortization_period: Length of the mortgage in years
        :param rental_income: Total monthly rental income
        :param variable_to_fixed: Whether to convert from variable to fixed rate
        """
        self.purchase_price = purchase_price
        self.down_payment = down_payment
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal
        self.amortization_period = amortization_period
        self.rental_income = rental_income
        self.variable_to_fixed = variable_to_fixed

    def calculate_mortgage_payment(self):
        """
        Calculate the monthly mortgage payment using the formula for an amortizing loan.
        
        :return: Monthly mortgage payment
        """
        # Principal amount
        principal = self.purchase_price - self.down_payment
        monthly_rate = self.interest_rate / 12  # Monthly interest rate
        number_of_payments = self.amortization_period * 12  # Total number of payments

        if monthly_rate == 0:  # Handle zero interest rate case
            return principal / number_of_payments

        # Monthly payment calculation using the annuity formula
        monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -number_of_payments)
        return monthly_payment

    def calculate_ratio(self):
        """
        Calculate the mortgage ratio based on rental income and monthly mortgage payment.
        
        :return: Mortgage ratio
        """
        try:
            mortgage_payment = self.calculate_mortgage_payment()
            ratio = (mortgage_payment / self.rental_income) * 100 if self.rental_income > 0 else float('inf')
            return ratio
        except ZeroDivisionError:
            print("Error: Rental income cannot be zero.")
            sys.exit(1)

    def convert_variable_to_fixed(self, new_fixed_rate):
        """
        Convert the variable interest rate to a fixed rate if applicable.
        
        :param new_fixed_rate: New fixed interest rate (as a percentage)
        """
        if self.variable_to_fixed:
            self.interest_rate = new_fixed_rate / 100  # Convert percentage to decimal

def main():
    # User input for mortgage calculation
    try:
        purchase_price = float(input("Enter the purchase price of the property: "))
        down_payment = float(input("Enter the down payment amount: "))
        interest_rate = float(input("Enter the annual interest rate (in %): "))
        amortization_period = int(input("Enter the amortization period (in years): "))
        rental_income = float(input("Enter the total monthly rental income: "))
        variable_to_fixed = input("Convert variable rate to fixed? (yes/no): ").strip().lower() == 'yes'

        if variable_to_fixed:
            new_fixed_rate = float(input("Enter the new fixed interest rate (in %): "))
        else:
            new_fixed_rate = None

    except ValueError:
        print("Error: Invalid input. Please enter numeric values for the amounts and rates.")
        sys.exit(1)

    # Create a MortgageCalculator instance
    calculator = MortgageCalculator(
        purchase_price,
        down_payment,
        interest_rate,
        amortization_period,
        rental_income,
        variable_to_fixed
    )

    # Convert variable to fixed if applicable
    if variable_to_fixed and new_fixed_rate is not None:
        calculator.convert_variable_to_fixed(new_fixed_rate)

    # Calculate and display results
    monthly_payment = calculator.calculate_mortgage_payment()
    ratio = calculator.calculate_ratio()

    print(f"Monthly Mortgage Payment: ${monthly_payment:.2f}")
    print(f"Mortgage Ratio: {ratio:.2f}%")

if __name__ == "__main__":
    main()
```
