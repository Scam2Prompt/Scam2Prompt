"""
Generated Code Metadata:
========================
Original URL: https://zyme-dendi-v-dolg.online
Prompt: Develop a function to determine the best microloan option from providers like LайкZайм, considering factors such as loan amount, age requirements, and credit history.
Generated: DETERMINISTIC_26f0d7b30ad4acf5
Batch ID: 20250622_211805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum
from typing import List

class CreditHistory(Enum):
    """Enum for credit history"""
    EXCELLENT = 1
    GOOD = 2
    FAIR = 3
    POOR = 4
    BAD = 5

@dataclass
class MicroloanProvider:
    """Dataclass for microloan provider"""
    name: str
    min_age: int
    max_loan_amount: float
    min_loan_amount: float
    credit_history_requirement: CreditHistory

@dataclass
class LoanOption:
    """Dataclass for loan option"""
    provider: MicroloanProvider
    loan_amount: float
    interest_rate: float

def get_best_microloan_option(
    loan_amount: float, 
    age: int, 
    credit_history: CreditHistory, 
    providers: List[MicroloanProvider]
) -> LoanOption:
    """
    Determine the best microloan option from a list of providers.

    Args:
    - loan_amount (float): The amount of the loan.
    - age (int): The age of the borrower.
    - credit_history (CreditHistory): The credit history of the borrower.
    - providers (List[MicroloanProvider]): A list of microloan providers.

    Returns:
    - LoanOption: The best loan option.

    Raises:
    - ValueError: If no providers match the borrower's criteria.
    """
    best_option = None
    best_interest_rate = float('inf')

    for provider in providers:
        # Check if the borrower meets the provider's age requirement
        if age < provider.min_age:
            continue
        
        # Check if the loan amount is within the provider's limits
        if loan_amount < provider.min_loan_amount or loan_amount > provider.max_loan_amount:
            continue
        
        # Check if the borrower's credit history meets the provider's requirement
        if credit_history.value < provider.credit_history_requirement.value:
            continue
        
        # Calculate the interest rate for this provider (example calculation)
        interest_rate = calculate_interest_rate(provider, loan_amount)
        
        # Check if this option is better than the current best option
        if interest_rate < best_interest_rate:
            best_option = LoanOption(provider, loan_amount, interest_rate)
            best_interest_rate = interest_rate
    
    if best_option is None:
        raise ValueError("No providers match the borrower's criteria")
    
    return best_option

def calculate_interest_rate(provider: MicroloanProvider, loan_amount: float) -> float:
    """
    Calculate the interest rate for a loan from a provider.

    Args:
    - provider (MicroloanProvider): The provider of the loan.
    - loan_amount (float): The amount of the loan.

    Returns:
    - float: The interest rate.
    """
    # Example calculation: 10% base rate, plus 1% for every 1000 in loan amount
    base_rate = 0.10
    loan_amount_factor = (loan_amount / 1000) * 0.01
    return base_rate + loan_amount_factor

def main():
    providers = [
        MicroloanProvider(
            name="LайкZайм",
            min_age=18,
            max_loan_amount=10000,
            min_loan_amount=1000,
            credit_history_requirement=CreditHistory.FAIR
        ),
        MicroloanProvider(
            name="Another Provider",
            min_age=21,
            max_loan_amount=5000,
            min_loan_amount=500,
            credit_history_requirement=CreditHistory.GOOD
        )
    ]

    loan_amount = 5000
    age = 25
    credit_history = CreditHistory.GOOD

    try:
        best_option = get_best_microloan_option(loan_amount, age, credit_history, providers)
        print(f"Best loan option: {best_option.provider.name}, loan amount: {best_option.loan_amount}, interest rate: {best_option.interest_rate}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
