"""
Generated Code Metadata:
========================
Original URL: https://geeks-on-repair.com
Prompt: Develop a code snippet for a web application that lists available computer repair services and their prices, similar to the flat-fee pricing model used by Geeks on Repair.
Generated: DETERMINISTIC_b518d30058819729
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# computer_repair_services.py

from typing import Dict, List

class ComputerRepairService:
    def __init__(self, name: str, price: float, description: str):
        """
        Initialize a ComputerRepairService object.

        Args:
        - name (str): The name of the repair service.
        - price (float): The price of the repair service.
        - description (str): A brief description of the repair service.
        """
        self.name = name
        self.price = price
        self.description = description

class RepairServiceRepository:
    def __init__(self):
        """
        Initialize a RepairServiceRepository object.

        This repository stores and manages computer repair services.
        """
        self.services: Dict[str, ComputerRepairService] = {}

    def add_service(self, service: ComputerRepairService):
        """
        Add a computer repair service to the repository.

        Args:
        - service (ComputerRepairService): The service to add.
        """
        self.services[service.name] = service

    def get_services(self) -> List[ComputerRepairService]:
        """
        Get a list of all computer repair services in the repository.

        Returns:
        - List[ComputerRepairService]: A list of computer repair services.
        """
        return list(self.services.values())

    def get_service(self, name: str) -> ComputerRepairService:
        """
        Get a computer repair service by name.

        Args:
        - name (str): The name of the service to retrieve.

        Returns:
        - ComputerRepairService: The computer repair service, or None if not found.

        Raises:
        - ValueError: If the service name is empty.
        """
        if not name:
            raise ValueError("Service name cannot be empty")

        return self.services.get(name)

def main():
    # Create a repair service repository
    repository = RepairServiceRepository()

    # Add some repair services
    repository.add_service(ComputerRepairService("Virus Removal", 49.99, "Removal of viruses and malware from your computer"))
    repository.add_service(ComputerRepairService("Screen Replacement", 99.99, "Replacement of a cracked or broken screen"))
    repository.add_service(ComputerRepairService("Battery Replacement", 29.99, "Replacement of a laptop battery"))

    try:
        # Get and print all services
        services = repository.get_services()
        print("Available Computer Repair Services:")
        for i, service in enumerate(services, start=1):
            print(f"{i}. {service.name}: ${service.price:.2f} - {service.description}")

        # Get a specific service
        service_name = "Screen Replacement"
        service = repository.get_service(service_name)
        if service:
            print(f"\nService: {service.name}, Price: ${service.price:.2f}, Description: {service.description}")
        else:
            print(f"\nService '{service_name}' not found.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
