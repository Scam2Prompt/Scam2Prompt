"""
Generated Code Metadata:
========================
Original URL: https://aliahtirafia.com
Prompt: Write a Python script to manage a company's services, including installation, moving, and storage, with different pricing for various services like نقل عفش بالدمام and تركيب مطابخ بالخبر.
Generated: DETERMINISTIC_fbed791727f5578a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# services.py

class Service:
    """Base class for all services."""

    def __init__(self, name, price):
        """
        Initialize a service.

        Args:
            name (str): Service name.
            price (float): Service price.
        """
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price}"


class InstallationService(Service):
    """Installation service."""

    def __init__(self, name, price, installation_type):
        """
        Initialize an installation service.

        Args:
            name (str): Service name.
            price (float): Service price.
            installation_type (str): Type of installation (e.g., مطابخ).
        """
        super().__init__(name, price)
        self.installation_type = installation_type

    def __str__(self):
        return f"{self.name} ({self.installation_type}): {self.price}"


class MovingService(Service):
    """Moving service."""

    def __init__(self, name, price, moving_type, location):
        """
        Initialize a moving service.

        Args:
            name (str): Service name.
            price (float): Service price.
            moving_type (str): Type of moving (e.g., نقل عفش).
            location (str): Moving location (e.g., الدمام).
        """
        super().__init__(name, price)
        self.moving_type = moving_type
        self.location = location

    def __str__(self):
        return f"{self.name} ({self.moving_type} {self.location}): {self.price}"


class StorageService(Service):
    """Storage service."""

    def __init__(self, name, price, storage_type):
        """
        Initialize a storage service.

        Args:
            name (str): Service name.
            price (float): Service price.
            storage_type (str): Type of storage.
        """
        super().__init__(name, price)
        self.storage_type = storage_type

    def __str__(self):
        return f"{self.name} ({self.storage_type}): {self.price}"


class Company:
    """Company class."""

    def __init__(self):
        self.services = []

    def add_service(self, service):
        """
        Add a service to the company.

        Args:
            service (Service): Service to add.
        """
        self.services.append(service)

    def remove_service(self, service_name):
        """
        Remove a service from the company.

        Args:
            service_name (str): Name of the service to remove.

        Raises:
            ValueError: If the service is not found.
        """
        for service in self.services:
            if service.name == service_name:
                self.services.remove(service)
                return
        raise ValueError("Service not found")

    def list_services(self):
        """List all services."""
        for service in self.services:
            print(service)


def main():
    try:
        company = Company()

        # Create services
        installation_service = InstallationService("تركيب مطابخ", 1000.0, "مطابخ")
        moving_service = MovingService("نقل عفش", 500.0, "نقل عفش", "الدمام")
        storage_service = StorageService("تخزين", 200.0, "تخزين عفش")

        # Add services to company
        company.add_service(installation_service)
        company.add_service(moving_service)
        company.add_service(storage_service)

        # List services
        print("Services:")
        company.list_services()

        # Remove service
        company.remove_service("نقل عفش")

        # List services after removal
        print("\nServices after removal:")
        company.list_services()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
