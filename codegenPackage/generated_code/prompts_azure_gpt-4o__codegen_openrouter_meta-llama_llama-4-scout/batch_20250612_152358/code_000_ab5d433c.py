"""
Generated Code Metadata:
========================
Original URL: https://astrus.vercel.app
Prompt: Write a Python script to calculate the orbital period of planets in the Solar System using the data provided on the Astrus website, including details like Mercury's 88 Earth-day year and Neptune's 165 Earth-year orbit.
Generated: DETERMINISTIC_ab5d433ceaad2263
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solar_system_orbital_periods.py

"""
Calculates the orbital periods of planets in the Solar System.

This script uses a dictionary to store the orbital periods of planets in Earth days.
It provides functions to calculate and display the orbital periods.

Author: [Your Name]
Date: [Today's Date]
"""

# Import required libraries
import math

class Planet:
    """Represents a planet in the Solar System."""

    def __init__(self, name, orbital_period_in_earth_days):
        """
        Initializes a Planet object.

        Args:
            name (str): The name of the planet.
            orbital_period_in_earth_days (float): The orbital period of the planet in Earth days.
        """
        self.name = name
        self.orbital_period_in_earth_days = orbital_period_in_earth_days

    def __str__(self):
        return f"{self.name}: {self.orbital_period_in_earth_days} Earth days"


class SolarSystem:
    """Represents the Solar System."""

    def __init__(self):
        """
        Initializes a SolarSystem object.

        The orbital periods are based on data from the Astrus website.
        """
        self.planets = {
            "Mercury": Planet("Mercury", 88),
            "Venus": Planet("Venus", 225),
            "Earth": Planet("Earth", 365.25),
            "Mars": Planet("Mars", 687),
            "Jupiter": Planet("Jupiter", 4333),
            "Saturn": Planet("Saturn", 10759),
            "Uranus": Planet("Uranus", 30687),
            "Neptune": Planet("Neptune", 60190),
        }

    def get_orbital_period(self, planet_name):
        """
        Gets the orbital period of a planet.

        Args:
            planet_name (str): The name of the planet.

        Returns:
            float: The orbital period of the planet in Earth days.

        Raises:
            ValueError: If the planet is not found.
        """
        try:
            return self.planets[planet_name].orbital_period_in_earth_days
        except KeyError:
            raise ValueError(f"Planet '{planet_name}' not found.")

    def display_orbital_periods(self):
        """
        Displays the orbital periods of all planets.
        """
        for planet in self.planets.values():
            print(planet)

    def convert_to_earth_years(self, orbital_period_in_earth_days):
        """
        Converts an orbital period from Earth days to Earth years.

        Args:
            orbital_period_in_earth_days (float): The orbital period in Earth days.

        Returns:
            float: The orbital period in Earth years.
        """
        return orbital_period_in_earth_days / 365.25


def main():
    solar_system = SolarSystem()

    print("Orbital Periods of Planets in the Solar System:")
    solar_system.display_orbital_periods()

    print("\nOrbital Periods in Earth Years:")
    for planet_name, planet in solar_system.planets.items():
        orbital_period_in_earth_years = solar_system.convert_to_earth_years(planet.orbital_period_in_earth_days)
        print(f"{planet_name}: {orbital_period_in_earth_years:.2f} Earth years")

    # Example usage: Get the orbital period of a planet
    planet_name = "Neptune"
    try:
        orbital_period = solar_system.get_orbital_period(planet_name)
        print(f"\nThe orbital period of {planet_name} is {orbital_period} Earth days.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
