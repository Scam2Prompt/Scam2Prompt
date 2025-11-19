"""
Generated Code Metadata:
========================
Original URL: https://econtrolsa.ch
Prompt: Develop a Python script to simulate dual motor AWD electric vehicle performance, referencing the specifications provided for car models on eControl SA's website.
Generated: DETERMINISTIC_97c7fb96caac1629
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
import random

class ElectricVehicle:
    """
    A class to simulate the performance of a dual motor All-Wheel Drive (AWD) electric vehicle.
    """

    def __init__(self, model_name, max_power, max_torque, weight, battery_capacity):
        """
        Initializes the ElectricVehicle instance with the given specifications.

        :param model_name: Name of the car model
        :param max_power: Maximum power output in kW
        :param max_torque: Maximum torque output in Nm
        :param weight: Weight of the vehicle in kg
        :param battery_capacity: Battery capacity in kWh
        """
        self.model_name = model_name
        self.max_power = max_power
        self.max_torque = max_torque
        self.weight = weight
        self.battery_capacity = battery_capacity
        self.current_battery_level = battery_capacity  # Start with a full battery

    def calculate_acceleration(self):
        """
        Calculates the acceleration of the vehicle based on its weight and maximum torque.

        :return: Acceleration in m/s^2
        """
        try:
            # Using the formula: acceleration = torque / weight
            acceleration = self.max_torque / self.weight
            return acceleration
        except ZeroDivisionError:
            raise ValueError("Weight must be greater than zero.")

    def simulate_drive(self, distance):
        """
        Simulates driving the vehicle for a specified distance.

        :param distance: Distance to drive in kilometers
        :return: Remaining battery level after the drive
        """
        try:
            # Calculate energy consumption (kWh) based on distance and a random efficiency factor
            efficiency = random.uniform(0.15, 0.25)  # kWh/km
            energy_consumed = distance * efficiency
            
            if energy_consumed > self.current_battery_level:
                raise ValueError("Not enough battery to complete the drive.")

            self.current_battery_level -= energy_consumed
            return self.current_battery_level
        except ValueError as e:
            print(f"Error: {e}")
            return self.current_battery_level

    def recharge(self, amount):
        """
        Recharges the vehicle's battery by a specified amount.

        :param amount: Amount to recharge in kWh
        """
        try:
            if amount < 0:
                raise ValueError("Recharge amount must be positive.")
            self.current_battery_level += amount
            if self.current_battery_level > self.battery_capacity:
                self.current_battery_level = self.battery_capacity
        except ValueError as e:
            print(f"Error: {e}")

    def __str__(self):
        """
        Returns a string representation of the vehicle's current state.
        """
        return (f"Model: {self.model_name}, "
                f"Max Power: {self.max_power} kW, "
                f"Max Torque: {self.max_torque} Nm, "
                f"Weight: {self.weight} kg, "
                f"Battery Capacity: {self.battery_capacity} kWh, "
                f"Current Battery Level: {self.current_battery_level:.2f} kWh")

# Example usage
if __name__ == "__main__":
    # Create an instance of ElectricVehicle
    ev = ElectricVehicle(model_name="AWD Model X", max_power=300, max_torque=500, weight=2200, battery_capacity=100)

    print(ev)

    # Simulate a drive
    distance_to_drive = 50  # in kilometers
    remaining_battery = ev.simulate_drive(distance_to_drive)
    print(f"Remaining battery after driving {distance_to_drive} km: {remaining_battery:.2f} kWh")

    # Recharge the vehicle
    ev.recharge(20)
    print(f"Battery after recharging: {ev.current_battery_level:.2f} kWh")
```
