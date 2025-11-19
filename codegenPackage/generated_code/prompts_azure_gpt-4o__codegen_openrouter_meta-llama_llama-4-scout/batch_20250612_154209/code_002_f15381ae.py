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
from enum import Enum
from typing import Dict

class PlugType(Enum):
    """ Enum for different types of cleaning plugs """
    SPHERIC = 1
    CYLINDRIC = 2

class Pipe:
    """ Represents a pipe with specific dimensions """
    def __init__(self, diameter: float, length: float):
        """
        Initializes a Pipe object.

        Args:
        - diameter (float): The diameter of the pipe.
        - length (float): The length of the pipe.
        """
        self.diameter = diameter
        self.length = length

class CleaningPlug:
    """ Represents a cleaning plug with specific dimensions and type """
    def __init__(self, plug_type: PlugType, diameter: float, material: str):
        """
        Initializes a CleaningPlug object.

        Args:
        - plug_type (PlugType): The type of the cleaning plug.
        - diameter (float): The diameter of the cleaning plug.
        - material (str): The material of the cleaning plug.
        """
        self.plug_type = plug_type
        self.diameter = diameter
        self.material = material

class PipeCleaningSimulation:
    """ Simulates the pipe cleaning process using customizable cleaning plugs """
    def __init__(self):
        self.plugs: Dict[str, CleaningPlug] = {}
        self.pipes: Dict[str, Pipe] = {}

    def add_plug(self, plug_name: str, plug: CleaningPlug):
        """
        Adds a cleaning plug to the simulation.

        Args:
        - plug_name (str): The name of the cleaning plug.
        - plug (CleaningPlug): The cleaning plug object.
        """
        self.plugs[plug_name] = plug

    def add_pipe(self, pipe_name: str, pipe: Pipe):
        """
        Adds a pipe to the simulation.

        Args:
        - pipe_name (str): The name of the pipe.
        - pipe (Pipe): The pipe object.
        """
        self.pipes[pipe_name] = pipe

    def simulate_cleaning(self, pipe_name: str, plug_name: str):
        """
        Simulates the pipe cleaning process.

        Args:
        - pipe_name (str): The name of the pipe to clean.
        - plug_name (str): The name of the cleaning plug to use.

        Returns:
        - bool: True if the cleaning was successful, False otherwise.
        """
        if pipe_name not in self.pipes:
            raise ValueError(f"Pipe '{pipe_name}' not found")

        if plug_name not in self.plugs:
            raise ValueError(f"Cleaning plug '{plug_name}' not found")

        pipe = self.pipes[pipe_name]
        plug = self.plugs[plug_name]

        # Check if the plug diameter is compatible with the pipe diameter
        if abs(pipe.diameter - plug.diameter) > 0.1:
            print(f"Warning: Cleaning plug diameter ({plug.diameter}) is not compatible with pipe diameter ({pipe.diameter})")

        # Simulate the cleaning process
        print(f"Simulating cleaning of pipe '{pipe_name}' using plug '{plug_name}'")
        print(f"Pipe dimensions: diameter={pipe.diameter}, length={pipe.length}")
        print(f"Plug dimensions: diameter={plug.diameter}, type={plug.plug_type}, material={plug.material}")
        return True

def main():
    simulation = PipeCleaningSimulation()

    # Create pipes
    pipe1 = Pipe(diameter=10.0, length=100.0)
    pipe2 = Pipe(diameter=20.0, length=50.0)

    # Create cleaning plugs
    plug1 = CleaningPlug(PlugType.SPHERIC, diameter=9.5, material="Rubber")
    plug2 = CleaningPlug(PlugType.CYLINDRIC, diameter=19.0, material="Polyurethane")

    # Add pipes and plugs to the simulation
    simulation.add_pipe("pipe1", pipe1)
    simulation.add_pipe("pipe2", pipe2)
    simulation.add_plug("plug1", plug1)
    simulation.add_plug("plug2", plug2)

    # Simulate cleaning
    simulation.simulate_cleaning("pipe1", "plug1")
    simulation.simulate_cleaning("pipe2", "plug2")

if __name__ == "__main__":
    main()
```
