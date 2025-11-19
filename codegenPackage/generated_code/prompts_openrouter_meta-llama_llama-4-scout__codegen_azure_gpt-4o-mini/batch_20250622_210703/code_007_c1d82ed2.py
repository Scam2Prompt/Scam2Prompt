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
    A class to represent a military aircraft.

    Attributes:
        name (str): The name of the aircraft.
        model (str): The model of the aircraft.
        max_speed (float): The maximum speed of the aircraft in km/h.
        range (float): The operational range of the aircraft in km.
        armament (list): A list of armaments carried by the aircraft.
    """

    def __init__(self, name: str, model: str, max_speed: float, range: float, armament: list):
        """
        Initializes a MilitaryAircraft instance.

        Args:
            name (str): The name of the aircraft.
            model (str): The model of the aircraft.
            max_speed (float): The maximum speed of the aircraft in km/h.
            range (float): The operational range of the aircraft in km.
            armament (list): A list of armaments carried by the aircraft.
        """
        self.name = name
        self.model = model
        self.max_speed = max_speed
        self.range = range
        self.armament = armament

    def display_info(self):
        """Displays the aircraft's information."""
        info = (
            f"Aircraft Name: {self.name}\n"
            f"Model: {self.model}\n"
            f"Max Speed: {self.max_speed} km/h\n"
            f"Range: {self.range} km\n"
            f"Armament: {', '.join(self.armament)}"
        )
        print(info)

    def is_within_range(self, distance: float) -> bool:
        """
        Checks if the aircraft can operate within a given distance.

        Args:
            distance (float): The distance to check in km.

        Returns:
            bool: True if the aircraft can operate within the distance, False otherwise.
        """
        if distance < 0:
            raise ValueError("Distance cannot be negative.")
        return distance <= self.range

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of MilitaryAircraft
        aircraft = MilitaryAircraft(
            name="F-16 Fighting Falcon",
            model="F-16C",
            max_speed=2400,
            range=4000,
            armament=["AIM-120 AMRAAM", "AIM-9 Sidewinder", "GBU-12 Paveway II"]
        )

        # Display aircraft information
        aircraft.display_info()

        # Check if the aircraft can operate within a specified distance
        distance_to_check = 3500
        if aircraft.is_within_range(distance_to_check):
            print(f"The aircraft can operate within {distance_to_check} km.")
        else:
            print(f"The aircraft cannot operate within {distance_to_check} km.")
    
    except ValueError as e:
        print(f"Error: {e}")
```
