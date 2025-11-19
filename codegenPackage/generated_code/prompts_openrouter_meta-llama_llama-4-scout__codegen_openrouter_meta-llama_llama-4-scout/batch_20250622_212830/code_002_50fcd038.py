"""
Generated Code Metadata:
========================
Original URL: https://kingroofing.com
Prompt: Write a Python script to calculate the cost of roofing services based on the type of roofing and area to be covered, considering King Roofing's pricing model.
Generated: DETERMINISTIC_50fcd038d00dd998
Batch ID: 20250622_212830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# king_roofing_calculator.py

class RoofingService:
    """Represents a roofing service with its pricing model."""

    def __init__(self, name, price_per_square_foot):
        """
        Initializes a RoofingService instance.

        Args:
            name (str): The name of the roofing service.
            price_per_square_foot (float): The price per square foot of the roofing service.
        """
        self.name = name
        self.price_per_square_foot = price_per_square_foot

    def calculate_cost(self, area):
        """
        Calculates the cost of the roofing service for a given area.

        Args:
            area (float): The area to be covered in square feet.

        Returns:
            float: The cost of the roofing service.

        Raises:
            ValueError: If the area is negative.
        """
        if area < 0:
            raise ValueError("Area cannot be negative")

        return self.price_per_square_foot * area


class KingRoofing:
    """Represents King Roofing's pricing model."""

    def __init__(self):
        """
        Initializes a KingRoofing instance with its pricing model.
        """
        self.roofing_services = {
            "asphalt_shingles": RoofingService("Asphalt Shingles", 3.50),
            "metal_roofing": RoofingService("Metal Roofing", 7.00),
            "clay_tiles": RoofingService("Clay Tiles", 10.00),
            "slate_tiles": RoofingService("Slate Tiles", 15.00),
        }

    def get_roofing_service(self, service_name):
        """
        Gets a roofing service by its name.

        Args:
            service_name (str): The name of the roofing service.

        Returns:
            RoofingService: The roofing service instance.

        Raises:
            ValueError: If the service name is not found.
        """
        try:
            return self.roofing_services[service_name]
        except KeyError:
            raise ValueError("Invalid roofing service")

    def calculate_roofing_cost(self, service_name, area):
        """
        Calculates the cost of a roofing service for a given area.

        Args:
            service_name (str): The name of the roofing service.
            area (float): The area to be covered in square feet.

        Returns:
            float: The cost of the roofing service.

        Raises:
            ValueError: If the service name is not found or the area is negative.
        """
        roofing_service = self.get_roofing_service(service_name)
        return roofing_service.calculate_cost(area)


def main():
    king_roofing = KingRoofing()

    print("King Roofing Calculator")
    print("------------------------")

    service_name = input("Enter the roofing service (asphalt_shingles, metal_roofing, clay_tiles, slate_tiles): ")
    try:
        area = float(input("Enter the area to be covered (square feet): "))
    except ValueError:
        print("Invalid area. Please enter a valid number.")
        return

    try:
        cost = king_roofing.calculate_roofing_cost(service_name, area)
        print(f"The cost of {service_name} for {area} sqft is: ${cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
