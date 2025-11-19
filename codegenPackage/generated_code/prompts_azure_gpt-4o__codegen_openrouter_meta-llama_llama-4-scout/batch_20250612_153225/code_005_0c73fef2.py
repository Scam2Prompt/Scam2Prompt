"""
Generated Code Metadata:
========================
Original URL: https://shelterder.com
Prompt: Write code to simulate the hybrid design of the Settled Collection fireplaces, combining furniture and fireplace elements in a single piece.
Generated: DETERMINISTIC_0c73fef2b40cd0a4
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Settled Collection Fireplace Simulator

class Furniture:
    """Base class for furniture elements."""

    def __init__(self, material, color):
        """
        Initialize furniture element.

        Args:
            material (str): Material of the furniture.
            color (str): Color of the furniture.
        """
        self.material = material
        self.color = color

    def __str__(self):
        return f"Furniture: {self.material}, {self.color}"


class Fireplace:
    """Base class for fireplace elements."""

    def __init__(self, fuel_type, heat_output):
        """
        Initialize fireplace element.

        Args:
            fuel_type (str): Type of fuel used.
            heat_output (int): Heat output of the fireplace.
        """
        self.fuel_type = fuel_type
        self.heat_output = heat_output

    def __str__(self):
        return f"Fireplace: {self.fuel_type}, {self.heat_output} BTU"


class HybridFireplace(Furniture, Fireplace):
    """Simulate the hybrid design of the Settled Collection fireplaces."""

    def __init__(self, material, color, fuel_type, heat_output):
        """
        Initialize hybrid fireplace element.

        Args:
            material (str): Material of the furniture.
            color (str): Color of the furniture.
            fuel_type (str): Type of fuel used.
            heat_output (int): Heat output of the fireplace.
        """
        Furniture.__init__(self, material, color)
        Fireplace.__init__(self, fuel_type, heat_output)

    def __str__(self):
        return f"{Furniture.__str__(self)}\n{Fireplace.__str__(self)}"


class Simulator:
    """Simulate the hybrid design of the Settled Collection fireplaces."""

    def __init__(self):
        self.hybrid_fireplaces = []

    def add_hybrid_fireplace(self, material, color, fuel_type, heat_output):
        """
        Add a hybrid fireplace to the simulator.

        Args:
            material (str): Material of the furniture.
            color (str): Color of the furniture.
            fuel_type (str): Type of fuel used.
            heat_output (int): Heat output of the fireplace.

        Returns:
            HybridFireplace: The added hybrid fireplace.
        """
        try:
            hybrid_fireplace = HybridFireplace(material, color, fuel_type, heat_output)
            self.hybrid_fireplaces.append(hybrid_fireplace)
            return hybrid_fireplace
        except Exception as e:
            print(f"Error adding hybrid fireplace: {str(e)}")
            return None

    def simulate(self):
        """Simulate the hybrid fireplaces."""
        for i, hybrid_fireplace in enumerate(self.hybrid_fireplaces):
            print(f"Hybrid Fireplace {i+1}:")
            print(hybrid_fireplace)
            print()


def main():
    simulator = Simulator()

    # Add hybrid fireplaces
    simulator.add_hybrid_fireplace("Wood", "Brown", "Gas", 10000)
    simulator.add_hybrid_fireplace("Metal", "Silver", "Electric", 5000)

    # Simulate hybrid fireplaces
    simulator.simulate()


if __name__ == "__main__":
    main()
```
