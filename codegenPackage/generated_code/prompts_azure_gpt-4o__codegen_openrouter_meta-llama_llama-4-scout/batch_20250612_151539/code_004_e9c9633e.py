"""
Generated Code Metadata:
========================
Original URL: https://ksa4-gen-ai.appcino-tech.com
Prompt: Write a function to display and filter hospitality services, such as tourist accommodation facilities, using the data structure described on the webpage.
Generated: DETERMINISTIC_e9c9633e737b88f8
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hospitality_services.py

class HospitalityService:
    """Represents a hospitality service."""

    def __init__(self, id: int, name: str, accommodation_type: str, rating: float, price: float):
        """
        Initializes a HospitalityService.

        Args:
            id (int): Unique identifier for the service.
            name (str): Name of the service.
            accommodation_type (str): Type of accommodation (e.g., hotel, hostel, apartment).
            rating (float): Rating of the service (out of 5).
            price (float): Price per night.
        """
        self.id = id
        self.name = name
        self.accommodation_type = accommodation_type
        self.rating = rating
        self.price = price

    def __repr__(self):
        return f"HospitalityService(id={self.id}, name='{self.name}', accommodation_type='{self.accommodation_type}', rating={self.rating}, price={self.price})"


class HospitalityServiceFilter:
    """Filters hospitality services based on various criteria."""

    def __init__(self, services: list[HospitalityService]):
        """
        Initializes a HospitalityServiceFilter.

        Args:
            services (list[HospitalityService]): List of hospitality services.
        """
        self.services = services

    def filter_by_accommodation_type(self, accommodation_type: str) -> list[HospitalityService]:
        """
        Filters services by accommodation type.

        Args:
            accommodation_type (str): Type of accommodation to filter by.

        Returns:
            list[HospitalityService]: Filtered list of services.
        """
        return [s for s in self.services if s.accommodation_type.lower() == accommodation_type.lower()]

    def filter_by_rating(self, min_rating: float) -> list[HospitalityService]:
        """
        Filters services by minimum rating.

        Args:
            min_rating (float): Minimum rating to filter by.

        Returns:
            list[HospitalityService]: Filtered list of services.
        """
        if min_rating < 0 or min_rating > 5:
            raise ValueError("Rating must be between 0 and 5")

        return [s for s in self.services if s.rating >= min_rating]

    def filter_by_price(self, max_price: float) -> list[HospitalityService]:
        """
        Filters services by maximum price.

        Args:
            max_price (float): Maximum price to filter by.

        Returns:
            list[HospitalityService]: Filtered list of services.
        """
        if max_price < 0:
            raise ValueError("Price must be non-negative")

        return [s for s in self.services if s.price <= max_price]

    def display_services(self, services: list[HospitalityService]) -> None:
        """
        Displays a list of hospitality services.

        Args:
            services (list[HospitalityService]): List of services to display.
        """
        for service in services:
            print(f"ID: {service.id}")
            print(f"Name: {service.name}")
            print(f"Accommodation Type: {service.accommodation_type}")
            print(f"Rating: {service.rating}/5")
            print(f"Price: ${service.price:.2f}/night")
            print("------------------------")


def main() -> None:
    # Example usage
    services = [
        HospitalityService(1, "Hotel A", "Hotel", 4.5, 200.0),
        HospitalityService(2, "Hostel B", "Hostel", 3.8, 50.0),
        HospitalityService(3, "Apartment C", "Apartment", 4.8, 150.0),
        HospitalityService(4, "Hotel D", "Hotel", 4.2, 250.0),
    ]

    filter = HospitalityServiceFilter(services)

    print("All Services:")
    filter.display_services(services)

    print("\nFiltered by Hotel:")
    hotel_services = filter.filter_by_accommodation_type("Hotel")
    filter.display_services(hotel_services)

    print("\nFiltered by Rating >= 4.5:")
    high_rating_services = filter.filter_by_rating(4.5)
    filter.display_services(high_rating_services)

    print("\nFiltered by Price <= $150:")
    affordable_services = filter.filter_by_price(150.0)
    filter.display_services(affordable_services)


if __name__ == "__main__":
    main()
```
