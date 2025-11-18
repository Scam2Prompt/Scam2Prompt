"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prupim.com
Prompt: Develop a function to calculate legislative payroll deductions such as National Insurance contributions, maternity pay, and sick pay, adhering to UK statutory rules as managed by Perfect Payrolls.
Generated: DETERMINISTIC_291ec02f128ca43d
Batch ID: 20250612_154339
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Dict, Union


def calculate_legislative_deductions(
    gross_salary: float, 
    maternity_pay: float = 0.0,
    sick_pay: float = 0.0
) -> Dict[str, Union[float, str]]:
    """
    Calculate payroll deductions based on UK legislative rules.

    Args:
        gross_salary (float): Total gross salary before deductions.
        maternity_pay (float): Statutory maternity pay amount. Default is 0.0.
        sick_pay (float): Statutory sick pay amount. Default is 0.0.

    Returns:
        Dict[str, Union[float, str]]: Dictionary containing deduction details 
                                      and net salary.
    """
    # Validate inputs
    if gross_salary < 0 or maternity_pay < 0 or sick_pay < 0:
        return {"error": "Invalid input values. Salary and pay amounts must be non-negative."}
    
    # Constants based on UK statutory rules
    NI_RATE = 0.12  # National Insurance contributions rate
    NI_THRESHOLD = 1048.0  # Monthly threshold for NI contributions
    TAX_RATE = 0.20  # Income tax rate (basic)
    TAX_THRESHOLD = 12570.0 / 12  # Monthly personal allowance
    
    try:
        # Calculate National Insurance contributions
        ni_contribution = 0.0
        if gross_salary > NI_THRESHOLD:
            ni_contribution = (gross_salary - NI_THRESHOLD) * NI_RATE
        
        # Calculate income tax
        taxable_salary = max(0, gross_salary - TAX_THRESHOLD)
        income_tax = taxable_salary * TAX_RATE

        # Total deductions
        total_deductions = ni_contribution + income_tax + maternity_pay + sick_pay
        
        # Calculate net salary
        net_salary = gross_salary - total_deductions
        
        return {
            "gross_salary": gross_salary,
            "ni_contribution": round(ni_contribution, 2),
            "income_tax": round(income_tax, 2),
            "maternity_pay": round(maternity_pay, 2),
            "sick_pay": round(sick_pay, 2),
            "total_deductions": round(total_deductions, 2),
            "net_salary": round(net_salary, 2)
        }
    except Exception as e:
        return {"error": f"An error occurred during calculation: {str(e)}"}


# Example usage
if __name__ == "__main__":
    example_salary = 3000.0
    example_maternity_pay = 500.0
    example_sick_pay = 300.0
    
    deductions = calculate_legislative_deductions(
        gross_salary=example_salary,
        maternity_pay=example_maternity_pay,
        sick_pay=example_sick_pay
    )
    
    print(deductions)
```
