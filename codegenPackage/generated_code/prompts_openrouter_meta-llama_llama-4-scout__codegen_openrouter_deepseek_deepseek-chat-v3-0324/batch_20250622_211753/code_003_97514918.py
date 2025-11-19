"""
Generated Code Metadata:
========================
Original URL: https://woodao.org
Prompt: What are the different types of loans and credit facilities offered by بانک ملت, and what are the eligibility criteria and application processes for each?
Generated: DETERMINISTIC_97514918f784e13f
Batch ID: 20250622_211753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-
"""
Bank Melli Loan and Credit Facility Information System

This script provides information about various loan and credit facilities offered by Bank Melli (بانک ملت),
including eligibility criteria and application processes.

Note: This is a simulated system for demonstration purposes only.
Actual loan terms and conditions may vary and should be verified with the bank.
"""

from typing import Dict, List, Tuple
from enum import Enum
import json

class LoanType(Enum):
    """Enumeration of loan types offered by Bank Melli"""
    MORTGAGE = "Mortgage Loan"
    PERSONAL = "Personal Loan"
    AUTO = "Auto Loan"
    BUSINESS = "Business Loan"
    EDUCATION = "Education Loan"
    AGRICULTURE = "Agriculture Loan"
    MARRIAGE = "Marriage Loan"
    RENOVATION = "Home Renovation Loan"

class LoanInfo:
    """Class representing loan information including eligibility and application process"""
    
    def __init__(self, name: LoanType, description: str, 
                 eligibility: List[str], documents: List[str], 
                 process: List[str], max_amount: str, 
                 interest_rate: str, repayment_period: str):
        self.name = name
        self.description = description
        self.eligibility = eligibility
        self.documents = documents
        self.process = process
        self.max_amount = max_amount
        self.interest_rate = interest_rate
        self.repayment_period = repayment_period
    
    def to_dict(self) -> Dict:
        """Convert loan information to dictionary"""
        return {
            "name": self.name.value,
            "description": self.description,
            "eligibility": self.eligibility,
            "required_documents": self.documents,
            "application_process": self.process,
            "maximum_amount": self.max_amount,
            "interest_rate": self.interest_rate,
            "repayment_period": self.repayment_period
        }

class BankMelliLoanSystem:
    """Main class representing Bank Melli loan information system"""
    
    def __init__(self):
        self.loans = self._initialize_loans()
    
    def _initialize_loans(self) -> Dict[LoanType, LoanInfo]:
        """Initialize loan data"""
        loans = {
            LoanType.MORTGAGE: LoanInfo(
                name=LoanType.MORTGAGE,
                description="Loan for purchasing residential properties",
                eligibility=[
                    "Iranian citizenship",
                    "Minimum age of 18",
                    "Stable income source",
                    "Good credit history",
                    "Property appraisal"
                ],
                documents=[
                    "National ID",
                    "Income proof",
                    "Property documents",
                    "Bank statements (last 6 months)"
                ],
                process=[
                    "Submit application form",
                    "Provide required documents",
                    "Property appraisal",
                    "Loan approval",
                    "Sign contract",
                    "Disbursement"
                ],
                max_amount="Up to 80% of property value",
                interest_rate="Variable, based on central bank rates",
                repayment_period="Up to 20 years"
            ),
            LoanType.PERSONAL: LoanInfo(
                name=LoanType.PERSONAL,
                description="Multipurpose personal loan for various needs",
                eligibility=[
                    "Iranian citizenship",
                    "Minimum age of 18",
                    "Stable income source",
                    "Good credit history"
                ],
                documents=[
                    "National ID",
                    "Income proof",
                    "Bank statements (last 3 months)"
                ],
                process=[
                    "Submit application form",
                    "Provide required documents",
                    "Credit evaluation",
                    "Approval",
                    "Disbursement"
                ],
                max_amount="Up to 500 million IRR",
                interest_rate="Fixed rate as per bank policy",
                repayment_period="Up to 5 years"
            ),
            LoanType.AUTO: LoanInfo(
                name=LoanType.AUTO,
                description="Loan for purchasing new or used vehicles",
                eligibility=[
                    "Iranian citizenship",
                    "Minimum age of 18",
                    "Stable income source",
                    "Good credit history",
                    "Vehicle insurance"
                ],
                documents=[
                    "National ID",
                    "Income proof",
                    "Vehicle purchase agreement",
                    "Bank statements"
                ],
                process=[
                    "Submit application form",
                    "Provide required documents",
                    "Vehicle appraisal",
                    "Loan approval",
                    "Sign contract",
                    "Disbursement"
                ],
                max_amount="Up to 70% of vehicle value",
                interest_rate="Fixed rate as per bank policy",
                repayment_period="Up to 7 years"
            ),
            LoanType.BUSINESS: LoanInfo(
                name=LoanType.BUSINESS,
                description="Loan for business expansion or working capital",
                eligibility=[
                    "Registered business",
                    "Minimum 2 years operational history",
                    "Positive cash flow",
                    "Business plan"
                ],
                documents=[
                    "Business registration",
                    "Financial statements (2 years)",
                    "Tax records",
                    "Bank statements",
                    "Business plan"
                ],
                process=[
                    "Submit application form",
                    "Provide required documents",
                    "Business evaluation",
                    "Collateral assessment",
                    "Loan approval",
                    "Disbursement"
                ],
                max_amount="Based on business valuation",
                interest_rate="Variable, based on business risk",
                repayment_period="Up to 10 years"
            ),
            LoanType.EDUCATION: LoanInfo(
                name=LoanType.EDUCATION,
                description="Loan for covering education expenses",
                eligibility=[
                    "Iranian citizenship",
                    "Admission to accredited institution",
                    "Co-signer with stable income"
                ],
                documents=[
                    "National ID",
                    "Admission letter",
                    "Fee structure",
                    "Co-signer documents"
                ],
                process=[
                    "Submit application form",
                    "Provide required documents",
                    "Approval",
                    "Disbursement to institution"
                ],
                max_amount="Up to full tuition amount",
                interest_rate="Subsidized rate",
                repayment_period="Grace period + up to 5 years"
            )
        }
        return loans
    
    def get_loan_types(self) -> List[str]:
        """Get list of available loan types"""
        return [loan.value for loan in self.loans.keys()]
    
    def get_loan_info(self, loan_type: str) -> Dict:
        """
        Get detailed information about a specific loan type
        
        Args:
            loan_type: Name of the loan type to get information for
            
        Returns:
            Dictionary containing loan information
            
        Raises:
            ValueError: If loan type is not found
        """
        try:
            selected_loan = LoanType(loan_type)
            return self.loans[selected_loan].to_dict()
        except ValueError:
            raise ValueError(f"Invalid loan type. Available types are: {self.get_loan_types()}")
    
    def get_all_loans_info(self) -> List[Dict]:
        """Get information about all available loan types"""
        return [loan.to_dict() for loan in self.loans.values()]
    
    def to_json(self) -> str:
        """Export all loan information as JSON"""
        return json.dumps(self.get_all_loans_info(), ensure_ascii=False, indent=2)

def main():
    """Main function to demonstrate the system"""
    bank_system = BankMelliLoanSystem()
    
    print("Available loan types:")
    for loan in bank_system.get_loan_types():
        print(f"- {loan}")
    
    print("\nSample loan information (Mortgage Loan):")
    print(json.dumps(bank_system.get_loan_info("Mortgage Loan"), indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
```
