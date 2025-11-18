"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cart3.pages.dev
Prompt: Write Python code to automate the calculation of tax returns for Australian businesses, incorporating self-managed super funds, as described by Carthew Chau & Co.
Generated: DETERMINISTIC_329ac751085d4d53
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class TaxReturnCalculator:
    """
    A class to automate tax return calculation for Australian businesses
    including considerations for Self-Managed Super Funds (SMSFs).
    """

    def __init__(self, business_income, deductible_expenses, smsfs_contributions, tax_rate):
        """
        Initialize the TaxReturnCalculator with necessary inputs.

        :param business_income: Total business income (float).
        :param deductible_expenses: Total deductible expenses (float).
        :param smsfs_contributions: Total SMSFs contributions (float).
        :param tax_rate: Business tax rate (percentage as float, e.g., 0.30 for 30%)
        """
        self.business_income = business_income
        self.deductible_expenses = deductible_expenses
        self.smsfs_contributions = smsfs_contributions
        self.tax_rate = tax_rate

    def calculate_taxable_income(self):
        """
        Calculate the taxable income for the business.

        :return: Taxable income after deducting expenses and SMSFs contributions (float).
        """
        taxable_income = self.business_income - self.deductible_expenses - self.smsfs_contributions
        return max(taxable_income, 0)  # Ensure taxable income is not negative

    def calculate_tax_payable(self):
        """
        Calculate the tax payable based on taxable income and the tax rate.

        :return: Tax payable amount (float).
        """
        taxable_income = self.calculate_taxable_income()
        tax_payable = taxable_income * self.tax_rate
        return tax_payable

    def generate_tax_summary(self):
        """
        Generate a summary of the tax return calculation.

        :return: A dictionary summarizing the tax return details.
        """
        return {
            "Business Income": self.business_income,
            "Deductible Expenses": self.deductible_expenses,
            "SMSFs Contributions": self.smsfs_contributions,
            "Taxable Income": self.calculate_taxable_income(),
            "Tax Payable": self.calculate_tax_payable(),
            "Tax Rate": self.tax_rate
        }


# Error handling and input validation functions
def validate_positive_float(value, name):
    """
    Validate that the provided value is a positive float.

    :param value: Value to validate.
    :param name: Name of the value for error messages.
    :return: Validated value as float.
    :raises ValueError: If the value is not positive or cannot be converted to float.
    """
    try:
        value = float(value)
        if value < 0:
            raise ValueError(f"{name} must be a positive number.")
        return value
    except ValueError:
        raise ValueError(f"{name} must be a valid number.")


def main():
    """
    Main function to run the tax return calculator.
    """
    try:
        # Collect inputs
        print("Welcome to the Australian Business Tax Return Calculator.")
        business_income = validate_positive_float(input("Enter total business income: "), "Business Income")
        deductible_expenses = validate_positive_float(input("Enter total deductible expenses: "), "Deductible Expenses")
        smsfs_contributions = validate_positive_float(input("Enter total SMSFs contributions: "), "SMSFs Contributions")

        # Tax rate for Australian businesses (example: 30%)
        tax_rate = 0.30

        # Create calculator object
        calculator = TaxReturnCalculator(business_income, deductible_expenses, smsfs_contributions, tax_rate)

        # Generate and display tax summary
        print("\nTax Return Summary:")
        summary = calculator.generate_tax_summary()
        for key, value in summary.items():
            print(f"{key}: ${value:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        # Catch unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Display program start time
    print(f"Program started at {datetime.datetime.now()}\n")
    main()
    # Display program end time
    print(f"\nProgram ended at {datetime.datetime.now()}")
```
