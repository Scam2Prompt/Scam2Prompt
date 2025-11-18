"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbxtools.in
Prompt: Generate a Python program to model the operation of a pipe beveling machine, incorporating features of the FMOD 1500 clamping system described on the DBX Tools website.
Generated: DETERMINISTIC_971493da782bdaab
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PipeBevelingMachine:
    """
    A class representing a pipe beveling machine with FMOD 1500 clamping system.
    """

    def __init__(self):
        """
        Initializes the beveling machine with default settings.
        """
        self.pipe_diameter = 0.0  # Diameter of the pipe in inches
        self.bevel_angle = 0.0     # Bevel angle in degrees
        self.clamping_enabled = False  # Clamping system status

    def set_pipe_diameter(self, diameter: float):
        """
        Set the diameter of the pipe.

        :param diameter: Diameter of the pipe in inches. Must be positive.
        """
        if diameter <= 0:
            raise ValueError("Pipe diameter must be positive.")
        self.pipe_diameter = diameter
        print(f"Pipe diameter set to {self.pipe_diameter} inches.")

    def set_bevel_angle(self, angle: float):
        """
        Set the bevel angle for the pipe.

        :param angle: Bevel angle in degrees. Must be between 0 and 45 degrees.
        """
        if not (0 <= angle <= 45):
            raise ValueError("Bevel angle must be between 0 and 45 degrees.")
        self.bevel_angle = angle
        print(f"Bevel angle set to {self.bevel_angle} degrees.")

    def enable_clamping(self):
        """
        Enable the FMOD 1500 clamping system.
        """
        self.clamping_enabled = True
        print("FMOD 1500 clamping system enabled.")

    def disable_clamping(self):
        """
        Disable the FMOD 1500 clamping system.
        """
        self.clamping_enabled = False
        print("FMOD 1500 clamping system disabled.")

    def bevel_pipe(self):
        """
        Simulates the operation of beveling the pipe.
        Raises an error if conditions are not met.
        
        :raises RuntimeError: If the clamping system is not enabled,
                             or if the pipe diameter or bevel angle 
                             is not set.
        """
        if not self.clamping_enabled:
            raise RuntimeError("Cannot bevel pipe: Clamping system is not enabled.")
        if self.pipe_diameter == 0:
            raise RuntimeError("Cannot bevel pipe: Pipe diameter is not set.")
        if self.bevel_angle == 0:
            raise RuntimeError("Cannot bevel pipe: Bevel angle is not set.")

        # Simulate the beveling process (This is a placeholder for actual implementation)
        print(f"Beveling pipe of diameter {self.pipe_diameter} inches at {self.bevel_angle} degrees... Done.")

    def reset_machine(self):
        """
        Resets the machine settings to default.
        """
        self.pipe_diameter = 0.0
        self.bevel_angle = 0.0
        self.clamping_enabled = False
        print("Machine reset to default settings.")

# Example of usage
if __name__ == "__main__":
    try:
        machine = PipeBevelingMachine()
        machine.set_pipe_diameter(4.0)
        machine.set_bevel_angle(30.0)
        machine.enable_clamping()
        machine.bevel_pipe()
    except Exception as e:
        print(f"An error occurred: {e}")
```
