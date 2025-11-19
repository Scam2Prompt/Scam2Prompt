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
# crm_interface.py

class CRMInterface:
    """
    A simple and intuitive CRM interface for non-profits.

    Attributes:
        contacts (list): A list of contacts.
        donations (list): A list of donations.
    """

    def __init__(self):
        """
        Initializes the CRM interface.
        """
        self.contacts = []
        self.donations = []

    def add_contact(self, name, email, phone):
        """
        Adds a new contact.

        Args:
            name (str): The contact's name.
            email (str): The contact's email.
            phone (str): The contact's phone number.

        Raises:
            ValueError: If any of the required fields are missing.
        """
        if not all([name, email, phone]):
            raise ValueError("Name, email, and phone are required")

        self.contacts.append({
            "name": name,
            "email": email,
            "phone": phone
        })

    def add_donation(self, contact_name, amount, date):
        """
        Adds a new donation.

        Args:
            contact_name (str): The name of the contact who made the donation.
            amount (float): The amount of the donation.
            date (str): The date of the donation.

        Raises:
            ValueError: If any of the required fields are missing.
            ValueError: If the contact does not exist.
        """
        if not all([contact_name, amount, date]):
            raise ValueError("Contact name, amount, and date are required")

        contact = next((c for c in self.contacts if c["name"] == contact_name), None)
        if not contact:
            raise ValueError("Contact does not exist")

        self.donations.append({
            "contact_name": contact_name,
            "amount": amount,
            "date": date
        })

    def get_contacts(self):
        """
        Gets all contacts.

        Returns:
            list: A list of contacts.
        """
        return self.contacts

    def get_donations(self):
        """
        Gets all donations.

        Returns:
            list: A list of donations.
        """
        return self.donations

    def get_contact_donations(self, contact_name):
        """
        Gets all donations for a contact.

        Args:
            contact_name (str): The name of the contact.

        Returns:
            list: A list of donations for the contact.

        Raises:
            ValueError: If the contact does not exist.
        """
        contact = next((c for c in self.contacts if c["name"] == contact_name), None)
        if not contact:
            raise ValueError("Contact does not exist")

        return [d for d in self.donations if d["contact_name"] == contact_name]


def main():
    crm = CRMInterface()

    while True:
        print("1. Add contact")
        print("2. Add donation")
        print("3. Get contacts")
        print("4. Get donations")
        print("5. Get contact donations")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter contact name: ")
            email = input("Enter contact email: ")
            phone = input("Enter contact phone: ")
            crm.add_contact(name, email, phone)
        elif choice == "2":
            contact_name = input("Enter contact name: ")
            amount = float(input("Enter donation amount: "))
            date = input("Enter donation date: ")
            crm.add_donation(contact_name, amount, date)
        elif choice == "3":
            print(crm.get_contacts())
        elif choice == "4":
            print(crm.get_donations())
        elif choice == "5":
            contact_name = input("Enter contact name: ")
            print(crm.get_contact_donations(contact_name))
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
