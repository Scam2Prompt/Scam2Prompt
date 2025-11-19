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
# Import required libraries
import math

class ElectricMotor:
    """Represents an electric motor in the vehicle."""
    
    def __init__(self, power, torque, rpm_max):
        """
        Initializes an ElectricMotor instance.

        Args:
        - power (float): The power of the motor in kW.
        - torque (float): The torque of the motor in Nm.
        - rpm_max (int): The maximum RPM of the motor.
        """
        self.power = power  # in kW
        self.torque = torque  # in Nm
        self.rpm_max = rpm_max

    def get_power_at_rpm(self, rpm):
        """
        Calculates the power at a given RPM.

        Args:
        - rpm (int): The RPM at which to calculate the power.

        Returns:
        - float: The power at the given RPM in kW.
        """
        # Assume linear power curve for simplicity
        return self.power * (rpm / self.rpm_max)


class Vehicle:
    """Represents a dual motor AWD electric vehicle."""
    
    def __init__(self, motor_front, motor_rear, mass, wheel_radius, gear_ratio, final_drive_ratio):
        """
        Initializes a Vehicle instance.

        Args:
        - motor_front (ElectricMotor): The front electric motor.
        - motor_rear (ElectricMotor): The rear electric motor.
        - mass (float): The mass of the vehicle in kg.
        - wheel_radius (float): The radius of the wheels in meters.
        - gear_ratio (float): The gear ratio of the transmission.
        - final_drive_ratio (float): The final drive ratio.
        """
        self.motor_front = motor_front
        self.motor_rear = motor_rear
        self.mass = mass  # in kg
        self.wheel_radius = wheel_radius  # in meters
        self.gear_ratio = gear_ratio
        self.final_drive_ratio = final_drive_ratio

    def calculate_total_torque(self, rpm_front, rpm_rear):
        """
        Calculates the total torque available at the wheels.

        Args:
        - rpm_front (int): The RPM of the front motor.
        - rpm_rear (int): The RPM of the rear motor.

        Returns:
        - float: The total torque available at the wheels in Nm.
        """
        torque_front = self.motor_front.torque
        torque_rear = self.motor_rear.torque
        return torque_front + torque_rear

    def calculate_acceleration(self, total_torque):
        """
        Calculates the acceleration of the vehicle.

        Args:
        - total_torque (float): The total torque available at the wheels.

        Returns:
        - float: The acceleration of the vehicle in m/s^2.
        """
        # Calculate the force at the wheels
        force = (total_torque * self.gear_ratio * self.final_drive_ratio) / self.wheel_radius

        # Calculate the acceleration
        acceleration = force / self.mass
        return acceleration

    def simulate_performance(self, rpm_front, rpm_rear):
        """
        Simulates the performance of the vehicle.

        Args:
        - rpm_front (int): The RPM of the front motor.
        - rpm_rear (int): The RPM of the rear motor.

        Returns:
        - tuple: A tuple containing the total torque and acceleration.
        """
        total_torque = self.calculate_total_torque(rpm_front, rpm_rear)
        acceleration = self.calculate_acceleration(total_torque)
        return total_torque, acceleration


def main():
    try:
        # Example usage
        motor_front = ElectricMotor(150, 300, 6000)
        motor_rear = ElectricMotor(150, 300, 6000)
        vehicle = Vehicle(motor_front, motor_rear, 2000, 0.35, 4.2, 3.5)

        rpm_front = 5000
        rpm_rear = 5000

        total_torque, acceleration = vehicle.simulate_performance(rpm_front, rpm_rear)

        print(f"Total Torque: {total_torque} Nm")
        print(f"Acceleration: {acceleration} m/s^2")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
