"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cart3.pages.dev
Prompt: Suggest tools or libraries for implementing fixed-price legal and accounting service models, ensuring transparency and avoiding billable minutes, as practiced by Carthew Chau & Co.
Generated: DETERMINISTIC_6d1375484d161dea
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Legal and Accounting Services Management System
# This system implements a fixed-price service model ensuring transparency 
# and avoiding billable minutes for legal and accounting services.

class Service:
    """
    Represents a fixed-price service offered by the firm.
    """

    def __init__(self, name: str, price: float):
        """
        Initializes a new service with a name and price.

        :param name: Name of the service.
        :param price: Fixed price of the service.
        """
        if price < 0:
            raise ValueError("Price must be a non-negative value.")
        
        self.name = name
        self.price = price

    def __str__(self):
        """Returns a string representation of the service."""
        return f"Service(name={self.name}, price={self.price:.2f})"


class Client:
    """
    Represents a client who utilizes the services.
    """

    def __init__(self, name: str):
        """
        Initializes a new client with a name.

        :param name: Name of the client.
        """
        self.name = name
        self.services_used = []

    def add_service(self, service: Service):
        """
        Adds a service to the client's list of used services.

        :param service: An instance of Service.
        """
        self.services_used.append(service)

    def total_cost(self) -> float:
        """
        Calculates the total cost of services used by the client.

        :return: Total cost as a float.
        """
        return sum(service.price for service in self.services_used)

    def __str__(self):
        """Returns a string representation of the client and their services."""
        services = ', '.join(str(service) for service in self.services_used)
        return f"Client(name={self.name}, services_used=[{services}])"


class ServiceManager:
    """
    Manages the available services and client interactions.
    """

    def __init__(self):
        """Initializes the ServiceManager with an empty service list."""
        self.services = {}

    def add_service(self, name: str, price: float):
        """
        Adds a new fixed-price service.

        :param name: Name of the service to add.
        :param price: Fixed price of the service.
        """
        service = Service(name, price)
        self.services[name] = service

    def get_service(self, name: str) -> Service:
        """
        Retrieves a service by name.

        :param name: Name of the service to retrieve.
        :return: An instance of Service.
        :raises KeyError: If the service does not exist.
        """
        try:
            return self.services[name]
        except KeyError as e:
            raise KeyError(f"Service '{name}' not found.") from e

    def __str__(self):
        """Returns a string representation of all services."""
        return '\n'.join(str(service) for service in self.services.values())


# Example usage with error handling
if __name__ == "__main__":
    try:
        # Create a service manager
        service_manager = ServiceManager()
        
        # Add services
        service_manager.add_service("Consultation", 200.00)
        service_manager.add_service("Document Preparation", 150.00)

        # Create a new client
        client = Client("John Doe")

        # Add services to the client
        client.add_service(service_manager.get_service("Consultation"))
        client.add_service(service_manager.get_service("Document Preparation"))

        # Print client's total cost
        print(f"Total cost for {client.name}: ${client.total_cost():.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
