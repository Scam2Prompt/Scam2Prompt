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
# crm.py

class Volunteer:
    """Class to represent a volunteer in the nonprofit organization."""
    
    def __init__(self, name, email, phone):
        """
        Initialize a new volunteer.

        :param name: str - Name of the volunteer
        :param email: str - Email address of the volunteer
        :param phone: str - Phone number of the volunteer
        """
        self.name = name
        self.email = email
        self.phone = phone
        self.hours_logged = 0

    def log_hours(self, hours):
        """
        Log hours worked by the volunteer.

        :param hours: float - Number of hours to log
        :raises ValueError: If hours is negative
        """
        if hours < 0:
            raise ValueError("Hours cannot be negative.")
        self.hours_logged += hours

    def __str__(self):
        return f"Volunteer(Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Hours Logged: {self.hours_logged})"


class Beneficiary:
    """Class to represent a beneficiary in the nonprofit organization."""
    
    def __init__(self, name, contact_info):
        """
        Initialize a new beneficiary.

        :param name: str - Name of the beneficiary
        :param contact_info: str - Contact information of the beneficiary
        """
        self.name = name
        self.contact_info = contact_info

    def __str__(self):
        return f"Beneficiary(Name: {self.name}, Contact Info: {self.contact_info})"


class CRM:
    """Class to manage volunteers and beneficiaries in the nonprofit organization."""
    
    def __init__(self):
        """Initialize the CRM with empty lists for volunteers and beneficiaries."""
        self.volunteers = []
        self.beneficiaries = []

    def add_volunteer(self, volunteer):
        """
        Add a volunteer to the CRM.

        :param volunteer: Volunteer - The volunteer to add
        """
        self.volunteers.append(volunteer)

    def add_beneficiary(self, beneficiary):
        """
        Add a beneficiary to the CRM.

        :param beneficiary: Beneficiary - The beneficiary to add
        """
        self.beneficiaries.append(beneficiary)

    def list_volunteers(self):
        """Return a list of all volunteers."""
        return self.volunteers

    def list_beneficiaries(self):
        """Return a list of all beneficiaries."""
        return self.beneficiaries

    def __str__(self):
        return f"CRM(Volunteers: {len(self.volunteers)}, Beneficiaries: {len(self.beneficiaries)})"


# Example usage
if __name__ == "__main__":
    # Create a CRM instance
    crm = CRM()

    # Create and add volunteers
    volunteer1 = Volunteer("Alice Smith", "alice@example.com", "123-456-7890")
    volunteer2 = Volunteer("Bob Johnson", "bob@example.com", "098-765-4321")
    crm.add_volunteer(volunteer1)
    crm.add_volunteer(volunteer2)

    # Create and add beneficiaries
    beneficiary1 = Beneficiary("Charlie Brown", "charlie@example.com")
    beneficiary2 = Beneficiary("Daisy White", "daisy@example.com")
    crm.add_beneficiary(beneficiary1)
    crm.add_beneficiary(beneficiary2)

    # Log hours for a volunteer
    try:
        volunteer1.log_hours(5)
    except ValueError as e:
        print(f"Error logging hours: {e}")

    # Print CRM details
    print(crm)
    print("Volunteers:")
    for volunteer in crm.list_volunteers():
        print(volunteer)
    print("Beneficiaries:")
    for beneficiary in crm.list_beneficiaries():
        print(beneficiary)
```
