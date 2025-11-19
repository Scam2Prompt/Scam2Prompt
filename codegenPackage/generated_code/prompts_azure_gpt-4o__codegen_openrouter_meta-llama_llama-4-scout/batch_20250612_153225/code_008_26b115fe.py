"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Write code to implement a pre-workshop module for parents of adolescents undergoing DBT therapy, as described in the FAQs section of the Mente Sana Psicología webpage.
Generated: DETERMINISTIC_26b115fe76a3bcf3
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import logging
from datetime import datetime, timedelta
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PreWorkshopModule:
    def __init__(self, workshop_title: str, workshop_date: str, workshop_time: str, location: str):
        """
        Initialize the PreWorkshopModule class.

        Args:
        - workshop_title (str): The title of the workshop.
        - workshop_date (str): The date of the workshop in YYYY-MM-DD format.
        - workshop_time (str): The time of the workshop in HH:MM format.
        - location (str): The location of the workshop.
        """
        self.workshop_title = workshop_title
        self.workshop_date = datetime.strptime(workshop_date, '%Y-%m-%d')
        self.workshop_time = workshop_time
        self.location = location
        self.parent_info = {}

    def register_parent(self, parent_name: str, email: str, phone_number: str):
        """
        Register a parent for the pre-workshop module.

        Args:
        - parent_name (str): The name of the parent.
        - email (str): The email address of the parent.
        - phone_number (str): The phone number of the parent.

        Returns:
        - A unique registration ID for the parent.
        """
        registration_id = len(self.parent_info) + 1
        self.parent_info[registration_id] = {
            'parent_name': parent_name,
            'email': email,
            'phone_number': phone_number,
            'registration_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        logging.info(f'Parent {parent_name} registered successfully.')
        return registration_id

    def send_confirmation_email(self, registration_id: int):
        """
        Send a confirmation email to the parent.

        Args:
        - registration_id (int): The unique registration ID of the parent.

        Returns:
        - True if the email is sent successfully, False otherwise.
        """
        if registration_id not in self.parent_info:
            logging.error('Registration ID not found.')
            return False

        parent_email = self.parent_info[registration_id]['email']
        workshop_details = f"""
        Workshop Title: {self.workshop_title}
        Date: {self.workshop_date.strftime('%Y-%m-%d')}
        Time: {self.workshop_time}
        Location: {self.location}
        """
        try:
            # Simulate sending an email (replace with actual email sending code)
            logging.info(f'Email sent to {parent_email} with workshop details:\n{workshop_details}')
            return True
        except Exception as e:
            logging.error(f'Error sending email: {str(e)}')
            return False

    def get_workshop_details(self):
        """
        Get the workshop details.

        Returns:
        - A dictionary containing the workshop details.
        """
        return {
            'workshop_title': self.workshop_title,
            'workshop_date': self.workshop_date.strftime('%Y-%m-%d'),
            'workshop_time': self.workshop_time,
            'location': self.location
        }

def main():
    # Create a PreWorkshopModule instance
    pre_workshop_module = PreWorkshopModule(
        workshop_title='DBT Therapy for Adolescents',
        workshop_date='2024-09-20',
        workshop_time='10:00',
        location='Mente Sana Psicología'
    )

    # Register parents
    parent1_registration_id = pre_workshop_module.register_parent('John Doe', 'john.doe@example.com', '1234567890')
    parent2_registration_id = pre_workshop_module.register_parent('Jane Doe', 'jane.doe@example.com', '9876543210')

    # Send confirmation emails
    pre_workshop_module.send_confirmation_email(parent1_registration_id)
    pre_workshop_module.send_confirmation_email(parent2_registration_id)

    # Get workshop details
    workshop_details = pre_workshop_module.get_workshop_details()
    logging.info('Workshop Details:')
    for key, value in workshop_details.items():
        logging.info(f'{key.capitalize().replace("_", " ")}: {value}')

if __name__ == '__main__':
    main()
```
