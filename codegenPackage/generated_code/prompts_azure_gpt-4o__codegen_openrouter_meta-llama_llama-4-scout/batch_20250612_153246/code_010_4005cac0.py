"""
Generated Code Metadata:
========================
Original URL: https://spmepl.com
Prompt: Generate a Python program to simulate the operation of a chain-type pipe cutting machine, ensuring compatibility with manual pipe end heating torches as described on the SPM Equipment website.
Generated: DETERMINISTIC_4005cac0ef2bd4d3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pipe_cutting_machine.py

class Pipe:
    def __init__(self, diameter, material, thickness):
        """
        Initialize a Pipe object.

        Args:
            diameter (float): The diameter of the pipe in inches.
            material (str): The material of the pipe (e.g., steel, copper).
            thickness (float): The thickness of the pipe in inches.
        """
        self.diameter = diameter
        self.material = material
        self.thickness = thickness

    def __str__(self):
        return f"Pipe(diameter={self.diameter}, material='{self.material}', thickness={self.thickness})"


class CuttingMachine:
    def __init__(self, max_diameter, max_thickness):
        """
        Initialize a CuttingMachine object.

        Args:
            max_diameter (float): The maximum diameter of pipe the machine can cut.
            max_thickness (float): The maximum thickness of pipe the machine can cut.
        """
        self.max_diameter = max_diameter
        self.max_thickness = max_thickness
        self.pipe = None

    def load_pipe(self, pipe):
        """
        Load a pipe into the cutting machine.

        Args:
            pipe (Pipe): The pipe to load.

        Raises:
            ValueError: If the pipe's diameter or thickness exceeds the machine's limits.
        """
        if pipe.diameter > self.max_diameter or pipe.thickness > self.max_thickness:
            raise ValueError("Pipe exceeds machine's capacity")
        self.pipe = pipe

    def cut_pipe(self, heating_torch):
        """
        Cut the loaded pipe using a heating torch.

        Args:
            heating_torch (HeatingTorch): The heating torch to use.

        Raises:
            ValueError: If no pipe is loaded.
        """
        if not self.pipe:
            raise ValueError("No pipe loaded")
        heating_torch.apply_heat(self.pipe)
        # Simulate cutting operation
        print(f"Cutting {self.pipe} using {heating_torch}")


class HeatingTorch:
    def __init__(self, fuel_type, temperature):
        """
        Initialize a HeatingTorch object.

        Args:
            fuel_type (str): The type of fuel used by the torch (e.g., propane, acetylene).
            temperature (float): The temperature of the torch flame in degrees Fahrenheit.
        """
        self.fuel_type = fuel_type
        self.temperature = temperature

    def apply_heat(self, pipe):
        """
        Apply heat to a pipe.

        Args:
            pipe (Pipe): The pipe to heat.

        Raises:
            ValueError: If the pipe's material is incompatible with the torch's fuel type.
        """
        if pipe.material == "steel" and self.fuel_type == "propane":
            print(f"Applying heat to {pipe} using propane torch at {self.temperature}°F")
        elif pipe.material == "copper" and self.fuel_type == "acetylene":
            print(f"Applying heat to {pipe} using acetylene torch at {self.temperature}°F")
        else:
            raise ValueError("Incompatible fuel type and pipe material")

    def __str__(self):
        return f"HeatingTorch(fuel_type='{self.fuel_type}', temperature={self.temperature})"


def main():
    try:
        # Create a pipe
        pipe = Pipe(diameter=10.0, material="steel", thickness=0.5)
        print(pipe)

        # Create a cutting machine
        machine = CuttingMachine(max_diameter=12.0, max_thickness=1.0)

        # Load the pipe into the machine
        machine.load_pipe(pipe)

        # Create a heating torch
        torch = HeatingTorch(fuel_type="propane", temperature=2000.0)
        print(torch)

        # Cut the pipe using the heating torch
        machine.cut_pipe(torch)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
