"""
Generated Code Metadata:
========================
Original URL: https://dbm.mu
Prompt: Create a Python function to compare loan options for taxi operators purchasing electric vehicles, using the details provided by the Development Bank of Mauritius.
Generated: DETERMINISTIC_624e598d3acfee1b
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class LoanOption:
    """Represents a loan option with its terms and conditions."""
    name: str
    interest_rate: float  # annual interest rate as decimal (e.g., 0.05 for 5%)
    loan_term_years: int
    max_amount: float
    processing_fee: float
    early_repayment_penalty: Optional[float] = None  # as decimal (e.g., 0.02 for 2%)
    grace_period_months: int = 0

def calculate_monthly_payment(principal: float, annual_rate: float, term_years: int) -> float:
    """
    Calculate the monthly payment for a loan using the standard formula.
    
    Args:
        principal: Loan amount
        annual_rate: Annual interest rate as decimal
        term_years: Loan term in years
    
    Returns:
        Monthly payment amount
    """
    if principal <= 0:
        raise ValueError("Principal must be positive")
    if annual_rate < 0:
        raise ValueError("Interest rate cannot be negative")
    if term_years <= 0:
        raise ValueError("Loan term must be positive")
    
    monthly_rate = annual_rate / 12
    num_payments = term_years * 12
    if monthly_rate == 0:  # handle 0% interest case
        return principal / num_payments
    
    return principal * (monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)

def calculate_total_cost(loan_option: LoanOption, principal: float) -> float:
    """
    Calculate the total cost of a loan including interest and fees.
    
    Args:
        loan_option: Loan option details
        principal: Loan amount
    
    Returns:
        Total repayment amount over the loan term
    """
    if principal > loan_option.max_amount:
        raise ValueError(f"Loan amount exceeds maximum of {loan_option.max_amount}")
    
    monthly_payment = calculate_monthly_payment(principal, loan_option.interest_rate, loan_option.loan_term_years)
    total_repayment = monthly_payment * loan_option.loan_term_years * 12
    total_cost = total_repayment + loan_option.processing_fee
    
    return total_cost

def compare_loan_options(loan_options: List[LoanOption], principal: float) -> List[dict]:
    """
    Compare multiple loan options and return a sorted list with their details.
    
    Args:
        loan_options: List of LoanOption objects to compare
        principal: Desired loan amount
    
    Returns:
        List of dictionaries with comparison results, sorted by total cost
    """
    if not loan_options:
        raise ValueError("No loan options provided")
    if principal <= 0:
        raise ValueError("Principal must be positive")
    
    comparisons = []
    
    for option in loan_options:
        try:
            monthly_payment = calculate_monthly_payment(principal, option.interest_rate, option.loan_term_years)
            total_cost = calculate_total_cost(option, principal)
            
            comparisons.append({
                'name': option.name,
                'monthly_payment': round(monthly_payment, 2),
                'total_cost': round(total_cost, 2),
                'total_interest': round(total_cost - principal - option.processing_fee, 2),
                'processing_fee': option.processing_fee,
                'early_repayment_penalty': option.early_repayment_penalty,
                'grace_period_months': option.grace_period_months
            })
        except ValueError as e:
            print(f"Skipping option {option.name} due to error: {str(e)}")
    
    # Sort by total cost (cheapest first)
    comparisons.sort(key=lambda x: x['total_cost'])
    
    return comparisons

def print_comparison_table(comparisons: List[dict]):
    """Print the loan comparison results in a readable table format."""
    if not comparisons:
        print("No valid loan options to compare")
        return
    
    headers = [
        "Option", "Monthly Payment", "Total Cost", 
        "Total Interest", "Processing Fee", 
        "Early Penalty", "Grace Period"
    ]
    
    # Format table header
    header_row = "|".join(f"{h:^20}" for h in headers)
    separator = "-" * len(header_row)
    
    print(separator)
    print(header_row)
    print(separator)
    
    # Format each row
    for comp in comparisons:
        row = [
            comp['name'],
            f"Rs {comp['monthly_payment']:,.2f}",
            f"Rs {comp['total_cost']:,.2f}",
            f"Rs {comp['total_interest']:,.2f}",
            f"Rs {comp['processing_fee']:,.2f}",
            f"{comp['early_repayment_penalty']*100 if comp['early_repayment_penalty'] else 0:.1f}%" if comp['early_repayment_penalty'] is not None else "None",
            f"{comp['grace_period_months']} months"
        ]
        print("|".join(f"{r:^20}" for r in row))
    
    print(separator)

# Example usage
if __name__ == "__main__":
    # Sample loan options from Development Bank of Mauritius
    loan_options = [
        LoanOption(
            name="Green EV Loan",
            interest_rate=0.05,  # 5%
            loan_term_years=7,
            max_amount=2000000,
            processing_fee=5000,
            early_repayment_penalty=0.02,  # 2%
            grace_period_months=6
        ),
        LoanOption(
            name="Standard Auto Loan",
            interest_rate=0.075,  # 7.5%
            loan_term_years=5,
            max_amount=1500000,
            processing_fee=7500,
            early_repayment_penalty=0.03  # 3%
        ),
        LoanOption(
            name="Special Taxi Package",
            interest_rate=0.045,  # 4.5%
            loan_term_years=8,
            max_amount=2500000,
            processing_fee=3000,
            grace_period_months=3
        )
    ]
    
    try:
        principal = float(input("Enter the loan amount you need (Rs): "))
        comparisons = compare_loan_options(loan_options, principal)
        print_comparison_table(comparisons)
    except ValueError as e:
        print(f"Error: {str(e)}")
```
