"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nakashicnc.com
Prompt: Write a code snippet that simulates the operation of a 5-axis CNC machine, focusing on the quality assurance processes described by Nakashi CNC.
Generated: DETERMINISTIC_706e9bb9d45179a4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class CNCMachine:
    """
    A class representing a 5-axis CNC machine simulator.
    Simulates movement and quality assurance processes.
    """

    def __init__(self):
        """
        Initialize the CNC machine with default axis positions.
        """
        self.axis_positions = {"X": 0.0, "Y": 0.0, "Z": 0.0, "A": 0.0, "B": 0.0}  # Positions for 5 axes
        self.tool_status = "Idle"  # Status of the tool
        self.error_log = []  # Log for tracking errors

    def move_axis(self, axis, position):
        """
        Move a specific axis to the desired position.

        :param axis: Axis to move ('X', 'Y', 'Z', 'A', 'B')
        :param position: Target position (float)
        """
        try:
            if axis in self.axis_positions:
                self.axis_positions[axis] = position
                print(f"Moved axis {axis} to position {position}.")
            else:
                raise ValueError(f"Invalid axis '{axis}' specified.")
        except Exception as e:
            self.error_log.append(str(e))
            print(f"Error: {str(e)}")

    def perform_quality_assurance(self):
        """
        Perform a basic quality assurance check for the CNC machine.

        Simulates checking axis positions and tool status.
        """
        try:
            # Check if all axes are within operational limits
            for axis, position in self.axis_positions.items():
                if not (0 <= position <= 100):  # Example operational range
                    raise ValueError(f"Axis {axis} out of bounds with position {position}.")

            # Simulate tool inspection
            if self.tool_status != "Idle" and self.tool_status != "Operational":
                raise ValueError(f"Tool status '{self.tool_status}' is invalid.")

            # QA Passed
            print("Quality assurance passed. All systems are operational.")
        except Exception as e:
            self.error_log.append(str(e))
            print(f"Quality assurance failed: {str(e)}")

    def simulate_operation(self):
        """
        Simulate a basic operation sequence of the CNC machine.
        """
        print("Starting operation sequence...")
        self.move_axis("X", 50.0)
        self.move_axis("Y", 75.0)
        self.move_axis("Z", 25.0)
        self.move_axis("A", 90.0)
        self.move_axis("B", 45.0)

        self.tool_status = "Operational"  # Simulate tool status change
        self.perform_quality_assurance()

        print("Operation sequence completed.")

# Main execution
if __name__ == "__main__":
    cnc_machine = CNCMachine()
    cnc_machine.simulate_operation()

    # Display error log if any errors occurred
    if cnc_machine.error_log:
        print("\nError Log:")
        for error in cnc_machine.error_log:
            print(f"- {error}")
```
