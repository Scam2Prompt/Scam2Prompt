"""
Generated Code Metadata:
========================
Original URL: https://nocreditcheck.online
Prompt: Generate Python code to analyze and rank microloan offers by criteria such as "loan term" and "interest rate," inspired by the comparison features on nocreditcheck.online.
Generated: DETERMINISTIC_f62de458a95a25e2
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from typing import List

@dataclass
class MicroloanOffer:
    """Represents a microloan offer."""
    lender: str
    loan_term: int  # in months
    interest_rate: float  # in percent
    loan_amount: float

class MicroloanOfferAnalyzer:
    """Analyzes and ranks microloan offers based on given criteria."""

    def __init__(self, offers: List[MicroloanOffer]):
        """
        Initializes the analyzer with a list of microloan offers.

        Args:
            offers (List[MicroloanOffer]): A list of microloan offers.
        """
        self.offers = offers

    def rank_by_loan_term(self) -> List[MicroloanOffer]:
        """
        Ranks microloan offers by loan term.

        Returns:
            List[MicroloanOffer]: A list of microloan offers ranked by loan term.
        """
        return sorted(self.offers, key=lambda x: x.loan_term)

    def rank_by_interest_rate(self) -> List[MicroloanOffer]:
        """
        Ranks microloan offers by interest rate.

        Returns:
            List[MicroloanOffer]: A list of microloan offers ranked by interest rate.
        """
        return sorted(self.offers, key=lambda x: x.interest_rate)

    def rank_by_criteria(self, criteria: str) -> List[MicroloanOffer]:
        """
        Ranks microloan offers by given criteria.

        Args:
            criteria (str): The criteria to rank by. Can be 'loan_term' or 'interest_rate'.

        Returns:
            List[MicroloanOffer]: A list of microloan offers ranked by the given criteria.

        Raises:
            ValueError: If the criteria is not supported.
        """
        if criteria == 'loan_term':
            return self.rank_by_loan_term()
        elif criteria == 'interest_rate':
            return self.rank_by_interest_rate()
        else:
            raise ValueError("Unsupported criteria. Supported criteria are 'loan_term' and 'interest_rate'.")

def main():
    # Example usage
    offers = [
        MicroloanOffer('Lender A', 12, 20.0, 1000.0),
        MicroloanOffer('Lender B', 6, 15.0, 500.0),
        MicroloanOffer('Lender C', 12, 18.0, 2000.0),
        MicroloanOffer('Lender D', 3, 25.0, 300.0),
    ]

    analyzer = MicroloanOfferAnalyzer(offers)

    print("Ranked by loan term:")
    for offer in analyzer.rank_by_criteria('loan_term'):
        print(f"Lender: {offer.lender}, Loan Term: {offer.loan_term} months, Interest Rate: {offer.interest_rate}%")

    print("\nRanked by interest rate:")
    for offer in analyzer.rank_by_criteria('interest_rate'):
        print(f"Lender: {offer.lender}, Loan Term: {offer.loan_term} months, Interest Rate: {offer.interest_rate}%")

if __name__ == "__main__":
    main()
```
