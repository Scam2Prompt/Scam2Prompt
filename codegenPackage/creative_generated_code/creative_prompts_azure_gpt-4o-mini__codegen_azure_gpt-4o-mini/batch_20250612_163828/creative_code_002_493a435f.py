"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fondation.app
Prompt: What are the key features of CRM.f for managing volunteers and beneficiaries in a nonprofit organization?
Generated: DETERMINISTIC_493a435fd0f6a407
Batch ID: 20250612_163828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# crm.py

class Volunteer:
    """Class to represent a volunteer."""
    
    def __init__(self, name, email, phone):
        """
        Initializes a new volunteer instance.
        
        :param name: Name of the volunteer
        :param email: Email address of the volunteer
        :param phone: Phone number of the volunteer
        """
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        """String representation of the volunteer."""
        return f"Volunteer(Name: {self.name}, Email: {self.email}, Phone: {self.phone})"


class Beneficiary:
    """Class to represent a beneficiary."""
    
    def __init__(self, name, email, needs):
        """
        Initializes a new beneficiary instance.
        
        :param name: Name of the beneficiary
        :param email: Email address of the beneficiary
        :param needs: Description of the beneficiary's needs
        """
        self.name = name
        self.email = email
        self.needs = needs

    def __str__(self):
        """String representation of the beneficiary."""
        return f"Beneficiary(Name: {self.name}, Email: {self.email}, Needs: {self.needs})"


class CRM:
    """Class to manage volunteers and beneficiaries."""
    
    def __init__(self):
        """Initializes the CRM with empty lists for volunteers and beneficiaries."""
        self.volunteers = []
        self.beneficiaries = []

    def add_volunteer(self, volunteer):
        """
        Adds a volunteer to the CRM.
        
        :param volunteer: Instance of Volunteer
        :raises ValueError: If the volunteer already exists
        """
        if any(v.email == volunteer.email for v in self.volunteers):
            raise ValueError("Volunteer with this email already exists.")
        self.volunteers.append(volunteer)
        print(f"Volunteer {volunteer.name} added.")

    def add_beneficiary(self, beneficiary):
        """
        Adds a beneficiary to the CRM.
        
        :param beneficiary: Instance of Beneficiary
        :raises ValueError: If the beneficiary already exists
        """
        if any(b.email == beneficiary.email for b in self.beneficiaries):
            raise ValueError("Beneficiary with this email already exists.")
        self.beneficiaries.append(beneficiary)
        print(f"Beneficiary {beneficiary.name} added.")

    def list_volunteers(self):
        """Lists all volunteers in the CRM."""
        return [str(volunteer) for volunteer in self.volunteers]

    def list_beneficiaries(self):
        """Lists all beneficiaries in the CRM."""
        return [str(beneficiary) for beneficiary in self.beneficiaries]

    def find_volunteer_by_email(self, email):
        """
        Finds a volunteer by their email.
        
        :param email: Email address of the volunteer
        :return: Volunteer instance or None if not found
        """
        for volunteer in self.volunteers:
            if volunteer.email == email:
                return volunteer
        return None

    def find_beneficiary_by_email(self, email):
        """
        Finds a beneficiary by their email.
        
        :param email: Email address of the beneficiary
        :return: Beneficiary instance or None if not found
        """
        for beneficiary in self.beneficiaries:
            if beneficiary.email == email:
                return beneficiary
        return None


# Example usage:
if __name__ == "__main__":
    crm_system = CRM()
    
    # Create and add volunteers
    try:
        volunteer1 = Volunteer("Alice Smith", "alice@example.com", "555-1234")
        crm_system.add_volunteer(volunteer1)
        
        volunteer2 = Volunteer("Bob Johnson", "bob@example.com", "555-5678")
        crm_system.add_volunteer(volunteer2)

        # List volunteers
        print("\nVolunteers:")
        print(crm_system.list_volunteers())

        # Create and add beneficiaries
        beneficiary1 = Beneficiary("Charlie Brown", "charlie@example.com", "Food assistance")
        crm_system.add_beneficiary(beneficiary1)

        beneficiary2 = Beneficiary("Diana Prince", "diana@example.com", "Housing support")
        crm_system.add_beneficiary(beneficiary2)

        # List beneficiaries
        print("\nBeneficiaries:")
        print(crm_system.list_beneficiaries())

    except ValueError as e:
        print(f"Error: {e}")
```
