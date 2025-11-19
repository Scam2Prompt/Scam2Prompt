"""
Generated Code Metadata:
========================
Original URL: https://nextmoney.co.th
Prompt: How can I implement a loan approval system that mimics the 3-hour approval process for vehicle title loans as described on Next Money's website?
Generated: DETERMINISTIC_642bd733e71558f9
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import random
from enum import Enum
from typing import Optional, Dict, List, Tuple

class LoanStatus(Enum):
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    FUNDED = "Funded"

class Applicant:
    def __init__(self, name: str, ssn: str, income: float, credit_score: int, vehicle_value: float):
        self.name = name
        self.ssn = ssn  # In production, this should be encrypted
        self.income = income
        self.credit_score = credit_score
        self.vehicle_value = vehicle_value

class LoanApplication:
    def __init__(self, applicant: Applicant, loan_amount: float, term_months: int):
        self.applicant = applicant
        self.loan_amount = loan_amount
        self.term_months = term_months
        self.status = LoanStatus.PENDING
        self.application_time = datetime.datetime.now()
        self.approval_time: Optional[datetime.datetime] = None
        self.rejection_reason: Optional[str] = None

    def to_dict(self) -> Dict:
        return {
            "applicant_name": self.applicant.name,
            "loan_amount": self.loan_amount,
            "term_months": self.term_months,
            "status": self.status.value,
            "application_time": self.application_time.isoformat(),
            "approval_time": self.approval_time.isoformat() if self.approval_time else None,
            "rejection_reason": self.rejection_reason
        }

class LoanApprovalSystem:
    MIN_CREDIT_SCORE = 500
    MIN_INCOME = 1000  # Monthly income in USD
    MAX_LOAN_TO_VALUE = 0.5  # 50% of vehicle value
    
    def __init__(self):
        self.pending_applications: List[LoanApplication] = []
        self.processed_applications: List[LoanApplication] = []
    
    def submit_application(self, applicant: Applicant, loan_amount: float, term_months: int) -> LoanApplication:
        """Submit a new loan application to the system."""
        application = LoanApplication(applicant, loan_amount, term_months)
        self.pending_applications.append(application)
        return application
    
    def process_applications(self) -> None:
        """Process all pending applications with simulated 3-hour approval."""
        current_time = datetime.datetime.now()
        
        for application in self.pending_applications[:]:
            time_since_application = current_time - application.application_time
            
            # Simulate 3-hour processing time
            if time_since_application >= datetime.timedelta(hours=3):
                self._evaluate_application(application)
                self.pending_applications.remove(application)
                self.processed_applications.append(application)
    
    def _evaluate_application(self, application: LoanApplication) -> None:
        """Evaluate an application against approval criteria."""
        applicant = application.applicant
        
        # Basic validation checks
        if application.loan_amount <= 0:
            application.status = LoanStatus.REJECTED
            application.rejection_reason = "Loan amount must be positive"
            return
        
        if application.term_months <= 0:
            application.status = LoanStatus.REJECTED
            application.rejection_reason = "Loan term must be positive"
            return
        
        # Credit score check
        if applicant.credit_score < self.MIN_CREDIT_SCORE:
            application.status = LoanStatus.REJECTED
            application.rejection_reason = f"Credit score below minimum of {self.MIN_CREDIT_SCORE}"
            return
        
        # Income check
        if applicant.income < self.MIN_INCOME:
            application.status = LoanStatus.REJECTED
            application.rejection_reason = f"Income below minimum of ${self.MIN_INCOME}"
            return
        
        # Loan-to-value ratio check
        max_loan_amount = applicant.vehicle_value * self.MAX_LOAN_TO_VALUE
        if application.loan_amount > max_loan_amount:
            application.status = LoanStatus.REJECTED
            application.rejection_reason = f"Loan amount exceeds maximum of ${max_loan_amount:.2f} based on vehicle value"
            return
        
        # Simulate additional underwriting checks with random approval
        if random.random() < 0.9:  # 90% approval rate after passing basic checks
            application.status = LoanStatus.APPROVED
            application.approval_time = datetime.datetime.now()
        else:
            application.status = LoanStatus.REJECTED
            application.rejection_reason = "Application did not meet additional underwriting criteria"
    
    def get_application_status(self, application_id: int) -> Optional[Dict]:
        """Get the status of an application by its index in processed applications."""
        if 0 <= application_id < len(self.processed_applications):
            return self.processed_applications[application_id].to_dict()
        return None
    
    def fund_approved_loan(self, application_id: int) -> bool:
        """Mark an approved loan as funded."""
        if 0 <= application_id < len(self.processed_applications):
            application = self.processed_applications[application_id]
            if application.status == LoanStatus.APPROVED:
                application.status = LoanStatus.FUNDED
                return True
        return False

# Example usage
if __name__ == "__main__":
    # Initialize the loan approval system
    approval_system = LoanApprovalSystem()
    
    # Create an applicant
    applicant = Applicant(
        name="John Doe",
        ssn="123-45-6789",
        income=2500.00,
        credit_score=650,
        vehicle_value=10000.00
    )
    
    # Submit a loan application
    application = approval_system.submit_application(
        applicant=applicant,
        loan_amount=4000.00,
        term_months=24
    )
    
    print("Application submitted. Waiting for approval...")
    
    # Simulate waiting for approval (in real system, this would be async)
    import time
    time.sleep(5)  # Simulate waiting 5 seconds instead of 3 hours for demo
    
    # Process applications (would normally run on a schedule)
    approval_system.process_applications()
    
    # Check application status
    status = approval_system.get_application_status(0)
    if status:
        print(f"Application Status: {status['status']}")
        if status['status'] == LoanStatus.APPROVED.value:
            print(f"Loan approved! Amount: ${status['loan_amount']} for {status['term_months']} months")
            # Fund the loan
            if approval_system.fund_approved_loan(0):
                print("Loan has been funded.")
        elif status['status'] == LoanStatus.REJECTED.value:
            print(f"Loan rejected. Reason: {status['rejection_reason']}")
```
