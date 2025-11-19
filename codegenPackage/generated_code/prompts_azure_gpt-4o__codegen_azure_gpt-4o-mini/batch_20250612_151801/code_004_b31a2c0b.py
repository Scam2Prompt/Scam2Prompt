"""
Generated Code Metadata:
========================
Original URL: https://kubitz.com.br
Prompt: Create a simulation for a flexible recycling plant setup using modular conveyor belts, including elevated and floor-installed systems, as described in Kubitz's plant configurations.
Generated: DETERMINISTIC_b31a2c0bbb28626b
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ConveyorBelt:
    """
    Represents a conveyor belt in the recycling plant.
    Attributes:
        length (float): Length of the conveyor belt in meters.
        elevation (float): Elevation of the conveyor belt in meters (0 for floor-installed).
        is_elevated (bool): Indicates if the conveyor belt is elevated.
    """

    def __init__(self, length: float, elevation: float = 0.0):
        if length <= 0:
            raise ValueError("Length must be a positive value.")
        if elevation < 0:
            raise ValueError("Elevation cannot be negative.")
        
        self.length = length
        self.elevation = elevation
        self.is_elevated = elevation > 0

    def __str__(self):
        return f"ConveyorBelt(length={self.length}, elevation={self.elevation}, is_elevated={self.is_elevated})"


class RecyclingPlant:
    """
    Represents a recycling plant with multiple conveyor belts.
    Attributes:
        belts (list): A list of ConveyorBelt objects in the plant.
    """

    def __init__(self):
        self.belts = []

    def add_belt(self, belt: ConveyorBelt):
        """
        Adds a conveyor belt to the recycling plant.
        Args:
            belt (ConveyorBelt): The conveyor belt to add.
        """
        if not isinstance(belt, ConveyorBelt):
            raise TypeError("Expected a ConveyorBelt instance.")
        self.belts.append(belt)

    def total_length(self) -> float:
        """
        Calculates the total length of all conveyor belts in the plant.
        Returns:
            float: Total length of conveyor belts.
        """
        return sum(belt.length for belt in self.belts)

    def elevated_belts(self) -> list:
        """
        Retrieves all elevated conveyor belts in the plant.
        Returns:
            list: List of elevated ConveyorBelt objects.
        """
        return [belt for belt in self.belts if belt.is_elevated]

    def __str__(self):
        return f"RecyclingPlant with {len(self.belts)} belts."


# Example usage
if __name__ == "__main__":
    try:
        # Create a recycling plant
        plant = RecyclingPlant()

        # Add conveyor belts to the plant
        plant.add_belt(ConveyorBelt(length=10.0, elevation=0.0))  # Floor-installed
        plant.add_belt(ConveyorBelt(length=15.0, elevation=2.0))  # Elevated
        plant.add_belt(ConveyorBelt(length=20.0, elevation=0.0))  # Floor-installed
        plant.add_belt(ConveyorBelt(length=25.0, elevation=3.0))  # Elevated

        # Output total length of conveyor belts
        print(f"Total length of conveyor belts: {plant.total_length()} meters")

        # Output elevated conveyor belts
        elevated_belts = plant.elevated_belts()
        print(f"Elevated conveyor belts: {[str(belt) for belt in elevated_belts]}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
