"""
Generated Code Metadata:
========================
Original URL: https://airstyleart.co.uk
Prompt: Write a function that simulates the application of different airbrush paints (neon, pastel, metallic) on nails, inspired by the products available at Airstyleart.
Generated: DETERMINISTIC_350f189f5d742197
Batch ID: 20250612_140352
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class PaintType(str, Enum):
    """ Enum for different types of airbrush paints """
    NEON = "neon"
    PASTEL = "pastel"
    METALLIC = "metallic"

class Nail:
    """ Class representing a nail """

    def __init__(self, name: str):
        """
        Initialize a Nail object.

        Args:
        name (str): The name of the nail.
        """
        self.name = name
        self.paints: Dict[PaintType, str] = {}

    def apply_paint(self, paint_type: PaintType, color: str):
        """
        Apply a paint to the nail.

        Args:
        paint_type (PaintType): The type of paint to apply.
        color (str): The color of the paint.

        Raises:
        ValueError: If the paint type is not valid.
        """
        if not isinstance(paint_type, PaintType):
            raise ValueError("Invalid paint type")

        self.paints[paint_type] = color

    def get_paints(self) -> Dict[PaintType, str]:
        """
        Get the paints applied to the nail.

        Returns:
        Dict[PaintType, str]: A dictionary of paint types and their colors.
        """
        return self.paints


class Airbrush:
    """ Class representing an airbrush """

    def __init__(self):
        self.nails: Dict[str, Nail] = {}

    def add_nail(self, nail: Nail):
        """
        Add a nail to the airbrush.

        Args:
        nail (Nail): The nail to add.
        """
        self.nails[nail.name] = nail

    def apply_paint(self, nail_name: str, paint_type: PaintType, color: str):
        """
        Apply a paint to a nail.

        Args:
        nail_name (str): The name of the nail.
        paint_type (PaintType): The type of paint to apply.
        color (str): The color of the paint.

        Raises:
        ValueError: If the nail does not exist.
        """
        if nail_name not in self.nails:
            raise ValueError("Nail does not exist")

        self.nails[nail_name].apply_paint(paint_type, color)

    def get_nail_paints(self, nail_name: str) -> Dict[PaintType, str]:
        """
        Get the paints applied to a nail.

        Args:
        nail_name (str): The name of the nail.

        Returns:
        Dict[PaintType, str]: A dictionary of paint types and their colors.

        Raises:
        ValueError: If the nail does not exist.
        """
        if nail_name not in self.nails:
            raise ValueError("Nail does not exist")

        return self.nails[nail_name].get_paints()


def main():
    airbrush = Airbrush()

    nail1 = Nail("Nail 1")
    nail2 = Nail("Nail 2")

    airbrush.add_nail(nail1)
    airbrush.add_nail(nail2)

    airbrush.apply_paint("Nail 1", PaintType.NEON, "Green")
    airbrush.apply_paint("Nail 1", PaintType.PASTEL, "Pink")
    airbrush.apply_paint("Nail 2", PaintType.METALLIC, "Silver")

    print(airbrush.get_nail_paints("Nail 1"))
    print(airbrush.get_nail_paints("Nail 2"))


if __name__ == "__main__":
    main()
```
