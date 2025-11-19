"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://petrozartaj.com
Prompt: Write a Python script that simulates the operation of a static fluid measurement system, referencing the specifications outlined by Petro Kalaye Zartaj.
Generated: DETERMINISTIC_110ed2c6e25b8041
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Static Fluid Measurement System Simulation
Author: Expert Programmer
Date: YYYY-MM-DD

This script simulates the operation of a static fluid measurement system based
on the specifications outlined by Petro Kalaye Zartaj.

Features:
- Calculates fluid pressure at varying depths.
- Simulates a static fluid column with adjustable fluid density and gravity.
- Error handling for invalid inputs.
- Modular and follows Python best practices.

Usage: 
Run the script and follow the prompts to input system parameters.
"""

import sys

def calculate_pressure(depth, fluid_density, gravity=9.81):
    """
    Calculate the pressure at a given depth in a static fluid column.
    
    Parameters:
        depth (float): Depth in meters (non-negative).
        fluid_density (float): Fluid density in kg/m^3 (positive).
        gravity (float): Gravitational acceleration in m/s^2 (default: 9.81).
    
    Returns:
        float: Pressure in Pascals (Pa).
    
    Raises:
        ValueError: If inputs are invalid (e.g., negative depth or density).
    """
    if depth < 0:
        raise ValueError("Depth must be a non-negative value.")
    if fluid_density <= 0:
        raise ValueError("Fluid density must be a positive value.")

    # Pressure calculation using the hydrostatic pressure formula: P = ρ * g * h
    pressure = fluid_density * gravity * depth
    return pressure

def main():
    """
    Main function to simulate the static fluid measurement system.
    Collects user input, calculates pressure, and handles errors gracefully.
    """
    print("Static Fluid Measurement System Simulation")
    print("-" * 40)

    try:
        # Collect user input
        depth = float(input("Enter the fluid depth (meters): ").strip())
        fluid_density = float(input("Enter the fluid density (kg/m^3): ").strip())
        gravity = input("Enter gravitational acceleration (m/s^2, optional): ").strip()

        # Default gravity to Earth's value if not provided
        if gravity:
            gravity = float(gravity)
        else:
            gravity = 9.81

        # Calculate pressure
        pressure = calculate_pressure(depth, fluid_density, gravity)

        # Display result
        print(f"\nThe calculated pressure at {depth:.2f} meters depth is {pressure:.2f} Pascals.")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nSimulation complete. Exiting program.")

if __name__ == "__main__":
    # Ensure clean entry point for production readiness
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting...")
        sys.exit(1)
    except Exception as e:
        print(f"Critical Error: {e}")
        sys.exit(1)
```
