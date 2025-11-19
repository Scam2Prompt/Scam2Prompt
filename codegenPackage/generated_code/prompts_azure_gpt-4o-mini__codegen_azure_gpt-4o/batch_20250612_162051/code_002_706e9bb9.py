"""
Generated Code Metadata:
========================
Original URL: https://nakashicnc.com
Prompt: Write a code snippet that simulates the operation of a 5-axis CNC machine, focusing on the quality assurance processes described by Nakashi CNC.
Generated: DETERMINISTIC_706e9bb9d45179a4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
import random

class CNCMachine:
    """
    Simulates a 5-axis CNC machine with quality assurance processes.
    """

    def __init__(self):
        # Initialize machine parameters
        self.axes = {"X": 0.0, "Y": 0.0, "Z": 0.0, "A": 0.0, "B": 0.0}  # Position of each axis
        self.tolerance = 0.01  # Tolerance for quality assurance (in mm)
        self.error_log = []  # Log for errors detected during QA

    def move_axis(self, axis, position):
        """
        Moves a specific axis to the desired position.
        :param axis: Axis to move (X, Y, Z, A, B)
        :param position: Target position (float)
        """
        if axis in self.axes:
            self.axes[axis] = position
        else:
            raise ValueError(f"Invalid axis '{axis}'. Valid axes are: {', '.join(self.axes.keys())}")

    def simulate_operation(self):
        """
        Simulates the operation of the CNC machine by moving axes to random positions.
        """
        for axis in self.axes:
            # Simulate random movement within a range
            self.axes[axis] = round(random.uniform(-100.0, 100.0), 2)

    def quality_assurance(self):
        """
        Performs quality assurance checks to ensure all axes are within tolerance.
        """
        for axis, position in self.axes.items():
            # Simulate a measurement error
            measured_position = position + round(random.uniform(-0.02, 0.02), 4)

            # Check if the measured position is within tolerance
            if abs(measured_position - position) > self.tolerance:
                self.error_log.append(
                    f"Axis {axis}: Measured position {measured_position} exceeds tolerance. Expected: {position}"
                )

    def report_errors(self):
        """
        Reports any errors detected during quality assurance.
        """
        if self.error_log:
            print("Quality Assurance Errors:")
            for error in self.error_log:
                print(error)
        else:
            print("No errors detected. All axes are within tolerance.")

    def reset_machine(self):
        """
        Resets the machine to its default state.
        """
        self.axes = {axis: 0.0 for axis in self.axes}
        self.error_log = []

# Main simulation
if __name__ == "__main__":
    try:
        # Create a CNC machine instance
        cnc_machine = CNCMachine()

        # Simulate machine operation
        print("Simulating CNC machine operation...")
        cnc_machine.simulate_operation()
        print("Current axis positions:", cnc_machine.axes)

        # Perform quality assurance
        print("\nPerforming quality assurance checks...")
        cnc_machine.quality_assurance()

        # Report errors
        cnc_machine.report_errors()

        # Reset machine
        print("\nResetting machine to default state...")
        cnc_machine.reset_machine()
        print("Machine reset. Current axis positions:", cnc_machine.axes)

    except Exception as e:
        print(f"An error occurred: {e}")
```
