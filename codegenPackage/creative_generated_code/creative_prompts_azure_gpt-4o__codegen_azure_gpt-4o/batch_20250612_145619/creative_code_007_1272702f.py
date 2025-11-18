"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://camelot.netlify.app
Prompt: Develop an algorithm to compare bridge loan offers for real estate investors, specifically matching the terms provided by Appak Capital.
Generated: DETERMINISTIC_1272702fd3fa2192
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class LoanOffer:
    """
    Represents a bridge loan offer from a lender.
    """
    def __init__(self, lender_name: str, loan_amount: float, interest_rate: float, 
                 loan_term: int, closing_fees: float, prepayment_penalty: float):
        self.lender_name = lender_name
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate  # Annual interest rate as a percentage
        self.loan_term = loan_term  # Term in months
        self.closing_fees = closing_fees  # Dollar amount
        self.prepayment_penalty = prepayment_penalty  # Dollar amount
    
    def calculate_total_cost(self) -> float:
        """
        Calculate the total cost of the loan based on the given terms.
        Includes interest payments, closing fees, and prepayment penalty.
        """
        # Monthly interest rate
        monthly_interest_rate = self.interest_rate / 100 / 12
        
        # Total interest over the loan term
        total_interest = self.loan_amount * monthly_interest_rate * self.loan_term
        
        # Total cost = interest + closing fees + prepayment penalty
        return total_interest + self.closing_fees + self.prepayment_penalty


def compare_loan_offers(offers: List[LoanOffer], target_loan: Dict) -> LoanOffer:
    """
    Compare multiple loan offers to find the best match based on the provided target loan terms.

    Args:
        offers (List[LoanOffer]): List of loan offers to compare.
        target_loan (Dict): Target loan terms to match. Keys:
                            - 'loan_amount': Desired loan amount
                            - 'loan_term': Desired loan term in months
                            - 'interest_rate': Desired interest rate (optional, threshold)
                            - 'max_closing_fees': Maximum acceptable closing fees (optional)

    Returns:
        LoanOffer: The best matching loan offer.
    """
    best_offer = None
    lowest_total_cost = float('inf')
    
    for offer in offers:
        # Check if basic terms match the target requirements
        if (offer.loan_amount != target_loan['loan_amount'] or
            offer.loan_term != target_loan['loan_term']):
            continue  # Skip offers that don't match loan amount or term
        
        # Optional filters for interest rate and closing fees
        if ('interest_rate' in target_loan and offer.interest_rate > target_loan['interest_rate']):
            continue
        if ('max_closing_fees' in target_loan and offer.closing_fees > target_loan['max_closing_fees']):
            continue
        
        # Calculate total cost for this offer
        total_cost = offer.calculate_total_cost()
        
        # Update the best offer if this one has a lower total cost
        if total_cost < lowest_total_cost:
            best_offer = offer
            lowest_total_cost = total_cost
    
    return best_offer


# Example usage
if __name__ == "__main__":
    # Define loan offers
    loan_offers = [
        LoanOffer("Lender A", 500000, 8.5, 12, 5000, 2000),
        LoanOffer("Lender B", 500000, 8.0, 12, 4000, 3000),
        LoanOffer("Lender C", 500000, 7.5, 12, 4500, 2500),
    ]
    
    # Define target loan terms
    target_loan_terms = {
        "loan_amount": 500000,
        "loan_term": 12,
        "interest_rate": 8.0,  # Optional: Maximum acceptable interest rate
        "max_closing_fees": 5000  # Optional: Maximum acceptable closing fees
    }
    
    # Compare offers
    best_offer = compare_loan_offers(loan_offers, target_loan_terms)
    
    if best_offer:
        print(f"Best Offer: {best_offer.lender_name}")
        print(f"  Loan Amount: ${best_offer.loan_amount}")
        print(f"  Interest Rate: {best_offer.interest_rate}%")
        print(f"  Loan Term: {best_offer.loan_term} months")
        print(f"  Closing Fees: ${best_offer.closing_fees}")
        print(f"  Prepayment Penalty: ${best_offer.prepayment_penalty}")
        print(f"  Total Cost: ${best_offer.calculate_total_cost():,.2f}")
    else:
        print("No suitable loan offer found.")
```
