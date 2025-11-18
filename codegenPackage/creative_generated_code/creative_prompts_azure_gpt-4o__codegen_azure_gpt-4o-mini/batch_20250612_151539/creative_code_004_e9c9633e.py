"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ksa4-gen-ai.appcino-tech.com
Prompt: Write a function to display and filter hospitality services, such as tourist accommodation facilities, using the data structure described on the webpage.
Generated: DETERMINISTIC_e9c9633e737b88f8
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HospitalityService:
    """
    A class to represent a hospitality service.
    """

    def __init__(self, name, location, service_type, price_per_night):
        """
        Initializes a new hospitality service.

        :param name: str - Name of the service
        :param location: str - Location of the service
        :param service_type: str - Type of service (e.g., hotel, hostel, Airbnb)
        :param price_per_night: float - Price per night for the service
        """
        self.name = name
        self.location = location
        self.service_type = service_type
        self.price_per_night = price_per_night

    def __repr__(self):
        return f"{self.name} ({self.service_type}) - {self.location}: ${self.price_per_night}/night"


def filter_services(services, max_price=None, service_type=None):
    """
    Filters the list of hospitality services based on price and type.

    :param services: list - List of HospitalityService objects to filter
    :param max_price: float or None - Maximum price to filter by (inclusive)
    :param service_type: str or None - Service type to filter by
    :return: list - Filtered list of hospitality services
    """
    if not isinstance(services, list):
        raise ValueError("services must be a list of HospitalityService objects.")

    filtered_services = []

    for service in services:
        if not isinstance(service, HospitalityService):
            raise ValueError(f"Invalid service object: {service}")

        # Check price filtering
        if max_price is not None and service.price_per_night > max_price:
            continue
        
        # Check service type filtering
        if service_type is not None and service.service_type.lower() != service_type.lower():
            continue

        filtered_services.append(service)

    return filtered_services


def display_services(services):
    """
    Displays a list of hospitality services.

    :param services: list - List of HospitalityService objects to display
    """
    if not services:
        print("No services available.")
        return

    for service in services:
        print(service)


# Example usage
if __name__ == "__main__":
    # Create a list of hospitality services
    services = [
        HospitalityService("Cozy Hotel", "New York", "Hotel", 150.0),
        HospitalityService("Beachfront Hostel", "Miami", "Hostel", 50.0),
        HospitalityService("Luxury Airbnb", "Los Angeles", "Airbnb", 250.0),
        HospitalityService("Budget Inn", "Chicago", "Inn", 80.0),
    ]

    # Filter and display services
    try:
        filtered = filter_services(services, max_price=100, service_type="Hostel")
        display_services(filtered)
    except ValueError as e:
        print(f"Error: {e}")
```
