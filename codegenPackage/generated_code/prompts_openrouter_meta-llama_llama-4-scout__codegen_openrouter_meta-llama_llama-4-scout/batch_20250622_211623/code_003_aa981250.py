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
# loan_comparator.py

class LoanOffer:
    """Represents a loan offer from an MFO."""

    def __init__(self, name, interest_rate, loan_amount, duration, monthly_payment):
        """
        Initializes a LoanOffer object.

        Args:
            name (str): Name of the MFO.
            interest_rate (float): Interest rate of the loan.
            loan_amount (float): Loan amount offered.
            duration (int): Loan duration in months.
            monthly_payment (float): Monthly payment amount.
        """
        self.name = name
        self.interest_rate = interest_rate
        self.loan_amount = loan_amount
        self.duration = duration
        self.monthly_payment = monthly_payment

    def __repr__(self):
        return f"LoanOffer('{self.name}', {self.interest_rate}, {self.loan_amount}, {self.duration}, {self.monthly_payment})"


class LoanComparator:
    """Compares loan offers from various MFOs."""

    def __init__(self):
        self.loan_offers = []

    def add_loan_offer(self, loan_offer):
        """
        Adds a loan offer to the comparator.

        Args:
            loan_offer (LoanOffer): Loan offer to add.
        """
        self.loan_offers.append(loan_offer)

    def filter_loan_offers(self, loan_amount, duration):
        """
        Filters loan offers based on user input.

        Args:
            loan_amount (float): Desired loan amount.
            duration (int): Desired loan duration in months.

        Returns:
            list[LoanOffer]: Filtered loan offers.
        """
        return [
            offer
            for offer in self.loan_offers
            if offer.loan_amount >= loan_amount and offer.duration == duration
        ]

    def compare_loan_offers(self, loan_offers):
        """
        Compares loan offers based on interest rate and monthly payment.

        Args:
            loan_offers (list[LoanOffer]): Loan offers to compare.

        Returns:
            list[LoanOffer]: Sorted loan offers.
        """
        return sorted(
            loan_offers, key=lambda offer: (offer.interest_rate, offer.monthly_payment)
        )


def main():
    comparator = LoanComparator()

    # Sample loan offers from various MFOs in Kazakhstan
    loan_offers = [
        LoanOffer("ForteBank", 18.0, 1000000, 12, 90000),
        LoanOffer("Halyk Bank", 19.0, 1000000, 12, 92000),
        LoanOffer("KazInterBank", 17.0, 1000000, 12, 88000),
        LoanOffer("ForteBank", 18.5, 500000, 6, 85000),
    ]

    for offer in loan_offers:
        comparator.add_loan_offer(offer)

    try:
        loan_amount = float(input("Enter the desired loan amount: "))
        duration = int(input("Enter the desired loan duration in months: "))

        filtered_offers = comparator.filter_loan_offers(loan_amount, duration)
        if not filtered_offers:
            print("No loan offers found matching your criteria.")
            return

        sorted_offers = comparator.compare_loan_offers(filtered_offers)

        print("Sorted loan offers:")
        for i, offer in enumerate(sorted_offers, start=1):
            print(
                f"{i}. {offer.name}: Interest Rate = {offer.interest_rate}%, "
                f"Monthly Payment = {offer.monthly_payment}, "
                f"Loan Amount = {offer.loan_amount}, "
                f"Duration = {offer.duration} months"
            )

    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
```
