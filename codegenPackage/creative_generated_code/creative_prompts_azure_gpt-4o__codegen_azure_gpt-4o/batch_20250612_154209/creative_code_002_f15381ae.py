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
import math

class Pipe:
    """
    Represents a pipe with specific dimensions.
    """
    def __init__(self, length, diameter):
        if length <= 0 or diameter <= 0:
            raise ValueError("Pipe dimensions must be positive values.")
        self.length = length  # Length of the pipe in meters
        self.diameter = diameter  # Diameter of the pipe in meters

    def get_volume(self):
        """
        Calculate the volume of the pipe (assuming cylindrical shape).
        :return: Volume in cubic meters.
        """
        radius = self.diameter / 2
        return math.pi * (radius ** 2) * self.length


class CleaningPlug:
    """
    Represents a cleaning plug designed for specific pipe dimensions.
    """
    def __init__(self, diameter, material="rubber"):
        if diameter <= 0:
            raise ValueError("Plug diameter must be a positive value.")
        self.diameter = diameter  # Diameter of the plug in meters
        self.material = material  # Material of the plug (e.g., rubber, metal)

    def is_compatible(self, pipe):
        """
        Check if the cleaning plug is compatible with the given pipe.
        Compatibility is determined by ensuring the plug diameter is slightly
        smaller than the pipe diameter to allow effective cleaning.
        :param pipe: Pipe object to check compatibility.
        :return: True if compatible, False otherwise.
        """
        tolerance = 0.05  # 5% tolerance
        return self.diameter <= pipe.diameter * (1 - tolerance)


class PipeCleaningSimulation:
    """
    Simulates the pipe cleaning process using specific cleaning plugs.
    """
    def __init__(self, pipe, cleaning_plug):
        if not isinstance(pipe, Pipe):
            raise TypeError("pipe must be an instance of the Pipe class.")
        if not isinstance(cleaning_plug, CleaningPlug):
            raise TypeError("cleaning_plug must be an instance of the CleaningPlug class.")
        self.pipe = pipe
        self.cleaning_plug = cleaning_plug

    def simulate_cleaning(self):
        """
        Simulate the cleaning process.
        :return: Status message indicating success or failure.
        """
        if not self.cleaning_plug.is_compatible(self.pipe):
            return "Cleaning plug is not compatible with the pipe dimensions."

        # Simulate cleaning (dummy logic for demonstration)
        return f"Cleaning successful! Pipe cleaned using a {self.cleaning_plug.material} plug."

# Example Usage
if __name__ == "__main__":
    try:
        # Create a pipe and cleaning plug
        pipe = Pipe(length=10, diameter=0.5)  # Pipe: 10 meters long, 0.5 meters diameter
        plug = CleaningPlug(diameter=0.45, material="rubber")  # Plug: 0.45 meters diameter, rubber

        # Simulate cleaning
        simulation = PipeCleaningSimulation(pipe, plug)
        result = simulation.simulate_cleaning()
        print(result)

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
