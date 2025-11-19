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
class FinancingCalculator:
    """
    A class to represent a financing calculator for HVAC services.
    This calculator applies a fixed interest rate for financing options.
    """

    def __init__(self, principal, years, interest_rate=0.0999):
        """
        Initializes the FinancingCalculator with the principal amount,
        number of years for financing, and the interest rate.

        :param principal: The total amount to be financed.
        :param years: The number of years over which the financing will occur.
        :param interest_rate: The interest rate for the financing (default is 9.99%).
        """
        self.principal = principal
        self.years = years
        self.interest_rate = interest_rate
        self.validate_input()

    def validate_input(self):
        """
        Validates the input values for principal and years.
        Raises ValueError if inputs are invalid.
        """
        if self.principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if self.years <= 0:
            raise ValueError("Number of years must be greater than zero.")

    def calculate_monthly_payment(self):
        """
        Calculates the monthly payment using the amortization formula.

        :return: The monthly payment amount.
        """
        monthly_rate = self.interest_rate / 12
        num_payments = self.years * 12

        # Avoid division by zero by checking if monthly_rate is zero
        if monthly_rate == 0:
            return self.principal / num_payments

        monthly_payment = (self.principal * monthly_rate) / (1 - (1 + monthly_rate) ** -num_payments)
        return monthly_payment

    def total_payment(self):
        """
        Calculates the total payment over the financing period.

        :return: The total payment amount.
        """
        return self.calculate_monthly_payment() * self.years * 12

    def total_interest(self):
        """
        Calculates the total interest paid over the financing period.

        :return: The total interest amount.
        """
        return self.total_payment() - self.principal

if __name__ == "__main__":
    try:
        # Example usage of the FinancingCalculator
        principal_amount = 10000  # Example principal amount
        financing_years = 5       # Example financing period in years

        calculator = FinancingCalculator(principal_amount, financing_years)
        
        print(f"Monthly Payment: ${calculator.calculate_monthly_payment():.2f}")
        print(f"Total Payment: ${calculator.total_payment():.2f}")
        print(f"Total Interest: ${calculator.total_interest():.2f}")

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
