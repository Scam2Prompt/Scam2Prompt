"""
Generated Code Metadata:
========================
Original URL: https://eigennlayer.com
Prompt: Write Python code to simulate energy storage system management, incorporating solar PV and EV charging solutions as described by Eigen Energy's turnkey service model.
Generated: DETERMINISTIC_dd246de96444bc59
Batch ID: 20250612_154651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# energy_storage_system.py

class EnergyStorageSystem:
    def __init__(self, capacity, max_charge_power, max_discharge_power):
        """
        Initialize the energy storage system.

        Args:
            capacity (float): The total capacity of the energy storage system in kWh.
            max_charge_power (float): The maximum charge power of the energy storage system in kW.
            max_discharge_power (float): The maximum discharge power of the energy storage system in kW.
        """
        self.capacity = capacity
        self.max_charge_power = max_charge_power
        self.max_discharge_power = max_discharge_power
        self.current_state_of_charge = 0.0  # Initial state of charge is 0%

    def charge(self, power):
        """
        Charge the energy storage system.

        Args:
            power (float): The power at which to charge the energy storage system in kW.

        Raises:
            ValueError: If the charge power exceeds the maximum charge power.
        """
        if power > self.max_charge_power:
            raise ValueError("Charge power exceeds maximum charge power")

        # Calculate the new state of charge
        new_state_of_charge = min(self.current_state_of_charge + (power / 1000) * 1, 1)  # Assume 1 hour time step
        self.current_state_of_charge = new_state_of_charge

    def discharge(self, power):
        """
        Discharge the energy storage system.

        Args:
            power (float): The power at which to discharge the energy storage system in kW.

        Raises:
            ValueError: If the discharge power exceeds the maximum discharge power.
            ValueError: If the energy storage system is not sufficiently charged.
        """
        if power > self.max_discharge_power:
            raise ValueError("Discharge power exceeds maximum discharge power")
        if self.current_state_of_charge < (power / 1000) * 1 / self.capacity:
            raise ValueError("Insufficient charge")

        # Calculate the new state of charge
        new_state_of_charge = max(self.current_state_of_charge - (power / 1000) * 1, 0)  # Assume 1 hour time step
        self.current_state_of_charge = new_state_of_charge

    def get_state_of_charge(self):
        """
        Get the current state of charge of the energy storage system.

        Returns:
            float: The current state of charge as a fraction.
        """
        return self.current_state_of_charge


class SolarPV:
    def __init__(self, capacity):
        """
        Initialize the solar PV system.

        Args:
            capacity (float): The capacity of the solar PV system in kWp.
        """
        self.capacity = capacity

    def get_power_output(self, irradiance):
        """
        Get the power output of the solar PV system.

        Args:
            irradiance (float): The irradiance in W/m^2.

        Returns:
            float: The power output of the solar PV system in kW.
        """
        # Assume a simple linear relationship between irradiance and power output
        return self.capacity * irradiance / 1000


class ElectricVehicle:
    def __init__(self, battery_capacity):
        """
        Initialize the electric vehicle.

        Args:
            battery_capacity (float): The capacity of the electric vehicle battery in kWh.
        """
        self.battery_capacity = battery_capacity
        self.current_state_of_charge = 0.0  # Initial state of charge is 0%

    def charge(self, power):
        """
        Charge the electric vehicle.

        Args:
            power (float): The power at which to charge the electric vehicle in kW.

        Raises:
            ValueError: If the charge power would exceed the battery capacity.
        """
        # Calculate the new state of charge
        new_state_of_charge = min(self.current_state_of_charge + (power / 1000) * 1, 1)  # Assume 1 hour time step
        if new_state_of_charge > 1:
            raise ValueError("Charge power would exceed battery capacity")
        self.current_state_of_charge = new_state_of_charge

    def get_state_of_charge(self):
        """
        Get the current state of charge of the electric vehicle.

        Returns:
            float: The current state of charge as a fraction.
        """
        return self.current_state_of_charge


class EnergyManagementSystem:
    def __init__(self, energy_storage_system, solar_pv, electric_vehicle):
        """
        Initialize the energy management system.

        Args:
            energy_storage_system (EnergyStorageSystem): The energy storage system.
            solar_pv (SolarPV): The solar PV system.
            electric_vehicle (ElectricVehicle): The electric vehicle.
        """
        self.energy_storage_system = energy_storage_system
        self.solar_pv = solar_pv
        self.electric_vehicle = electric_vehicle

    def manage_energy(self, irradiance):
        """
        Manage energy based on the current irradiance.

        Args:
            irradiance (float): The current irradiance in W/m^2.
        """
        # Get the power output of the solar PV system
        solar_power = self.solar_pv.get_power_output(irradiance)

        # Charge the energy storage system with excess solar power
        excess_power = solar_power - 5  # Assume a base load of 5 kW
        if excess_power > 0:
            self.energy_storage_system.charge(excess_power)

        # Charge the electric vehicle with energy from the energy storage system or solar PV
        if self.electric_vehicle.get_state_of_charge() < 0.8:  # Charge EV if SOC < 80%
            if solar_power > 10:  # Prioritize solar power for EV charging
                self.electric_vehicle.charge(solar_power)
            elif self.energy_storage_system.get_state_of_charge() > 0.2:  # Use energy storage system if available
                self.electric_vehicle.charge(self.energy_storage_system.max_discharge_power)
                self.energy_storage_system.discharge(self.energy_storage_system.max_discharge_power)


# Example usage
if __name__ == "__main__":
    energy_storage_system = EnergyStorageSystem(100, 50, 50)
    solar_pv = SolarPV(50)
    electric_vehicle = ElectricVehicle(20)

    energy_management_system = EnergyManagementSystem(energy_storage_system, solar_pv, electric_vehicle)

    irradiance = 800  # W/m^2
    energy_management_system.manage_energy(irradiance)

    print("Energy Storage System SOC:", energy_storage_system.get_state_of_charge())
    print("Electric Vehicle SOC:", electric_vehicle.get_state_of_charge())
```
