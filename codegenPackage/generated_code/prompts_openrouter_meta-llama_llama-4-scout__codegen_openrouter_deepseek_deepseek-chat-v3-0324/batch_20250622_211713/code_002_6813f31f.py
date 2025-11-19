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
"""
Physics Calculator for Class XI/XII Students

This script provides a simple physics calculator to solve common numerical problems
in mechanics, thermodynamics, and electromagnetism.
"""

import math

def calculate_velocity(initial_velocity, acceleration, time):
    """
    Calculate final velocity using v = u + at.

    Args:
        initial_velocity (float): Initial velocity (u) in m/s
        acceleration (float): Acceleration (a) in m/s²
        time (float): Time (t) in seconds

    Returns:
        float: Final velocity in m/s
    """
    try:
        return initial_velocity + (acceleration * time)
    except TypeError:
        raise ValueError("All inputs must be numerical values")

def calculate_displacement(initial_velocity, time, acceleration):
    """
    Calculate displacement using s = ut + ½at².

    Args:
        initial_velocity (float): Initial velocity (u) in m/s
        time (float): Time (t) in seconds
        acceleration (float): Acceleration (a) in m/s²

    Returns:
        float: Displacement in meters
    """
    try:
        return (initial_velocity * time) + (0.5 * acceleration * time ** 2)
    except TypeError:
        raise ValueError("All inputs must be numerical values")

def calculate_force(mass, acceleration):
    """
    Calculate force using F = ma.

    Args:
        mass (float): Mass in kg
        acceleration (float): Acceleration in m/s²

    Returns:
        float: Force in Newtons
    """
    try:
        return mass * acceleration
    except TypeError:
        raise ValueError("All inputs must be numerical values")

def calculate_work(force, displacement, angle=0):
    """
    Calculate work done using W = Fd cosθ.

    Args:
        force (float): Force in Newtons
        displacement (float): Displacement in meters
        angle (float, optional): Angle between force and displacement in degrees. Defaults to 0.

    Returns:
        float: Work done in Joules
    """
    try:
        angle_rad = math.radians(angle)
        return force * displacement * math.cos(angle_rad)
    except TypeError:
        raise ValueError("All inputs must be numerical values")

def calculate_power(work, time):
    """
    Calculate power using P = W/t.

    Args:
        work (float): Work done in Joules
        time (float): Time in seconds

    Returns:
        float: Power in Watts
    """
    try:
        if time == 0:
            raise ValueError("Time cannot be zero")
        return work / time
    except TypeError:
        raise ValueError("All inputs must be numerical values")

def calculate_ohm_law(voltage=None, current=None, resistance=None):
    """
    Calculate missing value in Ohm's Law (V = IR).

    Args:
        voltage (float, optional): Voltage in Volts
        current (float, optional): Current in Amperes
        resistance (float, optional): Resistance in Ohms

    Returns:
        float: The calculated missing value
    """
    try:
        if voltage is None and current is not None and resistance is not None:
            return current * resistance
        elif current is None and voltage is not None and resistance is not None:
            if resistance == 0:
                raise ValueError("Resistance cannot be zero")
            return voltage / resistance
        elif resistance is None and voltage is not None and current is not None:
            if current == 0:
                raise ValueError("Current cannot be zero")
            return voltage / current
        else:
            raise ValueError("Exactly two parameters must be provided")
    except TypeError:
        raise ValueError("All inputs must be numerical values")

def calculate_kinetic_energy(mass, velocity):
    """
    Calculate kinetic energy using KE = ½mv².

    Args:
        mass (float): Mass in kg
        velocity (float): Velocity in m/s

    Returns:
        float: Kinetic energy in Joules
    """
    try:
        return 0.5 * mass * (velocity ** 2)
    except TypeError:
        raise ValueError("All inputs must be numerical values")

def calculate_potential_energy(mass, height, gravity=9.81):
    """
    Calculate gravitational potential energy using PE = mgh.

    Args:
        mass (float): Mass in kg
        height (float): Height in meters
        gravity (float, optional): Acceleration due to gravity in m/s². Defaults to 9.81.

    Returns:
        float: Potential energy in Joules
    """
    try:
        return mass * gravity * height
    except TypeError:
        raise ValueError("All inputs must be numerical values")

def main():
    """Main function to demonstrate the physics calculator."""
    print("Physics Calculator for Class XI/XII")
    print("----------------------------------")
    
    try:
        # Example calculations
        v = calculate_velocity(10, 2, 5)
        print(f"Final velocity: {v:.2f} m/s")
        
        s = calculate_displacement(10, 5, 2)
        print(f"Displacement: {s:.2f} m")
        
        f = calculate_force(5, 2)
        print(f"Force: {f:.2f} N")
        
        w = calculate_work(10, 5, 30)
        print(f"Work done: {w:.2f} J")
        
        p = calculate_power(100, 5)
        print(f"Power: {p:.2f} W")
        
        r = calculate_ohm_law(voltage=12, current=3)
        print(f"Resistance: {r:.2f} Ω")
        
        ke = calculate_kinetic_energy(2, 5)
        print(f"Kinetic energy: {ke:.2f} J")
        
        pe = calculate_potential_energy(2, 10)
        print(f"Potential energy: {pe:.2f} J")
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
