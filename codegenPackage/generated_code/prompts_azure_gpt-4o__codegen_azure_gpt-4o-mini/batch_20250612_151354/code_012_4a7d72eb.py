"""
Generated Code Metadata:
========================
Original URL: https://fondation.app
Prompt: Suggest best practices for designing a clear and intuitive CRM interface for non-profits, inspired by CRM.f's focus on simplicity and usability.
Generated: DETERMINISTIC_4a7d72eb8aa84cb8
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CRMInterface:
    """
    A class to represent a simple and intuitive CRM interface for non-profits.
    This interface focuses on usability and clarity, inspired by best practices.
    """

    def __init__(self):
        """
        Initializes the CRM interface with default settings.
        """
        self.contacts = []  # List to store contact information
        self.donations = []  # List to store donation records

    def add_contact(self, name: str, email: str, phone: str) -> None:
        """
        Adds a new contact to the CRM.

        Parameters:
        name (str): The name of the contact.
        email (str): The email address of the contact.
        phone (str): The phone number of the contact.

        Raises:
        ValueError: If any of the parameters are empty or invalid.
        """
        if not name or not email or not phone:
            raise ValueError("Name, email, and phone cannot be empty.")
        
        contact = {
            'name': name,
            'email': email,
            'phone': phone
        }
        self.contacts.append(contact)
        print(f"Contact added: {contact}")

    def record_donation(self, donor_name: str, amount: float) -> None:
        """
        Records a donation made by a donor.

        Parameters:
        donor_name (str): The name of the donor.
        amount (float): The amount donated.

        Raises:
        ValueError: If the donor name is empty or the amount is not positive.
        """
        if not donor_name:
            raise ValueError("Donor name cannot be empty.")
        if amount <= 0:
            raise ValueError("Donation amount must be positive.")

        donation = {
            'donor_name': donor_name,
            'amount': amount
        }
        self.donations.append(donation)
        print(f"Donation recorded: {donation}")

    def display_contacts(self) -> None:
        """
        Displays all contacts in the CRM.
        """
        if not self.contacts:
            print("No contacts available.")
            return
        
        print("Contacts:")
        for contact in self.contacts:
            print(f"- {contact['name']} | Email: {contact['email']} | Phone: {contact['phone']}")

    def display_donations(self) -> None:
        """
        Displays all donations recorded in the CRM.
        """
        if not self.donations:
            print("No donations recorded.")
            return
        
        print("Donations:")
        for donation in self.donations:
            print(f"- Donor: {donation['donor_name']} | Amount: ${donation['amount']:.2f}")

# Example usage
if __name__ == "__main__":
    crm = CRMInterface()
    
    try:
        crm.add_contact("John Doe", "john@example.com", "123-456-7890")
        crm.record_donation("John Doe", 100.0)
        crm.display_contacts()
        crm.display_donations()
    except ValueError as e:
        print(f"Error: {e}")
```
