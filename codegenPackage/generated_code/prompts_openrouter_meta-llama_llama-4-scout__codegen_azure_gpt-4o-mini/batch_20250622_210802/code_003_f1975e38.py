"""
Generated Code Metadata:
========================
Original URL: https://cooperativacooprometa.com
Prompt: Write a Python script to calculate loan credits for educational purposes based on the services described by Cooperativa Cooprometa.
Generated: DETERMINISTIC_f1975e385cd78b34
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class LoanCalculator:
    """
    A class to calculate loan credits for educational purposes based on the services
    described by Cooperativa Cooprometa.
    """

    def __init__(self, principal, annual_interest_rate, years):
        """
        Initializes the LoanCalculator with principal, annual interest rate, and loan term in years.

        :param principal: The total amount of the loan
        :param annual_interest_rate: The annual interest rate (as a percentage)
        :param years: The term of the loan in years
        """
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.years = years

    def calculate_monthly_payment(self):
        """
        Calculates the monthly payment for the loan.

        :return: The monthly payment amount
        """
        try:
            monthly_interest_rate = self.annual_interest_rate / 12
            number_of_payments = self.years * 12

            # Monthly payment formula
            monthly_payment = (self.principal * monthly_interest_rate) / \
                              (1 - (1 + monthly_interest_rate) ** -number_of_payments)

            return monthly_payment
        except ZeroDivisionError:
            print("Error: The annual interest rate cannot be zero.")
            sys.exit(1)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)

    def total_payment(self):
        """
        Calculates the total payment over the life of the loan.

        :return: The total payment amount
        """
        monthly_payment = self.calculate_monthly_payment()
        total_payment = monthly_payment * self.years * 12
        return total_payment

    def total_interest(self):
        """
        Calculates the total interest paid over the life of the loan.

        :return: The total interest amount
        """
        total_payment = self.total_payment()
        total_interest = total_payment - self.principal
        return total_interest

def main():
    """
    Main function to execute the loan calculation.
    """
    try:
        # Input values for loan calculation
        principal = float(input("Enter the loan amount (principal): "))
        annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
        years = int(input("Enter the term of the loan in years: "))

        # Create a LoanCalculator instance
        loan_calculator = LoanCalculator(principal, annual_interest_rate, years)

        # Calculate and display results
        monthly_payment = loan_calculator.calculate_monthly_payment()
        total_payment = loan_calculator.total_payment()
        total_interest = loan_calculator.total_interest()

        print(f"\nMonthly Payment: ${monthly_payment:.2f}")
        print(f"Total Payment over {years} years: ${total_payment:.2f}")
        print(f"Total Interest Paid: ${total_interest:.2f}")

    except ValueError:
        print("Error: Please enter valid numeric values.")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
