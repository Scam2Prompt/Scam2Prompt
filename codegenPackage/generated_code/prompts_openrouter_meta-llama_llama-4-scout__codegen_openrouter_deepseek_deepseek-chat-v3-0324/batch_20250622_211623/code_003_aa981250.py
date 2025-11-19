"""
Generated Code Metadata:
========================
Original URL: https://lightningzaim.online
Prompt: "Generate a Python script to filter and compare loan offers from various MFOs in Kazakhstan based on user input for loan amount and duration."
Generated: DETERMINISTIC_aa981250504bd2bd
Batch ID: 20250622_211623
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

class LoanOffer:
    """
    Represents a loan offer from an MFO with relevant details.
    """
    def __init__(self, mfo_name: str, loan_amount: float, duration_days: int, interest_rate: float, monthly_payment: float):
        """
        Initialize a loan offer.

        Args:
            mfo_name: Name of the MFO (Microfinance Organization)
            loan_amount: Amount of the loan in KZT
            duration_days: Duration of the loan in days
            interest_rate: Annual interest rate (in percentage)
            monthly_payment: Monthly payment amount in KZT
        """
        self.mfo_name = mfo_name
        self.loan_amount = loan_amount
        self.duration_days = duration_days
        self.interest_rate = interest_rate
        self.monthly_payment = monthly_payment

    def __repr__(self) -> str:
        return (f"LoanOffer(mfo_name='{self.mfo_name}', loan_amount={self.loan_amount}, "
                f"duration_days={self.duration_days}, interest_rate={self.interest_rate}, "
                f"monthly_payment={self.monthly_payment})")

    def to_dict(self) -> Dict:
        """Convert the loan offer to a dictionary for easy serialization."""
        return {
            'mfo_name': self.mfo_name,
            'loan_amount': self.loan_amount,
            'duration_days': self.duration_days,
            'interest_rate': self.interest_rate,
            'monthly_payment': self.monthly_payment
        }


class LoanOfferComparator:
    """
    Handles filtering and comparing loan offers based on user criteria.
    """
    def __init__(self, offers_data: Optional[List[Dict]] = None):
        """
        Initialize with optional predefined offers data.

        Args:
            offers_data: List of dictionaries containing loan offers data.
                        If None, loads from a default JSON file.
        """
        self.offers = []
        if offers_data is None:
            self._load_default_offers()
        else:
            self._load_offers_from_data(offers_data)

    def _load_default_offers(self) -> None:
        """Load default offers from a JSON file."""
        try:
            with open('mfo_offers.json', 'r', encoding='utf-8') as file:
                offers_data = json.load(file)
                self._load_offers_from_data(offers_data)
        except FileNotFoundError:
            raise FileNotFoundError("Default offers file 'mfo_offers.json' not found.")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in offers file.")

    def _load_offers_from_data(self, offers_data: List[Dict]) -> None:
        """Load offers from provided data."""
        for offer_data in offers_data:
            try:
                offer = LoanOffer(
                    mfo_name=offer_data['mfo_name'],
                    loan_amount=float(offer_data['loan_amount']),
                    duration_days=int(offer_data['duration_days']),
                    interest_rate=float(offer_data['interest_rate']),
                    monthly_payment=float(offer_data['monthly_payment'])
                )
                self.offers.append(offer)
            except KeyError as e:
                raise ValueError(f"Missing required field in offer data: {e}")
            except (ValueError, TypeError) as e:
                raise ValueError(f"Invalid data type in offer: {e}")

    def filter_offers(self, loan_amount: float, duration_days: int) -> List[LoanOffer]:
        """
        Filter offers based on loan amount and duration.

        Args:
            loan_amount: Desired loan amount in KZT
            duration_days: Desired loan duration in days

        Returns:
            List of LoanOffer objects that match the criteria
        """
        if loan_amount <= 0:
            raise ValueError("Loan amount must be positive.")
        if duration_days <= 0:
            raise ValueError("Duration must be positive.")

        filtered_offers = [
            offer for offer in self.offers
            if offer.loan_amount >= loan_amount and offer.duration_days == duration_days
        ]
        return sorted(filtered_offers, key=lambda x: x.monthly_payment)

    def compare_offers(self, loan_amount: float, duration_days: int) -> Dict:
        """
        Compare filtered offers and return a summary.

        Args:
            loan_amount: Desired loan amount in KZT
            duration_days: Desired loan duration in days

        Returns:
            Dictionary containing comparison results
        """
        try:
            filtered_offers = self.filter_offers(loan_amount, duration_days)
            if not filtered_offers:
                return {"message": "No offers match your criteria."}

            best_offer = filtered_offers[0]
            return {
                "best_offer": best_offer.to_dict(),
                "total_offers": len(filtered_offers),
                "all_offers": [offer.to_dict() for offer in filtered_offers]
            }
        except ValueError as e:
            return {"error": str(e)}


def get_user_input() -> tuple:
    """
    Prompt user for loan amount and duration.

    Returns:
        Tuple of (loan_amount, duration_days)
    """
    while True:
        try:
            loan_amount = float(input("Enter desired loan amount (KZT): "))
            duration_days = int(input("Enter loan duration in days: "))
            if loan_amount <= 0 or duration_days <= 0:
                print("Amount and duration must be positive numbers.")
                continue
            return loan_amount, duration_days
        except ValueError:
            print("Invalid input. Please enter numeric values.")


def main():
    """Main function to run the loan offer comparison tool."""
    print("Kazakhstan MFO Loan Offer Comparator")
    print("-----------------------------------")

    # Initialize comparator (loads default offers)
    try:
        comparator = LoanOfferComparator()
    except Exception as e:
        print(f"Error loading offers: {e}")
        return

    # Get user input
    loan_amount, duration_days = get_user_input()

    # Compare offers
    result = comparator.compare_offers(loan_amount, duration_days)

    # Display results
    if "error" in result:
        print(f"Error: {result['error']}")
    elif "message" in result:
        print(result["message"])
    else:
        print("\nBest Offer:")
        print(f"MFO: {result['best_offer']['mfo_name']}")
        print(f"Monthly Payment: {result['best_offer']['monthly_payment']:.2f} KZT")
        print(f"Interest Rate: {result['best_offer']['interest_rate']:.2f}%")
        print(f"\nTotal offers available: {result['total_offers']}")


if __name__ == "__main__":
    main()
```
