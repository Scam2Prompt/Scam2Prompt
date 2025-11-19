"""
Generated Code Metadata:
========================
Original URL: https://hameiriz.co.il
Prompt: Generate a code snippet to calculate income tax and national insurance contributions for self-employed individuals in Israel, taking into account the guidelines provided by the Israeli Tax Authority.
Generated: DETERMINISTIC_dec63717b22b6d1f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Israeli Self-Employment Tax Calculator
# Calculates income tax and national insurance contributions based on Israeli Tax Authority guidelines

def calculate_self_employment_tax(annual_income, is_member_of_kupat_cholim=True):
    """
    Calculate income tax and national insurance contributions for self-employed individuals in Israel.
    
    Args:
        annual_income (float): Annual income in NIS
        is_member_of_kupat_cholim (bool): Whether the individual is a member of Kupat Cholim (health insurance)
        
    Returns:
        dict: Dictionary containing tax breakdown with keys:
            - 'income_tax': Calculated income tax
            - 'national_insurance': National insurance contributions
            - 'health_insurance': Health insurance contributions
            - 'total_tax': Sum of all taxes
    """
    try:
        # Validate input
        if not isinstance(annual_income, (int, float)) or annual_income < 0:
            raise ValueError("Annual income must be a positive number")
            
        # Income tax brackets and rates for 2023 (in NIS)
        tax_brackets = [
            (0, 77400, 0.10),
            (77400, 110880, 0.14),
            (110880, 178080, 0.20),
            (178080, 247440, 0.31),
            (247440, 514920, 0.35),
            (514920, 663240, 0.47),
            (663240, float('inf'), 0.50)
        ]
        
        # Calculate income tax
        remaining_income = annual_income
        income_tax = 0.0
        
        for lower, upper, rate in tax_brackets:
            if remaining_income <= 0:
                break
            taxable_amount = min(remaining_income, upper - lower) if upper != float('inf') else remaining_income
            income_tax += taxable_amount * rate
            remaining_income -= taxable_amount
        
        # National Insurance calculations
        national_insurance = 0.0
        if annual_income > 6300 * 12:  # Minimum annual income threshold
            # Self-employed pay 12.6% up to 60% of average wage (75,070 NIS/month in 2023)
            max_ni_income = 75070 * 12 * 0.6  # 60% of average annual wage
            taxable_ni_income = min(annual_income, max_ni_income)
            national_insurance = taxable_ni_income * 0.126  # 12.6% rate
            
        # Health Insurance calculations
        health_insurance = 0.0
        if is_member_of_kupat_cholim and annual_income > 6300 * 12:
            # Self-employed pay 5% up to 60% of average wage
            max_hi_income = 75070 * 12 * 0.6  # 60% of average annual wage
            taxable_hi_income = min(annual_income, max_hi_income)
            health_insurance = taxable_hi_income * 0.05  # 5% rate
            
        total_tax = income_tax + national_insurance + health_insurance
        
        return {
            'income_tax': round(income_tax, 2),
            'national_insurance': round(national_insurance, 2),
            'health_insurance': round(health_insurance, 2),
            'total_tax': round(total_tax, 2)
        }
        
    except Exception as e:
        raise ValueError(f"Error calculating taxes: {str(e)}")
```
