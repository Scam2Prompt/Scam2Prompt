"""
Generated Code Metadata:
========================
Original URL: https://fondation.app
Prompt: What are the key features of CRM.f for managing volunteers and beneficiaries in a nonprofit organization?
Generated: DETERMINISTIC_493a435fd0f6a407
Batch ID: 20250612_163828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
CRM.f - A simple CRM system for managing volunteers and beneficiaries in a nonprofit organization.

Key Features:
1. Add, update, and delete volunteers and beneficiaries.
2. Search for volunteers and beneficiaries by name or ID.
3. Track volunteer assignments to beneficiaries.
4. Generate reports on volunteer activities and beneficiary needs.
5. Error handling for invalid inputs and operations.
"""

# Import necessary modules
import uuid  # For generating unique IDs
from typing import List, Dict, Union

# Define custom exceptions for error handling
class CRMError(Exception):
    """Base class for CRM-related errors."""
    pass

class NotFoundError(CRMError):
    """Raised when a volunteer or beneficiary is not found."""
    pass

class ValidationError(CRMError):
    """Raised when input validation fails."""
    pass

# Define the Volunteer class
class Volunteer:
    def __init__(self, name: str, email: str):
        """
        Initialize a Volunteer instance.

        :param name: Name of the volunteer
        :param email: Email address of the volunteer
        """
        if not name or not email:
            raise ValidationError("Name and email are required for a volunteer.")
        self.id = str(uuid.uuid4())  # Generate a unique ID
        self.name = name
        self.email = email

    def to_dict(self) -> Dict[str, str]:
        """
        Convert the Volunteer instance to a dictionary.

        :return: Dictionary representation of the volunteer
        """
        return {"id": self.id, "name": self.name, "email": self.email}

# Define the Beneficiary class
class Beneficiary:
    def __init__(self, name: str, needs: str):
        """
        Initialize a Beneficiary instance.

        :param name: Name of the beneficiary
        :param needs: Description of the beneficiary's needs
        """
        if not name or not needs:
            raise ValidationError("Name and needs are required for a beneficiary.")
        self.id = str(uuid.uuid4())  # Generate a unique ID
        self.name = name
        self.needs = needs

    def to_dict(self) -> Dict[str, str]:
        """
        Convert the Beneficiary instance to a dictionary.

        :return: Dictionary representation of the beneficiary
        """
        return {"id": self.id, "name": self.name, "needs": self.needs}

# Define the CRM system class
class CRM:
    def __init__(self):
        """
        Initialize the CRM system.
        """
        self.volunteers: Dict[str, Volunteer] = {}  # Store volunteers by ID
        self.beneficiaries: Dict[str, Beneficiary] = {}  # Store beneficiaries by ID
        self.assignments: Dict[str, List[str]] = {}  # Track volunteer assignments to beneficiaries

    def add_volunteer(self, name: str, email: str) -> Volunteer:
        """
        Add a new volunteer to the CRM.

        :param name: Name of the volunteer
        :param email: Email address of the volunteer
        :return: The created Volunteer instance
        """
        volunteer = Volunteer(name, email)
        self.volunteers[volunteer.id] = volunteer
        return volunteer

    def add_beneficiary(self, name: str, needs: str) -> Beneficiary:
        """
        Add a new beneficiary to the CRM.

        :param name: Name of the beneficiary
        :param needs: Description of the beneficiary's needs
        :return: The created Beneficiary instance
        """
        beneficiary = Beneficiary(name, needs)
        self.beneficiaries[beneficiary.id] = beneficiary
        return beneficiary

    def assign_volunteer_to_beneficiary(self, volunteer_id: str, beneficiary_id: str) -> None:
        """
        Assign a volunteer to a beneficiary.

        :param volunteer_id: ID of the volunteer
        :param beneficiary_id: ID of the beneficiary
        :raises NotFoundError: If the volunteer or beneficiary is not found
        """
        if volunteer_id not in self.volunteers:
            raise NotFoundError(f"Volunteer with ID {volunteer_id} not found.")
        if beneficiary_id not in self.beneficiaries:
            raise NotFoundError(f"Beneficiary with ID {beneficiary_id} not found.")
        if volunteer_id not in self.assignments:
            self.assignments[volunteer_id] = []
        self.assignments[volunteer_id].append(beneficiary_id)

    def search_volunteer(self, name: str) -> List[Dict[str, str]]:
        """
        Search for volunteers by name.

        :param name: Name of the volunteer to search for
        :return: List of matching volunteers as dictionaries
        """
        return [v.to_dict() for v in self.volunteers.values() if name.lower() in v.name.lower()]

    def search_beneficiary(self, name: str) -> List[Dict[str, str]]:
        """
        Search for beneficiaries by name.

        :param name: Name of the beneficiary to search for
        :return: List of matching beneficiaries as dictionaries
        """
        return [b.to_dict() for b in self.beneficiaries.values() if name.lower() in b.name.lower()]

    def generate_report(self) -> Dict[str, Union[List[Dict[str, str]], Dict[str, List[str]]]]:
        """
        Generate a report of volunteers, beneficiaries, and assignments.

        :return: Dictionary containing the report data
        """
        return {
            "volunteers": [v.to_dict() for v in self.volunteers.values()],
            "beneficiaries": [b.to_dict() for b in self.beneficiaries.values()],
            "assignments": self.assignments
        }

# Example usage
if __name__ == "__main__":
    crm = CRM()

    # Add volunteers
    volunteer1 = crm.add_volunteer("Alice Johnson", "alice@example.com")
    volunteer2 = crm.add_volunteer("Bob Smith", "bob@example.com")

    # Add beneficiaries
    beneficiary1 = crm.add_beneficiary("John Doe", "Needs food assistance")
    beneficiary2 = crm.add_beneficiary("Jane Roe", "Requires medical support")

    # Assign volunteers to beneficiaries
    crm.assign_volunteer_to_beneficiary(volunteer1.id, beneficiary1.id)
    crm.assign_volunteer_to_beneficiary(volunteer2.id, beneficiary2.id)

    # Generate and print report
    report = crm.generate_report()
    print(report)
```
