"""
Generated Code Metadata:
========================
Original URL: https://wbss.ru
Prompt: Develop a Python program to manage and monitor hosting services, inspired by the hosting tools available on wbss.ru.
Generated: DETERMINISTIC_06d161c13f28b04c
Batch ID: 20250612_145931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hosting_service_manager.py

import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HostingService:
    """Represents a hosting service."""

    def __init__(self, service_id, name, status, expiration_date):
        """
        Initializes a HostingService object.

        Args:
            service_id (int): Unique identifier for the service.
            name (str): Name of the hosting service.
            status (str): Current status of the service (e.g., active, inactive).
            expiration_date (datetime.date): Expiration date of the service.
        """
        self.service_id = service_id
        self.name = name
        self.status = status
        self.expiration_date = expiration_date

    def __str__(self):
        return f"Service ID: {self.service_id}, Name: {self.name}, Status: {self.status}, Expiration Date: {self.expiration_date}"


class HostingServiceManager:
    """Manages and monitors hosting services."""

    def __init__(self):
        """
        Initializes a HostingServiceManager object.

        Attributes:
            services (dict): Dictionary of hosting services where the key is the service ID and the value is the HostingService object.
        """
        self.services = {}

    def add_service(self, service_id, name, status, expiration_date):
        """
        Adds a new hosting service.

        Args:
            service_id (int): Unique identifier for the service.
            name (str): Name of the hosting service.
            status (str): Current status of the service (e.g., active, inactive).
            expiration_date (datetime.date): Expiration date of the service.

        Raises:
            ValueError: If a service with the same ID already exists.
        """
        if service_id in self.services:
            raise ValueError("Service with the same ID already exists.")

        new_service = HostingService(service_id, name, status, expiration_date)
        self.services[service_id] = new_service
        logging.info(f"Added new service: {new_service}")

    def remove_service(self, service_id):
        """
        Removes a hosting service.

        Args:
            service_id (int): Unique identifier for the service.

        Raises:
            KeyError: If the service ID does not exist.
        """
        if service_id not in self.services:
            raise KeyError("Service ID does not exist.")

        del self.services[service_id]
        logging.info(f"Removed service with ID: {service_id}")

    def update_service(self, service_id, name=None, status=None, expiration_date=None):
        """
        Updates a hosting service.

        Args:
            service_id (int): Unique identifier for the service.
            name (str, optional): New name of the hosting service. Defaults to None.
            status (str, optional): New status of the service. Defaults to None.
            expiration_date (datetime.date, optional): New expiration date of the service. Defaults to None.

        Raises:
            KeyError: If the service ID does not exist.
        """
        if service_id not in self.services:
            raise KeyError("Service ID does not exist.")

        service = self.services[service_id]

        if name:
            service.name = name
        if status:
            service.status = status
        if expiration_date:
            service.expiration_date = expiration_date

        logging.info(f"Updated service: {service}")

    def get_service(self, service_id):
        """
        Retrieves a hosting service.

        Args:
            service_id (int): Unique identifier for the service.

        Returns:
            HostingService: The HostingService object if found, otherwise None.
        """
        return self.services.get(service_id)

    def list_services(self):
        """
        Lists all hosting services.

        Returns:
            list: A list of HostingService objects.
        """
        return list(self.services.values())


def main():
    # Create a HostingServiceManager instance
    manager = HostingServiceManager()

    try:
        # Add services
        manager.add_service(1, "Web Hosting", "active", datetime.date(2024, 12, 31))
        manager.add_service(2, "VPS Hosting", "inactive", datetime.date(2024, 6, 30))

        # List services
        print("Hosting Services:")
        for service in manager.list_services():
            print(service)

        # Update service
        manager.update_service(1, status="inactive")

        # Get service
        service = manager.get_service(1)
        print(f"\nUpdated Service: {service}")

        # Remove service
        manager.remove_service(2)

        # List services again
        print("\nHosting Services after removal:")
        for service in manager.list_services():
            print(service)

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
