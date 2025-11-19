"""
Generated Code Metadata:
========================
Original URL: https://www.otment.com
Prompt: What are the core services offered by OTM Entertainment LLC?
Generated: DETERMINISTIC_02ab80ae63ce9db8
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class OTMEntertainment:
    """
    A class to represent the core services offered by OTM Entertainment LLC.
    """

    def __init__(self):
        """
        Initializes the OTMEntertainment class with a list of services.
        """
        self.services = [
            "Film Production",
            "Television Production",
            "Music Production",
            "Event Management",
            "Talent Management",
            "Content Creation",
            "Marketing and Promotion",
            "Distribution Services"
        ]

    def get_services(self):
        """
        Returns the list of core services offered by OTM Entertainment LLC.

        Returns:
            list: A list of services.
        """
        return self.services

    def add_service(self, service):
        """
        Adds a new service to the list of core services.

        Args:
            service (str): The name of the service to be added.

        Raises:
            ValueError: If the service is already in the list or is empty.
        """
        if not service or service in self.services:
            raise ValueError("Service must be a non-empty string and not already exist.")
        self.services.append(service)

    def remove_service(self, service):
        """
        Removes a service from the list of core services.

        Args:
            service (str): The name of the service to be removed.

        Raises:
            ValueError: If the service is not found in the list.
        """
        if service not in self.services:
            raise ValueError("Service not found in the list.")
        self.services.remove(service)

# Example usage
if __name__ == "__main__":
    try:
        otm = OTMEntertainment()
        print("Core Services Offered by OTM Entertainment LLC:")
        print(otm.get_services())

        # Adding a new service
        otm.add_service("Virtual Reality Experiences")
        print("\nUpdated Services List:")
        print(otm.get_services())

        # Removing a service
        otm.remove_service("Event Management")
        print("\nServices List After Removal:")
        print(otm.get_services())

    except ValueError as e:
        print(f"Error: {e}")
```
