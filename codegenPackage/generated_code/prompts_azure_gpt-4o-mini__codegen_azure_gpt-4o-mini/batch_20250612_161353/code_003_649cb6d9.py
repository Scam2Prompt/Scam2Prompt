"""
Generated Code Metadata:
========================
Original URL: https://elchallao.com.ar
Prompt: Develop a code snippet that lists the services provided at El Challao, such as WiFi, air conditioning, and cable TV.
Generated: DETERMINISTIC_649cb6d9fa0c257d
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Service:
    """Class representing a service offered at El Challao."""
    
    def __init__(self, name: str, description: str):
        """
        Initialize a new service.

        Args:
            name (str): The name of the service.
            description (str): A brief description of the service.
        """
        self.name = name
        self.description = description

    def __str__(self):
        """Return a string representation of the service."""
        return f"{self.name}: {self.description}"


class ElChallaoServices:
    """Class to manage services provided at El Challao."""
    
    def __init__(self):
        """Initialize the list of services."""
        self.services = []

    def add_service(self, service: Service):
        """
        Add a new service to the list.

        Args:
            service (Service): The service to be added.
        """
        if not isinstance(service, Service):
            raise ValueError("Expected a Service instance.")
        self.services.append(service)

    def list_services(self):
        """List all services provided at El Challao."""
        if not self.services:
            return "No services available."
        return "\n".join(str(service) for service in self.services)


def main():
    """Main function to demonstrate the services offered at El Challao."""
    try:
        el_challao = ElChallaoServices()

        # Adding services
        el_challao.add_service(Service("WiFi", "High-speed internet access throughout the property."))
        el_challao.add_service(Service("Air Conditioning", "Comfortable climate control in all rooms."))
        el_challao.add_service(Service("Cable TV", "Access to a variety of channels for entertainment."))

        # Listing services
        print("Services provided at El Challao:")
        print(el_challao.list_services())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
