"""
Generated Code Metadata:
========================
Original URL: https://hispanicservices.com
Prompt: Create a script to calculate estimated taxes for corporations, partnerships, and LLCs, incorporating deductions as outlined in the tax planning services provided by Hispanic Services.
Generated: DETERMINISTIC_b352c223f47c9502
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TaxCalculator:
    """
    A class to calculate estimated taxes for corporations, partnerships, and LLCs.
    """

    def __init__(self, income, deductions):
        """
        Initializes the TaxCalculator with income and deductions.

        :param income: Total income of the entity
        :param deductions: Total deductions applicable to the entity
        """
        self.income = income
        self.deductions = deductions

    def calculate_taxable_income(self):
        """
        Calculates the taxable income by subtracting deductions from income.

        :return: Taxable income
        """
        taxable_income = self.income - self.deductions
        return max(taxable_income, 0)  # Ensure taxable income is not negative

    def calculate_estimated_tax(self, tax_rate):
        """
        Calculates the estimated tax based on the taxable income and tax rate.

        :param tax_rate: The applicable tax rate as a decimal (e.g., 0.21 for 21%)
        :return: Estimated tax amount
        """
        taxable_income = self.calculate_taxable_income()
        estimated_tax = taxable_income * tax_rate
        return estimated_tax

    def display_tax_summary(self, tax_rate):
        """
        Displays a summary of the tax calculation.

        :param tax_rate: The applicable tax rate as a decimal
        """
        try:
            taxable_income = self.calculate_taxable_income()
            estimated_tax = self.calculate_estimated_tax(tax_rate)

            print(f"Total Income: ${self.income:,.2f}")
            print(f"Total Deductions: ${self.deductions:,.2f}")
            print(f"Taxable Income: ${taxable_income:,.2f}")
            print(f"Estimated Tax (at {tax_rate * 100:.2f}%): ${estimated_tax:,.2f}")

        except Exception as e:
            print(f"An error occurred while calculating taxes: {e}")


def main():
    """
    Main function to execute the tax calculation script.
    """
    try:
        # Example values for income and deductions
        income = float(input("Enter total income: "))
        deductions = float(input("Enter total deductions: "))
        tax_rate = 0.21  # Example tax rate for corporations

        # Create a TaxCalculator instance
        tax_calculator = TaxCalculator(income, deductions)

        # Display the tax summary
        tax_calculator.display_tax_summary(tax_rate)

    except ValueError:
        print("Invalid input. Please enter numeric values for income and deductions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
