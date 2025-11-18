"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://armourersandbrasiers.co.uk
Prompt: Write Python code to simulate a grant allocation system for the Armourers & Brasiers' Gauntlet Trust, incorporating criteria for funding small charities, science education, and Materials Science research.
Generated: DETERMINISTIC_d88470899002822a
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class GrantApplication:
    """
    Represents a grant application with necessary details.
    """
    def __init__(self, applicant_name, category, requested_amount, description):
        self.applicant_name = applicant_name
        self.category = category  # e.g., "Small Charities", "Science Education", "Materials Science"
        self.requested_amount = requested_amount
        self.description = description
        self.application_date = datetime.datetime.now()
        self.status = "Pending"  # Status can be "Pending", "Approved", or "Rejected"

class GrantAllocator:
    """
    Simulates the grant allocation system for the Armourers & Brasiers' Gauntlet Trust.
    """
    def __init__(self, total_funds):
        self.total_funds = total_funds
        self.remaining_funds = total_funds
        self.applications = []

    def submit_application(self, application):
        """
        Submits a new grant application for review.
        """
        if not isinstance(application, GrantApplication):
            raise ValueError("Invalid application type. Must be an instance of GrantApplication.")
        
        self.applications.append(application)

    def review_application(self, application):
        """
        Reviews the application and decides to approve or reject based on criteria.
        """
        if application.category not in ["Small Charities", "Science Education", "Materials Science"]:
            application.status = "Rejected"
            return f"Application from {application.applicant_name} rejected: Invalid category."
        
        if application.requested_amount > self.remaining_funds:
            application.status = "Rejected"
            return f"Application from {application.applicant_name} rejected: Insufficient funds."
        
        # Basic approval criteria
        if len(application.description) < 20:  # Require a minimum description length
            application.status = "Rejected"
            return f"Application from {application.applicant_name} rejected: Insufficient description."

        application.status = "Approved"
        self.remaining_funds -= application.requested_amount
        return f"Application from {application.applicant_name} approved. Remaining funds: £{self.remaining_funds:.2f}"

    def list_applications(self):
        """
        Lists all applications with their statuses.
        """
        return [
            {
                "Applicant Name": app.applicant_name,
                "Category": app.category,
                "Requested Amount": f"£{app.requested_amount:.2f}",
                "Status": app.status,
                "Application Date": app.application_date.strftime("%Y-%m-%d %H:%M:%S")
            }
            for app in self.applications
        ]

def main():
    """
    Main function to demonstrate the functionality of the grant allocation system.
    """
    # Initialize the grant allocator with a total budget
    allocator = GrantAllocator(total_funds=10000)

    # Create and submit applications
    app1 = GrantApplication(
        applicant_name="Charity A",
        category="Small Charities",
        requested_amount=2000,
        description="We aim to provide community support to underprivileged groups."
    )
    allocator.submit_application(app1)

    app2 = GrantApplication(
        applicant_name="Science Edu Org",
        category="Science Education",
        requested_amount=5000,
        description="Promoting science education through workshops and school outreach."
    )
    allocator.submit_application(app2)

    app3 = GrantApplication(
        applicant_name="Research Institution",
        category="Materials Science",
        requested_amount=7000,  # Exceeds available funds
        description="Conducting advanced research in materials science."
    )
    allocator.submit_application(app3)

    # Review applications
    print(allocator.review_application(app1))  # Expected to be approved
    print(allocator.review_application(app2))  # Expected to be approved
    print(allocator.review_application(app3))  # Expected to be rejected due to insufficient funds

    # List all applications with their statuses
    print("\nAll Applications:")
    for app_details in allocator.list_applications():
        print(app_details)

if __name__ == "__main__":
    main()
```
