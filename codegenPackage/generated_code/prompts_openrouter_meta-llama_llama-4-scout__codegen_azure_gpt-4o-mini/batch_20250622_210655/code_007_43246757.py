"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: "Generate a sample consulting services agreement that includes provisions for additional services beyond the initial scope of work."
Generated: DETERMINISTIC_432467573e51d4b6
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ConsultingServicesAgreement:
    """
    A class to represent a Consulting Services Agreement.

    Attributes:
        client_name (str): The name of the client.
        consultant_name (str): The name of the consultant.
        initial_scope (str): Description of the initial scope of work.
        additional_services (list): List of additional services beyond the initial scope.
        payment_terms (str): Payment terms for the services.
    """

    def __init__(self, client_name, consultant_name, initial_scope, payment_terms):
        """
        Initializes the ConsultingServicesAgreement with client and consultant details.

        Args:
            client_name (str): The name of the client.
            consultant_name (str): The name of the consultant.
            initial_scope (str): Description of the initial scope of work.
            payment_terms (str): Payment terms for the services.
        """
        self.client_name = client_name
        self.consultant_name = consultant_name
        self.initial_scope = initial_scope
        self.additional_services = []
        self.payment_terms = payment_terms

    def add_additional_service(self, service_description):
        """
        Adds an additional service to the agreement.

        Args:
            service_description (str): Description of the additional service.

        Raises:
            ValueError: If the service description is empty.
        """
        if not service_description:
            raise ValueError("Service description cannot be empty.")
        self.additional_services.append(service_description)

    def generate_agreement(self):
        """
        Generates the text of the consulting services agreement.

        Returns:
            str: The formatted consulting services agreement.
        """
        agreement = f"Consulting Services Agreement\n"
        agreement += f"Client: {self.client_name}\n"
        agreement += f"Consultant: {self.consultant_name}\n\n"
        agreement += f"Initial Scope of Work:\n{self.initial_scope}\n\n"
        agreement += f"Additional Services:\n"
        if self.additional_services:
            for service in self.additional_services:
                agreement += f"- {service}\n"
        else:
            agreement += "None\n"
        agreement += f"\nPayment Terms:\n{self.payment_terms}\n"
        return agreement


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the ConsultingServicesAgreement
        agreement = ConsultingServicesAgreement(
            client_name="ABC Corp",
            consultant_name="John Doe Consulting",
            initial_scope="Provide marketing strategy consultation for Q1 2024.",
            payment_terms="Payment due within 30 days of invoice."
        )

        # Add additional services
        agreement.add_additional_service("Social media management for Q2 2024.")
        agreement.add_additional_service("Website redesign consultation.")

        # Generate and print the agreement
        print(agreement.generate_agreement())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
