"""
Generated Code Metadata:
========================
Original URL: https://agdbank.com.br
Prompt: Generate a script to simulate agricultural financing scenarios, incorporating AGDbank's approach to connecting agribusinesses with investors via capital markets.
Generated: DETERMINISTIC_0ace3e59a1618d07
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Union

class AgriculturalLoan:
    """
    Represents an agricultural loan product with terms and conditions.
    """
    def __init__(
        self,
        loan_id: str,
        principal: float,
        interest_rate: float,
        term_years: int,
        loan_type: str,
        collateral_required: bool,
        risk_level: str
    ):
        self.loan_id = loan_id
        self.principal = principal
        self.interest_rate = interest_rate
        self.term_years = term_years
        self.loan_type = loan_type  # e.g., "Equipment", "Land", "Operating"
        self.collateral_required = collateral_required
        self.risk_level = risk_level  # "Low", "Medium", "High"
        self.creation_date = datetime.now()
        self.status = "Available"
        
    def to_dict(self) -> Dict:
        """Convert loan object to dictionary for serialization."""
        return {
            "loan_id": self.loan_id,
            "principal": self.principal,
            "interest_rate": self.interest_rate,
            "term_years": self.term_years,
            "loan_type": self.loan_type,
            "collateral_required": self.collateral_required,
            "risk_level": self.risk_level,
            "creation_date": self.creation_date.isoformat(),
            "status": self.status
        }

class Investor:
    """
    Represents an investor participating in agricultural financing.
    """
    def __init__(
        self,
        investor_id: str,
        name: str,
        investment_capacity: float,
        risk_appetite: str,
        preferred_loan_types: List[str]
    ):
        self.investor_id = investor_id
        self.name = name
        self.investment_capacity = investment_capacity
        self.risk_appetite = risk_appetite  # "Low", "Medium", "High"
        self.preferred_loan_types = preferred_loan_types
        self.invested_amount = 0.0
        
    def can_invest(self, loan: AgriculturalLoan) -> bool:
        """Check if investor can invest in the given loan."""
        return (
            self.investment_capacity - self.invested_amount >= loan.principal and
            self.risk_appetite == loan.risk_level and
            loan.loan_type in self.preferred_loan_types
        )
        
    def invest(self, loan: AgriculturalLoan) -> bool:
        """Invest in a loan if criteria are met."""
        if self.can_invest(loan):
            self.invested_amount += loan.principal
            return True
        return False
        
    def to_dict(self) -> Dict:
        """Convert investor object to dictionary for serialization."""
        return {
            "investor_id": self.investor_id,
            "name": self.name,
            "investment_capacity": self.investment_capacity,
            "risk_appetite": self.risk_appetite,
            "preferred_loan_types": self.preferred_loan_types,
            "invested_amount": self.invested_amount
        }

class AGDMarketplace:
    """
    Simulates AGDbank's agricultural financing marketplace connecting agribusinesses with investors.
    """
    def __init__(self):
        self.loans: List[AgriculturalLoan] = []
        self.investors: List[Investor] = []
        
    def add_loan(self, loan: AgriculturalLoan) -> None:
        """Add a new loan to the marketplace."""
        self.loans.append(loan)
        
    def add_investor(self, investor: Investor) -> None:
        """Add a new investor to the marketplace."""
        self.investors.append(investor)
        
    def match_loans_to_investors(self) -> Dict[str, List[Dict]]:
        """
        Match available loans to suitable investors based on criteria.
        Returns a dictionary of matches and unmatched loans.
        """
        matches = []
        unmatched_loans = []
        
        for loan in self.loans:
            if loan.status != "Available":
                continue
                
            matched = False
            for investor in self.investors:
                if investor.can_invest(loan):
                    if investor.invest(loan):
                        loan.status = "Funded"
                        matches.append({
                            "loan_id": loan.loan_id,
                            "investor_id": investor.investor_id,
                            "amount": loan.principal,
                            "match_date": datetime.now().isoformat()
                        })
                        matched = True
                        break
                        
            if not matched:
                unmatched_loans.append(loan.to_dict())
                
        return {
            "matches": matches,
            "unmatched_loans": unmatched_loans
        }
        
    def generate_loan_repayment_schedule(self, loan_id: str) -> Optional[List[Dict]]:
        """
        Generate a repayment schedule for a funded loan.
        Returns None if loan not found or not funded.
        """
        loan = next((l for l in self.loans if l.loan_id == loan_id), None)
        if not loan or loan.status != "Funded":
            return None
            
        schedule = []
        monthly_payment = self._calculate_monthly_payment(
            loan.principal,
            loan.interest_rate,
            loan.term_years
        )
        
        current_date = datetime.now()
        remaining_balance = loan.principal
        
        for month in range(1, loan.term_years * 12 + 1):
            interest_payment = remaining_balance * (loan.interest_rate / 12 / 100)
            principal_payment = monthly_payment - interest_payment
            remaining_balance -= principal_payment
            
            if remaining_balance < 0:
                remaining_balance = 0
                
            schedule.append({
                "month": month,
                "payment_date": (current_date + timedelta(days=30*month)).strftime("%Y-%m-%d"),
                "payment_amount": monthly_payment,
                "principal": principal_payment,
                "interest": interest_payment,
                "remaining_balance": remaining_balance
            })
            
        return schedule
        
    def _calculate_monthly_payment(self, principal: float, rate: float, years: int) -> float:
        """Calculate monthly payment using standard loan formula."""
        monthly_rate = rate / 12 / 100
        months = years * 12
        if monthly_rate == 0:
            return principal / months
        return principal * monthly_rate * (1 + monthly_rate)**months / ((1 + monthly_rate)**months - 1)
        
    def get_marketplace_summary(self) -> Dict:
        """Generate a summary of the marketplace state."""
        funded_loans = [l for l in self.loans if l.status == "Funded"]
        available_loans = [l for l in self.loans if l.status == "Available"]
        
        return {
            "total_loans": len(self.loans),
            "funded_loans": len(funded_loans),
            "available_loans": len(available_loans),
            "total_loan_value": sum(l.principal for l in self.loans),
            "funded_loan_value": sum(l.principal for l in funded_loans),
            "available_loan_value": sum(l.principal for l in available_loans),
            "total_investors": len(self.investors),
            "total_investment_capacity": sum(i.investment_capacity for i in self.investors),
            "utilized_capacity": sum(i.invested_amount for i in self.investors)
        }
        
    def save_state(self, filename: str) -> bool:
        """Save marketplace state to a JSON file."""
        try:
            state = {
                "loans": [loan.to_dict() for loan in self.loans],
                "investors": [investor.to_dict() for investor in self.investors]
            }
            with open(filename, 'w') as f:
                json.dump(state, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving state: {e}")
            return False
            
    def load_state(self, filename: str) -> bool:
        """Load marketplace state from a JSON file."""
        try:
            with open(filename, 'r') as f:
                state = json.load(f)
                
            self.loans = [
                AgriculturalLoan(
                    loan_id=loan["loan_id"],
                    principal=loan["principal"],
                    interest_rate=loan["interest_rate"],
                    term_years=loan["term_years"],
                    loan_type=loan["loan_type"],
                    collateral_required=loan["collateral_required"],
                    risk_level=loan["risk_level"]
                ) for loan in state["loans"]
            ]
            
            self.investors = [
                Investor(
                    investor_id=investor["investor_id"],
                    name=investor["name"],
                    investment_capacity=investor["investment_capacity"],
                    risk_appetite=investor["risk_appetite"],
                    preferred_loan_types=investor["preferred_loan_types"]
