"""
Generated Code Metadata:
========================
Original URL: https://www.haim-lawyer.co.il
Prompt: What services does the law firm of Haim Shokrani offer in the areas of civil and commercial law?
Generated: DETERMINISTIC_8e128c315596301f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define a class for LawFirm to encapsulate its services
class LawFirm:
    def __init__(self, name):
        """
        Initialize a LawFirm object.

        Args:
            name (str): The name of the law firm.
        """
        self.name = name
        self.services = {}

    def add_service(self, area_of_law, service):
        """
        Add a service offered by the law firm.

        Args:
            area_of_law (str): The area of law (e.g., civil, commercial).
            service (str): The service offered.
        """
        if area_of_law not in self.services:
            self.services[area_of_law] = []
        self.services[area_of_law].append(service)

    def get_services(self, area_of_law=None):
        """
        Get services offered by the law firm.

        Args:
            area_of_law (str, optional): The area of law. Defaults to None.

        Returns:
            dict or list: Services offered in the specified area of law or all services if no area is specified.
        """
        if area_of_law:
            return self.services.get(area_of_law, [])
        return self.services


def main():
    try:
        # Create a LawFirm object for Haim Shokrani
        haim_shokrani_law_firm = LawFirm("Haim Shokrani")

        # Add services offered in civil and commercial law
        haim_shokrani_law_firm.add_service("civil", "Contract Disputes")
        haim_shokrani_law_firm.add_service("civil", "Personal Injury")
        haim_shokrani_law_firm.add_service("commercial", "Business Litigation")
        haim_shokrani_law_firm.add_service("commercial", "Intellectual Property")

        # Get services offered in civil and commercial law
        civil_services = haim_shokrani_law_firm.get_services("civil")
        commercial_services = haim_shokrani_law_firm.get_services("commercial")

        # Print services offered
        print(f"Services offered by {haim_shokrani_law_firm.name} in Civil Law:")
        for service in civil_services:
            print(f"- {service}")

        print(f"\nServices offered by {haim_shokrani_law_firm.name} in Commercial Law:")
        for service in commercial_services:
            print(f"- {service}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
