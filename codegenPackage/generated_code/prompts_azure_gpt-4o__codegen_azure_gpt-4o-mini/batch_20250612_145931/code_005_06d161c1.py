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
import json
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HostingService:
    """Class to represent a hosting service."""

    def __init__(self, name: str, status: str, ip_address: str):
        self.name = name
        self.status = status
        self.ip_address = ip_address

    def __repr__(self):
        return f"HostingService(name={self.name}, status={self.status}, ip_address={self.ip_address})"

class HostingManager:
    """Class to manage a collection of hosting services."""

    def __init__(self):
        self.services: List[HostingService] = []

    def add_service(self, service: HostingService) -> None:
        """Add a new hosting service to the manager."""
        self.services.append(service)
        logging.info(f"Added service: {service}")

    def remove_service(self, name: str) -> None:
        """Remove a hosting service by name."""
        original_count = len(self.services)
        self.services = [service for service in self.services if service.name != name]
        if len(self.services) < original_count:
            logging.info(f"Removed service: {name}")
        else:
            logging.warning(f"Service {name} not found for removal.")

    def update_service_status(self, name: str, status: str) -> None:
        """Update the status of a hosting service."""
        for service in self.services:
            if service.name == name:
                service.status = status
                logging.info(f"Updated service {name} status to {status}")
                return
        logging.warning(f"Service {name} not found for status update.")

    def list_services(self) -> List[Dict[str, Any]]:
        """List all hosting services."""
        return [service.__dict__ for service in self.services]

    def save_to_file(self, filename: str) -> None:
        """Save the current services to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_services(), file, indent=4)
            logging.info(f"Services saved to {filename}")
        except IOError as e:
            logging.error(f"Failed to save services to {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load services from a JSON file."""
        try:
            with open(filename, 'r') as file:
                services_data = json.load(file)
                self.services = [HostingService(**data) for data in services_data]
            logging.info(f"Services loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Failed to load services from {filename}: {e}")

def main():
    """Main function to demonstrate the HostingManager functionality."""
    manager = HostingManager()

    # Example usage
    manager.add_service(HostingService(name="Service1", status="active", ip_address="192.168.1.1"))
    manager.add_service(HostingService(name="Service2", status="inactive", ip_address="192.168.1.2"))

    print("Current services:")
    print(manager.list_services())

    manager.update_service_status("Service1", "inactive")
    manager.remove_service("Service2")

    print("Updated services:")
    print(manager.list_services())

    # Save to file
    manager.save_to_file("services.json")

    # Load from file
    manager.load_from_file("services.json")

if __name__ == "__main__":
    main()
```
