"""
Generated Code Metadata:
========================
Original URL: https://spmepl.com
Prompt: "Develop a script to control a pipe bending machine using hydraulic wedge bending mandrels."
Generated: DETERMINISTIC_7f0b730eb8a24007
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pipe_bending_machine.py

"""
Script to control a pipe bending machine using hydraulic wedge bending mandrels.

This script provides a basic interface to interact with the pipe bending machine.
It allows users to set bending parameters, start the bending process, and monitor the machine's status.

Author: [Your Name]
Date: [Today's Date]
"""

import time
import threading
from enum import Enum

# Define the machine's status
class MachineStatus(Enum):
    IDLE = 1
    BENDING = 2
    ERROR = 3

class PipeBendingMachine:
    def __init__(self):
        self.status = MachineStatus.IDLE
        self.bending_angle = 0
        self.pipe_diameter = 0
        self.mandrel_position = 0

    def set_bending_parameters(self, bending_angle, pipe_diameter):
        """
        Set the bending parameters.

        Args:
            bending_angle (float): The desired bending angle in degrees.
            pipe_diameter (float): The diameter of the pipe being bent.

        Raises:
            ValueError: If the bending angle or pipe diameter is invalid.
        """
        if bending_angle < 0 or bending_angle > 180:
            raise ValueError("Invalid bending angle. Must be between 0 and 180 degrees.")
        if pipe_diameter <= 0:
            raise ValueError("Invalid pipe diameter. Must be greater than 0.")

        self.bending_angle = bending_angle
        self.pipe_diameter = pipe_diameter

    def start_bending(self):
        """
        Start the bending process.

        Raises:
            RuntimeError: If the machine is not in the IDLE state.
        """
        if self.status != MachineStatus.IDLE:
            raise RuntimeError("Machine is not in the IDLE state.")

        self.status = MachineStatus.BENDING
        threading.Thread(target=self._bend_pipe).start()

    def _bend_pipe(self):
        """
        Perform the pipe bending process.

        This method simulates the bending process by adjusting the mandrel position.
        In a real-world implementation, this method would interact with the machine's hardware.
        """
        try:
            # Simulate the bending process
            for i in range(self.bending_angle):
                self.mandrel_position = i
                time.sleep(0.1)  # Simulate the bending time

            self.status = MachineStatus.IDLE
        except Exception as e:
            self.status = MachineStatus.ERROR
            print(f"Error occurred during bending: {e}")

    def get_status(self):
        """
        Get the machine's current status.

        Returns:
            MachineStatus: The machine's current status.
        """
        return self.status

    def get_bending_parameters(self):
        """
        Get the current bending parameters.

        Returns:
            tuple: A tuple containing the bending angle and pipe diameter.
        """
        return self.bending_angle, self.pipe_diameter

def main():
    machine = PipeBendingMachine()

    while True:
        print("\nPipe Bending Machine Control")
        print("1. Set bending parameters")
        print("2. Start bending")
        print("3. Get machine status")
        print("4. Get bending parameters")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                bending_angle = float(input("Enter bending angle (degrees): "))
                pipe_diameter = float(input("Enter pipe diameter: "))
                machine.set_bending_parameters(bending_angle, pipe_diameter)
                print("Bending parameters set successfully.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            try:
                machine.start_bending()
                print("Bending process started.")
            except RuntimeError as e:
                print(f"Error: {e}")
        elif choice == "3":
            status = machine.get_status()
            print(f"Machine status: {status.name}")
        elif choice == "4":
            bending_angle, pipe_diameter = machine.get_bending_parameters()
            print(f"Bending angle: {bending_angle} degrees")
            print(f"Pipe diameter: {pipe_diameter}")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
