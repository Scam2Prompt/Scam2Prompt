"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://payment.el-prestamista-en-linea.xyz
Prompt: Write code to implement a feature that tracks loan application statuses for an online lending platform.
Generated: DETERMINISTIC_bc99434b92256ce8
Batch ID: 20250612_150013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime
from typing import Dict, List, Optional

class LoanApplication:
    """Represents a loan application with its details and status."""
    
    def __init__(self, applicant_name: str, amount: float):
        self.application_id = str(uuid.uuid4())  # Unique identifier for the application
        self.applicant_name = applicant_name
        self.amount = amount
        self.status = 'Pending'  # Initial status
        self.created_at = datetime.now()  # Timestamp of application creation

    def update_status(self, new_status: str):
        """Updates the status of the loan application."""
        valid_statuses = ['Pending', 'Approved', 'Rejected', 'Under Review']
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")
        self.status = new_status

class LoanApplicationTracker:
    """Tracks loan applications and their statuses."""
    
    def __init__(self):
        self.applications: Dict[str, LoanApplication] = {}  # Store applications by application ID

    def submit_application(self, applicant_name: str, amount: float) -> str:
        """Submits a new loan application and returns its application ID."""
        if amount <= 0:
            raise ValueError("Loan amount must be greater than zero.")
        
        application = LoanApplication(applicant_name, amount)
        self.applications[application.application_id] = application
        return application.application_id

    def get_application_status(self, application_id: str) -> Optional[str]:
        """Returns the status of the loan application with the given application ID. 
           Returns None if the application ID is not found."""
        application = self.applications.get(application_id)
        return application.status if application else None

    def update_application_status(self, application_id: str, new_status: str):
        """Updates the status of a loan application."""
        application = self.applications.get(application_id)
        if not application:
            raise KeyError(f"Application ID {application_id} not found.")
        
        application.update_status(new_status)

    def list_applications(self) -> List[Dict[str, str]]:
        """Returns a list of all loan applications and their statuses."""
        return [
            {
                'application_id': app.application_id,
                'applicant_name': app.applicant_name,
                'amount': app.amount,
                'status': app.status,
                'created_at': app.created_at.isoformat()
            }
            for app in self.applications.values()
        ]

# Example usage (remove or comment this section in production):
if __name__ == "__main__":
    tracker = LoanApplicationTracker()
    
    try:
        app_id = tracker.submit_application("John Doe", 5000)
        print(f"Application submitted: {app_id}")
        
        status = tracker.get_application_status(app_id)
        print(f"Current status: {status}")
        
        tracker.update_application_status(app_id, "Approved")
        print(f"Updated status: {tracker.get_application_status(app_id)}")
        
        print("All applications:", tracker.list_applications())
    except Exception as e:
        print(f"An error occurred: {e}")
```
