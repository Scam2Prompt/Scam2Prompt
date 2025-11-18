"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigennlayer.com
Prompt: Write Python code to simulate energy storage system management, incorporating solar PV and EV charging solutions as described by Eigen Energy's turnkey service model.
Generated: DETERMINISTIC_dd246de96444bc59
Batch ID: 20250612_154651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EnergyStorageSystem:
    """
    A class to simulate an energy storage system management, incorporating solar PV and EV charging solutions.
    """

    def __init__(self, battery_capacity_kWh, solar_capacity_kW, ev_battery_capacity_kWh):
        """
        Initializes the energy storage system with given parameters.

        :param battery_capacity_kWh: Total capacity of the energy storage battery in kWh.
        :param solar_capacity_kW: Maximum output capacity of the solar PV system in kW.
        :param ev_battery_capacity_kWh: Capacity of the electric vehicle's battery in kWh.
        """
        self.battery_capacity_kWh = battery_capacity_kWh
        self.solar_capacity_kW = solar_capacity_kW
        self.ev_battery_capacity_kWh = ev_battery_capacity_kWh
        self.current_storage_kWh = 0

    def charge_battery(self, solar_power_kW, hours):
        """
        Charges the battery with solar power over a specified duration.

        :param solar_power_kW: The amount of solar power available in kW.
        :param hours: The number of hours to charge the battery.
        :raises ValueError: If the charge exceeds the battery capacity.
        """
        if solar_power_kW > self.solar_capacity_kW:
            logging.warning(f"Requested solar power {solar_power_kW} kW exceeds capacity. Capping to {self.solar_capacity_kW} kW.")
            solar_power_kW = self.solar_capacity_kW

        energy_generated_kWh = solar_power_kW * hours
        new_storage = self.current_storage_kWh + energy_generated_kWh

        if new_storage > self.battery_capacity_kWh:
            raise ValueError("Charging exceeds battery capacity. Please reduce charging duration or solar output.")
        
        self.current_storage_kWh = new_storage
        logging.info(f"Battery charged. Current storage: {self.current_storage_kWh} kWh")

    def discharge_battery(self, requested_kWh):
        """
        Discharges the battery to power the EV or other applications.

        :param requested_kWh: Amount of energy to discharge in kWh.
        :raises ValueError: If the requested discharge exceeds current storage.
        """
        if requested_kWh > self.current_storage_kWh:
            raise ValueError("Requested discharge exceeds current storage.")

        self.current_storage_kWh -= requested_kWh
        logging.info(f"Battery discharged. Current storage: {self.current_storage_kWh} kWh")

    def charge_ev(self, ev_current_storage_kWh, charge_amount_kWh):
        """
        Charges the electric vehicle from the energy storage system.

        :param ev_current_storage_kWh: Current energy storage level of the EV in kWh.
        :param charge_amount_kWh: Amount of energy to charge the EV in kWh.
        :raises ValueError: If the charge amount exceeds available storage or EV capacity.
        """
        if charge_amount_kWh > self.current_storage_kWh:
            raise ValueError("Not enough storage to charge the EV.")

        if ev_current_storage_kWh + charge_amount_kWh > self.ev_battery_capacity_kWh:
            raise ValueError("Charge amount exceeds EV battery capacity.")

        self.discharge_battery(charge_amount_kWh)
        logging.info(f"EV charged with {charge_amount_kWh} kWh. EV Current storage: {ev_current_storage_kWh + charge_amount_kWh} kWh")

    def get_current_storage(self):
        """
        Returns the current energy storage level.

        :return: Current storage in kWh.
        """
        return self.current_storage_kWh


def main():
    try:
        # Example configuration
        ess = EnergyStorageSystem(battery_capacity_kWh=100, solar_capacity_kW=10, ev_battery_capacity_kWh=75)

        # Simulate charging the battery with solar energy
        ess.charge_battery(solar_power_kW=8, hours=5)  # Charging with 8 kW for 5 hours

        # Check current storage
        logging.info(f"Current storage after charging: {ess.get_current_storage()} kWh")

        # Simulating EV charging
        ess.charge_ev(ev_current_storage_kWh=20, charge_amount_kWh=30)  # Charging EV with 30 kWh

        # Display final storage
        logging.info(f"Final storage after EV charging: {ess.get_current_storage()} kWh")

    except ValueError as e:
        logging.error(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
```
