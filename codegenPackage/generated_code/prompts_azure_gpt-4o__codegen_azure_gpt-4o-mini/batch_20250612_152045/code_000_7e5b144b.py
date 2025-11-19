"""
Generated Code Metadata:
========================
Original URL: https://www.vircomem.ro
Prompt: Write Python code to simulate the functionality of industrial brushes used for mechanical cleaning, incorporating customizable dimensions and characteristics as described on the VIRCOMEM website.
Generated: DETERMINISTIC_7e5b144b4d9c92e4
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class IndustrialBrush:
    """
    A class to represent an industrial brush used for mechanical cleaning.

    Attributes:
        diameter (float): The diameter of the brush in centimeters.
        length (float): The length of the brush bristles in centimeters.
        material (str): The material of the brush bristles.
        stiffness (int): The stiffness of the brush on a scale from 1 to 10.
    """

    def __init__(self, diameter: float, length: float, material: str, stiffness: int):
        """
        Initializes an IndustrialBrush instance with specified dimensions and characteristics.

        Args:
            diameter (float): The diameter of the brush.
            length (float): The length of the bristles.
            material (str): The material of the bristles.
            stiffness (int): The stiffness of the brush.

        Raises:
            ValueError: If any of the parameters are invalid.
        """
        if diameter <= 0:
            raise ValueError("Diameter must be a positive value.")
        if length <= 0:
            raise ValueError("Length must be a positive value.")
        if stiffness < 1 or stiffness > 10:
            raise ValueError("Stiffness must be between 1 and 10.")

        self.diameter = diameter
        self.length = length
        self.material = material
        self.stiffness = stiffness

    def clean_surface(self, surface_type: str):
        """
        Simulates the cleaning action of the brush on a specified surface type.

        Args:
            surface_type (str): The type of surface to clean (e.g., 'metal', 'wood', 'plastic').

        Returns:
            str: A message indicating the cleaning action performed.

        Raises:
            ValueError: If the surface type is not recognized.
        """
        valid_surfaces = ['metal', 'wood', 'plastic']
        if surface_type not in valid_surfaces:
            raise ValueError(f"Surface type '{surface_type}' is not recognized. Valid options are: {valid_surfaces}")

        return f"Cleaning {surface_type} surface with a {self.diameter}cm {self.material} brush of {self.length}cm bristle length and stiffness {self.stiffness}."

    def __str__(self):
        """
        Returns a string representation of the IndustrialBrush instance.

        Returns:
            str: Description of the brush.
        """
        return (f"Industrial Brush - Diameter: {self.diameter}cm, "
                f"Bristle Length: {self.length}cm, Material: {self.material}, "
                f"Stiffness: {self.stiffness}/10")

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of IndustrialBrush
        brush = IndustrialBrush(diameter=10.0, length=5.0, material='Nylon', stiffness=7)

        # Print brush details
        print(brush)

        # Simulate cleaning a surface
        result = brush.clean_surface('metal')
        print(result)

    except ValueError as e:
        print(f"Error: {e}")
```
