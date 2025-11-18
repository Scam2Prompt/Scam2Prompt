"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adelanto.cl
Prompt: Provide a Python example of an intermediary financial service that connects SMEs with lenders for short, medium, and long-term credit, as described on Adelanto.cl.
Generated: DETERMINISTIC_c21c925d3f0f5064
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List


class SME:
    """
    Represents a Small or Medium Enterprise (SME).
    """
    def __init__(self, name: str, sector: str, annual_revenue: float, credit_score: int):
        """
        Initializes an SME instance.

        :param name: Name of the SME.
        :param sector: Business sector of the SME (e.g., Retail, Manufacturing).
        :param annual_revenue: Annual revenue of the SME.
        :param credit_score: Credit score of the SME.
        """
        self.name = name
        self.sector = sector
        self.annual_revenue = annual_revenue
        self.credit_score = credit_score

    def __repr__(self):
        return f"SME(name={self.name}, sector={self.sector}, annual_revenue={self.annual_revenue}, credit_score={self.credit_score})"


class Lender:
    """
    Represents a lender offering credit to SMEs.
    """
    def __init__(self, name: str, max_credit_limit: float, minimum_credit_score: int, interest_rate: float):
        """
        Initializes a Lender instance.

        :param name: Name of the lender.
        :param max_credit_limit: Maximum credit limit the lender can provide.
        :param minimum_credit_score: Minimum credit score required to qualify for lending.
        :param interest_rate: Interest rate offered by the lender.
        """
        self.name = name
        self.max_credit_limit = max_credit_limit
        self.minimum_credit_score = minimum_credit_score
        self.interest_rate = interest_rate

    def __repr__(self):
        return f"Lender(name={self.name}, max_credit_limit={self.max_credit_limit}, minimum_credit_score={self.minimum_credit_score}, interest_rate={self.interest_rate})"


class CreditRequest:
    """
    Represents a credit request made by an SME.
    """
    def __init__(self, sme: SME, amount: float, term: str):
        """
        Initializes a CreditRequest instance.

        :param sme: The SME requesting the credit.
        :param amount: Amount of credit requested.
        :param term: Term of the credit (e.g., 'short', 'medium', 'long').
        """
        self.sme = sme
        self.amount = amount
        self.term = term
        self.request_date = datetime.datetime.now()

    def __repr__(self):
        return f"CreditRequest(sme={self.sme.name}, amount={self.amount}, term={self.term}, request_date={self.request_date})"


class FinancialService:
    """
    Intermediary financial service connecting SMEs with lenders.
    """
    def __init__(self):
        """
        Initializes the FinancialService instance.
        """
        self.lenders: List[Lender] = []

    def register_lender(self, lender: Lender):
        """
        Registers a lender to the service.

        :param lender: Lender to register.
        """
        self.lenders.append(lender)

    def find_lender_for_request(self, credit_request: CreditRequest) -> List[Lender]:
        """
        Finds suitable lenders for the given credit request.

        :param credit_request: The credit request made by an SME.
        :return: A list of lenders that match the request criteria.
        """
        suitable_lenders = []
        for lender in self.lenders:
            if (
                credit_request.amount <= lender.max_credit_limit and
                credit_request.sme.credit_score >= lender.minimum_credit_score
            ):
                suitable_lenders.append(lender)
        return suitable_lenders

    def process_credit_request(self, credit_request: CreditRequest) -> str:
        """
        Processes a credit request and matches it with suitable lenders.

        :param credit_request: The credit request made by an SME.
        :return: A message indicating the outcome of the request.
        """
        try:
            suitable_lenders = self.find_lender_for_request(credit_request)
            if not suitable_lenders:
                return f"No lenders found for SME '{credit_request.sme.name}' requesting {credit_request.amount} on a {credit_request.term}-term."
            return f"Suitable lenders for SME '{credit_request.sme.name}': {[lender.name for lender in suitable_lenders]}"
        except Exception as e:
            return f"Error processing credit request: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Create SMEs
    sme1 = SME(name="Tech Innovators", sector="Technology", annual_revenue=500000, credit_score=750)
    sme2 = SME(name="Green Builders", sector="Construction", annual_revenue=300000, credit_score=650)

    # Create lenders
    lender1 = Lender(name="Lender A", max_credit_limit=1000000, minimum_credit_score=700, interest_rate=5.0)
    lender2 = Lender(name="Lender B", max_credit_limit=500000, minimum_credit_score=650, interest_rate=4.5)

    # Register lenders
    financial_service = FinancialService()
    financial_service.register_lender(lender1)
    financial_service.register_lender(lender2)

    # Create credit requests
    credit_request1 = CreditRequest(sme=sme1, amount=200000, term="medium")
    credit_request2 = CreditRequest(sme=sme2, amount=600000, term="long")

    # Process credit requests
    print(financial_service.process_credit_request(credit_request1))
    print(financial_service.process_credit_request(credit_request2))
```
