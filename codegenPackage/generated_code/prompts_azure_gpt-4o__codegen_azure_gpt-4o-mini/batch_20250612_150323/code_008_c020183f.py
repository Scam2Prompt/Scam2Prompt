"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Create a Python script to calculate monthly payments for HVAC systems based on the TVA Heat Pump Program details provided by Quality Sheet Metal, Inc., including "no money down" and 10-year payment plans.
Generated: DETERMINISTIC_c020183f80a7f063
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class HVACPaymentCalculator:
    """
    A class to calculate monthly payments for HVAC systems based on the TVA Heat Pump Program.
    """

    def __init__(self, total_cost, interest_rate=0.0, loan_term_years=10):
        """
        Initializes the HVACPaymentCalculator with the total cost, interest rate, and loan term.

        :param total_cost: Total cost of the HVAC system
        :param interest_rate: Annual interest rate (as a decimal, e.g., 0.05 for 5%)
        :param loan_term_years: Duration of the loan in years
        """
        self.total_cost = total_cost
        self.interest_rate = interest_rate
        self.loan_term_years = loan_term_years

    def calculate_monthly_payment(self):
        """
        Calculates the monthly payment using the formula for an amortizing loan.

        :return: Monthly payment amount
        """
        try:
            # Monthly interest rate
            monthly_rate = self.interest_rate / 12
            # Total number of payments
            total_payments = self.loan_term_years * 12
            
            if self.interest_rate == 0:
                # If interest rate is 0, simply divide total cost by number of payments
                monthly_payment = self.total_cost / total_payments
            else:
                # Monthly payment formula
                monthly_payment = (self.total_cost * monthly_rate) / (1 - (1 + monthly_rate) ** -total_payments)

            return monthly_payment
        except ZeroDivisionError:
            print("Error: Division by zero encountered in payment calculation.")
            sys.exit(1)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)

def main():
    """
    Main function to execute the HVAC payment calculation.
    """
    try:
        # Example values for the HVAC system
        total_cost = float(input("Enter the total cost of the HVAC system: "))
        interest_rate = float(input("Enter the annual interest rate (as a percentage, e.g., 5 for 5%): ")) / 100
        loan_term_years = 10  # Fixed loan term as per the request

        # Create an instance of the HVACPaymentCalculator
        calculator = HVACPaymentCalculator(total_cost, interest_rate, loan_term_years)

        # Calculate the monthly payment
        monthly_payment = calculator.calculate_monthly_payment()

        # Output the result
        print(f"The monthly payment for the HVAC system is: ${monthly_payment:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values for cost and interest rate.")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
