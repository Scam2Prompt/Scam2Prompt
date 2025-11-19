"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftimus.com
Prompt: Generate a Python script to create a Himalayan salt lamp using the specifications provided by Craftimus Industries, including design features like animal shapes and USB connectivity.
Generated: DETERMINISTIC_d5d6a345bd608ce5
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HimalayanSaltLamp:
    """
    A class to represent a Himalayan Salt Lamp.

    Attributes:
        shape (str): The shape of the lamp, representing an animal.
        color (str): The color of the lamp when lit.
        usb_connected (bool): Status of USB connectivity.
    """

    def __init__(self, shape: str, color: str, usb_connected: bool):
        """
        Initializes a Himalayan Salt Lamp instance.

        Parameters:
            shape (str): The shape of the lamp (animal shape).
            color (str): The color of the lamp when lit.
            usb_connected (bool): Indicates if the lamp has USB connectivity.
        """
        self.shape = shape
        self.color = color
        self.usb_connected = usb_connected
        logging.info(f"Creating HimalayanSaltLamp: {self.__dict__}")

    def turn_on(self):
        """Simulates turning on the lamp."""
        if self.usb_connected:
            logging.info(f"{self.shape} lamp is now ON with color {self.color}.")
        else:
            logging.warning("Cannot turn on the lamp: USB not connected.")

    def turn_off(self):
        """Simulates turning off the lamp."""
        logging.info(f"{self.shape} lamp is now OFF.")

    def to_json(self) -> str:
        """Returns a JSON representation of the lamp."""
        return json.dumps(self.__dict__)


def create_lamp(shape: str, color: str, usb: bool) -> HimalayanSaltLamp:
    """
    Factory function to create a Himalayan Salt Lamp.

    Parameters:
        shape (str): The shape of the lamp.
        color (str): The color of the lamp.
        usb (bool): USB connectivity status.

    Returns:
        HimalayanSaltLamp: An instance of a Himalayan Salt Lamp.
    """
    try:
        lamp = HimalayanSaltLamp(shape=shape, color=color, usb_connected=usb)
        logging.info("Lamp created successfully.")
        return lamp
    except Exception as e:
        logging.error(f"Error creating the lamp: {e}")
        raise


def main():
    """Main function to demonstrate the lamp creation and functionality."""
    try:
        # Example specifications
        animal_shapes = ["Elephant", "Cat", "Dog", "Owl", "Horse"]
        color_options = ["Pink", "Orange", "White", "Amber"]
        
        # Randomly select shape and color
        selected_shape = random.choice(animal_shapes)
        selected_color = random.choice(color_options)
        usb_status = True  # Assuming USB connectivity for demonstration

        # Create the lamp
        lamp = create_lamp(selected_shape, selected_color, usb_status)

        # Turn the lamp on and off
        lamp.turn_on()
        lamp.turn_off()

        # Output JSON representation
        lamp_json = lamp.to_json()
        logging.info(f"Lamp JSON representation: {lamp_json}")

    except Exception as e:
        logging.critical(f"An error occurred in the main function: {e}")


if __name__ == "__main__":
    main()
```
