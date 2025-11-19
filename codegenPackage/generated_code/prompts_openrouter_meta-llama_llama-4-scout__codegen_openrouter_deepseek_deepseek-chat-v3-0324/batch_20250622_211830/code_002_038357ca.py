"""
Generated Code Metadata:
========================
Original URL: https://maestrofinance.co.uk
Prompt: "Compare and contrast the features of a Revolving Credit Facility and an Invoice Finance solution for a small business in the UK, focusing on flexibility and cost implications."
Generated: DETERMINISTIC_038357ca601f3453
Batch ID: 20250622_211830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional

class FinanceType(Enum):
    """Enumeration for types of financing solutions."""
    REVOLVING_CREDIT = auto()
    INVOICE_FINANCE = auto()

@dataclass
class FinanceSolution:
    """Base class for financial solutions."""
    name: str
    finance_type: FinanceType
    flexibility_score: int  # Scale of 1-10
    cost_implications: str  # Description of cost implications
    eligibility_criteria: List[str]
    max_amount: Optional[float] = None  # Optional maximum amount in GBP

    def get_features(self) -> str:
        """Returns a formatted string of the solution's features."""
        return (
            f"Name: {self.name}\n"
            f"Type: {self.finance_type.name}\n"
            f"Flexibility Score: {self.flexibility_score}/10\n"
            f"Cost Implications: {self.cost_implications}\n"
            f"Eligibility Criteria: {', '.join(self.eligibility_criteria)}\n"
            f"Max Amount: {self.max_amount if self.max_amount else 'Not specified'} GBP"
        )

def compare_solutions(solution1: FinanceSolution, solution2: FinanceSolution) -> str:
    """
    Compares two financial solutions and returns a comparison summary.
    
    Args:
        solution1: First financial solution to compare.
        solution2: Second financial solution to compare.
    
    Returns:
        A formatted string comparing the two solutions.
    """
    comparison = (
        f"Comparison between {solution1.name} and {solution2.name}:\n"
        f"1. Flexibility: {solution1.name} scores {solution1.flexibility_score}/10, "
        f"while {solution2.name} scores {solution2.flexibility_score}/10.\n"
        f"2. Cost Implications: {solution1.name} - {solution1.cost_implications}. "
        f"{solution2.name} - {solution2.cost_implications}.\n"
        f"3. Eligibility: {solution1.name} requires {', '.join(solution1.eligibility_criteria)}. "
        f"{solution2.name} requires {', '.join(solution2.eligibility_criteria)}.\n"
    )
    return comparison

# Example usage
if __name__ == "__main__":
    # Define Revolving Credit Facility
    revolving_credit = FinanceSolution(
        name="Revolving Credit Facility",
        finance_type=FinanceType.REVOLVING_CREDIT,
        flexibility_score=8,
        cost_implications="Interest charged on drawn amount, arrangement fees may apply",
        eligibility_criteria=["Good credit history", "Established business", "Collateral may be required"],
        max_amount=100000.00
    )

    # Define Invoice Finance solution
    invoice_finance = FinanceSolution(
        name="Invoice Finance",
        finance_type=FinanceType.INVOICE_FINANCE,
        flexibility_score=6,
        cost_implications="Discount fee on invoice value, service charges apply",
        eligibility_criteria=["Creditworthy customers", "Invoices with reliable debtors"],
        max_amount=50000.00
    )

    # Print individual features
    print(revolving_credit.get_features())
    print("\n")
    print(invoice_finance.get_features())
    print("\n")

    # Compare the two solutions
    print(compare_solutions(revolving_credit, invoice_finance))
```
