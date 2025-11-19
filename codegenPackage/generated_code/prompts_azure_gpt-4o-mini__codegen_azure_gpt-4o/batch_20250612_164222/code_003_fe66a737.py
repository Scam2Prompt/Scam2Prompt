"""
Generated Code Metadata:
========================
Original URL: https://hispanicservices.com
Prompt: Develop a function that calculates estimated taxes for individuals based on the guidelines provided by Hispanic Services.
Generated: DETERMINISTIC_fe66a7379cad4e49
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tax_calculator.py

def calculate_estimated_taxes(income, filing_status):
    """
    Calculate estimated taxes for individuals based on income and filing status.

    Parameters:
        income (float): The individual's annual income in USD.
        filing_status (str): The individual's filing status. 
                             Accepted values: 'single', 'married', 'head_of_household'.

    Returns:
        float: The estimated tax amount in USD.

    Raises:
        ValueError: If income is negative or filing_status is invalid.
    """
    # Validate input
    if income < 0:
        raise ValueError("Income cannot be negative.")
    if filing_status not in ['single', 'married', 'head_of_household']:
        raise ValueError("Invalid filing status. Must be 'single', 'married', or 'head_of_household'.")

    # Tax brackets and rates based on filing status
    tax_brackets = {
        'single': [
            (0, 9875, 0.10),
            (9876, 40125, 0.12),
            (40126, 85525, 0.22),
            (85526, 163300, 0.24),
            (163301, 207350, 0.32),
            (207351, 518400, 0.35),
            (518401, float('inf'), 0.37)
        ],
        'married': [
            (0, 19750, 0.10),
            (19751, 80250, 0.12),
            (80251, 171050, 0.22),
            (171051, 326600, 0.24),
            (326601, 414700, 0.32),
            (414701, 622050, 0.35),
            (622051, float('inf'), 0.37)
        ],
        'head_of_household': [
            (0, 14100, 0.10),
            (14101, 53700, 0.12),
            (53701, 85500, 0.22),
            (85501, 163300, 0.24),
            (163301, 207350, 0.32),
            (207351, 518400, 0.35),
            (518401, float('inf'), 0.37)
        ]
    }

    # Calculate taxes based on brackets
    tax_amount = 0.0
    for bracket in tax_brackets[filing_status]:
        lower, upper, rate = bracket
        if income > lower:
            taxable_income = min(income, upper) - lower
            tax_amount += taxable_income * rate

    return round(tax_amount, 2)


# Example usage
if __name__ == "__main__":
    try:
        # Input values
        annual_income = 75000  # Example income
        status = 'single'      # Example filing status

        # Calculate taxes
        estimated_tax = calculate_estimated_taxes(annual_income, status)
        print(f"Estimated tax for an income of ${annual_income} and filing status '{status}': ${estimated_tax}")
    except ValueError as e:
        print(f"Error: {e}")
```
