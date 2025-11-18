"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://econtrolsa.ch
Prompt: Develop a Python script to simulate dual motor AWD electric vehicle performance, referencing the specifications provided for car models on eControl SA's website.
Generated: DETERMINISTIC_97c7fb96caac1629
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class ElectricVehicle:
    """
    A class to represent an all-wheel drive electric vehicle with dual motors.

    Attributes
    ----------
    model : str
        The model name of the vehicle.
    motor_power : float
        The power of each motor in kilowatts (kW).
    battery_capacity : float
        The battery capacity in kilowatt-hours (kWh).
    efficiency : float
        The energy efficiency in kilometers per kWh.
    total_power : float
        The total power output of the vehicle in kilowatts.
    range : float
        The maximum range of the vehicle in kilometers.

    Methods
    -------
    calculate_range():
        Calculates the maximum range of the vehicle based on battery capacity and efficiency.
    accelerate(time: float):
        Simulates the acceleration of the vehicle over a given time in seconds.
    """
    
    def __init__(self, model: str, motor_power: float, battery_capacity: float, efficiency: float):
        """
        Initializes the ElectricVehicle with specified model, motor power, battery capacity, and efficiency.

        Parameters
        ----------
        model : str
            The model name of the vehicle.
        motor_power : float
            The power of each motor in kilowatts (kW).
        battery_capacity : float
            The battery capacity in kilowatt-hours (kWh).
        efficiency : float
            The energy efficiency in kilometers per kWh.
        """
        self.model = model
        self.motor_power = motor_power
        self.battery_capacity = battery_capacity
        self.efficiency = efficiency
        self.total_power = 2 * motor_power  # Dual motors
        self.range = self.calculate_range()

    def calculate_range(self) -> float:
        """
        Calculates the maximum range of the vehicle based on battery capacity and efficiency.

        Returns
        -------
        float
            The maximum range in kilometers.
        """
        return self.battery_capacity * self.efficiency

    def accelerate(self, time: float) -> float:
        """
        Simulates the acceleration of the vehicle over a given time in seconds.

        Parameters
        ----------
        time : float
            The time in seconds over which to accelerate.

        Returns
        -------
        float
            The distance covered during acceleration in kilometers.
        """
        if time < 0:
            raise ValueError("Time must be a non-negative value.")
        
        # Assuming a simplistic linear acceleration model
        acceleration = self.total_power / 1000  # kW to kN
        distance = 0.5 * acceleration * (time ** 2) * (1 / 1000)  # Convert from meters to kilometers
        
        return distance

def main():
    """
    Main function to create an instance of ElectricVehicle and simulate its performance.
    """
    try:
        # Example specifications (These should be replaced with actual specifications)
        ev_model = "EV-Model-X"
        ev_motor_power = 150.0  # kW for each motor
        ev_battery_capacity = 75.0  # kWh
        ev_efficiency = 6.0  # km/kWh

        # Create an ElectricVehicle instance
        vehicle = ElectricVehicle(ev_model, ev_motor_power, ev_battery_capacity, ev_efficiency)

        # Simulate acceleration over 5 seconds
        acceleration_time = 5.0  # seconds
        distance_covered = vehicle.accelerate(acceleration_time)

        print(f"{vehicle.model} covered {distance_covered:.2f} km in {acceleration_time} seconds.")
        print(f"Maximum range: {vehicle.range:.2f} km")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
