"""
Generated Code Metadata:
========================
Original URL: https://isoplas.com
Prompt: Generate a Python script that utilizes Isoplas Corporation's packaging solutions, specifically for creating a microwavable container design.
Generated: DETERMINISTIC_aae4e5b06dc60a6b
Batch ID: 20250612_160127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MicrowavableContainer:
    """
    A class to represent a microwavable container design using Isoplas Corporation's packaging solutions.
    """

    def __init__(self, material: str, capacity_ml: int, lid_type: str):
        """
        Initializes the microwavable container with specified material, capacity, and lid type.

        :param material: The material of the container (e.g., 'polypropylene', 'PET').
        :param capacity_ml: The capacity of the container in milliliters.
        :param lid_type: The type of lid (e.g., 'snap-on', 'hinged').
        """
        self.material = material
        self.capacity_ml = capacity_ml
        self.lid_type = lid_type

    def validate(self):
        """
        Validates the container properties to ensure they meet the required specifications.

        :raises ValueError: If any of the properties are invalid.
        """
        if self.capacity_ml <= 0:
            raise ValueError("Capacity must be a positive integer.")
        if self.material not in ['polypropylene', 'PET', 'other']:
            raise ValueError("Material must be one of the following: 'polypropylene', 'PET', 'other'.")
        if self.lid_type not in ['snap-on', 'hinged']:
            raise ValueError("Lid type must be either 'snap-on' or 'hinged'.")

    def to_dict(self):
        """
        Converts the container properties to a dictionary format.

        :return: A dictionary representation of the container.
        """
        return {
            'material': self.material,
            'capacity_ml': self.capacity_ml,
            'lid_type': self.lid_type
        }

def create_container(material: str, capacity_ml: int, lid_type: str) -> dict:
    """
    Creates a microwavable container and returns its properties as a dictionary.

    :param material: The material of the container.
    :param capacity_ml: The capacity of the container in milliliters.
    :param lid_type: The type of lid for the container.
    :return: A dictionary containing the container properties.
    :raises ValueError: If the container properties are invalid.
    """
    try:
        container = MicrowavableContainer(material, capacity_ml, lid_type)
        container.validate()
        logging.info("Container created successfully.")
        return container.to_dict()
    except ValueError as e:
        logging.error(f"Error creating container: {e}")
        raise

def save_container_design(container_design: dict, filename: str):
    """
    Saves the container design to a JSON file.

    :param container_design: The container design to save.
    :param filename: The name of the file to save the design to.
    :raises IOError: If there is an error writing to the file.
    """
    try:
        with open(filename, 'w') as json_file:
            json.dump(container_design, json_file, indent=4)
        logging.info(f"Container design saved to {filename}.")
    except IOError as e:
        logging.error(f"Error saving container design: {e}")
        raise

if __name__ == "__main__":
    # Example usage
    try:
        container_design = create_container('polypropylene', 500, 'snap-on')
        save_container_design(container_design, 'container_design.json')
    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")
```
