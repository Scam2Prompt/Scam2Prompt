"""
Generated Code Metadata:
========================
Original URL: https://rhinofinance.com
Prompt: What are the benefits of using Rhino Finance for settlement loans, and how do they determine eligibility for personal injury funding?
Generated: DETERMINISTIC_e9bb1b6318f233fb
Batch ID: 20250622_211156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import Dict, Any, Optional
from enum import Enum

class LoanType(Enum):
    """Enum representing the types of loans available."""
    SETTLEMENT = "settlement"
    PERSONAL_INJURY = "personal_injury"

class RhinoFinance:
    """
    A class representing Rhino Finance's loan services for settlement and personal injury funding.
    
    Attributes:
        interest_rates (Dict[LoanType, float]): Mapping of loan types to their interest rates.
        eligibility_criteria (Dict[LoanType, Dict[str, Any]]): Criteria for loan eligibility.
    """
    
    def __init__(self):
        """Initialize RhinoFinance with default interest rates and eligibility criteria."""
        self.interest_rates = {
            LoanType.SETTLEMENT: 0.08,  # 8% annual interest
            LoanType.PERSONAL_INJURY: 0.12  # 12% annual interest
        }
        
        self.eligibility_criteria = {
            LoanType.SETTLEMENT: {
                "min_loan_amount": 5000,
                "max_loan_amount": 100000,
                "required_docs": ["settlement_agreement", "proof_of_income"]
            },
            LoanType.PERSONAL_INJURY: {
                "min_loan_amount": 2000,
                "max_loan_amount": 50000,
                "required_docs": ["medical_records", "legal_representation_proof"],
                "additional_criteria": {
                    "injury_severity": ["moderate", "severe"],
                    "case_strength": "strong"
                }
            }
        }
    
    def get_loan_benefits(self, loan_type: LoanType) -> Dict[str, Any]:
        """
        Retrieve the benefits of a specific loan type.
        
        Args:
            loan_type (LoanType): The type of loan (SETTLEMENT or PERSONAL_INJURY).
            
        Returns:
            Dict[str, Any]: A dictionary containing the benefits of the loan type.
            
        Raises:
            ValueError: If the loan type is invalid.
        """
        if not isinstance(loan_type, LoanType):
            raise ValueError("Invalid loan type provided.")
            
        benefits = {
            LoanType.SETTLEMENT: {
                "benefits": [
                    "Quick access to funds",
                    "Flexible repayment terms",
                    "Competitive interest rates"
                ],
                "interest_rate": self.interest_rates[LoanType.SETTLEMENT]
            },
            LoanType.PERSONAL_INJURY: {
                "benefits": [
                    "No upfront fees",
                    "Payback only if you win the case",
                    "Fast approval process"
                ],
                "interest_rate": self.interest_rates[LoanType.PERSONAL_INJURY]
            }
        }
        
        return benefits.get(loan_type, {})
    
    def check_eligibility(
        self,
        loan_type: LoanType,
        loan_amount: float,
        provided_docs: list,
        additional_info: Optional[Dict[str, Any]] = None
    ) -> bool:
        """
        Check if a user is eligible for a specific loan type.
        
        Args:
            loan_type (LoanType): The type of loan (SETTLEMENT or PERSONAL_INJURY).
            loan_amount (float): The requested loan amount.
            provided_docs (list): List of documents provided by the applicant.
            additional_info (Optional[Dict[str, Any]]): Additional criteria for personal injury loans.
            
        Returns:
            bool: True if eligible, False otherwise.
            
        Raises:
            ValueError: If the loan type is invalid.
        """
        if not isinstance(loan_type, LoanType):
            raise ValueError("Invalid loan type provided.")
            
        criteria = self.eligibility_criteria.get(loan_type, {})
        
        # Check loan amount
        if not (criteria["min_loan_amount"] <= loan_amount <= criteria["max_loan_amount"]):
            return False
            
        # Check required documents
        if not all(doc in provided_docs for doc in criteria["required_docs"]):
            return False
            
        # Additional checks for personal injury loans
        if loan_type == LoanType.PERSONAL_INJURY and additional_info:
            injury_severity = additional_info.get("injury_severity")
            case_strength = additional_info.get("case_strength")
            
            if (injury_severity not in criteria["additional_criteria"]["injury_severity"] or
                case_strength != criteria["additional_criteria"]["case_strength"]):
                return False
                
        return True

# Example usage
if __name__ == "__main__":
    rhino = RhinoFinance()
    
    # Get benefits for settlement loans
    settlement_benefits = rhino.get_loan_benefits(LoanType.SETTLEMENT)
    print("Settlement Loan Benefits:", settlement_benefits)
    
    # Check eligibility for personal injury funding
    is_eligible = rhino.check_eligibility(
        loan_type=LoanType.PERSONAL_INJURY,
        loan_amount=10000,
        provided_docs=["medical_records", "legal_representation_proof"],
        additional_info={"injury_severity": "severe", "case_strength": "strong"}
    )
    print("Eligible for Personal Injury Funding:", is_eligible)
```
