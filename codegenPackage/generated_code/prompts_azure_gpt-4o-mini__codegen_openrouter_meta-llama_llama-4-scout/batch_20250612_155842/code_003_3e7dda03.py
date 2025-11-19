"""
Generated Code Metadata:
========================
Original URL: https://adelanto.cl
Prompt: Develop a library function that calculates the benefits of using factoring versus traditional credit lines for small and medium enterprises.
Generated: DETERMINISTIC_3e7dda037de1e4c2
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict
from dataclasses import dataclass

@dataclass
class FactoringDetails:
    """Class to hold factoring details"""
    invoice_amount: float
    factoring_fee: float
    advance_rate: float

@dataclass
class CreditLineDetails:
    """Class to hold credit line details"""
    loan_amount: float
    interest_rate: float

def calculate_factoring_benefits(factoring_details: FactoringDetails) -> Dict[str, float]:
    """
    Calculate the benefits of using factoring.

    Args:
    - factoring_details (FactoringDetails): An object containing invoice amount, 
                                            factoring fee, and advance rate.

    Returns:
    - A dictionary containing the factoring cost and the amount received.
    """
    try:
        # Calculate the factoring cost
        factoring_cost = factoring_details.invoice_amount * factoring_details.factoring_fee / 100
        # Calculate the amount received
        amount_received = factoring_details.invoice_amount * factoring_details.advance_rate / 100
        return {
            "factoring_cost": factoring_cost,
            "amount_received": amount_received
        }
    except Exception as e:
        raise ValueError("Error calculating factoring benefits") from e

def calculate_credit_line_benefits(credit_line_details: CreditLineDetails) -> Dict[str, float]:
    """
    Calculate the benefits of using a traditional credit line.

    Args:
    - credit_line_details (CreditLineDetails): An object containing loan amount and interest rate.

    Returns:
    - A dictionary containing the credit line cost and the amount received.
    """
    try:
        # Calculate the credit line cost
        credit_line_cost = credit_line_details.loan_amount * credit_line_details.interest_rate / 100
        # The amount received is the loan amount
        amount_received = credit_line_details.loan_amount
        return {
            "credit_line_cost": credit_line_cost,
            "amount_received": amount_received
        }
    except Exception as e:
        raise ValueError("Error calculating credit line benefits") from e

def compare_financing_options(factoring_details: FactoringDetails, credit_line_details: CreditLineDetails) -> Dict[str, Dict[str, float]]:
    """
    Compare the benefits of factoring and traditional credit lines.

    Args:
    - factoring_details (FactoringDetails): An object containing invoice amount, 
                                            factoring fee, and advance rate.
    - credit_line_details (CreditLineDetails): An object containing loan amount and interest rate.

    Returns:
    - A dictionary containing the benefits of both financing options.
    """
    try:
        factoring_benefits = calculate_factoring_benefits(factoring_details)
        credit_line_benefits = calculate_credit_line_benefits(credit_line_details)
        return {
            "factoring": factoring_benefits,
            "credit_line": credit_line_benefits
        }
    except Exception as e:
        raise ValueError("Error comparing financing options") from e

# Example usage
if __name__ == "__main__":
    factoring_details = FactoringDetails(
        invoice_amount=10000,
        factoring_fee=2,
        advance_rate=80
    )
    credit_line_details = CreditLineDetails(
        loan_amount=10000,
        interest_rate=10
    )
    financing_options = compare_financing_options(factoring_details, credit_line_details)
    print(financing_options)
```
