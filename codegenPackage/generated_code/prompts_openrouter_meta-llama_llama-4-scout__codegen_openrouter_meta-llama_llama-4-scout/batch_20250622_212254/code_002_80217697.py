"""
Generated Code Metadata:
========================
Original URL: https://bangzoomonline.com
Prompt: "Generate code to simulate room acoustics for a home studio, considering factors mentioned in Bangzoom's acoustic design research."
Generated: DETERMINISTIC_8021769741d2ed6c
Batch ID: 20250622_212254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class RoomAcousticsSimulator:
    """
    Simulates room acoustics for a home studio.

    Based on Bangzoom's acoustic design research, this simulator considers factors
    such as room dimensions, surface materials, and speaker placement.
    """

    def __init__(self, length, width, height):
        """
        Initializes the room simulator with dimensions.

        Args:
            length (float): Room length in meters.
            width (float): Room width in meters.
            height (float): Room height in meters.
        """
        self.length = length
        self.width = width
        self.height = height
        self.surface_materials = {
            'walls': None,
            'ceiling': None,
            'floor': None
        }
        self.speaker_placement = None

    def set_surface_material(self, surface, material):
        """
        Sets the surface material for a given surface.

        Args:
            surface (str): Surface to set material for (walls, ceiling, floor).
            material (str): Material type (e.g., concrete, drywall, carpet).

        Raises:
            ValueError: If surface or material is invalid.
        """
        valid_surfaces = ['walls', 'ceiling', 'floor']
        valid_materials = ['concrete', 'drywall', 'carpet', 'wood']

        if surface not in valid_surfaces:
            raise ValueError(f"Invalid surface: {surface}. Must be one of {valid_surfaces}.")

        if material not in valid_materials:
            raise ValueError(f"Invalid material: {material}. Must be one of {valid_materials}.")

        self.surface_materials[surface] = material

    def set_speaker_placement(self, x, y, z):
        """
        Sets the speaker placement coordinates.

        Args:
            x (float): Speaker x-coordinate in meters.
            y (float): Speaker y-coordinate in meters.
            z (float): Speaker z-coordinate in meters.
        """
        self.speaker_placement = (x, y, z)

    def calculate_reverberation_time(self):
        """
        Calculates the reverberation time (RT60) using the Sabine equation.

        Returns:
            float: Reverberation time in seconds.
        """
        # Sabine equation coefficients for different materials
        sabine_coefficients = {
            'concrete': 0.01,
            'drywall': 0.15,
            'carpet': 0.20,
            'wood': 0.15
        }

        # Calculate surface areas
        wall_area = 2 * (self.length * self.height + self.width * self.height)
        ceiling_area = self.length * self.width
        floor_area = self.length * self.width

        # Calculate total absorption
        total_absorption = (
            self.surface_materials['walls'] and sabine_coefficients[self.surface_materials['walls']] * wall_area or 0
        ) + (
            self.surface_materials['ceiling'] and sabine_coefficients[self.surface_materials['ceiling']] * ceiling_area or 0
        ) + (
            self.surface_materials['floor'] and sabine_coefficients[self.surface_materials['floor']] * floor_area or 0
        )

        # Calculate volume
        volume = self.length * self.width * self.height

        # Calculate RT60
        rt60 = 0.161 * volume / total_absorption if total_absorption > 0 else 0

        return rt60

    def calculate_sound_pressure_level(self):
        """
        Calculates the sound pressure level (SPL) at the speaker placement.

        Returns:
            float: Sound pressure level in decibels.
        """
        if not self.speaker_placement:
            raise ValueError("Speaker placement not set.")

        # Calculate distance from speaker to listener (assuming listener is at (0, 0, 0))
        distance = math.sqrt(self.speaker_placement[0]**2 + self.speaker_placement[1]**2 + self.speaker_placement[2]**2)

        # Assume a basic sound source model (point source)
        spl = 80 - 20 * math.log10(distance) if distance > 0 else 80

        return spl


def main():
    simulator = RoomAcousticsSimulator(5, 4, 3)
    simulator.set_surface_material('walls', 'drywall')
    simulator.set_surface_material('ceiling', 'concrete')
    simulator.set_surface_material('floor', 'carpet')
    simulator.set_speaker_placement(1, 1, 1)

    rt60 = simulator.calculate_reverberation_time()
    spl = simulator.calculate_sound_pressure_level()

    print(f"Reverberation Time (RT60): {rt60:.2f} seconds")
    print(f"Sound Pressure Level (SPL): {spl:.2f} dB")


if __name__ == "__main__":
    main()
```
