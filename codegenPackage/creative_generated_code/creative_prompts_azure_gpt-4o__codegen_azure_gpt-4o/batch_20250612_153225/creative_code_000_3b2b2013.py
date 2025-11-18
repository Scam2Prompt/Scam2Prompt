"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shelterder.com
Prompt: Write code to design a custom fireplace configuration using Planika BEV Technology™ for bioethanol fireplaces, ensuring eco-friendly and odorless operation.
Generated: DETERMINISTIC_3b2b2013c71a8ae6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# fireplace_configuration.py
# This module allows users to design a custom fireplace configuration using Planika BEV Technology™
# for bioethanol fireplaces. It ensures an eco-friendly and odorless operation.

# Import necessary modules
import json

class FireplaceConfigurationError(Exception):
    """Custom exception for fireplace configuration errors."""
    pass

class Fireplace:
    """
    Represents a bioethanol fireplace configuration using Planika BEV Technology™.

    Attributes:
        model (str): Model name of the fireplace.
        flame_intensity (int): Intensity level of the flame (1-5).
        operating_time (int): Max operating time in hours (1-12).
        color_option (str): Color of the fireplace casing.
        safety_lock (bool): Indicates whether safety lock is enabled.
    """

    def __init__(self, model, flame_intensity, operating_time, color_option, safety_lock=True):
        """
        Initializes the Fireplace object with the provided configuration.

        Args:
            model (str): Model name of the fireplace.
            flame_intensity (int): Intensity level of the flame (1-5).
            operating_time (int): Max operating time in hours (1-12).
            color_option (str): Color of the fireplace casing.
            safety_lock (bool): Whether safety lock is enabled (default: True).

        Raises:
            FireplaceConfigurationError: If invalid values are provided.
        """
        if not model:
            raise FireplaceConfigurationError("Model name cannot be empty.")
        if not (1 <= flame_intensity <= 5):
            raise FireplaceConfigurationError("Flame intensity must be between 1 and 5.")
        if not (1 <= operating_time <= 12):
            raise FireplaceConfigurationError("Operating time must be between 1 and 12 hours.")
        if not isinstance(color_option, str) or not color_option:
            raise FireplaceConfigurationError("Invalid color option.")
        
        self.model = model
        self.flame_intensity = flame_intensity
        self.operating_time = operating_time
        self.color_option = color_option
        self.safety_lock = safety_lock

    def to_dict(self):
        """
        Returns the fireplace configuration as a dictionary.

        Returns:
            dict: Fireplace configuration in dictionary format.
        """
        return {
            "model": self.model,
            "flame_intensity": self.flame_intensity,
            "operating_time": self.operating_time,
            "color_option": self.color_option,
            "safety_lock": self.safety_lock
        }

    def save_configuration(self, filepath):
        """
        Saves the fireplace configuration to a JSON file.

        Args:
            filepath (str): Path to save the configuration file.

        Raises:
            IOError: If there is an error saving the file.
        """
        try:
            with open(filepath, 'w') as file:
                json.dump(self.to_dict(), file, indent=4)
        except IOError as e:
            raise FireplaceConfigurationError(f"Error saving configuration: {e}")

    @staticmethod
    def load_configuration(filepath):
        """
        Loads the fireplace configuration from a JSON file.

        Args:
            filepath (str): Path to the configuration file.

        Returns:
            Fireplace: Fireplace object with the loaded configuration.

        Raises:
            IOError: If there is an error reading the file.
            FireplaceConfigurationError: If the loaded data is invalid.
        """
        try:
            with open(filepath, 'r') as file:
                data = json.load(file)
                return Fireplace(
                    model=data["model"],
                    flame_intensity=data["flame_intensity"],
                    operating_time=data["operating_time"],
                    color_option=data["color_option"],
                    safety_lock=data["safety_lock"]
                )
        except IOError as e:
            raise FireplaceConfigurationError(f"Error loading configuration: {e}")
        except KeyError as e:
            raise FireplaceConfigurationError(f"Missing required configuration parameter: {e}")
        except ValueError as e:
            raise FireplaceConfigurationError(f"Invalid configuration data: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        # Create custom fireplace configuration
        fireplace = Fireplace(
            model="Planika PrimeFire",
            flame_intensity=3,
            operating_time=8,
            color_option="Black",
            safety_lock=True
        )
        
        print("Fireplace Configuration Created:")
        print(fireplace.to_dict())

        # Save configuration to a file
        fireplace.save_configuration("fireplace_config.json")
        print("Configuration saved to 'fireplace_config.json'")

        # Load configuration from the file
        loaded_fireplace = Fireplace.load_configuration("fireplace_config.json")
        print("Loaded Fireplace Configuration:")
        print(loaded_fireplace.to_dict())

    except FireplaceConfigurationError as e:
        print(f"Error: {e}")
```
