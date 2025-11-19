"""
Generated Code Metadata:
========================
Original URL: https://elara-celestia.com
Prompt: Create a data model to represent the L&T Elara Celestia project, including attributes for apartment configurations, pricing, and amenities.
Generated: DETERMINISTIC_0f84a4d514eed6a4
Batch ID: 20250622_212053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Apartment:
    """
    Represents an apartment in the L&T Elara Celestia project.

    Attributes:
        apartment_id (str): Unique identifier for the apartment.
        configuration (str): Description of the apartment configuration (e.g., 1BHK, 2BHK).
        area (float): Area of the apartment in square feet.
        price (float): Price of the apartment in currency.
        amenities (list): List of amenities available in the apartment.
    """

    def __init__(self, apartment_id: str, configuration: str, area: float, price: float, amenities: list):
        """
        Initializes an Apartment instance.

        Args:
            apartment_id (str): Unique identifier for the apartment.
            configuration (str): Description of the apartment configuration.
            area (float): Area of the apartment in square feet.
            price (float): Price of the apartment in currency.
            amenities (list): List of amenities available in the apartment.
        """
        self.apartment_id = apartment_id
        self.configuration = configuration
        self.area = area
        self.price = price
        self.amenities = amenities

    def __str__(self):
        """Returns a string representation of the apartment."""
        return f"Apartment {self.apartment_id}: {self.configuration}, Area: {self.area} sqft, Price: {self.price}, Amenities: {', '.join(self.amenities)}"


class Project:
    """
    Represents the L&T Elara Celestia project.

    Attributes:
        project_name (str): Name of the project.
        apartments (list): List of Apartment instances in the project.
    """

    def __init__(self, project_name: str):
        """
        Initializes a Project instance.

        Args:
            project_name (str): Name of the project.
        """
        self.project_name = project_name
        self.apartments = []

    def add_apartment(self, apartment: Apartment):
        """
        Adds an apartment to the project.

        Args:
            apartment (Apartment): The apartment to be added.

        Raises:
            ValueError: If the apartment already exists in the project.
        """
        if any(a.apartment_id == apartment.apartment_id for a in self.apartments):
            raise ValueError(f"Apartment with ID {apartment.apartment_id} already exists in the project.")
        self.apartments.append(apartment)

    def get_apartment(self, apartment_id: str) -> Apartment:
        """
        Retrieves an apartment by its ID.

        Args:
            apartment_id (str): The ID of the apartment to retrieve.

        Returns:
            Apartment: The apartment instance.

        Raises:
            LookupError: If the apartment is not found.
        """
        for apartment in self.apartments:
            if apartment.apartment_id == apartment_id:
                return apartment
        raise LookupError(f"Apartment with ID {apartment_id} not found.")

    def list_apartments(self):
        """Lists all apartments in the project."""
        for apartment in self.apartments:
            print(apartment)


# Example usage
if __name__ == "__main__":
    try:
        elara_celestia = Project("L&T Elara Celestia")

        # Adding apartments
        elara_celestia.add_apartment(Apartment("APT001", "1BHK", 650, 5000000, ["Gym", "Pool", "Garden"]))
        elara_celestia.add_apartment(Apartment("APT002", "2BHK", 850, 7500000, ["Gym", "Pool", "Garden", "Clubhouse"]))

        # Listing apartments
        elara_celestia.list_apartments()

        # Retrieving a specific apartment
        apartment = elara_celestia.get_apartment("APT001")
        print(f"Retrieved: {apartment}")

    except (ValueError, LookupError) as e:
        print(f"Error: {e}")
```
