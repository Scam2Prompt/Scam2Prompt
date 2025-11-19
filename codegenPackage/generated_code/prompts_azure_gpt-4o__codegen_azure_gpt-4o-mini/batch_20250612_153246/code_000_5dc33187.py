"""
Generated Code Metadata:
========================
Original URL: https://afms.in
Prompt: Write Python code to automate scheduling of housekeeping services using the contact details and service categories provided by Ashvi Facility Management Services.
Generated: DETERMINISTIC_5dc3318707c3d2aa
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import smtplib
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from typing import List, Dict, Any

class HousekeepingScheduler:
    def __init__(self, service_data: str):
        """
        Initializes the HousekeepingScheduler with service data.

        :param service_data: JSON string containing service categories and contact details.
        """
        self.services = self.load_services(service_data)

    @staticmethod
    def load_services(service_data: str) -> List[Dict[str, Any]]:
        """
        Loads service data from a JSON string.

        :param service_data: JSON string containing service categories and contact details.
        :return: List of services as dictionaries.
        """
        try:
            return json.loads(service_data)
        except json.JSONDecodeError as e:
            raise ValueError("Invalid service data format") from e

    def schedule_service(self, service_name: str, contact_email: str, date: str) -> None:
        """
        Schedules a housekeeping service and sends a confirmation email.

        :param service_name: Name of the service to schedule.
        :param contact_email: Email address of the contact person.
        :param date: Date for the service in 'YYYY-MM-DD' format.
        """
        if not self.is_valid_email(contact_email):
            raise ValueError("Invalid email address provided")

        service = self.find_service(service_name)
        if not service:
            raise ValueError(f"Service '{service_name}' not found")

        service_date = self.parse_date(date)
        self.send_confirmation_email(contact_email, service_name, service_date)

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """
        Validates the email format.

        :param email: Email address to validate.
        :return: True if valid, False otherwise.
        """
        import re
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    @staticmethod
    def parse_date(date_str: str) -> datetime:
        """
        Parses a date string into a datetime object.

        :param date_str: Date string in 'YYYY-MM-DD' format.
        :return: Corresponding datetime object.
        """
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError("Invalid date format, should be 'YYYY-MM-DD'") from e

    @staticmethod
    def find_service(service_name: str) -> Dict[str, Any]:
        """
        Finds a service by name.

        :param service_name: Name of the service to find.
        :return: Service dictionary if found, None otherwise.
        """
        for service in self.services:
            if service['name'].lower() == service_name.lower():
                return service
        return None

    @staticmethod
    def send_confirmation_email(to_email: str, service_name: str, service_date: datetime) -> None:
        """
        Sends a confirmation email for the scheduled service.

        :param to_email: Recipient's email address.
        :param service_name: Name of the scheduled service.
        :param service_date: Date of the scheduled service.
        """
        subject = f"Housekeeping Service Scheduled: {service_name}"
        body = f"Your housekeeping service '{service_name}' has been scheduled for {service_date.strftime('%Y-%m-%d')}."
        
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = "no-reply@ashvifacilitymanagement.com"
        msg['To'] = to_email

        try:
            with smtplib.SMTP('smtp.example.com', 587) as server:
                server.starttls()
                server.login("your_email@example.com", "your_password")
                server.send_message(msg)
        except Exception as e:
            raise RuntimeError("Failed to send email") from e

# Example usage
if __name__ == "__main__":
    service_data = '''
    [
        {"name": "Basic Cleaning", "duration": "2 hours"},
        {"name": "Deep Cleaning", "duration": "4 hours"},
        {"name": "Window Cleaning", "duration": "1 hour"}
    ]
    '''
    
    scheduler = HousekeepingScheduler(service_data)
    try:
        scheduler.schedule_service("Basic Cleaning", "client@example.com", "2023-10-15")
        print("Service scheduled successfully.")
    except Exception as e:
        print(f"Error: {e}")
```
