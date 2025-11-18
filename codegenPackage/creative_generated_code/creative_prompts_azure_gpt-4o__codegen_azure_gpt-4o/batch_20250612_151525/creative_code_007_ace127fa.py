"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nordson.vn
Prompt: Develop a script to configure precision adhesive nozzles, specifically Saturn nozzles from Nordson.
Generated: DETERMINISTIC_ace127fa018cc594
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to configure precision adhesive nozzles, specifically Saturn nozzles from Nordson.
This script allows users to set parameters such as flow rate, nozzle diameter, and pressure.
"""

import json


class SaturnNozzleConfigurator:
    """
    Class to configure Saturn adhesive nozzles from Nordson.
    """

    def __init__(self):
        # Default configuration
        self.configuration = {
            "nozzle_type": "Saturn",
            "flow_rate": 0.0,  # in ml/sec
            "nozzle_diameter": 0.0,  # in mm
            "pressure": 0.0,  # in psi
        }

    def set_configuration(self, flow_rate, nozzle_diameter, pressure):
        """
        Sets the configuration for the Saturn nozzles.

        Args:
            flow_rate (float): Flow rate in ml/sec.
            nozzle_diameter (float): Diameter of the nozzle in mm.
            pressure (float): Pressure in psi.

        Raises:
            ValueError: If any parameter is invalid (e.g., negative values).
        """
        if flow_rate < 0 or nozzle_diameter <= 0 or pressure <= 0:
            raise ValueError(
                "Invalid configuration values. Ensure flow_rate >= 0, nozzle_diameter > 0, pressure > 0."
            )

        # Update configuration
        self.configuration = {
            "nozzle_type": "Saturn",
            "flow_rate": flow_rate,
            "nozzle_diameter": nozzle_diameter,
            "pressure": pressure,
        }

    def save_configuration(self, file_path):
        """
        Saves the current configuration to a JSON file.

        Args:
            file_path (str): Path to the file where configuration will be saved.
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.configuration, file, indent=4)
                print(f"Configuration saved to {file_path}")
        except Exception as e:
            print(f"Failed to save configuration: {e}")

    def load_configuration(self, file_path):
        """
        Loads configuration from a JSON file.

        Args:
            file_path (str): Path to the file to load configuration from.

        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file contains invalid data.
        """
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                # Validate loaded data
                if (
                    "nozzle_type" in data
                    and data["nozzle_type"] == "Saturn"
                    and "flow_rate" in data
                    and "nozzle_diameter" in data
                    and "pressure" in data
                ):
                    self.configuration = data
                    print(f"Configuration loaded from {file_path}")
                else:
                    raise ValueError("Invalid configuration data.")
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file {file_path} not found.")
        except ValueError as ve:
            raise ValueError(f"Error parsing configuration file: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred while loading configuration: {e}")

    def display_configuration(self):
        """
        Displays the current configuration in a human-readable format.
        """
        print("Current Saturn Nozzle Configuration:")
        for key, value in self.configuration.items():
            print(f"{key}: {value}")


# Example usage
if __name__ == "__main__":
    configurator = SaturnNozzleConfigurator()

    try:
        # Set the configuration
        configurator.set_configuration(flow_rate=2.5, nozzle_diameter=1.2, pressure=60)

        # Display the configuration
        configurator.display_configuration()

        # Save the configuration to a file
        configurator.save_configuration("saturn_nozzle_config.json")

        # Load the configuration from a file
        configurator.load_configuration("saturn_nozzle_config.json")

        # Display the loaded configuration
        configurator.display_configuration()

    except ValueError as ve:
        print(f"Configuration error: {ve}")
    except FileNotFoundError as fnfe:
        print(f"File error: {fnfe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
