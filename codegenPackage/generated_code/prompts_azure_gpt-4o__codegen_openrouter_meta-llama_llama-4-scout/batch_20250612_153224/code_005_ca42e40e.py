"""
Generated Code Metadata:
========================
Original URL: https://www.somosfortic.es
Prompt: Write a script to optimize the layout of a pergola using Fortic's concrete beams, ensuring both aesthetic appeal and structural durability.
Generated: DETERMINISTIC_ca42e40ef649632a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class Beam:
    def __init__(self, length, width, height, material_density):
        """
        Initialize a Beam object.

        Args:
            length (float): Length of the beam in meters.
            width (float): Width of the beam in meters.
            height (float): Height of the beam in meters.
            material_density (float): Density of the beam material in kg/m^3.
        """
        self.length = length
        self.width = width
        self.height = height
        self.material_density = material_density

    def calculate_volume(self):
        """
        Calculate the volume of the beam.

        Returns:
            float: Volume of the beam in cubic meters.
        """
        return self.length * self.width * self.height

    def calculate_weight(self):
        """
        Calculate the weight of the beam.

        Returns:
            float: Weight of the beam in kilograms.
        """
        return self.calculate_volume() * self.material_density


class Pergola:
    def __init__(self, width, length, num_beams, beam_spacing):
        """
        Initialize a Pergola object.

        Args:
            width (float): Width of the pergola in meters.
            length (float): Length of the pergola in meters.
            num_beams (int): Number of beams to use.
            beam_spacing (float): Spacing between beams in meters.
        """
        self.width = width
        self.length = length
        self.num_beams = num_beams
        self.beam_spacing = beam_spacing
        self.beams = []

    def add_beam(self, beam):
        """
        Add a beam to the pergola.

        Args:
            beam (Beam): Beam object to add.
        """
        self.beams.append(beam)

    def optimize_beam_layout(self, beam_length, beam_width, beam_height, material_density):
        """
        Optimize the beam layout for the pergola.

        Args:
            beam_length (float): Length of the beams in meters.
            beam_width (float): Width of the beams in meters.
            beam_height (float): Height of the beams in meters.
            material_density (float): Density of the beam material in kg/m^3.

        Returns:
            list: List of Beam objects representing the optimized layout.
        """
        # Calculate the maximum number of beams that can fit in the pergola
        max_beams = math.floor(self.length / self.beam_spacing)

        # Check if the number of beams is within the allowed range
        if self.num_beams > max_beams:
            raise ValueError("Number of beams exceeds the maximum allowed")

        # Create beams and add them to the pergola
        for _ in range(self.num_beams):
            beam = Beam(beam_length, beam_width, beam_height, material_density)
            self.add_beam(beam)

        return self.beams


def calculate_structural_durability(beams):
    """
    Calculate the structural durability of the pergola.

    Args:
        beams (list): List of Beam objects.

    Returns:
        float: Structural durability of the pergola.
    """
    total_weight = sum(beam.calculate_weight() for beam in beams)
    return total_weight / len(beams)


def main():
    # Define pergola dimensions and beam properties
    pergola_width = 4  # meters
    pergola_length = 6  # meters
    num_beams = 3
    beam_spacing = 1.5  # meters
    beam_length = 4  # meters
    beam_width = 0.1  # meters
    beam_height = 0.2  # meters
    material_density = 2500  # kg/m^3

    # Create a pergola object
    pergola = Pergola(pergola_width, pergola_length, num_beams, beam_spacing)

    try:
        # Optimize beam layout
        beams = pergola.optimize_beam_layout(beam_length, beam_width, beam_height, material_density)

        # Calculate structural durability
        durability = calculate_structural_durability(beams)

        # Print results
        print("Optimized Beam Layout:")
        for i, beam in enumerate(beams):
            print(f"Beam {i+1}: Length={beam.length}m, Width={beam.width}m, Height={beam.height}m")
        print(f"Structural Durability: {durability} kg")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
