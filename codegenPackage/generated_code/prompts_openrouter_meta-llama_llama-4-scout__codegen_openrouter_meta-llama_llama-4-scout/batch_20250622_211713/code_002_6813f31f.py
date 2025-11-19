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
# physics_calculator.py

"""
Simple Physics Calculator for Class XI and XII students.

Provides functionality to calculate:
- Distance, Displacement, Speed, Velocity, Acceleration
- Force, Mass, and Acceleration using Newton's Second Law
- Energy (Kinetic and Potential)
- Momentum
"""

import math

def calculate_distance(speed, time):
    """
    Calculate distance traveled by an object.

    Args:
        speed (float): Speed of the object in m/s.
        time (float): Time in seconds.

    Returns:
        float: Distance in meters.
    """
    return speed * time

def calculate_displacement(initial_velocity, acceleration, time):
    """
    Calculate displacement of an object under constant acceleration.

    Args:
        initial_velocity (float): Initial velocity in m/s.
        acceleration (float): Acceleration in m/s^2.
        time (float): Time in seconds.

    Returns:
        float: Displacement in meters.
    """
    return initial_velocity * time + 0.5 * acceleration * time**2

def calculate_speed(distance, time):
    """
    Calculate speed of an object.

    Args:
        distance (float): Distance in meters.
        time (float): Time in seconds.

    Returns:
        float: Speed in m/s.
    """
    if time == 0:
        raise ValueError("Time cannot be zero.")
    return distance / time

def calculate_velocity(displacement, time):
    """
    Calculate velocity of an object.

    Args:
        displacement (float): Displacement in meters.
        time (float): Time in seconds.

    Returns:
        float: Velocity in m/s.
    """
    if time == 0:
        raise ValueError("Time cannot be zero.")
    return displacement / time

def calculate_acceleration(change_in_velocity, time):
    """
    Calculate acceleration of an object.

    Args:
        change_in_velocity (float): Change in velocity in m/s.
        time (float): Time in seconds.

    Returns:
        float: Acceleration in m/s^2.
    """
    if time == 0:
        raise ValueError("Time cannot be zero.")
    return change_in_velocity / time

def calculate_force(mass, acceleration):
    """
    Calculate force applied to an object using Newton's Second Law.

    Args:
        mass (float): Mass in kg.
        acceleration (float): Acceleration in m/s^2.

    Returns:
        float: Force in Newtons.
    """
    return mass * acceleration

def calculate_mass(force, acceleration):
    """
    Calculate mass of an object using Newton's Second Law.

    Args:
        force (float): Force in Newtons.
        acceleration (float): Acceleration in m/s^2.

    Returns:
        float: Mass in kg.
    """
    if acceleration == 0:
        raise ValueError("Acceleration cannot be zero.")
    return force / acceleration

def calculate_kinetic_energy(mass, velocity):
    """
    Calculate kinetic energy of an object.

    Args:
        mass (float): Mass in kg.
        velocity (float): Velocity in m/s.

    Returns:
        float: Kinetic energy in Joules.
    """
    return 0.5 * mass * velocity**2

def calculate_potential_energy(mass, height, gravitational_acceleration=9.81):
    """
    Calculate potential energy of an object.

    Args:
        mass (float): Mass in kg.
        height (float): Height in meters.
        gravitational_acceleration (float, optional): Gravitational acceleration. Defaults to 9.81.

    Returns:
        float: Potential energy in Joules.
    """
    return mass * gravitational_acceleration * height

def calculate_momentum(mass, velocity):
    """
    Calculate momentum of an object.

    Args:
        mass (float): Mass in kg.
        velocity (float): Velocity in m/s.

    Returns:
        float: Momentum in kg*m/s.
    """
    return mass * velocity

def main():
    while True:
        print("\nPhysics Calculator Menu:")
        print("1. Distance")
        print("2. Displacement")
        print("3. Speed")
        print("4. Velocity")
        print("5. Acceleration")
        print("6. Force")
        print("7. Mass")
        print("8. Kinetic Energy")
        print("9. Potential Energy")
        print("10. Momentum")
        print("11. Quit")

        choice = input("Enter your choice (1-11): ")

        if choice == "1":
            speed = float(input("Enter speed (m/s): "))
            time = float(input("Enter time (s): "))
            print(f"Distance: {calculate_distance(speed, time)} m")
        elif choice == "2":
            initial_velocity = float(input("Enter initial velocity (m/s): "))
            acceleration = float(input("Enter acceleration (m/s^2): "))
            time = float(input("Enter time (s): "))
            print(f"Displacement: {calculate_displacement(initial_velocity, acceleration, time)} m")
        elif choice == "3":
            distance = float(input("Enter distance (m): "))
            time = float(input("Enter time (s): "))
            try:
                print(f"Speed: {calculate_speed(distance, time)} m/s")
            except ValueError as e:
                print(str(e))
        elif choice == "4":
            displacement = float(input("Enter displacement (m): "))
            time = float(input("Enter time (s): "))
            try:
                print(f"Velocity: {calculate_velocity(displacement, time)} m/s")
            except ValueError as e:
                print(str(e))
        elif choice == "5":
            change_in_velocity = float(input("Enter change in velocity (m/s): "))
            time = float(input("Enter time (s): "))
            try:
                print(f"Acceleration: {calculate_acceleration(change_in_velocity, time)} m/s^2")
            except ValueError as e:
                print(str(e))
        elif choice == "6":
            mass = float(input("Enter mass (kg): "))
            acceleration = float(input("Enter acceleration (m/s^2): "))
            print(f"Force: {calculate_force(mass, acceleration)} N")
        elif choice == "7":
            force = float(input("Enter force (N): "))
            acceleration = float(input("Enter acceleration (m/s^2): "))
            try:
                print(f"Mass: {calculate_mass(force, acceleration)} kg")
            except ValueError as e:
                print(str(e))
        elif choice == "8":
            mass = float(input("Enter mass (kg): "))
            velocity = float(input("Enter velocity (m/s): "))
            print(f"Kinetic Energy: {calculate_kinetic_energy(mass, velocity)} J")
        elif choice == "9":
            mass = float(input("Enter mass (kg): "))
            height = float(input("Enter height (m): "))
            print(f"Potential Energy: {calculate_potential_energy(mass, height)} J")
        elif choice == "10":
            mass = float(input("Enter mass (kg): "))
            velocity = float(input("Enter velocity (m/s): "))
            print(f"Momentum: {calculate_momentum(mass, velocity)} kg*m/s")
        elif choice == "11":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
