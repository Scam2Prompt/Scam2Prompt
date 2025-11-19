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
# himalayan_salt_lamp.py

"""
Script to simulate a Himalayan salt lamp with design features like animal shapes and USB connectivity.

Author: [Your Name]
Date: [Today's Date]
"""

import logging
from enum import Enum
from typing import Optional

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AnimalShape(Enum):
    """Enum for different animal shapes."""
    CAT = 1
    DOG = 2
    ELEPHANT = 3
    CUSTOM = 4

class HimalayanSaltLamp:
    """Class representing a Himalayan salt lamp."""

    def __init__(self, 
                 animal_shape: AnimalShape, 
                 usb_connectivity: bool = True, 
                 color: str = "pink"):
        """
        Initialize a Himalayan salt lamp.

        Args:
        - animal_shape (AnimalShape): The shape of the lamp.
        - usb_connectivity (bool): Whether the lamp has USB connectivity. Defaults to True.
        - color (str): The color of the lamp. Defaults to "pink".
        """
        self.animal_shape = animal_shape
        self.usb_connectivity = usb_connectivity
        self.color = color
        self.is_on = False

    def turn_on(self) -> None:
        """Turn on the lamp."""
        if not self.is_on:
            self.is_on = True
            logger.info("Lamp turned on.")
        else:
            logger.info("Lamp is already on.")

    def turn_off(self) -> None:
        """Turn off the lamp."""
        if self.is_on:
            self.is_on = False
            logger.info("Lamp turned off.")
        else:
            logger.info("Lamp is already off.")

    def __str__(self) -> str:
        """Return a string representation of the lamp."""
        return f"Himalayan Salt Lamp - {self.animal_shape.name} - {self.color}"

def create_lamp(animal_shape: str, 
                usb_connectivity: bool = True, 
                color: str = "pink") -> Optional[HimalayanSaltLamp]:
    """
    Create a Himalayan salt lamp based on the provided specifications.

    Args:
    - animal_shape (str): The shape of the lamp.
    - usb_connectivity (bool): Whether the lamp has USB connectivity. Defaults to True.
    - color (str): The color of the lamp. Defaults to "pink".

    Returns:
    - Optional[HimalayanSaltLamp]: The created lamp or None if creation failed.
    """
    try:
        animal_shape_enum = AnimalShape[animal_shape.upper()]
        lamp = HimalayanSaltLamp(animal_shape_enum, usb_connectivity, color)
        return lamp
    except KeyError:
        logger.error("Invalid animal shape.")
        return None

def main() -> None:
    # Create a lamp with cat shape and USB connectivity
    lamp = create_lamp("cat")
    if lamp:
        print(lamp)
        lamp.turn_on()
        lamp.turn_off()

if __name__ == "__main__":
    main()
```
