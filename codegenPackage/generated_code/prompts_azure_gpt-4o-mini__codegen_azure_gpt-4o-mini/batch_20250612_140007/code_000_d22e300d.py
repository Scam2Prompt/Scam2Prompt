"""
Generated Code Metadata:
========================
Original URL: https://celestia.agency
Prompt: What are the key features of the Celestia agency's services related to web development?
Generated: DETERMINISTIC_d22e300db568475a
Batch ID: 20250612_140007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CelestiaAgency:
    """
    A class to represent the Celestia agency's web development services.
    """

    def __init__(self):
        """
        Initializes the CelestiaAgency with a list of services.
        """
        self.services = [
            "Custom Web Development",
            "Responsive Design",
            "E-commerce Solutions",
            "Content Management Systems (CMS)",
            "Search Engine Optimization (SEO)",
            "Web Application Development",
            "API Development and Integration",
            "Website Maintenance and Support",
            "User Experience (UX) Design",
            "Performance Optimization"
        ]

    def get_services(self):
        """
        Returns a list of web development services offered by the agency.

        Returns:
            list: A list of services.
        """
        return self.services

    def add_service(self, service):
        """
        Adds a new service to the list of services.

        Args:
            service (str): The name of the service to add.

        Raises:
            ValueError: If the service is already in the list.
        """
        if service in self.services:
            raise ValueError(f"Service '{service}' already exists.")
        self.services.append(service)

    def remove_service(self, service):
        """
        Removes a service from the list of services.

        Args:
            service (str): The name of the service to remove.

        Raises:
            ValueError: If the service is not found in the list.
        """
        try:
            self.services.remove(service)
        except ValueError:
            raise ValueError(f"Service '{service}' not found in the list.")

    def display_services(self):
        """
        Displays the list of services in a formatted manner.
        """
        print("Celestia Agency Web Development Services:")
        for idx, service in enumerate(self.services, start=1):
            print(f"{idx}. {service}")

# Example usage
if __name__ == "__main__":
    agency = CelestiaAgency()
    agency.display_services()

    # Adding a new service
    try:
        agency.add_service("Mobile App Development")
    except ValueError as e:
        print(e)

    # Display updated services
    agency.display_services()

    # Removing a service
    try:
        agency.remove_service("SEO")
    except ValueError as e:
        print(e)

    # Display final services
    agency.display_services()
```
