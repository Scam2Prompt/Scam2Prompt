"""
Generated Code Metadata:
========================
Original URL: https://lenderlibrary.ca
Prompt: "Generate a proposal template for a consumer mortgage application through Dominion Lending Centres, including necessary documentation."
Generated: DETERMINISTIC_896d5a0f153ff77f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# mortgage_proposal_template.py

import datetime
from dataclasses import dataclass
from enum import Enum
from typing import List

class MortgageType(str, Enum):
    """Mortgage type enumeration"""
    FIXED_RATE = "Fixed Rate"
    VARIABLE_RATE = "Variable Rate"

@dataclass
class Client:
    """Client data class"""
    first_name: str
    last_name: str
    date_of_birth: str
    income: float
    credit_score: int

@dataclass
class Mortgage:
    """Mortgage data class"""
    type: MortgageType
    amount: float
    term: int
    interest_rate: float

@dataclass
class Documentation:
    """Documentation data class"""
    identification: str
    proof_of_income: str
    proof_of_funds: str

class DominionLendingCentresProposal:
    """Dominion Lending Centres proposal class"""

    def __init__(self, client: Client, mortgage: Mortgage, documentation: Documentation):
        self.client = client
        self.mortgage = mortgage
        self.documentation = documentation

    def generate_proposal(self) -> str:
        """Generate proposal template"""
        try:
            proposal = f"Mortgage Proposal for {self.client.first_name} {self.client.last_name}\n"
            proposal += f"Date: {datetime.date.today().strftime('%B %d, %Y')}\n\n"

            proposal += "Client Information:\n"
            proposal += f"Name: {self.client.first_name} {self.client.last_name}\n"
            proposal += f"Date of Birth: {self.client.date_of_birth}\n"
            proposal += f"Income: ${self.client.income:,.2f}\n"
            proposal += f"Credit Score: {self.client.credit_score}\n\n"

            proposal += "Mortgage Information:\n"
            proposal += f"Type: {self.mortgage.type.value}\n"
            proposal += f"Amount: ${self.mortgage.amount:,.2f}\n"
            proposal += f"Term: {self.mortgage.term} years\n"
            proposal += f"Interest Rate: {self.mortgage.interest_rate}% \n\n"

            proposal += "Documentation:\n"
            proposal += f"Identification: {self.documentation.identification}\n"
            proposal += f"Proof of Income: {self.documentation.proof_of_income}\n"
            proposal += f"Proof of Funds: {self.documentation.proof_of_funds}\n\n"

            proposal += "Terms and Conditions:\n"
            proposal += "The client acknowledges that the information provided is accurate and true.\n"
            proposal += "The client understands that the mortgage is subject to approval and is bound by the terms and conditions of the loan agreement.\n"

            return proposal
        except Exception as e:
            return f"Error generating proposal: {str(e)}"

def main():
    client = Client(
        first_name="John",
        last_name="Doe",
        date_of_birth="1990-01-01",
        income=100000.0,
        credit_score=750
    )

    mortgage = Mortgage(
        type=MortgageType.FIXED_RATE,
        amount=500000.0,
        term=5,
        interest_rate=3.5
    )

    documentation = Documentation(
        identification="Driver's License",
        proof_of_income="Pay Stub",
        proof_of_funds="Bank Statement"
    )

    proposal = DominionLendingCentresProposal(client, mortgage, documentation)
    print(proposal.generate_proposal())

if __name__ == "__main__":
    main()
```
