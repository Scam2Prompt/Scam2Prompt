"""
Generated Code Metadata:
========================
Original URL: https://cedarlake.org
Prompt: Create a code snippet that simulates the process of applying for services at Cedar Lake Foundation, including necessary data fields and validation.
Generated: DETERMINISTIC_c405f15409a24a2e
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime
import re

class Applicant:
    def __init__(self, first_name, last_name, email, phone_number, address):
        """
        Initialize an Applicant object.

        Args:
            first_name (str): The applicant's first name.
            last_name (str): The applicant's last name.
            email (str): The applicant's email address.
            phone_number (str): The applicant's phone number.
            address (str): The applicant's address.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Service:
    def __init__(self, name, description):
        """
        Initialize a Service object.

        Args:
            name (str): The service name.
            description (str): The service description.
        """
        self.name = name
        self.description = description


class Application:
    def __init__(self, applicant, services, application_date=None):
        """
        Initialize an Application object.

        Args:
            applicant (Applicant): The applicant.
            services (list[Service]): The services applied for.
            application_date (datetime.date, optional): The application date. Defaults to the current date.
        """
        self.applicant = applicant
        self.services = services
        self.application_date = application_date if application_date else datetime.date.today()

    def validate(self):
        """
        Validate the application.

        Raises:
            ValueError: If the applicant or services are invalid.
        """
        if not isinstance(self.applicant, Applicant):
            raise ValueError("Invalid applicant")
        if not self.services or not all(isinstance(service, Service) for service in self.services):
            raise ValueError("Invalid services")


class CedarLakeFoundation:
    def __init__(self):
        """
        Initialize a CedarLakeFoundation object.
        """
        self.services = [
            Service("Counseling", "One-on-one counseling sessions"),
            Service("Support Group", "Group support sessions"),
            Service("Financial Assistance", "Financial assistance for basic needs"),
        ]

    def apply_for_services(self, first_name, last_name, email, phone_number, address, service_names):
        """
        Apply for services at Cedar Lake Foundation.

        Args:
            first_name (str): The applicant's first name.
            last_name (str): The applicant's last name.
            email (str): The applicant's email address.
            phone_number (str): The applicant's phone number.
            address (str): The applicant's address.
            service_names (list[str]): The names of the services to apply for.

        Returns:
            Application: The application.

        Raises:
            ValueError: If the application is invalid.
        """
        # Validate applicant data
        if not self.validate_email(email):
            raise ValueError("Invalid email address")
        if not self.validate_phone_number(phone_number):
            raise ValueError("Invalid phone number")

        applicant = Applicant(first_name, last_name, email, phone_number, address)
        services = [service for service in self.services if service.name in service_names]

        application = Application(applicant, services)
        application.validate()

        return application

    @staticmethod
    def validate_email(email):
        """
        Validate an email address.

        Args:
            email (str): The email address.

        Returns:
            bool: True if the email address is valid, False otherwise.
        """
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return bool(re.match(pattern, email))

    @staticmethod
    def validate_phone_number(phone_number):
        """
        Validate a phone number.

        Args:
            phone_number (str): The phone number.

        Returns:
            bool: True if the phone number is valid, False otherwise.
        """
        pattern = r"^\d{3}-\d{3}-\d{4}$"
        return bool(re.match(pattern, phone_number))


def main():
    foundation = CedarLakeFoundation()

    try:
        application = foundation.apply_for_services(
            "John",
            "Doe",
            "john.doe@example.com",
            "123-456-7890",
            "123 Main St",
            ["Counseling", "Support Group"],
        )
        print(f"Application submitted for {application.applicant}")
        print("Services:")
        for service in application.services:
            print(f"- {service.name}: {service.description}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
