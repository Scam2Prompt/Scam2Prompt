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
import math

class ElectricVehicle:
    """
    A class to simulate the performance of a dual motor AWD electric vehicle.
    """

    def __init__(self, front_motor_power_kw, rear_motor_power_kw, battery_capacity_kwh, weight_kg, drag_coefficient,
                 frontal_area_m2, wheel_radius_m):
        """
        Constructor to initialize the electric vehicle parameters.

        :param front_motor_power_kw: Power of the front motor in kilowatts.
        :param rear_motor_power_kw: Power of the rear motor in kilowatts.
        :param battery_capacity_kwh: Battery capacity in kilowatt-hours.
        :param weight_kg: Weight of the vehicle in kilograms.
        :param drag_coefficient: Drag coefficient of the vehicle (dimensionless).
        :param frontal_area_m2: Frontal area of the vehicle in square meters.
        :param wheel_radius_m: Radius of the wheels in meters.
        """
        self.front_motor_power_kw = front_motor_power_kw
        self.rear_motor_power_kw = rear_motor_power_kw
        self.total_motor_power_kw = front_motor_power_kw + rear_motor_power_kw
        self.battery_capacity_kwh = battery_capacity_kwh
        self.weight_kg = weight_kg
        self.drag_coefficient = drag_coefficient
        self.frontal_area_m2 = frontal_area_m2
        self.wheel_radius_m = wheel_radius_m

    def calculate_total_torque(self):
        """
        Calculate the total torque produced by the motors.

        :return: Total torque in Nm (Newton-meters).
        """
        # Assume motor efficiency of 95% and convert kW to Nm using motor speed at 3600 RPM.
        motor_efficiency = 0.95
        rpm = 3600
        torque_nm = (self.total_motor_power_kw * 1000 * motor_efficiency) / (2 * math.pi * (rpm / 60))
        return torque_nm

    def calculate_acceleration(self):
        """
        Calculate the vehicle's theoretical acceleration (0-100 km/h).

        :return: Acceleration in m/s².
        """
        # Assume no losses due to drivetrain and tires, and ignore aerodynamic drag initially.
        force_n = self.calculate_total_torque() / self.wheel_radius_m
        acceleration_mps2 = force_n / self.weight_kg
        return acceleration_mps2

    def estimate_range(self, average_speed_kmh):
        """
        Estimate the range of the vehicle based on average speed and other parameters.

        :param average_speed_kmh: Average speed in km/h.
        :return: Estimated range in kilometers.
        """
        # Aerodynamic drag force: F_drag = 0.5 * air_density * drag_coefficient * frontal_area * velocity²
        air_density = 1.225  # kg/m³ (standard sea level)
        velocity_mps = average_speed_kmh * 1000 / 3600  # Convert km/h to m/s
        drag_force_n = 0.5 * air_density * self.drag_coefficient * self.frontal_area_m2 * (velocity_mps ** 2)

        # Power required to overcome drag force: P_drag = F_drag * velocity
        power_drag_kw = drag_force_n * velocity_mps / 1000  # Convert W to kW

        # Total power consumption: Add rolling resistance and motor losses (simplified model)
        # Assume rolling resistance coefficient of 0.01
        rolling_resistance_force_n = 0.01 * self.weight_kg * 9.81
        power_rolling_kw = rolling_resistance_force_n * velocity_mps / 1000

        total_power_kw = power_drag_kw + power_rolling_kw

        # Estimate range: Range = (Battery Capacity / Total Power) * Average Speed
        range_km = (self.battery_capacity_kwh / total_power_kw) * average_speed_kmh
        return range_km


def main():
    """
    Main function to simulate electric vehicle performance.
    """
    # Example vehicle specifications (replace with real values from eControl SA's website)
    vehicle_spec = {
        'front_motor_power_kw': 200,  # Front motor power in kW
        'rear_motor_power_kw': 250,  # Rear motor power in kW
        'battery_capacity_kwh': 100,  # Battery capacity in kWh
        'weight_kg': 2200,  # Vehicle weight in kg
        'drag_coefficient': 0.28,  # Drag coefficient (dimensionless)
        'frontal_area_m2': 2.5,  # Frontal area in square meters
        'wheel_radius_m': 0.35  # Wheel radius in meters
    }

    # Initialize the vehicle
    ev = ElectricVehicle(**vehicle_spec)

    # Perform calculations
    print("Electric Vehicle Performance Simulation:")
    print(f"Total Torque (Nm): {ev.calculate_total_torque():.2f}")
    print(f"Theoretical Acceleration (m/s²): {ev.calculate_acceleration():.2f}")
    average_speed = 100  # km/h
    print(f"Estimated Range at {average_speed} km/h (km): {ev.estimate_range(average_speed):.2f}")


if __name__ == "__main__":
    # Run the simulation
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
