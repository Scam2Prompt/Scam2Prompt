"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toolfix.online
Prompt: Develop a tool to calculate income tax liability for FY 2024–25, using the Income Tax Calculator described on the IFSC Finder webpage.
Generated: DETERMINISTIC_dcfb89d3322a0af4
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

# Income tax calculator for FY 2024–25
def calculate_income_tax(income, age):
    """
    Calculate income tax liability based on the taxpayer's annual income and age.

    Parameters:
        income (float): Annual taxable income of the taxpayer.
        age (int): Age of the taxpayer.

    Returns:
        float: Calculated tax liability.
    """

    try:
        # Validate inputs
        if income < 0:
            raise ValueError("Income cannot be negative.")
        if age < 0:
            raise ValueError("Age cannot be negative.")

        # Define tax slabs for FY 2024–25 (New Regime)
        tax_slabs = [
            (0, 300000, 0),       # Income up to ₹3,00,000: No tax
            (300001, 600000, 0.05),  # ₹3,00,001 to ₹6,00,000: 5% tax
            (600001, 900000, 0.1),   # ₹6,00,001 to ₹9,00,000: 10% tax
            (900001, 1200000, 0.15), # ₹9,00,001 to ₹12,00,000: 15% tax
            (1200001, 1500000, 0.2), # ₹12,00,001 to ₹15,00,000: 20% tax
            (1500001, float('inf'), 0.3)  # Above ₹15,00,000: 30% tax
        ]

        # Senior citizen benefits (age 60+)
        exemption_limit = 300000
        if age >= 60:
            exemption_limit = 500000

        # Calculate tax liability
        taxable_income = max(0, income - exemption_limit)
        tax_liability = 0

        for slab_start, slab_end, rate in tax_slabs:
            # If income falls within the current slab
            if taxable_income <= slab_start:
                break
            slab_income = min(taxable_income, slab_end) - slab_start
            tax_liability += slab_income * rate

        return tax_liability
    
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return None

# Main function to capture user input and calculate tax
def main():
    """
    Entry point to the Income Tax Calculator application.
    """
    try:
        # Capture user input
        print("Income Tax Calculator for FY 2024–25")
        income = float(input("Enter your annual taxable income (in ₹): "))
        age = int(input("Enter your age: "))

        # Calculate tax
        tax = calculate_income_tax(income, age)

        if tax is not None:
            print(f"Your calculated income tax liability is: ₹{tax:.2f}")
        else:
            print("Could not calculate tax due to an error.")

    except ValueError:
        print("Invalid input. Please enter numeric values for income and age.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

# Execute the program
if __name__ == "__main__":
    main()
```
