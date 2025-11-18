"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fondation.app
Prompt: Suggest best practices for designing a clear and intuitive CRM interface for non-profits, inspired by CRM.f's focus on simplicity and usability.
Generated: DETERMINISTIC_4a7d72eb8aa84cb8
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CRMInterface:
    """
    A class to represent a simple CRM interface designed for non-profits.
    This interface prioritizes clarity and usability, inspired by best practices.
    """

    def __init__(self):
        """
        Initializes the CRM interface with default values and settings.
        """
        self.contacts = []
        self.donations = []
        self.events = []
        self.settings = {
            'theme': 'light',
            'language': 'en',
        }

    def add_contact(self, name, email):
        """
        Adds a new contact to the CRM.

        Parameters:
            name (str): The name of the contact.
            email (str): The email address of the contact.

        Raises:
            ValueError: If the email is not valid.
        """
        if not self.is_valid_email(email):
            raise ValueError("Invalid email address.")
        
        contact = {'name': name, 'email': email}
        self.contacts.append(contact)
        print(f"Contact {name} added successfully.")

    def add_donation(self, amount, donor_name):
        """
        Records a new donation.

        Parameters:
            amount (float): The donation amount.
            donor_name (str): The name of the donor.

        Raises:
            ValueError: If the amount is not a positive number.
        """
        if amount <= 0:
            raise ValueError("Donation amount must be positive.")

        donation = {'amount': amount, 'donor_name': donor_name}
        self.donations.append(donation)
        print(f"Donation of ${amount} from {donor_name} recorded successfully.")

    def create_event(self, event_name, event_date):
        """
        Creates a new event.

        Parameters:
            event_name (str): The name of the event.
            event_date (str): The date of the event in 'YYYY-MM-DD' format.

        Raises:
            ValueError: If the event date is invalid.
        """
        if not self.is_valid_date(event_date):
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")

        event = {'event_name': event_name, 'event_date': event_date}
        self.events.append(event)
        print(f"Event '{event_name}' scheduled for {event_date}.")

    @staticmethod
    def is_valid_email(email):
        """
        Validates the email format.

        Parameters:
            email (str): The email address to validate.

        Returns:
            bool: True if the email is valid, False otherwise.
        """
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    @staticmethod
    def is_valid_date(date_string):
        """
        Validates the date format.

        Parameters:
            date_string (str): The date string to validate.

        Returns:
            bool: True if the date format is valid, False otherwise.
        """
        from datetime import datetime
        try:
            datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def change_setting(self, key, value):
        """
        Changes a setting in the CRM.

        Parameters:
            key (str): The setting key to change.
            value: The new value for the setting.

        Raises:
            KeyError: If the setting key does not exist.
        """
        if key not in self.settings:
            raise KeyError(f"Setting '{key}' does not exist.")
        
        self.settings[key] = value
        print(f"Setting '{key}' updated to {value}.")

# Example usage
if __name__ == "__main__":
    crm = CRMInterface()
    try:
        crm.add_contact("John Doe", "john.doe@example.com")
        crm.add_donation(100.5, "John Doe")
        crm.create_event("Fundraising Gala", "2023-12-15")
        crm.change_setting('theme', 'dark')
    except Exception as e:
        print(f"An error occurred: {e}")
```
