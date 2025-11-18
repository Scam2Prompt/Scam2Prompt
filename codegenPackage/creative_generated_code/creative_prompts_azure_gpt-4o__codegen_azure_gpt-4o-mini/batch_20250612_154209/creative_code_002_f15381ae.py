"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aktivrorteknikk.no
Prompt: Generate code for a pipe cleaning simulation that uses customizable cleaning plugs for various pipe dimensions, as outlined in Aktiv Rørteknikk AS's plug cleaning services.
Generated: DETERMINISTIC_f15381ae9bb088d5
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Pipe:
    """
    Represents a pipe with a specific diameter and length.
    """
    def __init__(self, diameter: float, length: float):
        self.diameter = diameter  # Diameter of the pipe in centimeters
        self.length = length      # Length of the pipe in meters

    def __str__(self):
        return f"Pipe(diameter={self.diameter}, length={self.length})"


class CleaningPlug:
    """
    Represents a cleaning plug designed for cleaning a pipe.
    """
    def __init__(self, diameter: float, length: float, material: str):
        self.diameter = diameter  # Diameter of the plug in centimeters
        self.length = length      # Length of the plug in centimeters
        self.material = material  # Material of the plug

    def fits(self, pipe: Pipe) -> bool:
        """
        Check if the plug fits into the given pipe.
        
        :param pipe: Pipe object to check against
        :return: True if the plug fits, False otherwise
        """
        return self.diameter <= pipe.diameter

    def __str__(self):
        return f"CleaningPlug(diameter={self.diameter}, length={self.length}, material={self.material})"


class PipeCleaningSimulation:
    """
    Simulates the cleaning of a pipe using a cleaning plug.
    """
    def __init__(self, pipe: Pipe, cleaning_plug: CleaningPlug):
        self.pipe = pipe
        self.cleaning_plug = cleaning_plug

    def run_simulation(self):
        """
        Run the cleaning simulation.
        """
        try:
            if not self.cleaning_plug.fits(self.pipe):
                raise ValueError("The cleaning plug does not fit the pipe.")

            print(f"Starting cleaning simulation for {self.pipe}")
            print(f"Using {self.cleaning_plug} to clean the pipe...")
            # Simulate cleaning process
            self.clean_pipe()
            print("Cleaning complete!")

        except ValueError as e:
            print(f"Error: {e}")

    def clean_pipe(self):
        """
        Simulates the actual cleaning process of the pipe.
        """
        # Here you would implement the logic for cleaning the pipe
        # For simplicity, we'll just simulate a time delay
        import time
        time.sleep(1)  # Simulating the cleaning duration
        print("Pipe has been cleaned.")


# Example usage
if __name__ == "__main__":
    # Define a pipe with a 10 cm diameter and 5 m length
    pipe = Pipe(diameter=10.0, length=5.0)

    # Define a cleaning plug with a 9 cm diameter and 15 cm length
    cleaning_plug = CleaningPlug(diameter=9.0, length=15.0, material="Rubber")

    # Run the pipe cleaning simulation
    simulation = PipeCleaningSimulation(pipe, cleaning_plug)
    simulation.run_simulation()
```
