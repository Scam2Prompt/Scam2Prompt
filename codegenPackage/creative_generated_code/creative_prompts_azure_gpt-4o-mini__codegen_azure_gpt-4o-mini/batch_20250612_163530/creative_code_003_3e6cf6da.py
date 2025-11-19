"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.chicoelectric.com
Prompt: Provide an example of how to implement a battery storage system for residential use, similar to the offerings by Chico Electric.
Generated: DETERMINISTIC_3e6cf6da5126e73c
Batch ID: 20250612_163530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BatteryStorageSystem:
    """
    A class to represent a battery storage system for residential use.
    
    Attributes
    ----------
    capacity : float
        Total capacity of the battery in kWh.
    current_charge : float
        Current charge of the battery in kWh.
    discharge_rate : float
        Rate at which the battery can discharge energy in kW.
    charge_rate : float
        Rate at which the battery can charge energy in kW.
    """

    def __init__(self, capacity, discharge_rate, charge_rate):
        """
        Initializes the BatteryStorageSystem with the given capacity, 
        discharge rate, and charge rate.

        Parameters
        ----------
        capacity : float
            Total capacity of the battery in kWh.
        discharge_rate : float
            Maximum discharge rate of the battery in kW.
        charge_rate : float
            Maximum charge rate of the battery in kW.
        """
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0.")
        if discharge_rate <= 0:
            raise ValueError("Discharge rate must be greater than 0.")
        if charge_rate <= 0:
            raise ValueError("Charge rate must be greater than 0.")

        self.capacity = capacity
        self.current_charge = 0.0  # Start with an empty battery
        self.discharge_rate = discharge_rate
        self.charge_rate = charge_rate

    def charge(self, hours):
        """
        Charges the battery for a given number of hours.

        Parameters
        ----------
        hours : float
            Number of hours to charge the battery.

        Raises
        ------
        ValueError
            If the resulting charge exceeds the battery capacity.
        """
        if hours < 0:
            raise ValueError("Charging hours must be non-negative.")

        charge_amount = self.charge_rate * hours
        if self.current_charge + charge_amount > self.capacity:
            raise ValueError("Charging exceeds battery capacity.")

        self.current_charge += charge_amount
        print(f"Battery charged. Current charge: {self.current_charge:.2f} kWh")

    def discharge(self, hours):
        """
        Discharges the battery for a given number of hours.

        Parameters
        ----------
        hours : float
            Number of hours to discharge the battery.

        Raises
        ------
        ValueError
            If the resulting discharge exceeds the current charge.
        """
        if hours < 0:
            raise ValueError("Discharging hours must be non-negative.")

        discharge_amount = self.discharge_rate * hours
        if discharge_amount > self.current_charge:
            raise ValueError("Discharging exceeds current charge.")

        self.current_charge -= discharge_amount
        print(f"Battery discharged. Current charge: {self.current_charge:.2f} kWh")

    def status(self):
        """
        Returns the current status of the battery.
        
        Returns
        -------
        dict
            A dictionary containing the total capacity and current charge.
        """
        return {
            "capacity": self.capacity,
            "current_charge": self.current_charge
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create a battery storage system with 10 kWh capacity, 
        # 2 kW discharge rate, and 2 kW charge rate
        battery_system = BatteryStorageSystem(capacity=10, discharge_rate=2, charge_rate=2)

        # Charge the battery for 3 hours
        battery_system.charge(hours=3)

        # Discharge the battery for 2 hours
        battery_system.discharge(hours=2)

        # Get battery status
        status = battery_system.status()
        print(f"Battery Status: {status}")

    except ValueError as e:
        print(f"Error: {e}")
```
