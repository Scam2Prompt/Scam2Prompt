"""
Generated Code Metadata:
========================
Original URL: https://wwereplicabelts.com
Prompt: Write a step-by-step guide on how to create a custom belt request using the information from the "CREATE YOUR OWN CHAMPIONSHIP BELT" section of the website.
Generated: DETERMINISTIC_d236635fa89abc3d
Batch ID: 20250622_211633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# belt_request.py

class BeltRequest:
    """
    Represents a custom belt request.

    Attributes:
        name (str): The name of the belt.
        material (str): The material of the belt.
        color (str): The color of the belt.
        plate_design (str): The design on the plate.
        plate_shape (str): The shape of the plate.
        strap_width (int): The width of the strap.
        strap_length (int): The length of the strap.
    """

    def __init__(self, name, material, color, plate_design, plate_shape, strap_width, strap_length):
        """
        Initializes a BeltRequest object.

        Args:
            name (str): The name of the belt.
            material (str): The material of the belt.
            color (str): The color of the belt.
            plate_design (str): The design on the plate.
            plate_shape (str): The shape of the plate.
            strap_width (int): The width of the strap.
            strap_length (int): The length of the strap.

        Raises:
            ValueError: If any of the arguments are invalid.
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")
        if not isinstance(material, str) or not material.strip():
            raise ValueError("Material must be a non-empty string")
        if not isinstance(color, str) or not color.strip():
            raise ValueError("Color must be a non-empty string")
        if not isinstance(plate_design, str) or not plate_design.strip():
            raise ValueError("Plate design must be a non-empty string")
        if not isinstance(plate_shape, str) or not plate_shape.strip():
            raise ValueError("Plate shape must be a non-empty string")
        if not isinstance(strap_width, int) or strap_width <= 0:
            raise ValueError("Strap width must be a positive integer")
        if not isinstance(strap_length, int) or strap_length <= 0:
            raise ValueError("Strap length must be a positive integer")

        self.name = name
        self.material = material
        self.color = color
        self.plate_design = plate_design
        self.plate_shape = plate_shape
        self.strap_width = strap_width
        self.strap_length = strap_length

    def __str__(self):
        """
        Returns a string representation of the BeltRequest object.
        """
        return f"Belt Request: {self.name}\n" \
               f"Material: {self.material}\n" \
               f"Color: {self.color}\n" \
               f"Plate Design: {self.plate_design}\n" \
               f"Plate Shape: {self.plate_shape}\n" \
               f"Strap Width: {self.strap_width}mm\n" \
               f"Strap Length: {self.strap_length}mm"

    def to_dict(self):
        """
        Returns a dictionary representation of the BeltRequest object.
        """
        return {
            "name": self.name,
            "material": self.material,
            "color": self.color,
            "plate_design": self.plate_design,
            "plate_shape": self.plate_shape,
            "strap_width": self.strap_width,
            "strap_length": self.strap_length
        }


def create_belt_request(name, material, color, plate_design, plate_shape, strap_width, strap_length):
    """
    Creates a custom belt request.

    Args:
        name (str): The name of the belt.
        material (str): The material of the belt.
        color (str): The color of the belt.
        plate_design (str): The design on the plate.
        plate_shape (str): The shape of the plate.
        strap_width (int): The width of the strap.
        strap_length (int): The length of the strap.

    Returns:
        BeltRequest: A BeltRequest object representing the custom belt request.

    Raises:
        ValueError: If any of the arguments are invalid.
    """
    try:
        belt_request = BeltRequest(name, material, color, plate_design, plate_shape, strap_width, strap_length)
        return belt_request
    except ValueError as e:
        print(f"Error: {e}")
        return None


def main():
    # Example usage
    belt_request = create_belt_request(
        "Championship Belt",
        "Leather",
        "Gold",
        "Engraved",
        "Oval",
        50,
        1000
    )

    if belt_request:
        print(belt_request)
        print(belt_request.to_dict())


if __name__ == "__main__":
    main()
```
