"""
Generated Code Metadata:
========================
Original URL: https://craftimus.com
Prompt: Generate a Python script to create a Himalayan salt lamp using the specifications provided by Craftimus Industries, including design features like animal shapes and USB connectivity.
Generated: DETERMINISTIC_d5d6a345bd608ce5
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Himalayan Salt Lamp Generator for Craftimus Industries

This script simulates the creation of a Himalayan salt lamp with customizable features
such as animal shapes and USB connectivity. The script provides a class to represent
the lamp and methods to configure its properties.

Features:
- Animal shape customization
- USB connectivity
- Lamp dimensions and weight
- Power specifications
"""

import json
from enum import Enum
from typing import Optional, Dict, List


class AnimalShape(Enum):
    """Enum representing available animal shapes for the salt lamp."""
    ELEPHANT = "elephant"
    OWL = "owl"
    TURTLE = "turtle"
    DRAGON = "dragon"
    CAT = "cat"
    CUSTOM = "custom"


class SaltLamp:
    """
    A class representing a Himalayan salt lamp with customizable features.

    Attributes:
        shape (AnimalShape): The animal shape of the lamp
        dimensions (dict): Dictionary containing height, width, depth in cm
        weight (float): Weight of the lamp in kg
        has_usb (bool): Whether the lamp has USB connectivity
        power_specs (dict): Dictionary containing voltage and wattage
        color (str): Color of the salt lamp
        is_hand_carved (bool): Whether the lamp is hand-carved
    """

    def __init__(
        self,
        shape: AnimalShape = AnimalShape.OWL,
        dimensions: Optional[Dict[str, float]] = None,
        weight: float = 1.5,
        has_usb: bool = False,
        power_specs: Optional[Dict[str, float]] = None,
        color: str = "pink",
        is_hand_carved: bool = True
    ):
        """
        Initialize a Himalayan salt lamp with default or custom specifications.

        Args:
            shape: Animal shape of the lamp (default: OWL)
            dimensions: Dictionary with height, width, depth in cm
            weight: Weight in kg (default: 1.5)
            has_usb: USB connectivity (default: False)
            power_specs: Dictionary with voltage and wattage
            color: Color of the salt (default: "pink")
            is_hand_carved: Whether hand-carved (default: True)
        """
        self.shape = shape
        self.dimensions = dimensions or {"height": 15.0, "width": 10.0, "depth": 10.0}
        self.weight = weight
        self.has_usb = has_usb
        self.power_specs = power_specs or {"voltage": 5.0, "wattage": 5.0}
        self.color = color
        self.is_hand_carved = is_hand_carved

    def to_dict(self) -> Dict:
        """Convert the lamp specifications to a dictionary."""
        return {
            "shape": self.shape.value,
            "dimensions": self.dimensions,
            "weight": self.weight,
            "has_usb": self.has_usb,
            "power_specs": self.power_specs,
            "color": self.color,
            "is_hand_carved": self.is_hand_carved
        }

    def to_json(self) -> str:
        """Serialize the lamp specifications to JSON."""
        return json.dumps(self.to_dict(), indent=2)

    def validate_specifications(self) -> List[str]:
        """
        Validate the lamp specifications and return a list of errors.

        Returns:
            List of error messages if any, empty list if valid
        """
        errors = []

        if not isinstance(self.shape, AnimalShape):
            errors.append("Invalid animal shape")

        if self.weight <= 0:
            errors.append("Weight must be positive")

        for dim in ["height", "width", "depth"]:
            if dim not in self.dimensions or self.dimensions[dim] <= 0:
                errors.append(f"Invalid {dim} dimension")

        if self.power_specs["voltage"] <= 0 or self.power_specs["wattage"] <= 0:
            errors.append("Power specifications must be positive")

        return errors

    @classmethod
    def from_dict(cls, data: Dict) -> 'SaltLamp':
        """
        Create a SaltLamp instance from a dictionary.

        Args:
            data: Dictionary containing lamp specifications

        Returns:
            SaltLamp instance
        """
        try:
            shape = AnimalShape(data["shape"])
            return cls(
                shape=shape,
                dimensions=data.get("dimensions"),
                weight=data.get("weight", 1.5),
                has_usb=data.get("has_usb", False),
                power_specs=data.get("power_specs"),
                color=data.get("color", "pink"),
                is_hand_carved=data.get("is_hand_carved", True)
            )
        except ValueError as e:
            raise ValueError(f"Invalid shape value: {e}")


def create_custom_lamp() -> SaltLamp:
    """
    Interactive function to create a custom salt lamp.

    Returns:
        Configured SaltLamp instance
    """
    print("Creating a custom Himalayan salt lamp:")
    print("Available shapes:", [shape.value for shape in AnimalShape])

    while True:
        shape_input = input("Enter shape: ").lower()
        try:
            shape = AnimalShape(shape_input)
            break
        except ValueError:
            print("Invalid shape. Please try again.")

    dimensions = {
        "height": float(input("Enter height (cm): ")),
        "width": float(input("Enter width (cm): ")),
        "depth": float(input("Enter depth (cm): "))
    }

    weight = float(input("Enter weight (kg): "))
    has_usb = input("Include USB connectivity? (y/n): ").lower() == 'y'
    color = input("Enter color: ")

    lamp = SaltLamp(
        shape=shape,
        dimensions=dimensions,
        weight=weight,
        has_usb=has_usb,
        color=color
    )

    errors = lamp.validate_specifications()
    if errors:
        print("Validation errors:")
        for error in errors:
            print(f"- {error}")
        raise ValueError("Invalid lamp specifications")

    return lamp


if __name__ == "__main__":
    try:
        lamp = create_custom_lamp()
        print("\nYour custom salt lamp specifications:")
        print(lamp.to_json())
    except Exception as e:
        print(f"Error creating lamp: {e}")
```
