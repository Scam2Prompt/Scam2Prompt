"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitum.cz
Prompt: Generate a Python script to calculate tax optimization strategies for a company, referencing Arbitum Consulting's approach to tax advisory and compliance.
Generated: DETERMINISTIC_3450217b3926fa98
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Tax Optimization Script for Companies
Inspired by Arbitum Consulting's approach to tax advisory and compliance.

This script calculates tax optimization strategies based on company income, expenses,
and applicable tax regulations. It provides recommendations for minimizing tax liability 
while ensuring compliance.
"""

import json

# Constants
TAX_RATES = {
    "corporate": 0.25,  # Corporate tax rate (25%)
    "capital_gains": 0.20,  # Capital gains tax rate (20%)
    "reduced_rate": 0.15   # Reduced rate for qualifying expenses (15%)
}

# Sample data for deductions (customize for your needs)
DEDUCTIONS = {
    "research_and_development": 0.30,  # Deduction percentage for R&D expenses
    "charitable_donations": 0.20,      # Deduction percentage for donations
    "energy_efficiency": 0.10          # Deduction percentage for energy-efficient upgrades
}

# Helper Functions
def calculate_taxable_income(total_income, total_expenses):
    """
    Calculate taxable income by subtracting expenses from income.
    :param total_income: The company's total annual income.
    :param total_expenses: The company's total annual expenses.
    :return: Taxable income.
    """
    return total_income - total_expenses

def apply_deductions(taxable_income, deduction_categories):
    """
    Apply deductions to taxable income based on eligible categories.
    :param taxable_income: The initial taxable income.
    :param deduction_categories: Dictionary of expense categories with their amounts.
    :return: Adjusted taxable income after deductions.
    """
    total_deductions = 0
    for category, amount in deduction_categories.items():
        if category in DEDUCTIONS:
            deduction_rate = DEDUCTIONS[category]
            total_deductions += amount * deduction_rate
    return taxable_income - total_deductions

def calculate_tax(taxable_income, tax_rate):
    """
    Calculate tax liability based on taxable income and tax rate.
    :param taxable_income: The adjusted taxable income after deductions.
    :param tax_rate: Applicable tax rate.
    :return: Tax liability.
    """
    return taxable_income * tax_rate

def get_optimized_tax_strategy(total_income, total_expenses, deduction_categories):
    """
    Generate tax optimization strategy for a company.
    :param total_income: The company's total annual income.
    :param total_expenses: The company's total annual expenses.
    :param deduction_categories: Dictionary of expense categories with their amounts.
    :return: Dictionary with optimization results.
    """
    try:
        # Step 1: Calculate taxable income
        taxable_income = calculate_taxable_income(total_income, total_expenses)
        
        # Step 2: Apply deductions
        adjusted_income = apply_deductions(taxable_income, deduction_categories)
        
        # Step 3: Calculate tax liability
        corporate_tax_liability = calculate_tax(adjusted_income, TAX_RATES["corporate"])
        
        # Step 4: Provide optimization recommendations
        return {
            "original_taxable_income": taxable_income,
            "adjusted_taxable_income": adjusted_income,
            "corporate_tax_liability": corporate_tax_liability,
            "recommendations": [
                "Increase R&D expenses to maximize deductions.",
                "Consider charitable contributions to reduce taxable income.",
                "Invest in energy-efficient upgrades for potential tax benefits."
            ]
        }
    except Exception as e:
        return {"error": str(e)}

# Main function
def main():
    """
    Main entry point for the script.
    """
    try:
        # Input data (replace with actual company data or user input)
        total_income = 1000000  # Example: $1,000,000 total income
        total_expenses = 500000  # Example: $500,000 total expenses
        deduction_categories = {
            "research_and_development": 100000,  # $100,000 spent on R&D
            "charitable_donations": 50000,       # $50,000 in donations
            "energy_efficiency": 20000           # $20,000 spent on energy-efficient upgrades
        }

        # Calculate optimized tax strategy
        strategy = get_optimized_tax_strategy(total_income, total_expenses, deduction_categories)

        # Output results in a readable format
        print("=== Tax Optimization Results ===")
        print(json.dumps(strategy, indent=4))

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the script
if __name__ == "__main__":
    main()
```
