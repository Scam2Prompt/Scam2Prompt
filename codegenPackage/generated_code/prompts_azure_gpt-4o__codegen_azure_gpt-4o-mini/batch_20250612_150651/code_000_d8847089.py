"""
Generated Code Metadata:
========================
Original URL: https://armourersandbrasiers.co.uk
Prompt: Write Python code to simulate a grant allocation system for the Armourers & Brasiers' Gauntlet Trust, incorporating criteria for funding small charities, science education, and Materials Science research.
Generated: DETERMINISTIC_d88470899002822a
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class GrantApplication:
    """Class representing a grant application."""
    
    def __init__(self, applicant_name: str, amount_requested: float, category: str, description: str):
        self.applicant_name = applicant_name
        self.amount_requested = amount_requested
        self.category = category
        self.description = description
        self.status = "Pending"  # Status can be Pending, Approved, or Rejected

    def approve(self):
        """Approve the grant application."""
        self.status = "Approved"

    def reject(self):
        """Reject the grant application."""
        self.status = "Rejected"

class GrantAllocationSystem:
    """Class to manage the grant allocation process."""
    
    def __init__(self):
        self.applications: List[GrantApplication] = []
        self.budget: float = 100000.0  # Total budget for grants

    def submit_application(self, application: GrantApplication) -> None:
        """Submit a new grant application."""
        self.applications.append(application)

    def review_applications(self) -> None:
        """Review all applications and allocate grants based on criteria."""
        for application in self.applications:
            if self.is_eligible(application):
                if application.amount_requested <= self.budget:
                    application.approve()
                    self.budget -= application.amount_requested
                else:
                    application.reject()
            else:
                application.reject()

    def is_eligible(self, application: GrantApplication) -> bool:
        """Check if the application meets the eligibility criteria."""
        eligible_categories = ["Small Charity", "Science Education", "Materials Science Research"]
        return application.category in eligible_categories

    def get_application_status(self) -> List[Dict[str, Any]]:
        """Get the status of all applications."""
        return [{"applicant_name": app.applicant_name, "status": app.status, "amount_requested": app.amount_requested} for app in self.applications]

    def save_applications(self, filename: str) -> None:
        """Save applications to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_application_status(), file, indent=4)
        except IOError as e:
            print(f"Error saving applications to file: {e}")

    def load_applications(self, filename: str) -> None:
        """Load applications from a JSON file."""
        try:
            with open(filename, 'r') as file:
                applications_data = json.load(file)
                for app_data in applications_data:
                    application = GrantApplication(app_data['applicant_name'], app_data['amount_requested'], app_data['category'], "")
                    application.status = app_data['status']
                    self.applications.append(application)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading applications from file: {e}")

# Example usage
if __name__ == "__main__":
    system = GrantAllocationSystem()
    
    # Submitting applications
    system.submit_application(GrantApplication("Charity A", 5000, "Small Charity", "Support for local community projects."))
    system.submit_application(GrantApplication("School B", 15000, "Science Education", "STEM workshops for students."))
    system.submit_application(GrantApplication("Research Lab C", 20000, "Materials Science Research", "Innovative materials research."))
    
    # Review applications
    system.review_applications()
    
    # Get application statuses
    statuses = system.get_application_status()
    print(json.dumps(statuses, indent=4))
    
    # Save to file
    system.save_applications("grant_applications.json")
    
    # Load from file
    system.load_applications("grant_applications.json")
```
