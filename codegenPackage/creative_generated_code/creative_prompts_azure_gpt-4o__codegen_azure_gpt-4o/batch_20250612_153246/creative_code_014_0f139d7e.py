"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spmepl.com
Prompt: Develop a Python script to simulate the operation of pipe blasting plugs and coating equipment, incorporating parameters like bubble remover rollers as described by SPM Equipment.
Generated: DETERMINISTIC_0f139d7e1dbc16d0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random


class PipeBlastingSimulation:
    """
    Class to simulate the operation of pipe blasting plugs and coating equipment.
    Includes bubble remover rollers functionality as described by SPM Equipment.
    """

    def __init__(self, pipe_length, pipe_diameter):
        """
        Initialize the pipe blasting simulation.

        :param pipe_length: Length of the pipe in meters.
        :param pipe_diameter: Diameter of the pipe in centimeters.
        """
        self.pipe_length = pipe_length
        self.pipe_diameter = pipe_diameter
        self.coating_applied = False
        self.bubbles_removed = False

    def blasting_operation(self):
        """
        Simulates the blasting operation of the pipe.
        """
        try:
            print("Starting blasting operation...")
            # Simulated check for pipe diameter suitability
            if self.pipe_diameter < 10:
                raise ValueError("Pipe diameter too small for blasting operation.")
            print("Blasting operation completed successfully.")
        except ValueError as e:
            print(f"Error during blasting operation: {e}")

    def apply_coating(self):
        """
        Simulates the application of coating to the pipe.
        """
        try:
            print("Applying coating...")
            # Simulated coating success/failure based on random chance
            success = random.choice([True, False])
            if not success:
                raise RuntimeError("Coating application failed due to equipment issue.")
            self.coating_applied = True
            print("Coating applied successfully.")
        except RuntimeError as e:
            print(f"Error during coating operation: {e}")

    def remove_bubbles(self):
        """
        Simulates the removal of bubbles using bubble remover rollers.
        """
        try:
            print("Removing bubbles using rollers...")
            # Simulated bubble removal success/failure based on random chance
            success = random.choice([True, False])
            if not success:
                raise RuntimeError("Bubble removal failed due to roller malfunction.")
            self.bubbles_removed = True
            print("Bubbles removed successfully.")
        except RuntimeError as e:
            print(f"Error during bubble removal: {e}")

    def simulate(self):
        """
        Runs the complete simulation for pipe blasting plugs and coating equipment.
        """
        print("Starting pipe blasting and coating simulation...")
        self.blasting_operation()
        self.apply_coating()
        self.remove_bubbles()

        # Final status summary
        print("\nSimulation Summary:")
        print(f"Pipe Length: {self.pipe_length} meters")
        print(f"Pipe Diameter: {self.pipe_diameter} cm")
        print(f"Coating Applied: {'Yes' if self.coating_applied else 'No'}")
        print(f"Bubbles Removed: {'Yes' if self.bubbles_removed else 'No'}")
        print("Simulation completed.")


if __name__ == "__main__":
    # Example simulation with user-defined parameters
    pipe_length = 25  # example length in meters
    pipe_diameter = 15  # example diameter in cm

    # Create the simulation object and run the simulation
    simulation = PipeBlastingSimulation(pipe_length, pipe_diameter)
    simulation.simulate()
```
