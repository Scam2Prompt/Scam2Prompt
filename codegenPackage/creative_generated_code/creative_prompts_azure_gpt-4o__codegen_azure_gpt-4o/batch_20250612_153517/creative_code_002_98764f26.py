"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fesit.cl
Prompt: Develop a script using Python to simulate the impact of proposed Chilean tax reforms on different income groups, incorporating FESIT's principles of equity and justice.
Generated: DETERMINISTIC_98764f266b7c7436
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

# Simulate Chilean tax reforms and their impact on income groups
def simulate_tax_reform(income_groups, tax_rates, reforms):
    """
    Simulates the impact of tax reforms on different income groups.

    Parameters:
        income_groups (list of dict): Each dictionary contains 'group_name', 'income', and 'size'.
        tax_rates (dict): Contains 'current' and 'proposed' tax rate structures as mappings of income thresholds to rates.
        reforms (dict): Contains the proposed changes in exemptions, deductions, and brackets.

    Returns:
        pd.DataFrame: A DataFrame showing the impact of the reform on each income group.
    """
    results = []

    for group in income_groups:
        group_name = group['group_name']
        income = group['income']
        size = group['size']

        # Calculate current tax
        current_tax = calculate_tax(income, tax_rates['current'])
        
        # Apply proposed reforms
        adjusted_income = apply_reforms(income, reforms)
        proposed_tax = calculate_tax(adjusted_income, tax_rates['proposed'])

        # Equity and justice principles
        tax_difference = proposed_tax - current_tax
        per_capita_difference = tax_difference / size

        # Append results
        results.append({
            'Group Name': group_name,
            'Current Income': income,
            'Adjusted Income': adjusted_income,
            'Current Tax': current_tax,
            'Proposed Tax': proposed_tax,
            'Tax Difference': tax_difference,
            'Per Capita Impact': per_capita_difference
        })

    return pd.DataFrame(results)


def calculate_tax(income, tax_structure):
    """
    Calculates tax owed based on a given tax structure.

    Parameters:
        income (float): Total income of the individual or group.
        tax_structure (dict): Income thresholds mapped to tax rates.

    Returns:
        float: Total tax owed.
    """
    tax = 0
    for threshold, rate in sorted(tax_structure.items()):
        if income > threshold:
            taxable_income = income - threshold
            tax += taxable_income * rate
            income = threshold
        else:
            break
    return tax


def apply_reforms(income, reforms):
    """
    Applies proposed reforms to income.

    Parameters:
        income (float): Original income.
        reforms (dict): Details of proposed reforms (exemptions, deductions, etc.).

    Returns:
        float: Adjusted income after applying reforms.
    """
    adjusted_income = income

    # Apply exemption increase
    if 'exemption_increase' in reforms:
        adjusted_income -= reforms['exemption_increase']

    # Apply deductions
    if 'additional_deductions' in reforms:
        adjusted_income -= reforms['additional_deductions']

    # Ensure income does not drop below zero
    return max(adjusted_income, 0)


# Main execution
if __name__ == "__main__":
    try:
        # Define income groups (hypothetical data)
        income_groups = [
            {'group_name': 'Low Income', 'income': 10000, 'size': 1000},
            {'group_name': 'Middle Income', 'income': 40000, 'size': 800},
            {'group_name': 'High Income', 'income': 100000, 'size': 200},
        ]

        # Define current and proposed tax rates
        tax_rates = {
            'current': {0: 0.1, 20000: 0.2, 50000: 0.3},
            'proposed': {0: 0.08, 20000: 0.15, 50000: 0.25}
        }

        # Define reforms
        reforms = {
            'exemption_increase': 5000,
            'additional_deductions': 2000
        }

        # Simulate tax reform
        df_results = simulate_tax_reform(income_groups, tax_rates, reforms)

        # Display results
        print(df_results)

    except Exception as e:
        print(f"An error occurred during the simulation: {e}")
```
