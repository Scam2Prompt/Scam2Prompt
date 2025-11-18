"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nocreditcheck.online
Prompt: Generate Python code to analyze and rank microloan offers by criteria such as "loan term" and "interest rate," inspired by the comparison features on nocreditcheck.online.
Generated: DETERMINISTIC_f62de458a95a25e2
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Any


class MicroloanOffer:
    """
    A class to represent a microloan offer.
    """
    def __init__(self, lender: str, loan_term: int, interest_rate: float, max_loan_amount: float):
        """
        Initialize MicroloanOffer object.

        :param lender: Name of the lender.
        :param loan_term: Loan term in months.
        :param interest_rate: Interest rate as a percentage (e.g., 5.5 for 5.5%).
        :param max_loan_amount: Maximum loan amount offered by the lender.
        """
        self.lender = lender
        self.loan_term = loan_term
        self.interest_rate = interest_rate
        self.max_loan_amount = max_loan_amount

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the MicroloanOffer object to a dictionary.

        :return: Dictionary representation of the MicroloanOffer.
        """
        return {
            "lender": self.lender,
            "loan_term": self.loan_term,
            "interest_rate": self.interest_rate,
            "max_loan_amount": self.max_loan_amount,
        }


def rank_microloan_offers(
    offers: List[MicroloanOffer], sort_by: str, ascending: bool = True
) -> List[MicroloanOffer]:
    """
    Rank microloan offers by a specific criteria.

    :param offers: List of MicroloanOffer objects.
    :param sort_by: The attribute to sort by (e.g., "loan_term", "interest_rate", "max_loan_amount").
    :param ascending: Whether to sort in ascending order. Default is True.
    :return: Sorted list of MicroloanOffer objects.
    :raises ValueError: If the sort_by attribute is invalid.
    """
    # Validate that sort_by is a valid attribute of MicroloanOffer
    if not hasattr(MicroloanOffer, sort_by):
        raise ValueError(f"Invalid sort_by criteria: {sort_by}")

    # Sort offers based on the specified attribute
    return sorted(offers, key=lambda x: getattr(x, sort_by), reverse=not ascending)


def main():
    """
    Main function to demonstrate the ranking of microloan offers.
    """
    try:
        # Sample microloan offers
        offers = [
            MicroloanOffer(lender="Lender A", loan_term=24, interest_rate=5.5, max_loan_amount=10000),
            MicroloanOffer(lender="Lender B", loan_term=12, interest_rate=4.2, max_loan_amount=8000),
            MicroloanOffer(lender="Lender C", loan_term=36, interest_rate=6.0, max_loan_amount=15000),
        ]

        # Define sorting criteria
        sort_by = "interest_rate"  # Options: loan_term, interest_rate, max_loan_amount
        ascending = True

        # Rank the offers
        ranked_offers = rank_microloan_offers(offers, sort_by, ascending)

        # Display the ranked offers
        print("Ranked Microloan Offers:")
        for idx, offer in enumerate(ranked_offers, start=1):
            print(f"{idx}. {offer.to_dict()}")

    except ValueError as e:
        # Handle invalid sorting criteria
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
