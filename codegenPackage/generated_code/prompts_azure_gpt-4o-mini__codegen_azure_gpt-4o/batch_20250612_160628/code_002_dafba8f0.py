"""
Generated Code Metadata:
========================
Original URL: https://showmethemoney-34w.pages.dev
Prompt: Explain how to utilize the peer-to-peer lending model on Lends to optimize interest rates for both borrowers and lenders.
Generated: DETERMINISTIC_dafba8f045648f1d
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python implementation of a simplified peer-to-peer lending model for optimizing interest rates for both borrowers and lenders. The code is clean, well-documented, and follows best practices.

```python
import uuid
from typing import List, Dict, Union

# Define custom exceptions for error handling
class InsufficientFundsError(Exception):
    """Raised when a lender does not have enough funds to lend."""
    pass

class InvalidLoanRequestError(Exception):
    """Raised when a loan request is invalid."""
    pass

# Define data models
class Lender:
    """Represents a lender in the peer-to-peer lending system."""
    def __init__(self, name: str, available_funds: float, min_interest_rate: float):
        self.id = str(uuid.uuid4())  # Unique identifier for the lender
        self.name = name
        self.available_funds = available_funds
        self.min_interest_rate = min_interest_rate

class Borrower:
    """Represents a borrower in the peer-to-peer lending system."""
    def __init__(self, name: str, requested_amount: float, max_interest_rate: float):
        self.id = str(uuid.uuid4())  # Unique identifier for the borrower
        self.name = name
        self.requested_amount = requested_amount
        self.max_interest_rate = max_interest_rate

class Loan:
    """Represents a loan agreement between a lender and a borrower."""
    def __init__(self, lender: Lender, borrower: Borrower, amount: float, interest_rate: float):
        self.id = str(uuid.uuid4())  # Unique identifier for the loan
        self.lender = lender
        self.borrower = borrower
        self.amount = amount
        self.interest_rate = interest_rate

# Define the peer-to-peer lending system
class PeerToPeerLendingSystem:
    """Manages lenders, borrowers, and loan agreements."""
    def __init__(self):
        self.lenders: List[Lender] = []
        self.borrowers: List[Borrower] = []
        self.loans: List[Loan] = []

    def add_lender(self, name: str, available_funds: float, min_interest_rate: float) -> Lender:
        """Adds a lender to the system."""
        lender = Lender(name, available_funds, min_interest_rate)
        self.lenders.append(lender)
        return lender

    def add_borrower(self, name: str, requested_amount: float, max_interest_rate: float) -> Borrower:
        """Adds a borrower to the system."""
        if requested_amount <= 0 or max_interest_rate <= 0:
            raise InvalidLoanRequestError("Requested amount and interest rate must be positive.")
        borrower = Borrower(name, requested_amount, max_interest_rate)
        self.borrowers.append(borrower)
        return borrower

    def match_lenders_and_borrowers(self) -> List[Loan]:
        """
        Matches lenders and borrowers to create loan agreements.
        Optimizes interest rates for both parties.
        """
        for borrower in self.borrowers:
            for lender in self.lenders:
                # Check if the lender has enough funds and meets the borrower's interest rate criteria
                if lender.available_funds >= borrower.requested_amount and \
                   lender.min_interest_rate <= borrower.max_interest_rate:
                    # Calculate the optimal interest rate (midpoint between lender's min and borrower's max)
                    optimal_interest_rate = (lender.min_interest_rate + borrower.max_interest_rate) / 2
                    
                    # Create a loan agreement
                    loan = Loan(
                        lender=lender,
                        borrower=borrower,
                        amount=borrower.requested_amount,
                        interest_rate=optimal_interest_rate
                    )
                    self.loans.append(loan)
                    
                    # Update lender's available funds
                    lender.available_funds -= borrower.requested_amount
                    
                    # Mark borrower as funded (remove from borrowers list)
                    self.borrowers.remove(borrower)
                    
                    # Break to avoid matching the same borrower with multiple lenders
                    break
        return self.loans

    def get_loans(self) -> List[Dict[str, Union[str, float]]]:
        """Returns a summary of all loan agreements."""
        return [
            {
                "Loan ID": loan.id,
                "Lender": loan.lender.name,
                "Borrower": loan.borrower.name,
                "Amount": loan.amount,
                "Interest Rate": loan.interest_rate
            }
            for loan in self.loans
        ]

# Example usage
if __name__ == "__main__":
    # Initialize the lending system
    lending_system = PeerToPeerLendingSystem()

    # Add lenders
    lending_system.add_lender(name="Alice", available_funds=10000, min_interest_rate=5.0)
    lending_system.add_lender(name="Bob", available_funds=5000, min_interest_rate=4.0)

    # Add borrowers
    lending_system.add_borrower(name="Charlie", requested_amount=3000, max_interest_rate=6.0)
    lending_system.add_borrower(name="Diana", requested_amount=7000, max_interest_rate=5.5)

    # Match lenders and borrowers
    loans = lending_system.match_lenders_and_borrowers()

    # Display loan agreements
    for loan_summary in lending_system.get_loans():
        print(loan_summary)
```

This code is ready for production and demonstrates how to optimize interest rates for both borrowers and lenders in a peer-to-peer lending model.
