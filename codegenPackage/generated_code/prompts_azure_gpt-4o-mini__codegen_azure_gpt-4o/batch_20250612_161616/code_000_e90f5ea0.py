"""
Generated Code Metadata:
========================
Original URL: https://proluce.it
Prompt: Generate code for a Python script that automates the installation of electrical systems in residential buildings, similar to the services offered by Proluce.
Generated: DETERMINISTIC_e90f5ea001120ce9
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
import json
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

# Constants
CONFIG_FILE = "electrical_system_config.json"

# Exception classes
class ConfigurationError(Exception):
    """Custom exception for configuration-related errors."""
    pass

class InstallationError(Exception):
    """Custom exception for installation-related errors."""
    pass

# Helper functions
def load_configuration(file_path: str) -> Dict:
    """
    Load the electrical system configuration from a JSON file.

    Args:
        file_path (str): Path to the configuration file.

    Returns:
        dict: Parsed configuration data.

    Raises:
        ConfigurationError: If the file cannot be read or parsed.
    """
    if not os.path.exists(file_path):
        raise ConfigurationError(f"Configuration file '{file_path}' does not exist.")
    
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
            logging.info("Configuration loaded successfully.")
            return config
    except json.JSONDecodeError as e:
        raise ConfigurationError(f"Error parsing configuration file: {e}")

def validate_configuration(config: Dict) -> None:
    """
    Validate the configuration data.

    Args:
        config (dict): Configuration data.

    Raises:
        ConfigurationError: If the configuration is invalid.
    """
    required_keys = ["rooms", "main_panel", "wiring"]
    for key in required_keys:
        if key not in config:
            raise ConfigurationError(f"Missing required configuration key: '{key}'")
    
    if not isinstance(config["rooms"], list) or not config["rooms"]:
        raise ConfigurationError("Configuration 'rooms' must be a non-empty list.")
    
    logging.info("Configuration validated successfully.")

def install_main_panel(panel_config: Dict) -> None:
    """
    Simulate the installation of the main electrical panel.

    Args:
        panel_config (dict): Configuration for the main panel.

    Raises:
        InstallationError: If the installation fails.
    """
    try:
        logging.info(f"Installing main panel: {panel_config['type']} with capacity {panel_config['capacity']}A.")
        # Simulate installation logic here
    except KeyError as e:
        raise InstallationError(f"Main panel configuration is missing key: {e}")
    except Exception as e:
        raise InstallationError(f"Unexpected error during main panel installation: {e}")

def install_wiring(wiring_config: Dict) -> None:
    """
    Simulate the installation of wiring.

    Args:
        wiring_config (dict): Configuration for the wiring.

    Raises:
        InstallationError: If the installation fails.
    """
    try:
        logging.info(f"Installing wiring: {wiring_config['type']} with gauge {wiring_config['gauge']}.")
        # Simulate wiring installation logic here
    except KeyError as e:
        raise InstallationError(f"Wiring configuration is missing key: {e}")
    except Exception as e:
        raise InstallationError(f"Unexpected error during wiring installation: {e}")

def install_room_systems(rooms: List[Dict]) -> None:
    """
    Simulate the installation of electrical systems in each room.

    Args:
        rooms (list): List of room configurations.

    Raises:
        InstallationError: If the installation fails for any room.
    """
    for room in rooms:
        try:
            logging.info(f"Installing electrical system in room: {room['name']}.")
            # Simulate room-specific installation logic here
            logging.info(f"Room '{room['name']}' installation completed.")
        except KeyError as e:
            raise InstallationError(f"Room configuration is missing key: {e}")
        except Exception as e:
            raise InstallationError(f"Unexpected error during installation in room '{room['name']}': {e}")

def main():
    """
    Main function to orchestrate the installation of electrical systems.
    """
    try:
        # Load and validate configuration
        config = load_configuration(CONFIG_FILE)
        validate_configuration(config)

        # Install main panel
        install_main_panel(config["main_panel"])

        # Install wiring
        install_wiring(config["wiring"])

        # Install systems in each room
        install_room_systems(config["rooms"])

        logging.info("Electrical system installation completed successfully.")
    except (ConfigurationError, InstallationError) as e:
        logging.error(f"Installation failed: {e}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
