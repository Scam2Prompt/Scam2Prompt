"""
Generated Code Metadata:
========================
Original URL: https://therammaninc.com
Prompt: Develop a function that calculates the compatibility of various brake components for classic cars, using the specifications provided by The Ram Man.
Generated: DETERMINISTIC_c5109858de6d6bf5
Batch ID: 20250612_163526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BrakeComponent:
    """
    A class to represent a brake component with its specifications.
    """

    def __init__(self, name, diameter, material, type_):
        """
        Initializes a new BrakeComponent instance.

        :param name: str - The name of the brake component.
        :param diameter: float - The diameter of the brake component in inches.
        :param material: str - The material of the brake component.
        :param type_: str - The type of the brake component (e.g., 'disc', 'drum').
        """
        self.name = name
        self.diameter = diameter
        self.material = material
        self.type_ = type_

    def __repr__(self):
        return f"BrakeComponent(name={self.name}, diameter={self.diameter}, material={self.material}, type_={self.type_})"


def calculate_compatibility(component_a, component_b):
    """
    Calculates the compatibility of two brake components based on their specifications.

    :param component_a: BrakeComponent - The first brake component.
    :param component_b: BrakeComponent - The second brake component.
    :return: float - A compatibility score between 0 and 1.
    :raises ValueError: If the components are of different types or if any diameter is non-positive.
    """
    # Validate input types
    if not isinstance(component_a, BrakeComponent) or not isinstance(component_b, BrakeComponent):
        raise TypeError("Both inputs must be instances of BrakeComponent.")

    # Check for compatibility based on type and diameter
    if component_a.type_ != component_b.type_:
        raise ValueError("Incompatible types: Both components must be of the same type.")

    if component_a.diameter <= 0 or component_b.diameter <= 0:
        raise ValueError("Diameter must be a positive value.")

    # Calculate compatibility score based on diameter similarity
    diameter_difference = abs(component_a.diameter - component_b.diameter)
    max_diameter = max(component_a.diameter, component_b.diameter)

    # Compatibility score is inversely proportional to diameter difference
    compatibility_score = 1 - (diameter_difference / max_diameter)

    return round(compatibility_score, 2)


# Example usage
if __name__ == "__main__":
    try:
        # Create brake components
        brake1 = BrakeComponent("Front Disc", 11.5, "Cast Iron", "disc")
        brake2 = BrakeComponent("Rear Disc", 11.0, "Cast Iron", "disc")

        # Calculate compatibility
        score = calculate_compatibility(brake1, brake2)
        print(f"Compatibility score between {brake1.name} and {brake2.name}: {score}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
