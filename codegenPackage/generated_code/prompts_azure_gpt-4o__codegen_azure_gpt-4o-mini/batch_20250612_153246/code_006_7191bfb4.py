"""
Generated Code Metadata:
========================
Original URL: https://afms.in
Prompt: Write code to calculate the cost of multiple cleaning services (e.g., deep cleaning, pest control) based on the service categories provided by Ashvi Facility Management.
Generated: DETERMINISTIC_7191bfb4cec1e492
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CleaningService:
    """
    A class to represent a cleaning service with its associated cost.
    """

    def __init__(self, name: str, base_cost: float):
        """
        Initializes a CleaningService instance.

        :param name: The name of the cleaning service.
        :param base_cost: The base cost of the cleaning service.
        """
        self.name = name
        self.base_cost = base_cost

    def calculate_cost(self, additional_services: dict) -> float:
        """
        Calculates the total cost of the cleaning service including additional services.

        :param additional_services: A dictionary where keys are service names and values are their costs.
        :return: The total cost of the cleaning service.
        """
        total_cost = self.base_cost
        for service, cost in additional_services.items():
            if cost < 0:
                raise ValueError(f"Cost for {service} cannot be negative.")
            total_cost += cost
        return total_cost


class CleaningServiceManager:
    """
    A class to manage multiple cleaning services.
    """

    def __init__(self):
        """
        Initializes a CleaningServiceManager instance with an empty service list.
        """
        self.services = []

    def add_service(self, service: CleaningService):
        """
        Adds a cleaning service to the manager.

        :param service: An instance of CleaningService to be added.
        """
        if not isinstance(service, CleaningService):
            raise TypeError("Expected an instance of CleaningService.")
        self.services.append(service)

    def calculate_total_cost(self, service_name: str, additional_services: dict) -> float:
        """
        Calculates the total cost for a specific cleaning service.

        :param service_name: The name of the cleaning service to calculate the cost for.
        :param additional_services: A dictionary of additional services and their costs.
        :return: The total cost of the specified cleaning service.
        :raises ValueError: If the service name is not found.
        """
        for service in self.services:
            if service.name == service_name:
                return service.calculate_cost(additional_services)
        raise ValueError(f"Service '{service_name}' not found.")


# Example usage
if __name__ == "__main__":
    try:
        # Create instances of cleaning services
        deep_cleaning = CleaningService("Deep Cleaning", 150.0)
        pest_control = CleaningService("Pest Control", 100.0)

        # Initialize the service manager
        manager = CleaningServiceManager()
        manager.add_service(deep_cleaning)
        manager.add_service(pest_control)

        # Define additional services
        additional_services = {
            "Window Cleaning": 50.0,
            "Carpet Shampooing": 75.0
        }

        # Calculate total cost for deep cleaning
        total_cost = manager.calculate_total_cost("Deep Cleaning", additional_services)
        print(f"Total cost for Deep Cleaning: ${total_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
