"""
Generated Code Metadata:
========================
Original URL: https://guillenrealtygrouphtx.com
Prompt: Generate a mortgage calculator code snippet that can be integrated into a real estate website, providing users with estimated mortgage payments based on home price, down payment, and interest rate.
Generated: DETERMINISTIC_60f44bea365632e1
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MortgageCalculator:
    """
    A class to calculate monthly mortgage payments.

    Attributes:
        home_price (float): The total price of the home.
        down_payment (float): The down payment amount.
        annual_interest_rate (float): The annual interest rate (as a percentage).
        loan_term_years (int): The term of the loan in years.
    """

    def __init__(self, home_price, down_payment, annual_interest_rate, loan_term_years):
        """
        Initializes the MortgageCalculator with the given parameters.

        Args:
            home_price (float): The total price of the home.
            down_payment (float): The down payment amount.
            annual_interest_rate (float): The annual interest rate (as a percentage).
            loan_term_years (int): The term of the loan in years.
        """
        self.home_price = home_price
        self.down_payment = down_payment
        self.annual_interest_rate = annual_interest_rate
        self.loan_term_years = loan_term_years

    def calculate_monthly_payment(self):
        """
        Calculates the monthly mortgage payment.

        Returns:
            float: The estimated monthly payment.
        """
        try:
            # Calculate the loan amount
            loan_amount = self.home_price - self.down_payment
            
            # Convert annual interest rate to a monthly and decimal format
            monthly_interest_rate = (self.annual_interest_rate / 100) / 12
            
            # Total number of payments
            total_payments = self.loan_term_years * 12
            
            # Calculate monthly payment using the formula
            if monthly_interest_rate == 0:  # Handle case of zero interest rate
                monthly_payment = loan_amount / total_payments
            else:
                monthly_payment = (loan_amount * monthly_interest_rate) / \
                                  (1 - (1 + monthly_interest_rate) ** -total_payments)
            
            return round(monthly_payment, 2)  # Round to 2 decimal places for currency format

        except ZeroDivisionError:
            raise ValueError("The interest rate cannot be zero.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating the mortgage payment: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        # Sample input values
        home_price = 300000  # Total price of the home
        down_payment = 60000  # Down payment amount
        annual_interest_rate = 3.5  # Annual interest rate in percentage
        loan_term_years = 30  # Loan term in years

        # Create an instance of MortgageCalculator
        mortgage_calculator = MortgageCalculator(home_price, down_payment, annual_interest_rate, loan_term_years)

        # Calculate and print the monthly payment
        monthly_payment = mortgage_calculator.calculate_monthly_payment()
        print(f"Estimated Monthly Payment: ${monthly_payment}")

    except Exception as e:
        print(f"Error: {e}")
```
