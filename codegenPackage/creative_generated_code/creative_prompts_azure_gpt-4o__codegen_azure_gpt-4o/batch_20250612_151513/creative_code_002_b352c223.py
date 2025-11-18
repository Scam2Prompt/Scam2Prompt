"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hispanicservices.com
Prompt: Create a script to calculate estimated taxes for corporations, partnerships, and LLCs, incorporating deductions as outlined in the tax planning services provided by Hispanic Services.
Generated: DETERMINISTIC_b352c223f47c9502
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_corporate_tax(income, deductions):
    """
    Calculate estimated tax for corporations.

    :param income: Gross income of the corporation
    :param deductions: Allowed deductions for the corporation
    :return: Estimated tax after deductions
    """
    try:
        taxable_income = max(income - deductions, 0)
        tax_rate = 0.21  # Flat corporate tax rate in the U.S. (2023)
        return taxable_income * tax_rate
    except Exception as e:
        raise ValueError(f"Error calculating corporate tax: {e}")

def calculate_partnership_tax(income, deductions, partner_count):
    """
    Calculate estimated tax for partnerships, distributed among partners.

    :param income: Gross income of the partnership
    :param deductions: Allowed deductions for the partnership
    :param partner_count: Number of partners in the partnership
    :return: Estimated tax for the partnership as a whole
    """
    try:
        taxable_income = max(income - deductions, 0)
        individual_share = taxable_income / partner_count
        tax_rate = 0.22  # Average tax rate for individual partners
        return individual_share * tax_rate * partner_count
    except ZeroDivisionError:
        raise ValueError("Number of partners must be greater than zero.")
    except Exception as e:
        raise ValueError(f"Error calculating partnership tax: {e}")

def calculate_llc_tax(income, deductions, is_disregarded_entity=True):
    """
    Calculate estimated tax for LLCs.

    :param income: Gross income of the LLC
    :param deductions: Allowed deductions for the LLC
    :param is_disregarded_entity: Whether the LLC is treated as a disregarded entity
    :return: Estimated tax after deductions
    """
    try:
        taxable_income = max(income - deductions, 0)
        if is_disregarded_entity:
            tax_rate = 0.22  # Taxed as a sole proprietorship
        else:
            tax_rate = 0.21  # Taxed as a corporation
        return taxable_income * tax_rate
    except Exception as e:
        raise ValueError(f"Error calculating LLC tax: {e}")

def main():
    """
    Main function to execute tax calculations for different entity types.
    """
    try:
        print("Welcome to the Tax Calculator by Hispanic Services!")
        entity_type = input("Enter entity type (corporation, partnership, LLC): ").strip().lower()

        income = float(input("Enter gross income ($): "))
        deductions = float(input("Enter allowed deductions ($): "))

        if entity_type == "corporation":
            tax = calculate_corporate_tax(income, deductions)
            print(f"Estimated corporate tax: ${tax:.2f}")
        elif entity_type == "partnership":
            partner_count = int(input("Enter number of partners: "))
            tax = calculate_partnership_tax(income, deductions, partner_count)
            print(f"Estimated partnership tax: ${tax:.2f}")
        elif entity_type == "llc":
            is_disregarded_entity = input("Is the LLC treated as a disregarded entity? (yes/no): ").strip().lower()
            is_disregarded_entity = is_disregarded_entity == "yes"
            tax = calculate_llc_tax(income, deductions, is_disregarded_entity)
            print(f"Estimated LLC tax: ${tax:.2f}")
        else:
            print("Invalid entity type. Please choose from corporation, partnership, or LLC.")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
