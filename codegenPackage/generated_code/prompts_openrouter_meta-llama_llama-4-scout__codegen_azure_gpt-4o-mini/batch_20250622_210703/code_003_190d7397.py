"""
Generated Code Metadata:
========================
Original URL: https://cidautos.com
Prompt: "Generate a Python code snippet to create a simple calculator for financing options on vehicles like the Kia Sorento at Cid Autos."
Generated: DETERMINISTIC_190d73976e75ff8a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class VehicleFinancingCalculator:
    """
    A simple calculator for financing options on vehicles.
    This class calculates monthly payments based on loan amount, interest rate, and loan term.
    """

    def __init__(self, loan_amount: float, annual_interest_rate: float, loan_term_years: int):
        """
        Initializes the financing calculator with loan details.

        :param loan_amount: Total amount of the loan (in dollars)
        :param annual_interest_rate: Annual interest rate (as a percentage)
        :param loan_term_years: Loan term in years
        """
        self.loan_amount = loan_amount
        self.annual_interest_rate = annual_interest_rate
        self.loan_term_years = loan_term_years

    def calculate_monthly_payment(self) -> float:
        """
        Calculates the monthly payment using the formula for an amortizing loan.

        :return: Monthly payment amount
        """
        try:
            # Convert annual interest rate to a monthly rate and decimal
            monthly_interest_rate = (self.annual_interest_rate / 100) / 12
            # Total number of payments
            total_payments = self.loan_term_years * 12

            # Calculate monthly payment using the formula
            monthly_payment = (self.loan_amount * monthly_interest_rate) / \
                              (1 - (1 + monthly_interest_rate) ** -total_payments)

            return monthly_payment
        except ZeroDivisionError:
            raise ValueError("Annual interest rate must be greater than zero.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating the monthly payment: {e}")

    def display_payment_schedule(self):
        """
        Displays the payment schedule for the loan.
        """
        try:
            monthly_payment = self.calculate_monthly_payment()
            print(f"Monthly Payment: ${monthly_payment:.2f}")

            # Displaying a simple payment schedule
            print("\nPayment Schedule:")
            for month in range(1, self.loan_term_years * 12 + 1):
                print(f"Month {month}: ${monthly_payment:.2f}")
        except Exception as e:
            print(f"Error displaying payment schedule: {e}")


if __name__ == "__main__":
    # Example usage
    try:
        # Initialize the calculator with example values
        loan_amount = 30000  # Example loan amount for a Kia Sorento
        annual_interest_rate = 5.0  # Example interest rate
        loan_term_years = 5  # Example loan term in years

        calculator = VehicleFinancingCalculator(loan_amount, annual_interest_rate, loan_term_years)
        calculator.display_payment_schedule()
    except Exception as e:
        print(f"An error occurred: {e}")
```
