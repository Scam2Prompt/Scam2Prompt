"""
Generated Code Metadata:
========================
Original URL: https://neumayaa.com.ar
Prompt: "What are the differences between various types of tires for construction equipment, such as macizas/solidas and neumáticas?"
Generated: DETERMINISTIC_b3b3b7cd137854fd
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Tire Information System

class Tire:
    """Base class for construction equipment tires."""

    def __init__(self, tire_type, size, weight_capacity):
        """
        Initialize a tire object.

        Args:
            tire_type (str): Type of tire (e.g., maciza, solida, neumática).
            size (str): Size of the tire.
            weight_capacity (float): Weight capacity of the tire in kg.
        """
        self.tire_type = tire_type
        self.size = size
        self.weight_capacity = weight_capacity

    def __str__(self):
        return f"{self.tire_type} tire, size: {self.size}, weight capacity: {self.weight_capacity} kg"


class SolidTire(Tire):
    """Solid tire for construction equipment."""

    def __init__(self, size, weight_capacity, material):
        """
        Initialize a solid tire object.

        Args:
            size (str): Size of the tire.
            weight_capacity (float): Weight capacity of the tire in kg.
            material (str): Material used to make the tire (e.g., rubber, polyurethane).
        """
        super().__init__("Solid", size, weight_capacity)
        self.material = material

    def __str__(self):
        return super().__str__() + f", material: {self.material}"


class PneumaticTire(Tire):
    """Pneumatic tire for construction equipment."""

    def __init__(self, size, weight_capacity, air_pressure):
        """
        Initialize a pneumatic tire object.

        Args:
            size (str): Size of the tire.
            weight_capacity (float): Weight capacity of the tire in kg.
            air_pressure (float): Recommended air pressure in PSI.
        """
        super().__init__("Pneumatic", size, weight_capacity)
        self.air_pressure = air_pressure

    def __str__(self):
        return super().__str__() + f", air pressure: {self.air_pressure} PSI"


def compare_tires(tire1, tire2):
    """
    Compare two tires.

    Args:
        tire1 (Tire): First tire to compare.
        tire2 (Tire): Second tire to compare.

    Returns:
        dict: Dictionary containing the comparison results.
    """
    comparison_results = {
        "Tire 1": str(tire1),
        "Tire 2": str(tire2),
        "Weight Capacity Difference": tire1.weight_capacity - tire2.weight_capacity,
    }
    return comparison_results


def main():
    try:
        # Create solid tires
        solid_tire1 = SolidTire("10x20", 5000, "Rubber")
        solid_tire2 = SolidTire("12x24", 7000, "Polyurethane")

        # Create pneumatic tires
        pneumatic_tire1 = PneumaticTire("10x20", 4000, 80)
        pneumatic_tire2 = PneumaticTire("12x24", 6000, 100)

        # Compare tires
        solid_comparison = compare_tires(solid_tire1, solid_tire2)
        pneumatic_comparison = compare_tires(pneumatic_tire1, pneumatic_tire2)

        # Print comparison results
        print("Solid Tire Comparison:")
        for key, value in solid_comparison.items():
            print(f"{key}: {value}")

        print("\nPneumatic Tire Comparison:")
        for key, value in pneumatic_comparison.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
