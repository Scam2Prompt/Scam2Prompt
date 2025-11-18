"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spmepl.com
Prompt: Generate a Python program to simulate the operation of a chain-type pipe cutting machine, ensuring compatibility with manual pipe end heating torches as described on the SPM Equipment website.
Generated: DETERMINISTIC_4005cac0ef2bd4d3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time


class PipeCuttingMachine:
    """
    A class to simulate the operation of a chain-type pipe cutting machine.
    This machine is compatible with manual pipe end heating torches.
    """

    def __init__(self, pipe_diameter: float, pipe_length: float):
        """
        Initializes the pipe cutting machine with pipe dimensions.

        :param pipe_diameter: Diameter of the pipe in centimeters.
        :param pipe_length: Length of the pipe in centimeters.
        """
        self.pipe_diameter = pipe_diameter
        self.pipe_length = pipe_length
        self.is_cutting = False
        self.is_torch_heating = False

    def start_cutting(self):
        """
        Starts the pipe cutting operation.
        """
        if self.is_cutting:
            print("The machine is already cutting.")
        else:
            self.is_cutting = True
            print("Pipe cutting operation started.")

    def stop_cutting(self):
        """
        Stops the pipe cutting operation.
        """
        if not self.is_cutting:
            print("The machine is not cutting.")
        else:
            self.is_cutting = False
            print("Pipe cutting operation stopped.")

    def start_torch_heating(self):
        """
        Activates manual pipe end heating torch.
        """
        if self.is_torch_heating:
            print("The torch is already heating.")
        else:
            self.is_torch_heating = True
            print("Torch heating operation started.")

    def stop_torch_heating(self):
        """
        Deactivates manual pipe end heating torch.
        """
        if not self.is_torch_heating:
            print("The torch is not heating.")
        else:
            self.is_torch_heating = False
            print("Torch heating operation stopped.")

    def simulate_cutting_process(self):
        """
        Simulates the cutting process based on pipe dimensions.
        Includes time delay for realistic simulation.
        """
        if not self.is_cutting:
            print("Cannot simulate cutting. Please start the cutting operation first.")
            return

        cutting_time = (self.pipe_diameter + self.pipe_length) / 10  # Simplistic time calculation
        print(f"Simulating cutting process for {cutting_time:.2f} seconds...")
        time.sleep(cutting_time)  # Simulate time taken to cut the pipe
        print("Cutting process complete.")

    def simulate_torch_heating_process(self):
        """
        Simulates the torch heating process.
        Includes time delay for realistic simulation.
        """
        if not self.is_torch_heating:
            print("Cannot simulate torch heating. Please start the torch heating operation first.")
            return

        heating_time = self.pipe_diameter / 5  # Simplistic time calculation
        print(f"Simulating torch heating process for {heating_time:.2f} seconds...")
        time.sleep(heating_time)  # Simulate time taken for heating
        print("Torch heating process complete.")

    def get_status(self):
        """
        Prints the current status of the machine.
        """
        print("Machine Status:")
        print(f"Pipe Diameter: {self.pipe_diameter} cm")
        print(f"Pipe Length: {self.pipe_length} cm")
        print(f"Cutting Status: {'Active' if self.is_cutting else 'Inactive'}")
        print(f"Torch Heating Status: {'Active' if self.is_torch_heating else 'Inactive'}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the pipe cutting machine with pipe dimensions
        machine = PipeCuttingMachine(pipe_diameter=30.0, pipe_length=200.0)

        # Print initial status
        machine.get_status()

        # Start cutting and simulate the process
        machine.start_cutting()
        machine.simulate_cutting_process()
        machine.stop_cutting()

        # Start torch heating and simulate the process
        machine.start_torch_heating()
        machine.simulate_torch_heating_process()
        machine.stop_torch_heating()

        # Print final status
        machine.get_status()

    except Exception as e:
        # Handle any unexpected errors gracefully
        print(f"An error occurred: {e}")
```
