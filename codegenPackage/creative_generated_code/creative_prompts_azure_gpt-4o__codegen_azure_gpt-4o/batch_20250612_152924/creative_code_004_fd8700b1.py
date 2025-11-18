"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mydrones.gr
Prompt: Write code to calculate the thrust distribution for quadcopters with two clockwise and two counterclockwise rotors, based on the technical description provided on the "Drone Media" website.
Generated: DETERMINISTIC_fd8700b1d3aca9c0
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Quadcopter Thrust Distribution Calculator

This script calculates the thrust distribution for quadcopters with two clockwise 
and two counterclockwise rotors based on user-provided inputs such as total required thrust 
and torque stabilization requirements.

Assumptions:
- Rotor thrusts are positive values.
- Clockwise rotors are at positions 1 and 3; Counterclockwise rotors are at positions 2 and 4.
"""

class QuadcopterThrustCalculator:
    def __init__(self, total_thrust, torque_x, torque_y):
        """
        Initializes the thrust calculator with total thrust and torque requirements.
        
        :param total_thrust: Total thrust required by the quadcopter (in Newtons).
        :param torque_x: Torque along the X-axis (roll stabilization).
        :param torque_y: Torque along the Y-axis (pitch stabilization).
        """
        self.total_thrust = total_thrust
        self.torque_x = torque_x
        self.torque_y = torque_y

    def calculate_thrust_distribution(self):
        """
        Calculates the thrust distribution for the quadcopter.
        
        :return: A dictionary containing the thrust values for the rotors.
        """
        try:
            # Ensure total thrust is distributed among 4 rotors.
            avg_thrust = self.total_thrust / 4

            # Adjust thrust for torque stabilization.
            # Clockwise rotors (positions 1, 3) vs counterclockwise rotors (positions 2, 4).
            thrust_1 = avg_thrust - self.torque_x + self.torque_y  # Rotor 1 (CW)
            thrust_2 = avg_thrust + self.torque_x + self.torque_y  # Rotor 2 (CCW)
            thrust_3 = avg_thrust - self.torque_x - self.torque_y  # Rotor 3 (CW)
            thrust_4 = avg_thrust + self.torque_x - self.torque_y  # Rotor 4 (CCW)

            # Ensure no thrust is negative (physical constraint).
            if min(thrust_1, thrust_2, thrust_3, thrust_4) < 0:
                raise ValueError("Calculated thrust values cannot be negative.")

            return {
                "Rotor 1 (CW)": thrust_1,
                "Rotor 2 (CCW)": thrust_2,
                "Rotor 3 (CW)": thrust_3,
                "Rotor 4 (CCW)": thrust_4
            }
        except ZeroDivisionError:
            raise ValueError("Total thrust must be greater than zero.")
        except Exception as e:
            raise RuntimeError(f"An error occurred during thrust calculation: {str(e)}")


if __name__ == "__main__":
    # Example usage:
    try:
        # Input values: total thrust (Newtons), torque along X-axis, torque along Y-axis.
        total_thrust = float(input("Enter total thrust (N): "))
        torque_x = float(input("Enter torque along X-axis (N*m): "))
        torque_y = float(input("Enter torque along Y-axis (N*m): "))

        # Create a calculator instance and compute thrust distribution.
        calculator = QuadcopterThrustCalculator(total_thrust, torque_x, torque_y)
        thrust_distribution = calculator.calculate_thrust_distribution()

        # Output the calculated thrust values.
        print("\nCalculated Thrust Distribution:")
        for rotor, thrust in thrust_distribution.items():
            print(f"{rotor}: {thrust:.2f} N")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")
```
