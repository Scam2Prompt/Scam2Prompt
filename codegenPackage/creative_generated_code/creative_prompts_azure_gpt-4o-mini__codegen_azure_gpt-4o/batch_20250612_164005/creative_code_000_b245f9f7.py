"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sameersphysicsclasses.com
Prompt: Generate a Python script that simulates physics experiments for Class XI students, incorporating concepts from CBSE Physics curriculum.
Generated: DETERMINISTIC_b245f9f7d3995591
Batch ID: 20250612_164005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def simulate_free_fall():
    """
    Simulates free fall experiment.

    Calculates time taken for an object to fall to the ground
    assuming no air resistance, using the formula:
    t = sqrt(2 * h / g)
    """
    try:
        # Constants
        g = 9.8  # Acceleration due to gravity in m/s^2
        
        # Input height
        height = float(input("Enter height (in meters) from which the object is dropped: "))
        if height < 0:
            raise ValueError("Height must be a positive value.")
        
        # Calculate time of fall
        time_of_fall = math.sqrt(2 * height / g)
        
        print(f"Time taken to hit the ground: {time_of_fall:.2f} seconds")
    except ValueError as e:
        print(f"Error: {e}")


def simulate_projectile_motion():
    """
    Simulates projectile motion experiment.

    Calculates the maximum height and range for a projectile
    launched with an initial velocity and angle, using the formulas:
    - Maximum height: h = (v^2 * sin^2(theta)) / (2 * g)
    - Range: R = (v^2 * sin(2 * theta)) / g
    """
    try:
        # Constants
        g = 9.8  # Acceleration due to gravity in m/s^2
        
        # Input initial velocity and angle
        velocity = float(input("Enter initial velocity (in m/s): "))
        angle_deg = float(input("Enter launch angle (in degrees): "))
        if velocity < 0 or not (0 <= angle_deg <= 90):
            raise ValueError("Velocity must be positive, and angle must be between 0 and 90 degrees.")
        
        angle_rad = math.radians(angle_deg)  # Convert angle to radians
        
        # Calculate maximum height and range
        max_height = (velocity**2 * math.sin(angle_rad)**2) / (2 * g)
        range_of_projectile = (velocity**2 * math.sin(2 * angle_rad)) / g
        
        print(f"Maximum Height: {max_height:.2f} meters")
        print(f"Range: {range_of_projectile:.2f} meters")
    except ValueError as e:
        print(f"Error: {e}")


def simulate_simple_pendulum():
    """
    Simulates simple pendulum experiment.

    Calculates the time period of a pendulum given its length, using the formula:
    T = 2 * pi * sqrt(L / g)
    """
    try:
        # Constants
        g = 9.8  # Acceleration due to gravity in m/s^2
        
        # Input length of pendulum
        length = float(input("Enter length of the pendulum (in meters): "))
        if length <= 0:
            raise ValueError("Length must be a positive value.")
        
        # Calculate time period
        time_period = 2 * math.pi * math.sqrt(length / g)
        
        print(f"Time Period of Pendulum: {time_period:.2f} seconds")
    except ValueError as e:
        print(f"Error: {e}")


def main_menu():
    """
    Displays the main menu and allows the user to select an experiment.
    """
    while True:
        print("\nPhysics Experiment Simulator - Class XI")
        print("1. Free Fall Simulation")
        print("2. Projectile Motion Simulation")
        print("3. Simple Pendulum Simulation")
        print("4. Exit")
        
        try:
            choice = int(input("Select an experiment (1-4): "))
            if choice == 1:
                simulate_free_fall()
            elif choice == 2:
                simulate_projectile_motion()
            elif choice == 3:
                simulate_simple_pendulum()
            elif choice == 4:
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Error: Please enter a valid integer.")


# Entry point of the program
if __name__ == "__main__":
    main_menu()
```
