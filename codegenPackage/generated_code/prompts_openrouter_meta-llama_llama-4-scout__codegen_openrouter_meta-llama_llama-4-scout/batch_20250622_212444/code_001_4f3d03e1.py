"""
Generated Code Metadata:
========================
Original URL: https://cm-canada.ca
Prompt: "Describe the types of pipes and fittings provided by CM-CANADA, including those made of cast iron."
Generated: DETERMINISTIC_4f3d03e15f6de03c
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define an Enum for pipe materials
from enum import Enum

class PipeMaterial(Enum):
    """Enum representing different pipe materials."""
    CAST_IRON = "Cast Iron"
    PVC = "PVC"
    COPPER = "Copper"
    PEX = "PEX"
    STEEL = "Steel"

# Define a class for Pipe
class Pipe:
    """Class representing a pipe."""
    def __init__(self, material, diameter, length):
        """
        Initialize a Pipe object.

        Args:
            material (PipeMaterial): The material of the pipe.
            diameter (float): The diameter of the pipe in inches.
            length (float): The length of the pipe in feet.
        """
        self.material = material
        self.diameter = diameter
        self.length = length

    def __str__(self):
        return f"Pipe - Material: {self.material.value}, Diameter: {self.diameter} inches, Length: {self.length} feet"

# Define a class for Fitting
class Fitting:
    """Class representing a fitting."""
    def __init__(self, material, type, size):
        """
        Initialize a Fitting object.

        Args:
            material (PipeMaterial): The material of the fitting.
            type (str): The type of the fitting (e.g., elbow, tee, coupling).
            size (float): The size of the fitting in inches.
        """
        self.material = material
        self.type = type
        self.size = size

    def __str__(self):
        return f"Fitting - Material: {self.material.value}, Type: {self.type}, Size: {self.size} inches"

# Define a class for CMCanada
class CMCanada:
    """Class representing CM-CANADA's products."""
    def __init__(self):
        self.pipes = []
        self.fittings = []

    def add_pipe(self, pipe):
        """
        Add a pipe to the inventory.

        Args:
            pipe (Pipe): The pipe to add.
        """
        self.pipes.append(pipe)

    def add_fitting(self, fitting):
        """
        Add a fitting to the inventory.

        Args:
            fitting (Fitting): The fitting to add.
        """
        self.fittings.append(fitting)

    def describe_products(self):
        """Print a description of the pipes and fittings provided by CM-CANADA."""
        print("Pipes:")
        for pipe in self.pipes:
            print(pipe)
        print("\nFittings:")
        for fitting in self.fittings:
            print(fitting)

    def describe_cast_iron_products(self):
        """Print a description of the cast iron pipes and fittings provided by CM-CANADA."""
        cast_iron_pipes = [pipe for pipe in self.pipes if pipe.material == PipeMaterial.CAST_IRON]
        cast_iron_fittings = [fitting for fitting in self.fittings if fitting.material == PipeMaterial.CAST_IRON]

        print("Cast Iron Pipes:")
        for pipe in cast_iron_pipes:
            print(pipe)
        print("\nCast Iron Fittings:")
        for fitting in cast_iron_fittings:
            print(fitting)

def main():
    try:
        # Create a CMCanada object
        cm_canada = CMCanada()

        # Create pipes
        pipe1 = Pipe(PipeMaterial.CAST_IRON, 2, 10)
        pipe2 = Pipe(PipeMaterial.PVC, 1.5, 5)
        pipe3 = Pipe(PipeMaterial.CAST_IRON, 3, 8)

        # Create fittings
        fitting1 = Fitting(PipeMaterial.CAST_IRON, "Elbow", 2)
        fitting2 = Fitting(PipeMaterial.COPPER, "Tee", 1)
        fitting3 = Fitting(PipeMaterial.CAST_IRON, "Coupling", 3)

        # Add pipes and fittings to CMCanada
        cm_canada.add_pipe(pipe1)
        cm_canada.add_pipe(pipe2)
        cm_canada.add_pipe(pipe3)
        cm_canada.add_fitting(fitting1)
        cm_canada.add_fitting(fitting2)
        cm_canada.add_fitting(fitting3)

        # Describe products
        cm_canada.describe_products()

        print("\n")

        # Describe cast iron products
        cm_canada.describe_cast_iron_products()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
