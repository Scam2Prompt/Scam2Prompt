"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qualitysheetmetalincorporated.org
Prompt: How can I implement a financing calculator for HVAC services that reflects the 9.99% financing options available at Quality Sheet Metal, Inc.?
Generated: DETERMINISTIC_5e66bf65c8669aca
Batch ID: 20250612_135105
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class FinancingCalculator:
    """
    A class to calculate financing options for HVAC services.
    This calculator is specifically designed for a 9.99% annual interest rate.
    """

    def __init__(self, amount, annual_interest_rate=9.99, loan_term_years=5):
        """
        Initializes the FinancingCalculator.

        :param amount: The principal amount for the loan (in USD).
        :param annual_interest_rate: The annual interest rate (percentage). Default is 9.99%.
        :param loan_term_years: The duration of the loan (in years). Default is 5 years.
        """
        self.amount = amount
        self.annual_interest_rate = annual_interest_rate
        self.loan_term_years = loan_term_years

    def calculate_monthly_payment(self):
        """
        Calculates the monthly payment for the loan using the formula for an amortizing loan.

        Formula:
        M = P * (r * (1 + r)^n) / ((1 + r)^n - 1)

        Where:
        M = monthly payment
        P = principal loan amount
        r = monthly interest rate (annual_interest_rate / 12 / 100)
        n = total number of payments (loan_term_years * 12)

        :return: The monthly payment amount (in USD).
        """
        try:
            # Convert annual interest rate to monthly interest rate
            monthly_interest_rate = self.annual_interest_rate / 12 / 100
            # Calculate the total number of payments
            total_payments = self.loan_term_years * 12

            # Calculate the monthly payment using the formula
            numerator = self.amount * monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments
            denominator = (1 + monthly_interest_rate) ** total_payments - 1
            monthly_payment = numerator / denominator

            return round(monthly_payment, 2)
        except ZeroDivisionError:
            # Handle edge cases where division by zero may occur
            raise ValueError("Invalid loan term or interest rate provided.")
        except Exception as e:
            # Catch-all for any other exceptions
            raise RuntimeError(f"An error occurred while calculating the monthly payment: {str(e)}")

    def calculate_total_payment(self):
        """
        Calculates the total payment made over the life of the loan.

        :return: The total payment amount (in USD).
        """
        try:
            monthly_payment = self.calculate_monthly_payment()
            total_payments = self.loan_term_years * 12

            # Total payment is simply monthly payment * total number of payments
            return round(monthly_payment * total_payments, 2)
        except Exception as e:
            # Catch-all for any exceptions
            raise RuntimeError(f"An error occurred while calculating the total payment: {str(e)}")

    def calculate_total_interest_paid(self):
        """
        Calculates the total interest paid over the life of the loan.

        :return: The total interest paid (in USD).
        """
        try:
            total_payment = self.calculate_total_payment()
            total_interest = total_payment - self.amount  # Total interest is the total payment minus the principal amount
            return round(total_interest, 2)
        except Exception as e:
            # Catch-all for any exceptions
            raise RuntimeError(f"An error occurred while calculating the total interest paid: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        # Input: Loan amount, annual interest rate, and loan term
        loan_amount = float(input("Enter the loan amount (in USD): "))
        loan_term_years = int(input("Enter the loan term (in years): "))

        # Create an instance of FinancingCalculator
        calculator = FinancingCalculator(amount=loan_amount, loan_term_years=loan_term_years)

        # Calculate and display results
        monthly_payment = calculator.calculate_monthly_payment()
        total_payment = calculator.calculate_total_payment()
        total_interest = calculator.calculate_total_interest_paid()

        print(f"\nFinancing Details:")
        print(f"Loan Amount: ${loan_amount}")
        print(f"Annual Interest Rate: {calculator.annual_interest_rate}%")
        print(f"Loan Term: {loan_term_years} years")
        print(f"Monthly Payment: ${monthly_payment}")
        print(f"Total Payment: ${total_payment}")
        print(f"Total Interest Paid: ${total_interest}")
    except ValueError as ve:
        print(f"Input Error: {str(ve)}")
    except RuntimeError as re:
        print(f"Calculation Error: {str(re)}")
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
```
