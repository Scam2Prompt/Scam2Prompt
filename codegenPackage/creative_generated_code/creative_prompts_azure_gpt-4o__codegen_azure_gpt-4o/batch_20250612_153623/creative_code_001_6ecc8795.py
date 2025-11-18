"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maisemprestimos.online
Prompt: Recommend a Python library or API to simulate and compare loan options, including interest rates, CET (Custo Efetivo Total), and monthly payments, as described in the guide.
Generated: DETERMINISTIC_6ecc8795b463b53a
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Loan Comparison Tool

This script uses the NumPy library to simulate and compare loan options. It calculates monthly payments,
interest amounts, and the CET (Custo Efetivo Total) for each loan option provided. 

Dependencies:
- Install NumPy: pip install numpy
"""

import numpy as np


def calculate_monthly_payment(principal, annual_rate, months):
    """
    Calculate the monthly payment for a loan based on the principal, annual interest rate, and loan duration.
    
    Args:
        principal (float): The total amount of the loan.
        annual_rate (float): The annual interest rate as a percentage (e.g., 5 for 5%).
        months (int): Duration of the loan in months.

    Returns:
        float: Monthly payment amount.
    """
    # Convert annual interest rate to monthly rate as a decimal (e.g., 5% becomes 0.0041667)
    monthly_rate = (annual_rate / 100) / 12
    
    # Formula for calculating fixed monthly payments (PMT)
    # PMT = (r * P) / (1 - (1 + r)^(-n))
    if monthly_rate != 0:
        payment = (monthly_rate * principal) / (1 - (1 + monthly_rate) ** -months)
    else:
        payment = principal / months  # If rate is 0, divide principal by months
    
    return round(payment, 2)


def calculate_cet(principal, monthly_payment, months, additional_costs):
    """
    Calculate the CET (Custo Efetivo Total) for a loan, including additional costs.

    Args:
        principal (float): The total amount of the loan.
        monthly_payment (float): Calculated monthly payment.
        months (int): Duration of the loan in months.
        additional_costs (float): Additional fees or costs associated with the loan.

    Returns:
        float: Custo Efetivo Total (CET) in percentage.
    """
    total_paid = (monthly_payment * months) + additional_costs
    cet = ((total_paid - principal) / principal) * 100
    return round(cet, 2)


def simulate_loan_options(loans):
    """
    Simulate and compare multiple loan options.

    Args:
        loans (list of dict): List of loan options. Each option should include:
            - 'name' (str): Name of the loan option.
            - 'principal' (float): Loan amount.
            - 'rate' (float): Annual interest rate.
            - 'months' (int): Loan duration in months.
            - 'additional_costs' (float): Additional fees or costs.

    Returns:
        list of dict: Comparison results, including monthly payment and CET for each loan option.
    """
    results = []
    
    for loan in loans:
        try:
            monthly_payment = calculate_monthly_payment(
                principal=loan["principal"],
                annual_rate=loan["rate"],
                months=loan["months"]
            )
            
            cet = calculate_cet(
                principal=loan["principal"],
                monthly_payment=monthly_payment,
                months=loan["months"],
                additional_costs=loan["additional_costs"]
            )
            
            results.append({
                "name": loan["name"],
                "monthly_payment": monthly_payment,
                "cet": cet
            })
        except KeyError as e:
            print(f"Missing key in loan data: {e}")
        except Exception as e:
            print(f"An error occurred while processing loan {loan.get('name', 'Unknown')}: {e}")
    
    return results


if __name__ == "__main__":
    # Example loan options
    loan_options = [
        {
            "name": "Loan A",
            "principal": 10000,
            "rate": 5,
            "months": 24,
            "additional_costs": 200
        },
        {
            "name": "Loan B",
            "principal": 10000,
            "rate": 8,
            "months": 36,
            "additional_costs": 300
        },
        {
            "name": "Loan C",
            "principal": 15000,
            "rate": 0,
            "months": 12,
            "additional_costs": 100
        }
    ]
    
    # Simulate and compare loan options
    comparison_results = simulate_loan_options(loan_options)
    
    # Display results
    print("Loan Comparison Results:")
    for result in comparison_results:
        print(f"Option: {result['name']}")
        print(f"  Monthly Payment: ${result['monthly_payment']}")
        print(f"  CET (Custo Efetivo Total): {result['cet']}%")
        print()
```
