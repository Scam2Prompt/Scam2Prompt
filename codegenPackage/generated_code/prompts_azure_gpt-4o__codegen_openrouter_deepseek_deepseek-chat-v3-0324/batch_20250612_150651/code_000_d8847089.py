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
from typing import Dict, List, Optional, Union
from enum import Enum
from dataclasses import dataclass
from datetime import datetime


class GrantCategory(Enum):
    SMALL_CHARITY = "Small Charity"
    SCIENCE_EDUCATION = "Science Education"
    MATERIALS_SCIENCE_RESEARCH = "Materials Science Research"


@dataclass
class Applicant:
    name: str
    contact_email: str
    organization: str
    charity_number: Optional[str] = None
    annual_income: Optional[float] = None
    research_focus: Optional[str] = None
    education_level: Optional[str] = None


@dataclass
class GrantApplication:
    applicant: Applicant
    category: GrantCategory
    amount_requested: float
    project_description: str
    application_date: datetime = datetime.now()


class GrantAllocationSystem:
    def __init__(self):
        self.applications: List[GrantApplication] = []
        self.allocated_grants: Dict[str, float] = {}
        self.total_funds: float = 1000000.00  # Example total funds available
        self.allocated_funds: float = 0.0

    def submit_application(self, application: GrantApplication) -> bool:
        """Submit a grant application to the system."""
        try:
            self._validate_application(application)
            self.applications.append(application)
            return True
        except ValueError as e:
            print(f"Application validation failed: {e}")
            return False

    def _validate_application(self, application: GrantApplication) -> None:
        """Validate the grant application based on category-specific criteria."""
        if application.amount_requested <= 0:
            raise ValueError("Requested amount must be positive")

        if application.category == GrantCategory.SMALL_CHARITY:
            if not application.applicant.charity_number:
                raise ValueError("Charity number is required for small charity applications")
            if not application.applicant.annual_income or application.applicant.annual_income > 50000:
                raise ValueError("Annual income must be provided and under £50,000 for small charities")

        elif application.category == GrantCategory.SCIENCE_EDUCATION:
            if not application.applicant.education_level:
                raise ValueError("Education level must be specified for science education applications")

        elif application.category == GrantCategory.MATERIALS_SCIENCE_RESEARCH:
            if not application.applicant.research_focus:
                raise ValueError("Research focus must be specified for materials science research applications")
            if "materials science" not in application.applicant.research_focus.lower():
                raise ValueError("Research must be focused on materials science")

    def review_applications(self) -> None:
        """Review all submitted applications and allocate grants based on criteria."""
        for application in self.applications:
            if self.allocated_funds >= self.total_funds:
                print("All funds have been allocated.")
                break

            if self._meets_funding_criteria(application):
                amount_allocated = min(
                    application.amount_requested,
                    self.total_funds - self.allocated_funds
                )
                self.allocated_grants[application.applicant.organization] = amount_allocated
                self.allocated_funds += amount_allocated
                print(f"Grant of £{amount_allocated:.2f} allocated to {application.applicant.organization}")

    def _meets_funding_criteria(self, application: GrantApplication) -> bool:
        """Check if an application meets the funding criteria."""
        if application.category == GrantCategory.SMALL_CHARITY:
            return (
                application.applicant.annual_income <= 50000 and
                len(application.applicant.organization) < 20  # Example small org criteria
            )
        elif application.category == GrantCategory.SCIENCE_EDUCATION:
            return "school" in application.applicant.organization.lower() or "college" in application.applicant.organization.lower()
        elif application.category == GrantCategory.MATERIALS_SCIENCE_RESEARCH:
            return "materials science" in application.applicant.research_focus.lower()
        return False

    def get_allocated_grants(self) -> Dict[str, float]:
        """Return a dictionary of allocated grants."""
        return self.allocated_grants

    def save_allocations_to_file(self, filename: str = "grant_allocations.json") -> None:
        """Save the allocated grants to a JSON file."""
        try:
            with open(filename, "w") as f:
                json.dump({
                    "allocations": self.allocated_grants,
                    "total_allocated": self.allocated_funds,
                    "remaining_funds": self.total_funds - self.allocated_funds
                }, f, indent=2)
            print(f"Allocations saved to {filename}")
        except IOError as e:
            print(f"Error saving allocations: {e}")


# Example usage
if __name__ == "__main__":
    system = GrantAllocationSystem()

    # Example applications
    charity_applicant = Applicant(
        name="John Doe",
        contact_email="john@smallcharity.org",
        organization="Small Charity Ltd",
        charity_number="123456",
        annual_income=45000
    )
    charity_application = GrantApplication(
        applicant=charity_applicant,
        category=GrantCategory.SMALL_CHARITY,
        amount_requested=10000,
        project_description="Community support program"
    )

    education_applicant = Applicant(
        name="Jane Smith",
        contact_email="jane@sciencecollege.edu",
        organization="Science College",
        education_level="Secondary"
    )
    education_application = GrantApplication(
        applicant=education_applicant,
        category=GrantCategory.SCIENCE_EDUCATION,
        amount_requested=15000,
        project_description="STEM outreach program"
    )

    research_applicant = Applicant(
        name="Dr. Alice Johnson",
        contact_email="alice@university.edu",
        organization="Materials Research Institute",
        research_focus="Advanced materials science for sustainable energy"
    )
    research_application = GrantApplication(
        applicant=research_applicant,
        category=GrantCategory.MATERIALS_SCIENCE_RESEARCH,
        amount_requested=50000,
        project_description="Novel materials for solar cells"
    )

    # Submit applications
    system.submit_application(charity_application)
    system.submit_application(education_application)
    system.submit_application(research_application)

    # Review and allocate grants
    system.review_applications()

    # Save allocations
    system.save_allocations_to_file()
```
