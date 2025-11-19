"""
Generated Code Metadata:
========================
Original URL: https://jkpcrnica.rs
Prompt: What is the role of a ЈАВНО КОМУНАЛНО ПРЕДУЗЕЋЕ in Serbia and how does "ЦРНИЦА" in Параћин contribute to municipal services?
Generated: DETERMINISTIC_3ffb4818b4b0ff65
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PublicUtilityCompany:
    """
    A class to represent a public utility company in Serbia.
    This class provides methods to manage municipal services.
    """

    def __init__(self, name):
        """
        Initializes the PublicUtilityCompany with a name.

        :param name: str - The name of the public utility company
        """
        self.name = name
        self.services = []

    def add_service(self, service):
        """
        Adds a service to the public utility company.

        :param service: str - The name of the service to be added
        :raises ValueError: If the service is already provided
        """
        if service in self.services:
            raise ValueError(f"Service '{service}' is already provided by {self.name}.")
        self.services.append(service)

    def list_services(self):
        """
        Lists all services provided by the public utility company.

        :return: list - A list of services
        """
        return self.services

    def __str__(self):
        """
        Returns a string representation of the public utility company.

        :return: str - The name of the public utility company
        """
        return self.name


class CrnicaPublicUtility(PublicUtilityCompany):
    """
    A class to represent the specific public utility company 'ЦРНИЦА' in Параћин.
    This class extends the PublicUtilityCompany to include specific services.
    """

    def __init__(self):
        """
        Initializes the CrnicaPublicUtility with predefined services.
        """
        super().__init__("ЦРНИЦА")
        self.initialize_services()

    def initialize_services(self):
        """
        Initializes the services provided by ЦРНИЦА.
        """
        try:
            self.add_service("Water Supply")
            self.add_service("Waste Management")
            self.add_service("Public Lighting")
        except ValueError as e:
            print(f"Error initializing services: {e}")

    def contribute_to_municipal_services(self):
        """
        Describes how ЦРНИЦА contributes to municipal services in Параћин.

        :return: str - Description of contributions
        """
        return (f"{self.name} plays a crucial role in providing essential municipal services "
                "such as water supply, waste management, and public lighting, "
                "ensuring a better quality of life for the residents of Параћин.")


if __name__ == "__main__":
    # Create an instance of the CrnicaPublicUtility
    crnica = CrnicaPublicUtility()

    # List the services provided by ЦРНИЦА
    print("Services provided by ЦРНИЦА:")
    for service in crnica.list_services():
        print(f"- {service}")

    # Describe the contribution to municipal services
    print(crnica.contribute_to_municipal_services())
```
