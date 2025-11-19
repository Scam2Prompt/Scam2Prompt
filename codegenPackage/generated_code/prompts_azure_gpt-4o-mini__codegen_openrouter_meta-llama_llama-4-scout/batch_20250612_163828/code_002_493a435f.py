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
# Import required libraries
import pandas as pd

class NonprofitCRM:
    """
    A simple CRM system for managing volunteers and beneficiaries in a nonprofit organization.

    Attributes:
        volunteers (list): A list of volunteer objects.
        beneficiaries (list): A list of beneficiary objects.
    """

    def __init__(self):
        self.volunteers = []
        self.beneficiaries = []

    def add_volunteer(self, name, email, phone, skills):
        """
        Add a new volunteer to the CRM.

        Args:
            name (str): The volunteer's name.
            email (str): The volunteer's email address.
            phone (str): The volunteer's phone number.
            skills (list): A list of the volunteer's skills.

        Raises:
            ValueError: If the volunteer's name, email, or phone number is missing.
        """
        if not name or not email or not phone:
            raise ValueError("Name, email, and phone number are required.")

        volunteer = {
            "name": name,
            "email": email,
            "phone": phone,
            "skills": skills
        }
        self.volunteers.append(volunteer)

    def add_beneficiary(self, name, email, phone, needs):
        """
        Add a new beneficiary to the CRM.

        Args:
            name (str): The beneficiary's name.
            email (str): The beneficiary's email address.
            phone (str): The beneficiary's phone number.
            needs (list): A list of the beneficiary's needs.

        Raises:
            ValueError: If the beneficiary's name, email, or phone number is missing.
        """
        if not name or not email or not phone:
            raise ValueError("Name, email, and phone number are required.")

        beneficiary = {
            "name": name,
            "email": email,
            "phone": phone,
            "needs": needs
        }
        self.beneficiaries.append(beneficiary)

    def get_volunteer(self, name):
        """
        Get a volunteer by name.

        Args:
            name (str): The name of the volunteer to retrieve.

        Returns:
            dict: The volunteer object, or None if not found.
        """
        for volunteer in self.volunteers:
            if volunteer["name"] == name:
                return volunteer
        return None

    def get_beneficiary(self, name):
        """
        Get a beneficiary by name.

        Args:
            name (str): The name of the beneficiary to retrieve.

        Returns:
            dict: The beneficiary object, or None if not found.
        """
        for beneficiary in self.beneficiaries:
            if beneficiary["name"] == name:
                return beneficiary
        return None

    def assign_volunteer_to_beneficiary(self, volunteer_name, beneficiary_name):
        """
        Assign a volunteer to a beneficiary.

        Args:
            volunteer_name (str): The name of the volunteer to assign.
            beneficiary_name (str): The name of the beneficiary to assign to.

        Raises:
            ValueError: If the volunteer or beneficiary is not found.
        """
        volunteer = self.get_volunteer(volunteer_name)
        beneficiary = self.get_beneficiary(beneficiary_name)

        if not volunteer:
            raise ValueError("Volunteer not found.")
        if not beneficiary:
            raise ValueError("Beneficiary not found.")

        # Assign the volunteer to the beneficiary
        beneficiary["assigned_volunteer"] = volunteer

    def export_to_csv(self, filename):
        """
        Export the volunteers and beneficiaries to a CSV file.

        Args:
            filename (str): The name of the CSV file to export to.
        """
        volunteers_df = pd.DataFrame(self.volunteers)
        beneficiaries_df = pd.DataFrame(self.beneficiaries)

        with open(filename, "w") as f:
            volunteers_df.to_csv(f, index=False)
            f.write("\n")
            beneficiaries_df.to_csv(f, index=False)


def main():
    crm = NonprofitCRM()

    # Add some volunteers and beneficiaries
    crm.add_volunteer("John Doe", "john@example.com", "123-456-7890", ["fundraising", "event planning"])
    crm.add_volunteer("Jane Smith", "jane@example.com", "987-654-3210", ["social media", "communications"])
    crm.add_beneficiary("Bob Johnson", "bob@example.com", "555-123-4567", ["food assistance", "housing support"])
    crm.add_beneficiary("Alice Williams", "alice@example.com", "444-987-6543", ["job training", "education"])

    # Assign a volunteer to a beneficiary
    crm.assign_volunteer_to_beneficiary("John Doe", "Bob Johnson")

    # Export to CSV
    crm.export_to_csv("nonprofit_crm.csv")


if __name__ == "__main__":
    main()
```
