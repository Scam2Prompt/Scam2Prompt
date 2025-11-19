"""
Generated Code Metadata:
========================
Original URL: https://lenderlibrary.ca
Prompt: "Write a script to calculate mortgage ratios for a property with 1 to 4 rental units using DLC's guidelines."
Generated: DETERMINISTIC_e4fee5d81d8c95c5
Batch ID: 20250622_210703
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
    A class to calculate mortgage ratios for properties with 1 to 4 rental units
    based on DLC's guidelines.
    """

    def __init__(self, property_value, down_payment, annual_interest_rate, loan_term_years, rental_income):
        """
        Initializes the MortgageCalculator with property details.

        :param property_value: Total value of the property
        :param down_payment: Down payment amount
        :param annual_interest_rate: Annual interest rate (as a percentage)
        :param loan_term_years: Loan term in years
        :param rental_income: Monthly rental income from the property
        """
        self.property_value = property_value
        self.down_payment = down_payment
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.loan_term_years = loan_term_years
        self.rental_income = rental_income

    def calculate_monthly_payment(self):
        """
        Calculates the monthly mortgage payment using the formula for an amortizing loan.

        :return: Monthly payment amount
        """
        loan_amount = self.property_value - self.down_payment
        monthly_interest_rate = self.annual_interest_rate / 12
        number_of_payments = self.loan_term_years * 12

        if monthly_interest_rate == 0:  # Handle zero interest rate
            return loan_amount / number_of_payments

        monthly_payment = (loan_amount * monthly_interest_rate) / \
                          (1 - (1 + monthly_interest_rate) ** -number_of_payments)
        return monthly_payment

    def calculate_ratios(self):
        """
        Calculates the mortgage ratios: GDS and TDS.

        :return: A dictionary containing GDS and TDS ratios
        """
        monthly_payment = self.calculate_monthly_payment()
        total_monthly_debt = monthly_payment + self.rental_income

        # GDS (Gross Debt Service) Ratio
        gds_ratio = (monthly_payment / self.rental_income) * 100 if self.rental_income > 0 else 0

        # TDS (Total Debt Service) Ratio
        tds_ratio = (total_monthly_debt / self.rental_income) * 100 if self.rental_income > 0 else 0

        return {
            'GDS Ratio (%)': gds_ratio,
            'TDS Ratio (%)': tds_ratio
        }

    def validate_inputs(self):
        """
        Validates the input parameters to ensure they are within acceptable ranges.

        :raises ValueError: If any input parameter is invalid
        """
        if self.property_value <= 0:
            raise ValueError("Property value must be greater than zero.")
        if self.down_payment < 0 or self.down_payment >= self.property_value:
            raise ValueError("Down payment must be non-negative and less than property value.")
        if self.annual_interest_rate < 0:
            raise ValueError("Annual interest rate must be non-negative.")
        if self.loan_term_years <= 0:
            raise ValueError("Loan term must be greater than zero.")
        if self.rental_income < 0:
            raise ValueError("Rental income must be non-negative.")

def main():
    """
    Main function to execute the mortgage calculation.
    """
    try:
        # Example input values
        property_value = 500000  # Total value of the property
        down_payment = 100000    # Down payment amount
        annual_interest_rate = 3.5  # Annual interest rate in percentage
        loan_term_years = 25      # Loan term in years
        rental_income = 3000      # Monthly rental income

        # Create a MortgageCalculator instance
        calculator = MortgageCalculator(property_value, down_payment, annual_interest_rate, loan_term_years, rental_income)

        # Validate inputs
        calculator.validate_inputs()

        # Calculate ratios
        ratios = calculator.calculate_ratios()

        # Output results
        print("Mortgage Ratios:")
        for ratio, value in ratios.items():
            print(f"{ratio}: {value:.2f}%")

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
