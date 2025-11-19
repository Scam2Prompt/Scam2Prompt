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
# A simple physics calculator for solving basic numerical problems.
# This calculator supports calculations for speed, force, and energy.

def calculate_speed(distance, time):
    """
    Calculate speed using the formula: speed = distance / time.
    
    Parameters:
        distance (float): Distance traveled (in meters).
        time (float): Time taken (in seconds).
    
    Returns:
        float: Speed (in meters per second).
    """
    try:
        if time <= 0:
            raise ValueError("Time must be greater than zero.")
        return distance / time
    except Exception as e:
        print(f"Error calculating speed: {e}")
        return None


def calculate_force(mass, acceleration):
    """
    Calculate force using the formula: force = mass * acceleration.
    
    Parameters:
        mass (float): Mass of the object (in kilograms).
        acceleration (float): Acceleration of the object (in meters per second squared).
    
    Returns:
        float: Force (in newtons).
    """
    try:
        return mass * acceleration
    except Exception as e:
        print(f"Error calculating force: {e}")
        return None


def calculate_kinetic_energy(mass, velocity):
    """
    Calculate kinetic energy using the formula: KE = 0.5 * mass * velocity^2.
    
    Parameters:
        mass (float): Mass of the object (in kilograms).
        velocity (float): Velocity of the object (in meters per second).
    
    Returns:
        float: Kinetic energy (in joules).
    """
    try:
        return 0.5 * mass * velocity ** 2
    except Exception as e:
        print(f"Error calculating kinetic energy: {e}")
        return None


def main():
    """
    Main function to interact with the user and perform calculations.
    """
    print("Welcome to the Physics Calculator!")
    print("Choose an option:")
    print("1. Calculate Speed")
    print("2. Calculate Force")
    print("3. Calculate Kinetic Energy")
    print("4. Exit")

    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                distance = float(input("Enter distance (in meters): "))
                time = float(input("Enter time (in seconds): "))
                speed = calculate_speed(distance, time)
                if speed is not None:
                    print(f"Speed: {speed} m/s")
            elif choice == 2:
                mass = float(input("Enter mass (in kilograms): "))
                acceleration = float(input("Enter acceleration (in m/s^2): "))
                force = calculate_force(mass, acceleration)
                if force is not None:
                    print(f"Force: {force} N")
            elif choice == 3:
                mass = float(input("Enter mass (in kilograms): "))
                velocity = float(input("Enter velocity (in m/s): "))
                energy = calculate_kinetic_energy(mass, velocity)
                if energy is not None:
                    print(f"Kinetic Energy: {energy} J")
            elif choice == 4:
                print("Exiting the Physics Calculator. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter numeric values where required.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Entry point of the program
if __name__ == "__main__":
    main()
```
