"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hispanicservices.com
Prompt: Develop a function that calculates estimated taxes for individuals based on the guidelines provided by Hispanic Services.
Generated: DETERMINISTIC_fe66a7379cad4e49
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Tax calculation function based on provided guidelines
# Developed for accurate, production-ready usage

def calculate_estimated_taxes(annual_income, filing_status, dependents=0):
    """
    Calculate estimated taxes based on provided income, filing status, and dependents.
    
    Args:
        annual_income (float): Annual income of the individual in dollars.
        filing_status (str): Filing status, must be one of "single", "married_jointly", or "head_of_household".
        dependents (int): Number of dependents claimed. Default is 0.
    
    Returns:
        float: Estimated tax in dollars.
    
    Raises:
        ValueError: If invalid inputs are provided for income, filing status, or dependents.
    """
    # Validate inputs
    if annual_income < 0:
        raise ValueError("Annual income must be a non-negative value.")
    if filing_status not in ["single", "married_jointly", "head_of_household"]:
        raise ValueError("Invalid filing status. Must be one of 'single', 'married_jointly', or 'head_of_household'.")
    if dependents < 0:
        raise ValueError("Number of dependents cannot be negative.")
    
    # Define tax brackets and rates based on filing status
    tax_brackets = {
        "single": [(0, 9875, 0.10), (9876, 40125, 0.12), (40126, 85525, 0.22), (85526, 163300, 0.24)],
        "married_jointly": [(0, 19750, 0.10), (19751, 80250, 0.12), (80251, 171050, 0.22), (171051, 326600, 0.24)],
        "head_of_household": [(0, 14100, 0.10), (14101, 53700, 0.12), (53701, 85500, 0.22), (85501, 163300, 0.24)]
    }
    
    # Standard deductions based on filing status
    standard_deductions = {
        "single": 12400,
        "married_jointly": 24800,
        "head_of_household": 18650
    }
    
    # Dependent credit
    dependent_credit = 2000  # $2,000 credit per dependent
    
    # Apply standard deduction
    taxable_income = annual_income - standard_deductions[filing_status]
    if taxable_income < 0:
        taxable_income = 0  # Ensure taxable income is not negative
    
    # Calculate taxes based on tax brackets
    tax_owed = 0.0
    for bracket in tax_brackets[filing_status]:
        lower_limit, upper_limit, rate = bracket
        if taxable_income > lower_limit:
            # Calculate the taxable amount within the current bracket
            taxable_amount = min(taxable_income, upper_limit) - lower_limit
            tax_owed += taxable_amount * rate
    
    # Apply dependent credit
    tax_owed -= dependents * dependent_credit
    if tax_owed < 0:
        tax_owed = 0  # Ensure taxes owed is not negative
    
    return round(tax_owed, 2)


# Example usage
if __name__ == "__main__":
    try:
        annual_income = 60000  # Example annual income
        filing_status = "single"  # Example filing status
        dependents = 2  # Example number of dependents
        estimated_tax = calculate_estimated_taxes(annual_income, filing_status, dependents)
        print(f"Estimated tax owed: ${estimated_tax}")
    except ValueError as e:
        print(f"Error: {e}")
```
