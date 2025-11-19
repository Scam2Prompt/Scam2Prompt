"""
Generated Code Metadata:
========================
Original URL: https://zerointerest24.online
Prompt: Напишите код для фильтрации предложений займов от микрофинансовых организаций в Казахстане на основе суммы, срока и процентной ставки.
Generated: DETERMINISTIC_f824e2a3db808261
Batch ID: 20250622_211800
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import List, Dict, Optional

class LoanOffer:
    """
    Represents a loan offer from a microfinance organization.
    """
    def __init__(self, lender: str, amount: float, term_days: int, interest_rate: float):
        """
        Initialize a loan offer.

        Args:
            lender: Name of the lending organization.
            amount: Loan amount in KZT.
            term_days: Loan term in days.
            interest_rate: Annual interest rate (e.g., 0.1 for 10%).
        """
        self.lender = lender
        self.amount = amount
        self.term_days = term_days
        self.interest_rate = interest_rate

    def __repr__(self) -> str:
        return f"LoanOffer(lender='{self.lender}', amount={self.amount}, term_days={self.term_days}, interest_rate={self.interest_rate})"

class LoanFilter:
    """
    Filters loan offers based on specified criteria.
    """
    def __init__(self, offers: List[LoanOffer]):
        """
        Initialize with a list of loan offers.

        Args:
            offers: List of LoanOffer objects to filter.
        """
        self.offers = offers

    def filter(
        self,
        min_amount: Optional[float] = None,
        max_amount: Optional[float] = None,
        min_term: Optional[int] = None,
        max_term: Optional[int] = None,
        min_interest: Optional[float] = None,
        max_interest: Optional[float] = None
    ) -> List[LoanOffer]:
        """
        Filter loan offers based on criteria.

        Args:
            min_amount: Minimum loan amount in KZT.
            max_amount: Maximum loan amount in KZT.
            min_term: Minimum loan term in days.
            max_term: Maximum loan term in days.
            min_interest: Minimum annual interest rate.
            max_interest: Maximum annual interest rate.

        Returns:
            List of LoanOffer objects that meet all criteria.
        """
        filtered = []
        for offer in self.offers:
            if min_amount is not None and offer.amount < min_amount:
                continue
            if max_amount is not None and offer.amount > max_amount:
                continue
            if min_term is not None and offer.term_days < min_term:
                continue
            if max_term is not None and offer.term_days > max_term:
                continue
            if min_interest is not None and offer.interest_rate < min_interest:
                continue
            if max_interest is not None and offer.interest_rate > max_interest:
                continue
            filtered.append(offer)
        return filtered

def validate_kzt_amount(amount: str) -> float:
    """
    Validate and convert KZT amount string to float.

    Args:
        amount: String representing amount in KZT (e.g., "10 000" or "10000").

    Returns:
        Validated amount as float.

    Raises:
        ValueError: If amount is invalid.
    """
    cleaned = re.sub(r'[^\d.]', '', amount)
    if not cleaned:
        raise ValueError("Invalid amount format")
    return float(cleaned)

# Example usage
if __name__ == "__main__":
    # Sample loan offers
    offers = [
        LoanOffer("Lender A", 50000, 30, 0.12),
        LoanOffer("Lender B", 100000, 60, 0.15),
        LoanOffer("Lender C", 200000, 90, 0.10),
        LoanOffer("Lender D", 30000, 15, 0.20)
    ]

    # Initialize filter
    loan_filter = LoanFilter(offers)

    # Filter offers: amount between 50k-200k, term 30-90 days, interest <= 15%
    filtered_offers = loan_filter.filter(
        min_amount=50000,
        max_amount=200000,
        min_term=30,
        max_term=90,
        max_interest=0.15
    )

    print("Filtered Offers:")
    for offer in filtered_offers:
        print(offer)
```
