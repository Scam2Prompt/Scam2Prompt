"""
Generated Code Metadata:
========================
Original URL: https://blackpanttthers.com
Prompt: "Design a domotic system for automating electric vehicle charging at home during off-peak hours or when excess renewable energy is available."
Generated: DETERMINISTIC_7c87bbcd83e2b82b
Batch ID: 20250622_211523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# domotic_system.py

import datetime
import logging
import time
from typing import Dict

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RenewableEnergySource:
    """Represents a renewable energy source (e.g., solar panels)."""
    def __init__(self, capacity: float, efficiency: float):
        """
        Initializes a renewable energy source.

        Args:
        - capacity (float): The maximum energy production capacity (in kWh).
        - efficiency (float): The efficiency of the energy production (between 0 and 1).
        """
        self.capacity = capacity
        self.efficiency = efficiency
        self.current_production = 0.0  # in kWh

    def update_production(self, production: float):
        """Updates the current energy production."""
        self.current_production = production

    def has_excess_energy(self) -> bool:
        """Checks if there is excess energy available."""
        return self.current_production > 0.0


class ElectricVehicle:
    """Represents an electric vehicle."""
    def __init__(self, battery_capacity: float, charging_rate: float):
        """
        Initializes an electric vehicle.

        Args:
        - battery_capacity (float): The battery capacity (in kWh).
        - charging_rate (float): The charging rate (in kW).
        """
        self.battery_capacity = battery_capacity
        self.current_charge_level = 0.0  # in %
        self.charging_rate = charging_rate

    def charge(self):
        """Charges the electric vehicle."""
        if self.current_charge_level < 100.0:
            self.current_charge_level += self.charging_rate * 0.1  # assume 0.1 hours charging
            logger.info(f"Charging EV... Current charge level: {self.current_charge_level}%")
        else:
            logger.info("EV is fully charged.")

    def is_charging(self) -> bool:
        """Checks if the electric vehicle is charging."""
        return self.current_charge_level < 100.0


class OffPeakChargingScheduler:
    """Schedules off-peak charging for electric vehicles."""
    def __init__(self, off_peak_hours: list, ev: ElectricVehicle):
        """
        Initializes an off-peak charging scheduler.

        Args:
        - off_peak_hours (list): A list of off-peak hours (in 24-hour format, e.g., [22, 23, 0, 1, 2]).
        - ev (ElectricVehicle): The electric vehicle to schedule charging for.
        """
        self.off_peak_hours = off_peak_hours
        self.ev = ev

    def should_charge(self) -> bool:
        """Checks if it's an off-peak hour and the EV is not fully charged."""
        current_hour = datetime.datetime.now().hour
        return current_hour in self.off_peak_hours and not self.ev.is_charging()


class RenewableEnergyChargingScheduler:
    """Schedules charging for electric vehicles based on excess renewable energy."""
    def __init__(self, renewable_energy_source: RenewableEnergySource, ev: ElectricVehicle):
        """
        Initializes a renewable energy charging scheduler.

        Args:
        - renewable_energy_source (RenewableEnergySource): The renewable energy source.
        - ev (ElectricVehicle): The electric vehicle to schedule charging for.
        """
        self.renewable_energy_source = renewable_energy_source
        self.ev = ev

    def should_charge(self) -> bool:
        """Checks if there is excess renewable energy and the EV is not fully charged."""
        return self.renewable_energy_source.has_excess_energy() and not self.ev.is_charging()


class DomoticSystem:
    """The domotic system for automating electric vehicle charging."""
    def __init__(self, 
                 renewable_energy_source: RenewableEnergySource, 
                 ev: ElectricVehicle, 
                 off_peak_hours: list):
        """
        Initializes the domotic system.

        Args:
        - renewable_energy_source (RenewableEnergySource): The renewable energy source.
        - ev (ElectricVehicle): The electric vehicle.
        - off_peak_hours (list): A list of off-peak hours.
        """
        self.renewable_energy_source = renewable_energy_source
        self.ev = ev
        self.off_peak_hours = off_peak_hours
        self.off_peak_scheduler = OffPeakChargingScheduler(off_peak_hours, ev)
        self.renewable_energy_scheduler = RenewableEnergyChargingScheduler(renewable_energy_source, ev)

    def run(self):
        """Runs the domotic system."""
        try:
            while True:
                if self.off_peak_scheduler.should_charge():
                    self.ev.charge()
                elif self.renewable_energy_scheduler.should_charge():
                    self.ev.charge()
                time.sleep(60)  # check every minute
        except Exception as e:
            logger.error(f"An error occurred: {e}")


if __name__ == "__main__":
    # Example usage
    renewable_energy_source = RenewableEnergySource(capacity=5.0, efficiency=0.8)
    ev = ElectricVehicle(battery_capacity=60.0, charging_rate=3.0)
    off_peak_hours = [22, 23, 0, 1, 2]

    domotic_system = DomoticSystem(renewable_energy_source, ev, off_peak_hours)

    # Simulate excess renewable energy
    renewable_energy_source.update_production(2.0)

    domotic_system.run()
```
