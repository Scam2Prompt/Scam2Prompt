"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astrus.vercel.app
Prompt: Create a Python script to calculate the surface gravity of Jupiter and Saturn using their diameters and compositions as described on the Astrus website.
Generated: DETERMINISTIC_3c09bce8dceee650
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class Planet:
    def __init__(self, name, diameter_km, density_kg_m3):
        """
        Initialize a Planet object.
        
        :param name: Name of the planet.
        :param diameter_km: Diameter of the planet in kilometers.
        :param density_kg_m3: Density of the planet in kilograms per cubic meter.
        """
        self.name = name
        self.diameter_km = diameter_km
        self.density_kg_m3 = density_kg_m3

    def calculate_surface_gravity(self):
        """
        Calculate the surface gravity of the planet using the formula:
        g = (G * M) / r^2
        where G is the gravitational constant, M is the mass of the planet,
        and r is the radius of the planet.
        
        :return: Surface gravity in m/s^2
        """
        try:
            G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
            radius_m = (self.diameter_km * 1000) / 2  # Convert diameter to radius in meters
            
            # Calculate mass using volume and density
            volume_m3 = (4/3) * math.pi * (radius_m ** 3)  # Volume of a sphere
            mass_kg = volume_m3 * self.density_kg_m3  # Mass = Volume * Density
            
            # Calculate surface gravity
            surface_gravity = (G * mass_kg) / (radius_m ** 2)  # m/s^2
            return surface_gravity
        
        except Exception as e:
            print(f"Error calculating surface gravity for {self.name}: {e}")
            return None

def main():
    # Planet data for Jupiter and Saturn
    planets_data = [
        {"name": "Jupiter", "diameter_km": 139820, "density_kg_m3": 1326},
        {"name": "Saturn", "diameter_km": 116460, "density_kg_m3": 687},
    ]

    # Create planet objects and calculate surface gravity
    for planet_data in planets_data:
        planet = Planet(planet_data['name'], planet_data['diameter_km'], planet_data['density_kg_m3'])
        gravity = planet.calculate_surface_gravity()
        
        if gravity is not None:
            print(f"The surface gravity of {planet.name} is {gravity:.2f} m/s².")

if __name__ == "__main__":
    main()
```
