"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maestrofinance.co.uk
Prompt: Write code to implement a growth guarantee scheme with flexible terms and low-interest rates, enabling businesses to expand as described on Maestro Finance.
Generated: DETERMINISTIC_30a376e2c8d6ea47
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Growth Guarantee Scheme Implementation
# This program implements a flexible growth guarantee scheme for businesses
# with low-interest rates, enabling expansion. It follows best practices for
# readability, maintainability, and error handling.

import datetime

class GrowthGuaranteeScheme:
    """
    A class to represent the Growth Guarantee Scheme.

    Attributes:
        business_name (str): Name of the business applying for the scheme.
        principal_amount (float): Initial loan amount provided to the business.
        interest_rate (float): Annual interest rate (percentage).
        term_years (int): Loan term in years.
        start_date (datetime.date): Start date of the scheme.
    """

    def __init__(self, business_name, principal_amount, interest_rate, term_years):
        """
        Constructor to initialize the Growth Guarantee Scheme.

        Args:
            business_name (str): The name of the business.
            principal_amount (float): The loan amount in USD.
            interest_rate (float): The interest rate (percentage).
            term_years (int): Duration of the loan in years.
        """
        if principal_amount <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if interest_rate <= 0 or interest_rate > 10:
            raise ValueError("Interest rate must be between 0 and 10%.")
        if term_years <= 0 or term_years > 30:
            raise ValueError("Term years must be between 1 and 30.")

        self.business_name = business_name
        self.principal_amount = principal_amount
        self.interest_rate = interest_rate
        self.term_years = term_years
        self.start_date = datetime.date.today()

    def calculate_total_repayment(self):
        """
        Calculate the total repayment amount at the end of the loan term.

        Returns:
            float: Total repayment amount in USD.
        """
        # Using the formula for compound interest: A = P * (1 + r)^n
        total_repayment = self.principal_amount * (1 + self.interest_rate / 100) ** self.term_years
        return round(total_repayment, 2)

    def calculate_annual_repayment(self):
        """
        Calculate the annual repayment amount.

        Returns:
            float: Annual repayment amount in USD.
        """
        total_repayment = self.calculate_total_repayment()
        annual_repayment = total_repayment / self.term_years
        return round(annual_repayment, 2)

    def display_scheme_details(self):
        """
        Display details of the scheme.
        """
        print("Growth Guarantee Scheme Details:")
        print(f"Business Name: {self.business_name}")
        print(f"Principal Amount: ${self.principal_amount}")
        print(f"Interest Rate: {self.interest_rate}%")
        print(f"Loan Term: {self.term_years} years")
        print(f"Start Date: {self.start_date}")
        print(f"Total Repayment Amount: ${self.calculate_total_repayment()}")
        print(f"Annual Repayment Amount: ${self.calculate_annual_repayment()}")

# Example usage:
if __name__ == "__main__":
    try:
        # Create an instance of the Growth Guarantee Scheme
        scheme = GrowthGuaranteeScheme(
            business_name="Maestro Finance",
            principal_amount=100000,  # $100,000
            interest_rate=5,         # 5% annual interest
            term_years=10            # 10 years loan term
        )

        # Display the scheme details
        scheme.display_scheme_details()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
