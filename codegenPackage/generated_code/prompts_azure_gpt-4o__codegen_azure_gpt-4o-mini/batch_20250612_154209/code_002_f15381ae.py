"""
Generated Code Metadata:
========================
Original URL: https://aktivrorteknikk.no
Prompt: Generate code for a pipe cleaning simulation that uses customizable cleaning plugs for various pipe dimensions, as outlined in Aktiv Rørteknikk AS's plug cleaning services.
Generated: DETERMINISTIC_f15381ae9bb088d5
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Pipe:
    """
    Represents a pipe with a specific diameter and length.
    """
    def __init__(self, diameter: float, length: float):
        if diameter <= 0 or length <= 0:
            raise ValueError("Diameter and length must be positive values.")
        self.diameter = diameter
        self.length = length

    def __str__(self):
        return f"Pipe(diameter={self.diameter}, length={self.length})"


class CleaningPlug:
    """
    Represents a cleaning plug that can be used to clean pipes.
    """
    def __init__(self, diameter: float):
        if diameter <= 0:
            raise ValueError("Diameter must be a positive value.")
        self.diameter = diameter

    def __str__(self):
        return f"CleaningPlug(diameter={self.diameter})"


class PipeCleaningSimulation:
    """
    Simulates the cleaning of a pipe using a cleaning plug.
    """
    def __init__(self, pipe: Pipe, cleaning_plug: CleaningPlug):
        self.pipe = pipe
        self.cleaning_plug = cleaning_plug

    def run_simulation(self):
        """
        Runs the cleaning simulation and returns the result.
        """
        if self.cleaning_plug.diameter > self.pipe.diameter:
            raise ValueError("Cleaning plug diameter cannot be larger than pipe diameter.")
        
        # Simulate the cleaning process
        print(f"Starting cleaning simulation for {self.pipe} with {self.cleaning_plug}...")
        # Here we would have the logic for the cleaning process
        # For demonstration, we will just print a success message
        print("Cleaning in progress...")
        print("Cleaning completed successfully!")

        return True


def main():
    """
    Main function to execute the pipe cleaning simulation.
    """
    try:
        # Create a pipe with a specific diameter and length
        pipe = Pipe(diameter=100.0, length=500.0)  # Diameter in mm, Length in mm

        # Create a cleaning plug with a specific diameter
        cleaning_plug = CleaningPlug(diameter=95.0)  # Diameter in mm

        # Initialize the cleaning simulation
        simulation = PipeCleaningSimulation(pipe, cleaning_plug)

        # Run the simulation
        simulation.run_simulation()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
