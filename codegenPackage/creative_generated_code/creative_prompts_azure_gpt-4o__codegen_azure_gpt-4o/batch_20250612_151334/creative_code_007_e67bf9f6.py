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
import datetime
import logging


# Configure logging for tracking errors and information
logging.basicConfig(
    filename='street_lighting_simulation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class StreetLight:
    """
    Class representing a single street light and its energy consumption.
    """
    def __init__(self, power_rating_watts, operational_hours_per_day):
        """
        Initializes a street light with its power rating and operational hours.
        
        Args:
            power_rating_watts (float): Power rating of the street light in watts.
            operational_hours_per_day (float): Operational hours per day for the street light.
        """
        self.power_rating_watts = power_rating_watts
        self.operational_hours_per_day = operational_hours_per_day

    def daily_energy_consumption_kwh(self):
        """
        Calculates the daily energy consumption of the street light in kilowatt-hours (kWh).
        
        Returns:
            float: Daily energy consumption in kWh.
        """
        return (self.power_rating_watts * self.operational_hours_per_day) / 1000


class StreetLightingSystem:
    """
    Class representing a system of street lights and simulating total energy consumption.
    """
    def __init__(self):
        """
        Initializes an empty street lighting system.
        """
        self.street_lights = []

    def add_street_light(self, street_light):
        """
        Adds a street light to the system.
        
        Args:
            street_light (StreetLight): Street light to add to the system.
        """
        if not isinstance(street_light, StreetLight):
            raise ValueError("Invalid street light object.")
        self.street_lights.append(street_light)
        logging.info(f"Street light added: {street_light}")

    def simulate_energy_consumption(self, days=1):
        """
        Simulates the total energy consumption of the street lighting system over a given number of days.
        
        Args:
            days (int): Number of days to simulate (default: 1).
        
        Returns:
            float: Total energy consumption in kWh over the given number of days.
        """
        if days <= 0:
            raise ValueError("Number of days must be greater than 0.")
        
        total_energy_kwh = 0
        for street_light in self.street_lights:
            daily_energy = street_light.daily_energy_consumption_kwh()
            total_energy_kwh += daily_energy * days
        logging.info(f"Simulated energy consumption for {days} days: {total_energy_kwh:.2f} kWh")
        return total_energy_kwh


# Example usage
def main():
    try:
        # Create a street lighting system
        system = StreetLightingSystem()

        # Add street lights to the system
        system.add_street_light(StreetLight(power_rating_watts=100, operational_hours_per_day=10))
        system.add_street_light(StreetLight(power_rating_watts=150, operational_hours_per_day=8))
        system.add_street_light(StreetLight(power_rating_watts=80, operational_hours_per_day=12))

        # Simulate energy consumption for 30 days
        total_energy = system.simulate_energy_consumption(days=30)
        print(f"Total energy consumption for 30 days: {total_energy:.2f} kWh")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")


# Run the script
if __name__ == '__main__':
    main()
```
