"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maestrofinance.co.uk
Prompt: Develop a script to compare over 120 lenders and generate personalized funding options for SMEs, mimicking the instant comparison process described on Maestro Finance.
Generated: DETERMINISTIC_f29b11647bf7c935
Batch ID: 20250612_150116
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/lenders": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from typing import List, Dict, Any, Optional

class Lender:
    """
    Class to represent a single lender and its funding options.
    """

    def __init__(self, name: str, interest_rate: float, terms: List[int], max_loan_amount: float):
        """
        Initializes a Lender instance.

        Args:
            name: The name of the lender.
            interest_rate: The interest rate offered by the lender.
            terms: List of loan terms in months offered by the lender.
            max_loan_amount: The maximum loan amount the lender is willing to provide.
        """
        self.name = name
        self.interest_rate = interest_rate
        self.terms = terms
        self.max_loan_amount = max_loan_amount

    def generate_funding_option(self, loan_amount: float, loan_term: int) -> Optional[Dict[str, Any]]:
        """
        Generates a funding option based on the loan amount and term.

        Args:
            loan_amount: The requested loan amount.
            loan_term: The loan term in months.

        Returns:
            A dictionary containing funding option details, or None if the option is not available.
        """
        if loan_amount > self.max_loan_amount or loan_term not in self.terms:
            return None
        interest_payment = loan_amount * (self.interest_rate / 100) * (loan_term / 12)
        total_repayment = loan_amount + interest_payment
        return {
            'lender': self.name,
            'loan_amount': loan_amount,
            'interest_rate': self.interest_rate,
            'loan_term': loan_term,
            'total_repayment': total_repayment
        }


class SMEFundingComparator:
    """
    Class to compare funding options from multiple lenders for SMEs.
    """

    def __init__(self, lenders: List[Lender]):
        """
        Initializes the SMEFundingComparator instance.

        Args:
            lenders: A list of Lender instances to compare.
        """
        self.lenders = lenders

    def compare_funding_options(self, loan_amount: float, loan_terms: List[int]) -> List[Dict[str, Any]]:
        """
        Compares funding options for a given loan amount and terms.

        Args:
            loan_amount: The requested loan amount.
            loan_terms: List of loan terms in months to compare.

        Returns:
            A list of funding options available from lenders.
        """
        options = []
        for lender in self.lenders:
            for term in loan_terms:
                option = lender.generate_funding_option(loan_amount, term)
                if option:
                    options.append(option)
        return options


def fetch_lenders_data(api_url: str) -> List[Lender]:
    """
    Fetches lender data from a given API URL.

    Args:
        api_url: The URL of the API endpoint to fetch lender data.

    Returns:
        A list of Lender instances.

    Raises:
        Exception: If the API request fails or returns invalid data.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        lenders_data = response.json()
        
        lenders = []
        for lender_info in lenders_data:
            lender = Lender(
                name=lender_info['name'],
                interest_rate=lender_info['interest_rate'],
                terms=lender_info['terms'],
                max_loan_amount=lender_info['max_loan_amount']
            )
            lenders.append(lender)
        
        return lenders

    except requests.RequestException as e:
        raise Exception(f"Failed to fetch lender data: {e}")
    except (KeyError, ValueError) as e:
        raise Exception(f"Invalid data format: {e}")


def main():
    """
    Main function to execute the lender comparison process.
    """
    # Define the API endpoint to fetch lenders
    api_url = "https://api.example.com/lenders"
    
    try:
        # Fetch lenders data
        lenders = fetch_lenders_data(api_url)
        
        # Create an instance of the comparator
        comparator = SMEFundingComparator(lenders)
        
        # Define loan parameters
        loan_amount = 50000  # Example loan amount
        loan_terms = [12, 24, 36]  # Example loan terms in months
        
        # Compare funding options
        funding_options = comparator.compare_funding_options(loan_amount, loan_terms)
        
        # Output the funding options
        for option in funding_options:
            print(option)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
