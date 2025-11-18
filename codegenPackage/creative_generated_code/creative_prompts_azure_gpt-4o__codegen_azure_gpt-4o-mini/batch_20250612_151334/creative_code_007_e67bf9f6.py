"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecpowerlightingltd.com
Prompt: Provide a Python script to simulate street lighting energy consumption, considering the services offered by E.C. Power & Lighting Ltd.
Generated: DETERMINISTIC_e67bf9f6a0135113
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class StreetLight:
    """Represents a street light and its energy consumption."""
    
    def __init__(self, id: int, wattage: float):
        """
        Initialize the street light with an ID and wattage.

        :param id: Unique identifier for the street light
        :param wattage: Power consumption of the street light in watts
        """
        self.id = id
        self.wattage = wattage  # Wattage of the street light
        self.is_on = False       # Current state of the street light (on/off)

    def turn_on(self):
        """Turn on the street light."""
        self.is_on = True
        logging.info(f'Street light {self.id} turned on.')

    def turn_off(self):
        """Turn off the street light."""
        self.is_on = False
        logging.info(f'Street light {self.id} turned off.')

    def energy_consumed(self, hours: float) -> float:
        """
        Calculate the energy consumed by the street light over a period.

        :param hours: The number of hours the light has been on
        :return: Energy consumed in kilowatt-hours (kWh)
        """
        if hours < 0:
            logging.error('Hours cannot be negative.')
            raise ValueError("Hours cannot be negative.")
        return (self.wattage / 1000) * hours  # Convert watts to kilowatts

class StreetLightingSystem:
    """Manages a collection of street lights and simulates their operations."""

    def __init__(self):
        """Initialize the street lighting system with an empty list of street lights."""
        self.lights = []

    def add_light(self, light: StreetLight):
        """
        Add a street light to the system.

        :param light: An instance of StreetLight to be added
        """
        self.lights.append(light)
        logging.info(f'Added street light {light.id} with wattage {light.wattage}W.')

    def simulate_night(self, hours: float):
        """
        Simulate the operation of street lights during a night.

        :param hours: The number of hours to simulate
        """
        if hours <= 0:
            logging.error('Simulation hours must be greater than zero.')
            raise ValueError("Simulation hours must be greater than zero.")

        for light in self.lights:
            light.turn_on()  # Turn on the light for the simulation
            energy = light.energy_consumed(hours)
            logging.info(f'Street light {light.id} consumed {energy:.2f} kWh over {hours} hours.')
            light.turn_off()  # Turn off the light after the simulation

def main():
    """Main function to run the street lighting simulation."""
    try:
        # Create a street lighting system
        lighting_system = StreetLightingSystem()

        # Add street lights to the system with random wattages
        for i in range(1, 6):
            wattage = random.choice([50, 75, 100])  # Random wattage for street lights
            lighting_system.add_light(StreetLight(id=i, wattage=wattage))

        # Simulate the street lights for a given number of hours
        lighting_system.simulate_night(hours=8)  # Simulate for 8 hours
    except Exception as e:
        logging.error(f'An error occurred: {e}')

if __name__ == "__main__":
    main()
```
