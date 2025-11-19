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
"""
Script to simulate the creation of a Himalayan salt lamp with specific design features
like animal shapes and USB connectivity. This script is a representation of the
steps required in software for a manufacturing workflow at Craftimus Industries.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import json

class HimalayanSaltLamp:
    """
    A class to represent a Himalayan salt lamp with customizable features.
    """
    def __init__(self, shape: str, usb_connectivity: bool, dimensions: dict):
        """
        Initialize the salt lamp with design specifications.

        :param shape: (str) Shape of the lamp (e.g., "cat", "dog", "owl").
        :param usb_connectivity: (bool) Whether the lamp supports USB connectivity.
        :param dimensions: (dict) Dimensions of the lamp (e.g., {"width": 10, "height": 15, "depth": 8}).
        """
        self.shape = shape
        self.usb_connectivity = usb_connectivity
        self.dimensions = dimensions

    def validate_dimensions(self):
        """
        Validate that dimensions are positive numbers.

        :return: (bool) True if dimensions are valid, False otherwise.
        """
        for key, value in self.dimensions.items():
            if value <= 0:
                raise ValueError(f"Invalid dimension '{key}' with value '{value}'. Must be positive.")
        return True

    def get_specifications(self):
        """
        Provide the specifications of the salt lamp.

        :return: (dict) Specifications of the salt lamp.
        """
        return {
            "shape": self.shape,
            "usb_connectivity": self.usb_connectivity,
            "dimensions": self.dimensions
        }


def create_salt_lamp():
    """
    Function to create a Himalayan salt lamp based on user input.

    :return: None
    """
    try:
        # Gather user input for lamp specifications
        shape = input("Enter the shape of the salt lamp (e.g., 'cat', 'dog', 'owl'): ").strip().lower()
        usb_connectivity = input("Does the lamp support USB connectivity? (yes/no): ").strip().lower() == 'yes'
        
        # Gather dimensions from user
        print("Enter the dimensions of the salt lamp:")
        width = float(input("Width (in cm): "))
        height = float(input("Height (in cm): "))
        depth = float(input("Depth (in cm): "))

        # Create dimensions dictionary
        dimensions = {"width": width, "height": height, "depth": depth}
        
        # Instantiate the salt lamp
        salt_lamp = HimalayanSaltLamp(shape, usb_connectivity, dimensions)
        
        # Validate dimensions
        salt_lamp.validate_dimensions()

        # Display specifications
        specifications = salt_lamp.get_specifications()
        print("\nSalt Lamp Specifications:")
        print(json.dumps(specifications, indent=4))
        
        print("\nSalt lamp successfully created!")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    print("Welcome to Craftimus Industries Himalayan Salt Lamp Maker!")
    create_salt_lamp()
```
