"""
Generated Code Metadata:
========================
Original URL: https://rhinofinance.com
Prompt: Design a disbursement financing plan for a client with a pending injury claim in Canada, using Rhino Finance's services and taking into account the client's financial needs and litigation timeline.
Generated: DETERMINISTIC_ea9a3a2d39aae12d
Batch ID: 20250622_211156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Optional

class Client:
    """
    Represents a client with a pending injury claim.
    """
    def __init__(self, name: str, claim_amount: float, litigation_end_date: datetime.date):
        self.name = name
        self.claim_amount = claim_amount
        self.litigation_end_date = litigation_end_date


class FinancingPlan:
    """
    Represents a disbursement financing plan for a client.
    """
    def __init__(self, client: Client, loan_amount: float, interest_rate: float, repayment_date: datetime.date):
        self.client = client
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.repayment_date = repayment_date

    def calculate_total_repayment(self) -> float:
        """
        Calculates the total repayment amount based on the loan amount and interest rate.
        """
        duration_in_years = (self.repayment_date - datetime.date.today()).days / 365.0
        total_repayment = self.loan_amount * (1 + self.interest_rate * duration_in_years)
        return round(total_repayment, 2)


class RhinoFinance:
    """
    Represents Rhino Finance's services for disbursement financing.
    """
    MAX_LOAN_PERCENTAGE = 0.5  # Maximum loan amount as a percentage of the claim amount
    DEFAULT_INTEREST_RATE = 0.12  # Default annual interest rate

    @staticmethod
    def create_financing_plan(client: Client, requested_loan_amount: float) -> Optional[FinancingPlan]:
        """
        Creates a financing plan for the client based on their claim amount and litigation timeline.
        """
        try:
            # Validate loan amount
            max_loan_amount = client.claim_amount * RhinoFinance.MAX_LOAN_PERCENTAGE
            if requested_loan_amount > max_loan_amount:
                raise ValueError(f"Requested loan amount exceeds the maximum allowable limit of ${max_loan_amount:.2f}.")

            # Determine repayment date (end of litigation timeline)
            repayment_date = client.litigation_end_date
            if repayment_date <= datetime.date.today():
                raise ValueError("Litigation end date must be in the future.")

            # Create financing plan
            financing_plan = FinancingPlan(
                client=client,
                loan_amount=requested_loan_amount,
                interest_rate=RhinoFinance.DEFAULT_INTEREST_RATE,
                repayment_date=repayment_date
            )
            return financing_plan
        except ValueError as e:
            print(f"Error creating financing plan: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Create a client with a pending injury claim
    client = Client(
        name="John Doe",
        claim_amount=100000.0,  # Claim amount in CAD
        litigation_end_date=datetime.date(2025, 12, 31)  # Expected litigation end date
    )

    # Request a financing plan
    requested_loan_amount = 40000.0  # Requested loan amount in CAD
    financing_plan = RhinoFinance.create_financing_plan(client, requested_loan_amount)

    if financing_plan:
        print(f"Financing Plan for {client.name}:")
        print(f"  Loan Amount: ${financing_plan.loan_amount:.2f}")
        print(f"  Interest Rate: {financing_plan.interest_rate * 100:.2f}% per year")
        print(f"  Repayment Date: {financing_plan.repayment_date}")
        print(f"  Total Repayment Amount: ${financing_plan.calculate_total_repayment():.2f}")
    else:
        print("Failed to create financing plan.")
```
