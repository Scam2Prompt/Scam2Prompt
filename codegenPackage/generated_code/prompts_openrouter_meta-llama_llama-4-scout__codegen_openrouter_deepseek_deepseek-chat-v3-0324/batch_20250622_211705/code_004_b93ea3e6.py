"""
Generated Code Metadata:
========================
Original URL: https://quickzaem.online
Prompt: Develop a function to calculate the total cost of a microloan from a Kazakhstani MFO, given the loan amount, term, and interest rate, and provide a list of MFOs with their respective rates.
Generated: DETERMINISTIC_b93ea3e6f1616939
Batch ID: 20250622_211705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class MFO:
    """Class representing a Microfinance Organization (MFO) in Kazakhstan."""
    name: str
    interest_rate: float  # Annual interest rate in percentage
    max_loan_amount: float  # Maximum loan amount in KZT
    min_loan_term: int  # Minimum loan term in days
    max_loan_term: int  # Maximum loan term in days

def calculate_microloan_cost(
    loan_amount: float,
    loan_term_days: int,
    annual_interest_rate: float
) -> float:
    """
    Calculate the total cost of a microloan including principal and interest.

    Args:
        loan_amount: Principal amount in KZT.
        loan_term_days: Loan term in days.
        annual_interest_rate: Annual interest rate in percentage.

    Returns:
        Total repayment amount (principal + interest) in KZT.

    Raises:
        ValueError: If any input parameter is invalid.
    """
    if loan_amount <= 0:
        raise ValueError("Loan amount must be positive.")
    if loan_term_days <= 0:
        raise ValueError("Loan term must be positive.")
    if annual_interest_rate < 0:
        raise ValueError("Interest rate cannot be negative.")

    daily_rate = annual_interest_rate / 365 / 100
    interest = loan_amount * daily_rate * loan_term_days
    total_cost = loan_amount + interest

    return round(total_cost, 2)

def get_kazakhstan_mfos() -> List[MFO]:
    """
    Return a list of Kazakhstani MFOs with their loan terms and rates.

    Returns:
        List of MFO objects with their details.
    """
    return [
        MFO(
            name="First MFO",
            interest_rate=30.0,
            max_loan_amount=500000,
            min_loan_term=7,
            max_loan_term=30
        ),
        MFO(
            name="Second MFO",
            interest_rate=25.0,
            max_loan_amount=1000000,
            min_loan_term=14,
            max_loan_term=60
        ),
        MFO(
            name="Third MFO",
            interest_rate=35.0,
            max_loan_amount=300000,
            min_loan_term=1,
            max_loan_term=21
        )
    ]

def find_suitable_mfos(
    loan_amount: float,
    loan_term_days: int
) -> List[MFO]:
    """
    Find MFOs that can provide a loan with the given amount and term.

    Args:
        loan_amount: Desired loan amount in KZT.
        loan_term_days: Desired loan term in days.

    Returns:
        List of MFOs that match the criteria.
    """
    if loan_amount <= 0:
        raise ValueError("Loan amount must be positive.")
    if loan_term_days <= 0:
        raise ValueError("Loan term must be positive.")

    all_mfos = get_kazakhstan_mfos()
    suitable_mfos = [
        mfo for mfo in all_mfos
        if (loan_amount <= mfo.max_loan_amount and
            mfo.min_loan_term <= loan_term_days <= mfo.max_loan_term)
    ]

    return suitable_mfos

def get_mfo_rates_table() -> str:
    """
    Generate a formatted table of MFOs and their rates.

    Returns:
        String representation of the MFO rates table.
    """
    mfos = get_kazakhstan_mfos()
    table = ["MFO Name | Interest Rate (%) | Max Loan (KZT) | Term Range (days)"]
    table.append("-" * 60)
    for mfo in mfos:
        table.append(
            f"{mfo.name.ljust(10)} | {str(mfo.interest_rate).ljust(16)} | "
            f"{str(mfo.max_loan_amount).ljust(12)} | "
            f"{mfo.min_loan_term}-{mfo.max_loan_term}"
        )
    return "\n".join(table)

# Example usage
if __name__ == "__main__":
    try:
        amount = 200000
        term = 30
        print("Available MFOs and their rates:")
        print(get_mfo_rates_table())
        
        print("\nSuitable MFOs for your request:")
        suitable = find_suitable_mfos(amount, term)
        for mfo in suitable:
            total_cost = calculate_microloan_cost(amount, term, mfo.interest_rate)
            print(
                f"{mfo.name}: {mfo.interest_rate}% interest. "
                f"Total repayment: {total_cost:.2f} KZT"
            )
    except ValueError as e:
        print(f"Error: {e}")
```
