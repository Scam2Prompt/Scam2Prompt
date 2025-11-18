"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carthewchautaxreports.pages.dev
Prompt: Write Python code to calculate tax returns for Australian clients, incorporating the principles outlined by Carthew Chau & Co's tax and accounting services.
Generated: DETERMINISTIC_ee01cb390d3f572b
Batch ID: 20250612_152615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Australian Tax Return Calculator
--------------------------------
This script calculates tax returns for Australian clients based on income, deductions, and applicable tax rates.
The logic is based on general principles of Australian taxation but may need to be adjusted for specific rules.
Ensure compliance with Carthew Chau & Co's guidelines for tax and accounting services.
"""

# Import necessary libraries
import sys


def calculate_taxable_income(gross_income, deductions):
    """
    Calculate taxable income by subtracting deductions from gross income.

    :param gross_income: Float - Total income before deductions
    :param deductions: Float - Total allowable deductions
    :return: Float - Taxable income
    """
    if gross_income < 0 or deductions < 0:
        raise ValueError("Gross income and deductions must be non-negative.")
    return max(0, gross_income - deductions)  # Taxable income cannot be negative


def calculate_income_tax(taxable_income):
    """
    Calculate income tax based on Australian tax brackets for individuals (FY 2023-2024).
    
    :param taxable_income: Float - Taxable income after deductions
    :return: Float - Income tax amount
    """
    if taxable_income <= 0:
        return 0

    # Australian Tax Brackets (2023-2024 - Example)
    tax_brackets = [
        (18200, 0),                  # No tax for income up to $18,200
        (45000, 0.19),               # 19% for income between $18,201 and $45,000
        (120000, 0.325),             # 32.5% for income between $45,001 and $120,000
        (180000, 0.37),              # 37% for income between $120,001 and $180,000
        (float('inf'), 0.45)         # 45% for income above $180,000
    ]

    tax = 0
    previous_limit = 0

    for bracket_limit, rate in tax_brackets:
        if taxable_income <= bracket_limit:
            tax += (taxable_income - previous_limit) * rate
            break
        else:
            tax += (bracket_limit - previous_limit) * rate
            previous_limit = bracket_limit

    return round(tax, 2)


def calculate_tax_return(gross_income, deductions, tax_withheld):
    """
    Calculate the tax return or payable amount.

    :param gross_income: Float - Total income before deductions
    :param deductions: Float - Total allowable deductions
    :param tax_withheld: Float - Tax already withheld by the employer
    :return: Tuple(Float, String) - Tax return/payable amount and a message
    """
    # Compute taxable income
    taxable_income = calculate_taxable_income(gross_income, deductions)

    # Compute income tax
    income_tax = calculate_income_tax(taxable_income)

    # Calculate tax return or payable
    result = tax_withheld - income_tax

    if result > 0:
        return result, "You are eligible for a tax return."
    elif result < 0:
        return abs(result), "You owe additional tax."
    else:
        return 0, "No tax return or payable. You have balanced your tax."


def main():
    """
    Main function to accept user input and calculate tax returns.
    """
    try:
        # Gather user inputs
        print("Welcome to the Australian Tax Return Calculator!")
        gross_income = float(input("Enter your gross income (AUD): "))
        deductions = float(input("Enter your total deductions (AUD): "))
        tax_withheld = float(input("Enter tax withheld by your employer (AUD): "))

        # Calculate the tax return/payable
        amount, message = calculate_tax_return(gross_income, deductions, tax_withheld)

        # Display results
        print("\n--- Tax Return Results ---")
        print(f"Amount: ${amount:.2f}")
        print(f"Message: {message}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for script execution
if __name__ == "__main__":
    main()
```
