"""
Generated Code Metadata:
========================
Original URL: https://sif.com.bo
Prompt: What are the different types of cobranzas services offered by SIF, and how do they differ from one another?
Generated: DETERMINISTIC_e32df48bfb7a98f7
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CobranzasService:
    """
    A class to represent different types of cobranzas services offered by SIF.
    """

    def __init__(self, service_name, description, fee_structure):
        """
        Initializes a new instance of CobranzasService.

        :param service_name: Name of the cobranzas service
        :param description: Description of the service
        :param fee_structure: Fee structure associated with the service
        """
        self.service_name = service_name
        self.description = description
        self.fee_structure = fee_structure

    def get_service_info(self):
        """
        Returns a summary of the service information.

        :return: A string containing service details
        """
        return f"Service: {self.service_name}\nDescription: {self.description}\nFee Structure: {self.fee_structure}"


class CobranzasServiceManager:
    """
    A class to manage multiple cobranzas services.
    """

    def __init__(self):
        """
        Initializes the service manager with an empty list of services.
        """
        self.services = []

    def add_service(self, service):
        """
        Adds a new cobranzas service to the manager.

        :param service: An instance of CobranzasService
        :raises ValueError: If the service is not an instance of CobranzasService
        """
        if not isinstance(service, CobranzasService):
            raise ValueError("service must be an instance of CobranzasService")
        self.services.append(service)

    def list_services(self):
        """
        Lists all cobranzas services managed by the manager.

        :return: A list of service information strings
        """
        return [service.get_service_info() for service in self.services]


def main():
    """
    Main function to demonstrate the usage of CobranzasService and CobranzasServiceManager.
    """
    try:
        # Create an instance of the service manager
        service_manager = CobranzasServiceManager()

        # Define different cobranzas services
        service1 = CobranzasService("Service A", "Description of Service A", "10% fee on collected amount")
        service2 = CobranzasService("Service B", "Description of Service B", "Flat fee of $100 per collection")
        service3 = CobranzasService("Service C", "Description of Service C", "15% fee on collected amount with a minimum of $50")

        # Add services to the manager
        service_manager.add_service(service1)
        service_manager.add_service(service2)
        service_manager.add_service(service3)

        # List all services
        for service_info in service_manager.list_services():
            print(service_info)
            print("-" * 40)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
