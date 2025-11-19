"""
Generated Code Metadata:
========================
Original URL: https://spottersbrasil.com.br
Prompt: Implement a Python class to represent a military aircraft, using attributes and methods inspired by the content on Spotters Brasil, and demonstrate its usage with an example.
Generated: DETERMINISTIC_c1d82ed2466bd60a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MilitaryAircraft:
    """
    Represents a military aircraft.

    Attributes:
        name (str): The name of the aircraft.
        manufacturer (str): The manufacturer of the aircraft.
        model (str): The model of the aircraft.
        country_of_origin (str): The country of origin of the aircraft.
        max_speed (float): The maximum speed of the aircraft in km/h.
        range_km (float): The range of the aircraft in km.
        crew (int): The number of crew members.
    """

    def __init__(self, name, manufacturer, model, country_of_origin, max_speed, range_km, crew):
        """
        Initializes a MilitaryAircraft object.

        Args:
            name (str): The name of the aircraft.
            manufacturer (str): The manufacturer of the aircraft.
            model (str): The model of the aircraft.
            country_of_origin (str): The country of origin of the aircraft.
            max_speed (float): The maximum speed of the aircraft in km/h.
            range_km (float): The range of the aircraft in km.
            crew (int): The number of crew members.

        Raises:
            ValueError: If any of the input values are invalid.
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")
        if not isinstance(manufacturer, str) or not manufacturer.strip():
            raise ValueError("Manufacturer must be a non-empty string")
        if not isinstance(model, str) or not model.strip():
            raise ValueError("Model must be a non-empty string")
        if not isinstance(country_of_origin, str) or not country_of_origin.strip():
            raise ValueError("Country of origin must be a non-empty string")
        if not isinstance(max_speed, (int, float)) or max_speed <= 0:
            raise ValueError("Max speed must be a positive number")
        if not isinstance(range_km, (int, float)) or range_km <= 0:
            raise ValueError("Range must be a positive number")
        if not isinstance(crew, int) or crew <= 0:
            raise ValueError("Crew must be a positive integer")

        self.name = name
        self.manufacturer = manufacturer
        self.model = model
        self.country_of_origin = country_of_origin
        self.max_speed = max_speed
        self.range_km = range_km
        self.crew = crew

    def __str__(self):
        """
        Returns a string representation of the aircraft.

        Returns:
            str: A string representation of the aircraft.
        """
        return f"{self.name} ({self.model}) - {self.manufacturer} ({self.country_of_origin})"

    def get_aircraft_info(self):
        """
        Returns a dictionary with detailed information about the aircraft.

        Returns:
            dict: A dictionary with detailed information about the aircraft.
        """
        return {
            "Name": self.name,
            "Manufacturer": self.manufacturer,
            "Model": self.model,
            "Country of Origin": self.country_of_origin,
            "Max Speed (km/h)": self.max_speed,
            "Range (km)": self.range_km,
            "Crew": self.crew,
        }

    def calculate_travel_time(self, distance_km):
        """
        Calculates the travel time for a given distance.

        Args:
            distance_km (float): The distance to travel in km.

        Returns:
            float: The travel time in hours.

        Raises:
            ValueError: If the distance is not a positive number.
        """
        if not isinstance(distance_km, (int, float)) or distance_km <= 0:
            raise ValueError("Distance must be a positive number")

        if self.max_speed == 0:
            raise ValueError("Max speed cannot be zero")

        return distance_km / self.max_speed


def main():
    try:
        aircraft = MilitaryAircraft(
            "F-35A Lightning II",
            "Lockheed Martin",
            "F-35A",
            "United States",
            1900,
            2200,
            1,
        )

        print(aircraft)
        print("\nAircraft Info:")
        for key, value in aircraft.get_aircraft_info().items():
            print(f"{key}: {value}")

        distance_km = 1000
        travel_time = aircraft.calculate_travel_time(distance_km)
        print(f"\nTravel Time for {distance_km} km: {travel_time:.2f} hours")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
