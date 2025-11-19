"""
Generated Code Metadata:
========================
Original URL: https://dbxtools.in
Prompt: Generate a Python program to model the operation of a pipe beveling machine, incorporating features of the FMOD 1500 clamping system described on the DBX Tools website.
Generated: DETERMINISTIC_971493da782bdaab
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pipe_beveling_machine.py

class Pipe:
    """Represents a pipe with a diameter and wall thickness."""

    def __init__(self, diameter: float, wall_thickness: float):
        """
        Initializes a Pipe object.

        Args:
            diameter (float): The diameter of the pipe.
            wall_thickness (float): The wall thickness of the pipe.

        Raises:
            ValueError: If diameter or wall_thickness is not positive.
        """
        if diameter <= 0 or wall_thickness <= 0:
            raise ValueError("Diameter and wall thickness must be positive.")
        self.diameter = diameter
        self.wall_thickness = wall_thickness


class ClampingSystem:
    """Simulates the FMOD 1500 clamping system."""

    def __init__(self, max_diameter: float, max_pressure: float):
        """
        Initializes a ClampingSystem object.

        Args:
            max_diameter (float): The maximum diameter the clamping system can handle.
            max_pressure (float): The maximum pressure the clamping system can apply.

        Raises:
            ValueError: If max_diameter or max_pressure is not positive.
        """
        if max_diameter <= 0 or max_pressure <= 0:
            raise ValueError("Max diameter and max pressure must be positive.")
        self.max_diameter = max_diameter
        self.max_pressure = max_pressure
        self.is_clamped = False
        self.pipe: Pipe | None = None

    def clamp_pipe(self, pipe: Pipe, pressure: float):
        """
        Clamps a pipe using the FMOD 1500 clamping system.

        Args:
            pipe (Pipe): The pipe to clamp.
            pressure (float): The pressure to apply.

        Raises:
            ValueError: If the pipe's diameter exceeds the max diameter or if the pressure exceeds the max pressure.
        """
        if pipe.diameter > self.max_diameter:
            raise ValueError("Pipe diameter exceeds the maximum diameter.")
        if pressure > self.max_pressure:
            raise ValueError("Pressure exceeds the maximum pressure.")
        self.pipe = pipe
        self.is_clamped = True
        print(f"Pipe clamped with pressure {pressure}.")

    def release_pipe(self):
        """Releases the clamped pipe."""
        if not self.is_clamped:
            print("No pipe is clamped.")
            return
        self.is_clamped = False
        self.pipe = None
        print("Pipe released.")


class BevelingMachine:
    """Simulates a pipe beveling machine with a clamping system."""

    def __init__(self, clamping_system: ClampingSystem):
        """
        Initializes a BevelingMachine object.

        Args:
            clamping_system (ClampingSystem): The clamping system to use.
        """
        self.clamping_system = clamping_system

    def bevel_pipe(self, angle: float, depth: float):
        """
        Bevels a clamped pipe.

        Args:
            angle (float): The bevel angle.
            depth (float): The bevel depth.

        Raises:
            ValueError: If no pipe is clamped.
        """
        if not self.clamping_system.is_clamped or self.clamping_system.pipe is None:
            raise ValueError("No pipe is clamped.")
        print(f"Beveling pipe with angle {angle} and depth {depth}.")


def main():
    try:
        # Create a pipe
        pipe = Pipe(diameter=10.0, wall_thickness=0.5)

        # Create a clamping system
        clamping_system = ClampingSystem(max_diameter=12.0, max_pressure=100.0)

        # Create a beveling machine
        beveling_machine = BevelingMachine(clamping_system)

        # Clamp the pipe
        clamping_system.clamp_pipe(pipe, pressure=50.0)

        # Bevel the pipe
        beveling_machine.bevel_pipe(angle=30.0, depth=0.2)

        # Release the pipe
        clamping_system.release_pipe()

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
