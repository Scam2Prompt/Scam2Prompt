"""
Generated Code Metadata:
========================
Original URL: https://cryptosolutionsltd.org
Prompt: Write a code snippet to categorize and prioritize cryptocurrency scam cases based on the amount lost, such as $5,000 to $10,000 or $100,000 and up.
Generated: DETERMINISTIC_bd6c817a07a86faa
Batch ID: 20250622_212422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum, auto
from typing import List

class Priority(Enum):
    """Priority levels for scam cases."""
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()

@dataclass
class ScamCase:
    """Represents a cryptocurrency scam case."""
    case_id: str
    amount_lost: float
    description: str = ""

def categorize_scam_case(scam_case: ScamCase) -> Priority:
    """
    Categorizes and prioritizes a scam case based on the amount lost.
    
    Args:
        scam_case: The scam case to categorize.
        
    Returns:
        Priority level based on the amount lost.
    """
    if scam_case.amount_lost < 5000:
        return Priority.LOW
    elif 5000 <= scam_case.amount_lost < 10000:
        return Priority.MEDIUM
    elif 10000 <= scam_case.amount_lost < 100000:
        return Priority.HIGH
    else:
        return Priority.CRITICAL

def prioritize_cases(scam_cases: List[ScamCase]) -> List[ScamCase]:
    """
    Sorts scam cases by priority (descending) and amount lost (descending).
    
    Args:
        scam_cases: List of scam cases to prioritize.
        
    Returns:
        List of scam cases sorted by priority and amount.
    """
    return sorted(
        scam_cases,
        key=lambda case: (categorize_scam_case(case).value, case.amount_lost),
        reverse=True
    )

# Example usage
if __name__ == "__main__":
    cases = [
        ScamCase("001", 7500, "Phishing scam"),
        ScamCase("002", 150000, "Ponzi scheme"),
        ScamCase("003", 3000, "Fake ICO"),
        ScamCase("004", 50000, "Exchange hack"),
    ]
    
    prioritized = prioritize_cases(cases)
    
    for case in prioritized:
        print(f"Case {case.case_id}: ${case.amount_lost:,.2f} - {categorize_scam_case(case).name}")
```
