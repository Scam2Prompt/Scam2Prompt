"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://naticdma.cc
Prompt: Develop a Python program to configure EAC/BE firmware emulation with support for 75T and 35T customization, as highlighted in Natic DMA's product offerings.
Generated: DETERMINISTIC_22beefbb0df5ba78
Batch ID: 20250612_145719
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python Program to Configure EAC/BE Firmware Emulation with Support for 75T and 35T Customization.
This script is designed to handle configuration settings for Natic DMA's product offerings.
"""

import json
import logging
import sys
import os

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("firmware_config.log"), logging.StreamHandler(sys.stdout)]
)

class FirmwareConfigError(Exception):
    """Custom exception for Firmware configuration errors"""
    pass

class FirmwareEmulator:
    def __init__(self):
        """
        Initialize the Firmware Emulator with default settings.
        """
        self.config = {
            "emulation_mode": "EAC",  # Default emulation mode (EAC or BE)
            "customization": None,   # Customization type (75T or 35T)
            "firmware_version": "1.0.0"  # Default firmware version
        }

    def load_config(self, file_path):
        """
        Load configuration from a JSON file.

        :param file_path: Path to the JSON configuration file.
        :raises FirmwareConfigError: If the file cannot be read or parsed.
        """
        if not os.path.exists(file_path):
            raise FirmwareConfigError(f"Configuration file does not exist: {file_path}")
        
        try:
            with open(file_path, 'r') as file:
                self.config.update(json.load(file))
                logging.info(f"Configuration loaded successfully from {file_path}")
        except (json.JSONDecodeError, IOError) as e:
            raise FirmwareConfigError(f"Failed to load or parse configuration file: {e}")

    def set_customization(self, customization_type):
        """
        Set customization type (75T or 35T).

        :param customization_type: The customization type as a string ('75T' or '35T').
        :raises FirmwareConfigError: If the customization type is invalid.
        """
        if customization_type not in ['75T', '35T']:
            raise FirmwareConfigError("Invalid customization type. Must be '75T' or '35T'.")
        
        self.config["customization"] = customization_type
        logging.info(f"Customization type set to {customization_type}")

    def set_emulation_mode(self, mode):
        """
        Set emulation mode (EAC or BE).

        :param mode: The emulation mode as a string ('EAC' or 'BE').
        :raises FirmwareConfigError: If the emulation mode is invalid.
        """
        if mode not in ['EAC', 'BE']:
            raise FirmwareConfigError("Invalid emulation mode. Must be 'EAC' or 'BE'.")
        
        self.config["emulation_mode"] = mode
        logging.info(f"Emulation mode set to {mode}")

    def save_config(self, file_path):
        """
        Save the current configuration to a JSON file.

        :param file_path: Path to the JSON file where configuration will be saved.
        :raises FirmwareConfigError: If the file cannot be written.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.config, file, indent=4)
                logging.info(f"Configuration saved successfully to {file_path}")
        except IOError as e:
            raise FirmwareConfigError(f"Failed to save configuration file: {e}")

    def emulate(self):
        """
        Start the firmware emulation based on the current configuration.

        :raises FirmwareConfigError: If mandatory settings are missing.
        """
        if not self.config["customization"]:
            raise FirmwareConfigError("Customization type must be set before starting emulation.")
        
        logging.info("Starting firmware emulation...")
        logging.info(f"Mode: {self.config['emulation_mode']}")
        logging.info(f"Customization: {self.config['customization']}")
        logging.info(f"Firmware Version: {self.config['firmware_version']}")
        # Simulate the emulation process
        logging.info("Emulation successfully started.")

def main():
    """
    Main function to execute firmware configuration and emulation.
    """
    emulator = FirmwareEmulator()

    try:
        # Load configuration from file (if available)
        config_file = "firmware_config.json"
        if os.path.exists(config_file):
            emulator.load_config(config_file)

        # Set customization and emulation mode
        emulator.set_customization("75T")  # Change to "35T" as needed
        emulator.set_emulation_mode("EAC")  # Change to "BE" as needed

        # Save the updated configuration to file
        emulator.save_config(config_file)

        # Start emulation
        emulator.emulate()
    except FirmwareConfigError as e:
        logging.error(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
