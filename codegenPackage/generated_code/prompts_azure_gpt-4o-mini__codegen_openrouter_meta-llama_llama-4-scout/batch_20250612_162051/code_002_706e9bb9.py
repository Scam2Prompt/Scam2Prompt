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
# Nakashi CNC 5-axis CNC Machine Simulator

class CNCMachine:
    def __init__(self):
        """
        Initialize the CNC machine with default settings.
        """
        self.axes = {
            'X': 0,
            'Y': 0,
            'Z': 0,
            'A': 0,  # 4th axis (rotational around X)
            'B': 0   # 5th axis (rotational around Y)
        }
        self.tool = None
        self.material = None

    def set_tool(self, tool):
        """
        Set the tool for the CNC machine.

        Args:
            tool (str): The tool to be used (e.g., 'end_mill', 'drill_bit')
        """
        self.tool = tool

    def set_material(self, material):
        """
        Set the material for the CNC machine.

        Args:
            material (str): The material to be machined (e.g., 'aluminum', 'steel')
        """
        self.material = material

    def move_axis(self, axis, position):
        """
        Move a specific axis to a given position.

        Args:
            axis (str): The axis to move (X, Y, Z, A, or B)
            position (float): The target position

        Raises:
            ValueError: If the axis is not valid
        """
        if axis not in self.axes:
            raise ValueError(f"Invalid axis: {axis}")
        self.axes[axis] = position

    def perform_operation(self, operation):
        """
        Perform a specific operation (e.g., milling, drilling).

        Args:
            operation (str): The operation to perform

        Raises:
            ValueError: If the operation is not supported
        """
        if not self.tool:
            raise ValueError("No tool set")
        if not self.material:
            raise ValueError("No material set")

        # Simulate the operation
        print(f"Performing {operation} with {self.tool} on {self.material}")

    def quality_assurance(self):
        """
        Perform quality assurance checks.

        Returns:
            bool: True if all checks pass, False otherwise
        """
        # Simulate quality assurance checks
        checks = [
            self._check_axis_positions(),
            self._check_tool_condition(),
            self._check_material_condition()
        ]
        return all(checks)

    def _check_axis_positions(self):
        """
        Check if axis positions are within tolerance.

        Returns:
            bool: True if all axis positions are within tolerance, False otherwise
        """
        tolerance = 0.01
        for axis, position in self.axes.items():
            if abs(position) > tolerance:
                print(f"Axis {axis} position out of tolerance: {position}")
                return False
        return True

    def _check_tool_condition(self):
        """
        Check if the tool is in good condition.

        Returns:
            bool: True if the tool is in good condition, False otherwise
        """
        # Simulate tool condition check
        return self.tool == 'end_mill'  # Replace with actual tool condition logic

    def _check_material_condition(self):
        """
        Check if the material is suitable for machining.

        Returns:
            bool: True if the material is suitable, False otherwise
        """
        # Simulate material condition check
        return self.material in ['aluminum', 'steel']  # Replace with actual material condition logic


def main():
    machine = CNCMachine()
    machine.set_tool('end_mill')
    machine.set_material('aluminum')

    machine.move_axis('X', 10)
    machine.move_axis('Y', 20)
    machine.move_axis('Z', 30)

    machine.perform_operation('milling')

    if machine.quality_assurance():
        print("Quality assurance checks passed")
    else:
        print("Quality assurance checks failed")


if __name__ == "__main__":
    main()
```
