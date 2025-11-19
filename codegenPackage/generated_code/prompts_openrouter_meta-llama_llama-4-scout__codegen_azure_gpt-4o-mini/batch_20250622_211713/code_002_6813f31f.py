"""
Generated Code Metadata:
========================
Original URL: https://sameersphysicsclasses.com
Prompt: Generate code for a simple physics calculator that can be used by students in Class XI or XII to solve numerical problems.
Generated: DETERMINISTIC_6813f31fd13760d9
Batch ID: 20250622_211713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PhysicsCalculator:
    """
    A simple physics calculator for Class XI and XII students to solve basic physics problems.
    """

    @staticmethod
    def calculate_velocity(distance, time):
        """
        Calculate velocity given distance and time.

        :param distance: Distance traveled (in meters)
        :param time: Time taken (in seconds)
        :return: Velocity (in meters per second)
        :raises ValueError: If time is zero or negative
        """
        if time <= 0:
            raise ValueError("Time must be greater than zero.")
        return distance / time

    @staticmethod
    def calculate_acceleration(initial_velocity, final_velocity, time):
        """
        Calculate acceleration given initial and final velocity and time.

        :param initial_velocity: Initial velocity (in meters per second)
        :param final_velocity: Final velocity (in meters per second)
        :param time: Time taken (in seconds)
        :return: Acceleration (in meters per second squared)
        :raises ValueError: If time is zero or negative
        """
        if time <= 0:
            raise ValueError("Time must be greater than zero.")
        return (final_velocity - initial_velocity) / time

    @staticmethod
    def calculate_force(mass, acceleration):
        """
        Calculate force using Newton's second law.

        :param mass: Mass (in kilograms)
        :param acceleration: Acceleration (in meters per second squared)
        :return: Force (in Newtons)
        :raises ValueError: If mass is negative or zero
        """
        if mass <= 0:
            raise ValueError("Mass must be greater than zero.")
        return mass * acceleration

    @staticmethod
    def calculate_energy(mass, height):
        """
        Calculate gravitational potential energy.

        :param mass: Mass (in kilograms)
        :param height: Height (in meters)
        :return: Potential energy (in Joules)
        :raises ValueError: If mass or height is negative
        """
        if mass < 0 or height < 0:
            raise ValueError("Mass and height must be non-negative.")
        g = 9.81  # Acceleration due to gravity (m/s^2)
        return mass * g * height

def main():
    """
    Main function to demonstrate the usage of the PhysicsCalculator.
    """
    try:
        # Example calculations
        distance = 100  # meters
        time = 10  # seconds
        velocity = PhysicsCalculator.calculate_velocity(distance, time)
        print(f"Velocity: {velocity} m/s")

        initial_velocity = 0  # m/s
        final_velocity = 20  # m/s
        acceleration_time = 5  # seconds
        acceleration = PhysicsCalculator.calculate_acceleration(initial_velocity, final_velocity, acceleration_time)
        print(f"Acceleration: {acceleration} m/s²")

        mass = 10  # kg
        force = PhysicsCalculator.calculate_force(mass, acceleration)
        print(f"Force: {force} N")

        height = 5  # meters
        energy = PhysicsCalculator.calculate_energy(mass, height)
        print(f"Potential Energy: {energy} J")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
