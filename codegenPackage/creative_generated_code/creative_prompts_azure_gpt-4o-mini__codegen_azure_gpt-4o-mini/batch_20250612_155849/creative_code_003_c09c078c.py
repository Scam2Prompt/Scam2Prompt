"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blackpanttthers.com
Prompt: Create a function that automates the charging schedule for electric vehicles based on energy production from solar panels.
Generated: DETERMINISTIC_c09c078c6325c625
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import random
from typing import List, Tuple

class ChargingScheduleError(Exception):
    """Custom exception for errors in the charging schedule."""
    pass

class ElectricVehicle:
    """Class to represent an electric vehicle."""
    
    def __init__(self, name: str, battery_capacity_kwh: float) -> None:
        """
        Initialize the Electric Vehicle with its name and battery capacity.
        
        :param name: Name of the electric vehicle
        :param battery_capacity_kwh: Total battery capacity in kilowatt-hours
        """
        self.name = name
        self.battery_capacity_kwh = battery_capacity_kwh
        self.current_charge_kwh = 0.0  # Current battery charge

    def charge(self, amount_kwh: float) -> None:
        """
        Charge the vehicle's battery.

        :param amount_kwh: Amount of energy to charge in kilowatt-hours
        :raises ChargingScheduleError: If charging exceeds battery capacity
        """
        if amount_kwh < 0:
            raise ChargingScheduleError("Charging amount must be non-negative.")
        if self.current_charge_kwh + amount_kwh > self.battery_capacity_kwh:
            raise ChargingScheduleError("Charging exceeds battery capacity.")
        
        self.current_charge_kwh += amount_kwh

    def __str__(self) -> str:
        return f"{self.name}: {self.current_charge_kwh:.2f} kWh / {self.battery_capacity_kwh:.2f} kWh"

def get_solar_energy_production() -> float:
    """
    Simulate solar energy production.

    :return: Simulated solar energy production in kilowatt-hours
    """
    return random.uniform(5.0, 30.0)  # Producing between 5 to 30 kWh

def generate_charging_schedule(ev: ElectricVehicle, hours: int) -> List[Tuple[datetime.datetime, float]]:
    """
    Generate a charging schedule for an electric vehicle based on solar energy production.

    :param ev: The electric vehicle to charge
    :param hours: Number of hours to generate the schedule
    :return: List of tuples containing datetime and energy charged (kWh)
    """
    schedule = []
    for hour in range(hours):
        time_slot = datetime.datetime.now() + datetime.timedelta(hours=hour)
        solar_energy = get_solar_energy_production()
        
        try:
            ev.charge(solar_energy)
            schedule.append((time_slot, solar_energy))
        except ChargingScheduleError as error:
            print(f"Error charging {ev.name} at {time_slot}: {error}")
            break
    
    return schedule

# Example Usage
if __name__ == "__main__":
    # Initialize an electric vehicle
    my_ev = ElectricVehicle(name="Tesla Model 3", battery_capacity_kwh=75.0)
    
    # Generate a charging schedule for the next 10 hours
    charging_schedule = generate_charging_schedule(my_ev, hours=10)
    
    # Print the charging schedule
    for time, energy in charging_schedule:
        print(f"Charged {energy:.2f} kWh at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Final state of the electric vehicle
    print(my_ev)
```
