"""
Generated Code Metadata:
========================
Original URL: https://blasterturismo.com
Prompt: "Write a Python script to calculate the total cost of a travel package to Ametista do Sul, RS, based on the prices of tourist attractions and accommodations from Blaster Agência de Turismo."
Generated: DETERMINISTIC_4c27e13cd7c64375
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# travel_package_calculator.py

class TouristAttraction:
    """Represents a tourist attraction with a name and price."""

    def __init__(self, name: str, price: float):
        """
        Initializes a TouristAttraction.

        Args:
            name (str): The name of the attraction.
            price (float): The price of the attraction.
        """
        self.name = name
        self.price = price


class Accommodation:
    """Represents an accommodation with a name, price, and duration."""

    def __init__(self, name: str, price: float, duration: int):
        """
        Initializes an Accommodation.

        Args:
            name (str): The name of the accommodation.
            price (float): The price of the accommodation per day.
            duration (int): The duration of stay in days.
        """
        self.name = name
        self.price = price
        self.duration = duration


class TravelPackage:
    """Represents a travel package with attractions and accommodations."""

    def __init__(self):
        """Initializes a TravelPackage."""
        self.attractions = []
        self.accommodations = []

    def add_attraction(self, attraction: TouristAttraction):
        """
        Adds a tourist attraction to the package.

        Args:
            attraction (TouristAttraction): The attraction to add.
        """
        self.attractions.append(attraction)

    def add_accommodation(self, accommodation: Accommodation):
        """
        Adds an accommodation to the package.

        Args:
            accommodation (Accommodation): The accommodation to add.
        """
        self.accommodations.append(accommodation)

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of the travel package.

        Returns:
            float: The total cost.
        """
        total_attraction_cost = sum(attraction.price for attraction in self.attractions)
        total_accommodation_cost = sum(accommodation.price * accommodation.duration for accommodation in self.accommodations)
        return total_attraction_cost + total_accommodation_cost


def main():
    try:
        # Define tourist attractions
        attractions = [
            TouristAttraction("Attraction 1", 50.0),
            TouristAttraction("Attraction 2", 30.0),
            TouristAttraction("Attraction 3", 20.0),
        ]

        # Define accommodations
        accommodations = [
            Accommodation("Hotel", 100.0, 3),
            Accommodation("Hostel", 50.0, 2),
        ]

        # Create a travel package
        package = TravelPackage()

        # Add attractions and accommodations to the package
        for attraction in attractions:
            package.add_attraction(attraction)

        for accommodation in accommodations:
            package.add_accommodation(accommodation)

        # Calculate and print the total cost
        total_cost = package.calculate_total_cost()
        print(f"Total cost of the travel package: R${total_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
