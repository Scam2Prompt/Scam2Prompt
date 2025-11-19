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
def calculate_estimated_taxes(income: float, filing_status: str, deductions: float = 0.0) -> float:
    """
    Calculate estimated taxes based on income, filing status, and deductions.
    
    Parameters:
    - income (float): The total income of the individual.
    - filing_status (str): The filing status of the individual ('single', 'married', 'head_of_household').
    - deductions (float): The deductions applicable to the individual (default is 0.0).
    
    Returns:
    - float: The estimated tax liability.
    
    Raises:
    - ValueError: If income is negative or if filing_status is invalid.
    """
    
    # Validate inputs
    if income < 0:
        raise ValueError("Income cannot be negative.")
    
    valid_statuses = ['single', 'married', 'head_of_household']
    if filing_status not in valid_statuses:
        raise ValueError(f"Invalid filing status. Must be one of {valid_statuses}.")
    
    # Define tax brackets and rates based on filing status
    tax_brackets = {
        'single': [(0, 9875, 0.10), (9876, 40125, 0.12), (40126, 85525, 0.22), (85526, float('inf'), 0.24)],
        'married': [(0, 19750, 0.10), (19751, 80250, 0.12), (80251, 171050, 0.22), (171051, float('inf'), 0.24)],
        'head_of_household': [(0, 14100, 0.10), (14101, 53700, 0.12), (53701, 85500, 0.22), (85501, float('inf'), 0.24)]
    }
    
    # Calculate taxable income
    taxable_income = income - deductions
    if taxable_income < 0:
        taxable_income = 0  # Prevent negative taxable income
    
    # Initialize tax liability
    tax_liability = 0.0
    
    # Calculate tax based on brackets
    for bracket in tax_brackets[filing_status]:
        lower_bound, upper_bound, rate = bracket
        
        if taxable_income > lower_bound:
            # Calculate the amount subject to the current tax rate
            income_in_bracket = min(taxable_income, upper_bound) - lower_bound
            tax_liability += income_in_bracket * rate
    
    return tax_liability


# Example usage (uncomment to use):
# try:
#     estimated_tax = calculate_estimated_taxes(income=50000, filing_status='single', deductions=12000)
#     print(f"Estimated Tax: ${estimated_tax:.2f}")
# except ValueError as e:
#     print(f"Error calculating taxes: {e}")
```
