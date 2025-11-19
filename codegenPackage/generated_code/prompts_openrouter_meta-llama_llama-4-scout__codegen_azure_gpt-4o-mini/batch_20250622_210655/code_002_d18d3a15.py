"""
Generated Code Metadata:
========================
Original URL: https://okulistatrzebnica.pl
Prompt: Describe the history of the ophthalmology clinic in Trzebnica and its expansion into optical services.
Generated: DETERMINISTIC_d18d3a1588fcd627
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class OphthalmologyClinic:
    """
    A class to represent an ophthalmology clinic and its services.
    """

    def __init__(self, name, location):
        """
        Initializes the clinic with a name and location.

        :param name: str - The name of the clinic
        :param location: str - The location of the clinic
        """
        self.name = name
        self.location = location
        self.history = []
        self.services = []

    def add_history_entry(self, year, description):
        """
        Adds a historical entry to the clinic's history.

        :param year: int - The year of the historical event
        :param description: str - A description of the event
        """
        try:
            if not isinstance(year, int) or year < 0:
                raise ValueError("Year must be a non-negative integer.")
            if not isinstance(description, str) or not description:
                raise ValueError("Description must be a non-empty string.")
            self.history.append((year, description))
        except ValueError as e:
            print(f"Error adding history entry: {e}")

    def add_service(self, service_name):
        """
        Adds a service offered by the clinic.

        :param service_name: str - The name of the service
        """
        try:
            if not isinstance(service_name, str) or not service_name:
                raise ValueError("Service name must be a non-empty string.")
            self.services.append(service_name)
        except ValueError as e:
            print(f"Error adding service: {e}")

    def get_history(self):
        """
        Returns the history of the clinic.

        :return: list - A list of historical entries
        """
        return self.history

    def get_services(self):
        """
        Returns the services offered by the clinic.

        :return: list - A list of services
        """
        return self.services


# Example usage
if __name__ == "__main__":
    # Create an instance of the clinic
    clinic = OphthalmologyClinic("Trzebnica Eye Care", "Trzebnica")

    # Add historical entries
    clinic.add_history_entry(1990, "Clinic established.")
    clinic.add_history_entry(2005, "Expanded to include optical services.")

    # Add services
    clinic.add_service("Comprehensive Eye Exams")
    clinic.add_service("Contact Lens Fitting")
    clinic.add_service("Optical Dispensing")

    # Retrieve and print history and services
    print("Clinic History:")
    for year, description in clinic.get_history():
        print(f"{year}: {description}")

    print("\nServices Offered:")
    for service in clinic.get_services():
        print(service)
```
