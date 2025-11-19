"""
Generated Code Metadata:
========================
Original URL: https://cart3.pages.dev
Prompt: Create a Python function to calculate superannuation contributions for self-managed super funds in Australia, aligning with the services provided by Carthew Chau & Co.
Generated: DETERMINISTIC_9449907048c0afbb
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_superannuation(
    income: float,
    is_employee: bool = False,
    is_self_employed: bool = False,
    is_employer_contributing: bool = False,
    employer_contribution_rate: float = 0.105,  # Default 10.5% as of 2022-2023
    personal_contribution_rate: float = 0.0,
    concessional_cap: float = 27500.0,  # 2022-2023 concessional contributions cap
    non_concessional_cap: float = 110000.0,  # 2022-2023 non-concessional cap
    previous_concessional_contributions: float = 0.0,
    previous_non_concessional_contributions: float = 0.0,
    age: int = None,
    financial_year: int = None
) -> dict:
    """
    Calculate superannuation contributions for self-managed super funds (SMSF) in Australia.
    
    Args:
        income (float): Annual taxable income.
        is_employee (bool): Whether the person is an employee.
        is_self_employed (bool): Whether the person is self-employed.
        is_employer_contributing (bool): Whether the employer is making contributions.
        employer_contribution_rate (float): Employer contribution rate (default 10.5%).
        personal_contribution_rate (float): Personal contribution rate (default 0%).
        concessional_cap (float): Annual concessional contributions cap (default $27,500).
        non_concessional_cap (float): Annual non-concessional contributions cap (default $110,000).
        previous_concessional_contributions (float): Previous concessional contributions in the financial year.
        previous_non_concessional_contributions (float): Previous non-concessional contributions in the financial year.
        age (int): Age of the contributor (for eligibility checks).
        financial_year (int): Financial year for contribution calculations.
        
    Returns:
        dict: Dictionary containing contribution breakdown and relevant information.
    """
    
    # Initialize result dictionary
    result = {
        'employer_contributions': 0.0,
        'personal_concessional_contributions': 0.0,
        'personal_non_concessional_contributions': 0.0,
        'total_concessional_contributions': 0.0,
        'total_non_concessional_contributions': 0.0,
        'remaining_concessional_cap': concessional_cap,
        'remaining_non_concessional_cap': non_concessional_cap,
        'notes': []
    }
    
    try:
        # Validate inputs
        if income < 0:
            raise ValueError("Income cannot be negative")
        if employer_contribution_rate < 0 or employer_contribution_rate > 1:
            raise ValueError("Employer contribution rate must be between 0 and 1")
        if personal_contribution_rate < 0 or personal_contribution_rate > 1:
            raise ValueError("Personal contribution rate must be between 0 and 1")
        if concessional_cap < 0:
            raise ValueError("Concessional cap cannot be negative")
        if non_concessional_cap < 0:
            raise ValueError("Non-concessional cap cannot be negative")
        if previous_concessional_contributions < 0:
            raise ValueError("Previous concessional contributions cannot be negative")
        if previous_non_concessional_contributions < 0:
            raise ValueError("Previous non-concessional contributions cannot be negative")
        
        # Calculate employer contributions (if applicable)
        if is_employee and is_employer_contributing:
            employer_contributions = income * employer_contribution_rate
            result['employer_contributions'] = employer_contributions
            result['total_concessional_contributions'] += employer_contributions
        
        # Calculate personal concessional contributions (if applicable)
        if personal_contribution_rate > 0:
            personal_concessional = income * personal_contribution_rate
            remaining_concessional = max(0, concessional_cap - previous_concessional_contributions - result['total_concessional_contributions'])
            
            if personal_concessional > remaining_concessional:
                result['notes'].append(f"Personal concessional contributions capped at ${remaining_concessional:,.2f} due to concessional cap")
                personal_concessional = remaining_concessional
            
            result['personal_concessional_contributions'] = personal_concessional
            result['total_concessional_contributions'] += personal_concessional
        
        # Calculate remaining caps
        result['remaining_concessional_cap'] = max(0, concessional_cap - result['total_concessional_contributions'] - previous_concessional_contributions)
        
        # Calculate non-concessional contributions (if applicable)
        if is_self_employed and personal_contribution_rate > 0:
            personal_non_concessional = income * personal_contribution_rate
            remaining_non_concessional = max(0, non_concessional_cap - previous_non_concessional_contributions)
            
            if personal_non_concessional > remaining_non_concessional:
                result['notes'].append(f"Personal non-concessional contributions capped at ${remaining_non_concessional:,.2f} due to non-concessional cap")
                personal_non_concessional = remaining_non_concessional
            
            result['personal_non_concessional_contributions'] = personal_non_concessional
            result['total_non_concessional_contributions'] = personal_non_concessional + previous_non_concessional_contributions
            result['remaining_non_concessional_cap'] = max(0, non_concessional_cap - result['total_non_concessional_contributions'])
        
        # Age-related checks
        if age is not None:
            if age < 18:
                result['notes'].append("Contributor is under 18 - special rules may apply")
            if age >= 67:
                result['notes'].append("Contributor is 67 or older - work test may apply")
        
        # Financial year note
        if financial_year is not None:
            result['notes'].append(f"Calculations based on {financial_year}-{financial_year+1} financial year caps")
        
        return result
    
    except ValueError as e:
        return {'error': str(e)}
    except Exception as e:
        return {'error': f"An unexpected error occurred: {str(e)}"}
```
