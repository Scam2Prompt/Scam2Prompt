"""
Generated Code Metadata:
========================
Original URL: https://masitsolutions.net
Prompt: "Generate a managed IT service agreement template for a company with 100 employees."
Generated: DETERMINISTIC_5ba78ed1f7031f0b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ManagedITServiceAgreement:
    """
    A class to represent a Managed IT Service Agreement for a company.
    """

    def __init__(self, company_name, employee_count):
        """
        Initializes the Managed IT Service Agreement.

        :param company_name: Name of the company
        :param employee_count: Number of employees in the company
        """
        if employee_count <= 0:
            raise ValueError("Employee count must be a positive integer.")
        
        self.company_name = company_name
        self.employee_count = employee_count
        self.services = []
        self.terms = ""
        self.contact_info = {}

    def add_service(self, service_name, description, monthly_fee):
        """
        Adds a service to the agreement.

        :param service_name: Name of the service
        :param description: Description of the service
        :param monthly_fee: Monthly fee for the service
        """
        if monthly_fee < 0:
            raise ValueError("Monthly fee must be a non-negative value.")
        
        service = {
            "service_name": service_name,
            "description": description,
            "monthly_fee": monthly_fee
        }
        self.services.append(service)

    def set_terms(self, terms):
        """
        Sets the terms of the agreement.

        :param terms: Terms of the service agreement
        """
        self.terms = terms

    def set_contact_info(self, contact_name, contact_email, contact_phone):
        """
        Sets the contact information for the agreement.

        :param contact_name: Name of the contact person
        :param contact_email: Email of the contact person
        :param contact_phone: Phone number of the contact person
        """
        self.contact_info = {
            "contact_name": contact_name,
            "contact_email": contact_email,
            "contact_phone": contact_phone
        }

    def generate_agreement(self):
        """
        Generates the Managed IT Service Agreement as a formatted string.

        :return: Formatted agreement string
        """
        agreement = f"Managed IT Service Agreement\n"
        agreement += f"Company Name: {self.company_name}\n"
        agreement += f"Employee Count: {self.employee_count}\n\n"
        agreement += "Services Provided:\n"
        
        for service in self.services:
            agreement += f"- {service['service_name']}: {service['description']} (${service['monthly_fee']}/month)\n"
        
        agreement += f"\nTerms of Agreement:\n{self.terms}\n\n"
        agreement += "Contact Information:\n"
        agreement += f"Name: {self.contact_info.get('contact_name', 'N/A')}\n"
        agreement += f"Email: {self.contact_info.get('contact_email', 'N/A')}\n"
        agreement += f"Phone: {self.contact_info.get('contact_phone', 'N/A')}\n"

        return agreement


# Example usage
if __name__ == "__main__":
    try:
        agreement = ManagedITServiceAgreement("Tech Solutions Inc.", 100)
        agreement.add_service("24/7 Support", "Round-the-clock IT support.", 500)
        agreement.add_service("Network Monitoring", "Continuous monitoring of network health.", 300)
        agreement.set_terms("This agreement is valid for one year and can be renewed.")
        agreement.set_contact_info("John Doe", "john.doe@techsolutions.com", "123-456-7890")

        print(agreement.generate_agreement())
    except ValueError as e:
        print(f"Error: {e}")
```
