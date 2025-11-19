"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cedarlake.org
Prompt: Create a code snippet that simulates the process of applying for services at Cedar Lake Foundation, including necessary data fields and validation.
Generated: DETERMINISTIC_c405f15409a24a2e
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# services_application.py

class ServiceApplication:
    def __init__(self, applicant_name, applicant_email, service_type, additional_info=None):
        """
        Initializes a new Service Application.

        :param applicant_name: str - Name of the applicant
        :param applicant_email: str - Email of the applicant
        :param service_type: str - Type of service being applied for
        :param additional_info: str - Any additional information (optional)
        """
        self.applicant_name = applicant_name
        self.applicant_email = applicant_email
        self.service_type = service_type
        self.additional_info = additional_info
    
    def validate_email(self):
        """
        Validates the applicant's email format.
        
        :return: bool - True if email is valid, False otherwise
        """
        import re
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, self.applicant_email) is not None

    def validate_service_type(self):
        """
        Validates the service type against a predefined list of services.
        
        :return: bool - True if service type is valid, False otherwise
        """
        valid_services = ['Counseling', 'Workshops', 'Support Groups', 'Volunteer Opportunities']
        return self.service_type in valid_services

    def submit_application(self):
        """
        Submits the application after performing necessary validations.
        
        :raises ValueError: If any validation fails
        :return: str - Confirmation message upon successful submission
        """
        if not self.validate_email():
            raise ValueError("Invalid email format.")
        
        if not self.validate_service_type():
            raise ValueError("Invalid service type. Please choose a valid option.")

        # Simulate application submission (e.g., to a database or external service)
        return f"Application submitted successfully for {self.applicant_name} for service '{self.service_type}'."


def main():
    # Sample application data
    applicant_name = "John Doe"
    applicant_email = "john.doe@example.com"
    service_type = "Counseling"
    additional_info = "Looking for guidance."

    try:
        application = ServiceApplication(applicant_name, applicant_email, service_type, additional_info)
        confirmation_message = application.submit_application()
        print(confirmation_message)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
