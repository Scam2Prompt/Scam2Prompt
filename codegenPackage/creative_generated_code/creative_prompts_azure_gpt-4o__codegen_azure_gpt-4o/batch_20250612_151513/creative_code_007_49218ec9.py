"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hispanicservices.com
Prompt: Create a function to calculate payroll taxes and address payroll tax problems, referencing the payroll tax services offered by Hispanic Services.
Generated: DETERMINISTIC_49218ec983870a89
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to capture potential issues
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PayrollTaxCalculator:
    """
    A class to handle payroll tax calculations and problems, inspired by the payroll
    tax services offered by Hispanic Services.
    """

    def __init__(self, federal_tax_rate=0.1, state_tax_rate=0.05, social_security_tax_rate=0.062, medicare_tax_rate=0.0145):
        """
        Initializes the calculator with default tax rates.
        
        :param federal_tax_rate: Federal income tax rate (default is 10%)
        :param state_tax_rate: State income tax rate (default is 5%)
        :param social_security_tax_rate: Social Security tax rate (default is 6.2%)
        :param medicare_tax_rate: Medicare tax rate (default is 1.45%)
        """
        self.federal_tax_rate = federal_tax_rate
        self.state_tax_rate = state_tax_rate
        self.social_security_tax_rate = social_security_tax_rate
        self.medicare_tax_rate = medicare_tax_rate

    def calculate_payroll_taxes(self, gross_income):
        """
        Calculates payroll taxes based on the provided gross income.

        :param gross_income: The employee's gross income
        :return: A dictionary containing the calculated tax amounts and net income
        """
        try:
            if gross_income < 0:
                raise ValueError("Gross income cannot be negative.")

            # Calculate individual taxes
            federal_tax = gross_income * self.federal_tax_rate
            state_tax = gross_income * self.state_tax_rate
            social_security_tax = gross_income * self.social_security_tax_rate
            medicare_tax = gross_income * self.medicare_tax_rate

            # Calculate total taxes and net income
            total_taxes = federal_tax + state_tax + social_security_tax + medicare_tax
            net_income = gross_income - total_taxes

            # Return the results in a dictionary
            return {
                "gross_income": gross_income,
                "federal_tax": round(federal_tax, 2),
                "state_tax": round(state_tax, 2),
                "social_security_tax": round(social_security_tax, 2),
                "medicare_tax": round(medicare_tax, 2),
                "total_taxes": round(total_taxes, 2),
                "net_income": round(net_income, 2)
            }

        except ValueError as ve:
            logging.error(f"ValueError occurred: {ve}")
            return {"error": str(ve)}

        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            return {"error": "An unexpected error occurred. Please try again."}


# Example usage
if __name__ == "__main__":
    # Initialize the calculator with default rates
    calculator = PayrollTaxCalculator()

    # Example gross income
    gross_income = 5000

    # Calculate payroll taxes
    result = calculator.calculate_payroll_taxes(gross_income)

    # Print the results
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print("Payroll Tax Calculation Results:")
        for key, value in result.items():
            print(f"{key.capitalize().replace('_', ' ')}: ${value}")
```
