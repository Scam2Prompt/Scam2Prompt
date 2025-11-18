"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypto-ax.com
Prompt: Create a function to simulate peer-to-peer funding for leveraged margin trading in cryptocurrencies, referencing the system described on crypto-hold.com.
Generated: DETERMINISTIC_965261bcae42b5f2
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Union

class PeerToPeerFunding:
    def __init__(self):
        self.lenders = []  # List to store lender accounts
        self.borrowers = []  # List to store borrower accounts
        self.open_loans = []  # List to store active loans

    def add_lender(self, lender_id: str, amount: float) -> None:
        """Add a lender to the system."""
        if amount <= 0:
            raise ValueError("Lender amount must be greater than zero.")
        lender = {'id': lender_id, 'amount': amount}
        self.lenders.append(lender)

    def add_borrower(self, borrower_id: str, amount: float, leverage: float) -> None:
        """Add a borrower to the system."""
        if amount <= 0 or leverage <= 1:
            raise ValueError("Borrower amount must be greater than zero and leverage must be greater than 1.")
        borrower = {'id': borrower_id, 'amount': amount, 'leverage': leverage}
        self.borrowers.append(borrower)

    def fund_borrowers(self) -> List[Dict[str, Union[str, float]]]:
        """Match lenders with borrowers and fund the loans."""
        funded_loans = []
        for borrower in self.borrowers:
            amount_needed = borrower['amount'] * borrower['leverage']
            available_funds = sum(lender['amount'] for lender in self.lenders)

            if available_funds < amount_needed:
                raise RuntimeError("Insufficient funds available for the requested loan.")

            # Randomly select lenders to fund the loan
            funding_amount = min(amount_needed, available_funds)
            loan = {'borrower_id': borrower['id'], 'amount': funding_amount}
            funded_loans.append(loan)

            # Deduct funded amount from lenders
            while funding_amount > 0 and self.lenders:
                lender = random.choice(self.lenders)
                lender_fund = lender['amount']
                if lender_fund > 0:
                    amount_to_fund = min(funding_amount, lender_fund)
                    lender['amount'] -= amount_to_fund
                    funding_amount -= amount_to_fund
                    self.open_loans.append(loan)

            # Remove lender if funded amount is zero
            self.lenders = [lender for lender in self.lenders if lender['amount'] > 0]

        return funded_loans

    def get_open_loans(self) -> List[Dict[str, Union[str, float]]]:
        """Retrieve the currently open loans."""
        return self.open_loans

# Example usage
if __name__ == "__main__":
    funding_system = PeerToPeerFunding()
    
    try:
        funding_system.add_lender("Lender1", 1000.0)
        funding_system.add_lender("Lender2", 500.0)
        
        funding_system.add_borrower("Borrower1", 200.0, 2.0)
        funding_system.add_borrower("Borrower2", 300.0, 1.5)
        
        funded_loans = funding_system.fund_borrowers()
        print("Funded Loans:", funded_loans)
        
        open_loans = funding_system.get_open_loans()
        print("Open Loans:", open_loans)
    
    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")
```
