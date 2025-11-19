"""
Generated Code Metadata:
========================
Original URL: https://adelanto.cl
Prompt: Provide a Python example of an intermediary financial service that connects SMEs with lenders for short, medium, and long-term credit, as described on Adelanto.cl.
Generated: DETERMINISTIC_c21c925d3f0f5064
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# financial_service.py

from enum import Enum
from typing import Dict, List
from datetime import datetime, timedelta

class CreditTerm(Enum):
    """Enum for credit terms"""
    SHORT_TERM = 1
    MEDIUM_TERM = 2
    LONG_TERM = 3

class SME:
    """Class representing a Small or Medium-sized Enterprise"""
    def __init__(self, id: int, name: str, financial_needs: float):
        """
        Initialize an SME

        Args:
        id (int): Unique identifier for the SME
        name (str): Name of the SME
        financial_needs (float): Financial needs of the SME
        """
        self.id = id
        self.name = name
        self.financial_needs = financial_needs

class Lender:
    """Class representing a lender"""
    def __init__(self, id: int, name: str, available_funds: float):
        """
        Initialize a lender

        Args:
        id (int): Unique identifier for the lender
        name (str): Name of the lender
        available_funds (float): Available funds of the lender
        """
        self.id = id
        self.name = name
        self.available_funds = available_funds

class CreditRequest:
    """Class representing a credit request"""
    def __init__(self, sme: SME, credit_term: CreditTerm, amount: float):
        """
        Initialize a credit request

        Args:
        sme (SME): SME making the credit request
        credit_term (CreditTerm): Term of the credit
        amount (float): Amount of the credit
        """
        self.sme = sme
        self.credit_term = credit_term
        self.amount = amount

class FinancialService:
    """Class representing the financial service"""
    def __init__(self):
        self.smes: List[SME] = []
        self.lenders: List[Lender] = []
        self.credit_requests: List[CreditRequest] = []

    def add_sme(self, sme: SME):
        """Add an SME to the financial service"""
        self.smes.append(sme)

    def add_lender(self, lender: Lender):
        """Add a lender to the financial service"""
        self.lenders.append(lender)

    def make_credit_request(self, credit_request: CreditRequest):
        """Make a credit request"""
        self.credit_requests.append(credit_request)
        self.process_credit_request(credit_request)

    def process_credit_request(self, credit_request: CreditRequest):
        """Process a credit request"""
        suitable_lenders = self.find_suitable_lenders(credit_request)
        if suitable_lenders:
            # Assign the credit to the most suitable lender
            lender = suitable_lenders[0]
            lender.available_funds -= credit_request.amount
            print(f"Credit of {credit_request.amount} assigned to {lender.name} for {credit_request.sme.name}")
        else:
            print(f"No suitable lender found for {credit_request.sme.name}")

    def find_suitable_lenders(self, credit_request: CreditRequest) -> List[Lender]:
        """Find suitable lenders for a credit request"""
        suitable_lenders = []
        for lender in self.lenders:
            if lender.available_funds >= credit_request.amount:
                suitable_lenders.append(lender)
        # Sort lenders by available funds in descending order
        suitable_lenders.sort(key=lambda x: x.available_funds, reverse=True)
        return suitable_lenders

def main():
    financial_service = FinancialService()

    sme1 = SME(1, "SME 1", 10000.0)
    sme2 = SME(2, "SME 2", 5000.0)

    lender1 = Lender(1, "Lender 1", 20000.0)
    lender2 = Lender(2, "Lender 2", 15000.0)

    financial_service.add_sme(sme1)
    financial_service.add_sme(sme2)

    financial_service.add_lender(lender1)
    financial_service.add_lender(lender2)

    credit_request1 = CreditRequest(sme1, CreditTerm.SHORT_TERM, 5000.0)
    credit_request2 = CreditRequest(sme2, CreditTerm.MEDIUM_TERM, 10000.0)

    financial_service.make_credit_request(credit_request1)
    financial_service.make_credit_request(credit_request2)

if __name__ == "__main__":
    main()
```
