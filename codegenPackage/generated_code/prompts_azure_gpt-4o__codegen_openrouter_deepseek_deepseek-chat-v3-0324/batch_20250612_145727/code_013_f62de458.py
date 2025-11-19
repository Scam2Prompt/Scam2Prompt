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
import json
from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum

class LoanTerm(Enum):
    SHORT = "short_term"
    MEDIUM = "medium_term"
    LONG = "long_term"

@dataclass
class MicroloanOffer:
    lender: str
    interest_rate: float
    term: LoanTerm
    max_amount: float
    min_amount: float
    fees: float
    approval_time: str  # e.g., "24_hours", "48_hours"
    eligibility_criteria: List[str]

class LoanAnalyzer:
    def __init__(self, offers: List[MicroloanOffer]):
        self.offers = offers

    def rank_by_interest_rate(self, ascending: bool = True) -> List[MicroloanOffer]:
        """Rank offers by interest rate (lowest first by default)."""
        return sorted(
            self.offers,
            key=lambda x: x.interest_rate,
            reverse=not ascending
        )

    def rank_by_loan_term(self, preferred_term: LoanTerm) -> List[MicroloanOffer]:
        """Rank offers by preferred loan term (matching term first)."""
        def term_priority(offer: MicroloanOffer) -> int:
            return 0 if offer.term == preferred_term else 1

        return sorted(self.offers, key=term_priority)

    def filter_by_amount(self, min_amount: Optional[float] = None, max_amount: Optional[float] = None) -> List[MicroloanOffer]:
        """Filter offers by loan amount range."""
        filtered = self.offers
        if min_amount is not None:
            filtered = [offer for offer in filtered if offer.min_amount <= min_amount]
        if max_amount is not None:
            filtered = [offer for offer in filtered if offer.max_amount >= max_amount]
        return filtered

    def get_best_offer(self, amount: float, preferred_term: Optional[LoanTerm] = None) -> Optional[MicroloanOffer]:
        """Get the best offer based on amount and optional preferred term."""
        filtered = self.filter_by_amount(min_amount=amount, max_amount=amount)
        
        if preferred_term:
            filtered = [offer for offer in filtered if offer.term == preferred_term]
        
        if not filtered:
            return None
            
        return min(filtered, key=lambda x: x.interest_rate)

    @classmethod
    def from_json(cls, file_path: str) -> 'LoanAnalyzer':
        """Create LoanAnalyzer from JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            offers = []
            for item in data['offers']:
                offers.append(
                    MicroloanOffer(
                        lender=item['lender'],
                        interest_rate=float(item['interest_rate']),
                        term=LoanTerm(item['term']),
                        max_amount=float(item['max_amount']),
                        min_amount=float(item['min_amount']),
                        fees=float(item['fees']),
                        approval_time=item['approval_time'],
                        eligibility_criteria=item['eligibility_criteria']
                    )
                )
            return cls(offers)
        except (FileNotFoundError, json.JSONDecodeError, KeyError, ValueError) as e:
            raise ValueError(f"Error loading JSON data: {str(e)}")

def display_offers(offers: List[MicroloanOffer]) -> None:
    """Display offers in a user-friendly format."""
    if not offers:
        print("No matching offers found.")
        return
    
    print("\nRank | Lender       | Interest Rate | Term        | Amount Range    | Fees   ")
    print("-" * 75)
    for i, offer in enumerate(offers, 1):
        print(
            f"{i:<4} | {offer.lender[:12]:<12} | {offer.interest_rate:<14.2f}% | "
            f"{offer.term.value[:10]:<10} | ${offer.min_amount:.0f}-${offer.max_amount:.0f} | "
            f"${offer.fees:.2f}"
        )

# Example usage
if __name__ == "__main__":
    try:
        analyzer = LoanAnalyzer.from_json("loan_offers.json")
        
        print("All offers:")
        display_offers(analyzer.offers)
        
        print("\nOffers ranked by interest rate (lowest first):")
        display_offers(analyzer.rank_by_interest_rate())
        
        print("\nOffers for medium-term loans:")
        display_offers(analyzer.rank_by_loan_term(LoanTerm.MEDIUM))
        
        print("\nBest offer for $1000 (short term):")
        best_offer = analyzer.get_best_offer(1000, LoanTerm.SHORT)
        display_offers([best_offer] if best_offer else [])
        
    except ValueError as e:
        print(f"Error: {str(e)}")
```
