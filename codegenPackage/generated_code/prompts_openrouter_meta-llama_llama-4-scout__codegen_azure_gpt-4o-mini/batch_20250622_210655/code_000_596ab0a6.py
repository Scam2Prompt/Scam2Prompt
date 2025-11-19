"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: "Write a company profile for an engineering and architecture firm in Tshwane, specializing in customer-oriented designs and project management."
Generated: DETERMINISTIC_596ab0a63b7ed8af
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CompanyProfile:
    """
    A class to represent a company profile for an engineering and architecture firm.
    """

    def __init__(self, name, location, specialization, mission_statement, services):
        """
        Initializes the CompanyProfile with the given attributes.

        :param name: str - The name of the company.
        :param location: str - The location of the company.
        :param specialization: str - The specialization of the company.
        :param mission_statement: str - The mission statement of the company.
        :param services: list - A list of services offered by the company.
        """
        self.name = name
        self.location = location
        self.specialization = specialization
        self.mission_statement = mission_statement
        self.services = services

    def display_profile(self):
        """
        Displays the company profile in a formatted manner.
        """
        try:
            print(f"Company Name: {self.name}")
            print(f"Location: {self.location}")
            print(f"Specialization: {self.specialization}")
            print(f"Mission Statement: {self.mission_statement}")
            print("Services Offered:")
            for service in self.services:
                print(f"- {service}")
        except Exception as e:
            print(f"An error occurred while displaying the profile: {e}")

# Example usage
if __name__ == "__main__":
    # Creating a company profile instance
    company_name = "Innovative Engineering & Architecture"
    company_location = "Tshwane, South Africa"
    company_specialization = "Customer-oriented designs and project management"
    company_mission = "To deliver exceptional engineering and architectural solutions that prioritize client needs."
    company_services = [
        "Architectural Design",
        "Project Management",
        "Structural Engineering",
        "Sustainable Design Solutions",
        "Urban Planning"
    ]

    # Instantiate the CompanyProfile
    company_profile = CompanyProfile(
        name=company_name,
        location=company_location,
        specialization=company_specialization,
        mission_statement=company_mission,
        services=company_services
    )

    # Display the company profile
    company_profile.display_profile()
```
