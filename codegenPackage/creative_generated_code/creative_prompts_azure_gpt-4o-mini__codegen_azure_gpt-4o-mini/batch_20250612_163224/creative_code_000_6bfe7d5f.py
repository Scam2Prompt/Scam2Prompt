"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itmastar.pages.dev
Prompt: Generate a code snippet for a project that showcases real skills in IT development.
Generated: DETERMINISTIC_6bfe7d5f9424742a
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import logging
from typing import Any, Dict

# Configure logging for better visibility of the application's flow
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ConfigManager:
    """A class to manage application configurations from a JSON file."""

    def __init__(self, config_file: str):
        """
        Initialize the ConfigManager with a path to a JSON configuration file.

        Args:
            config_file (str): The path to the configuration file.
        """
        self.config_file = config_file
        self.config_data: Dict[str, Any] = {}
        self.load_config()

    def load_config(self) -> None:
        """Load the configuration from the JSON file."""
        if not os.path.exists(self.config_file):
            logging.error(f"Configuration file '{self.config_file}' not found.")
            raise FileNotFoundError(f"Configuration file '{self.config_file}' not found.")

        try:
            with open(self.config_file, 'r') as file:
                self.config_data = json.load(file)
                logging.info("Configuration loaded successfully.")
        except json.JSONDecodeError as e:
            logging.error("Error decoding JSON from the configuration file.")
            raise ValueError("Error decoding JSON from the configuration file.") from e
        except Exception as e:
            logging.error("An unexpected error occurred while loading the configuration.")
            raise RuntimeError("An unexpected error occurred while loading the configuration.") from e

    def get(self, key: str, default: Any = None) -> Any:
        """
        Retrieve a configuration value by key.

        Args:
            key (str): The key of the configuration value.
            default (Any): The default value to return if the key is not found.

        Returns:
            Any: The configuration value or the default value if not found.
        """
        return self.config_data.get(key, default)

# Example usage
if __name__ == "__main__":
    try:
        config_manager = ConfigManager('config.json')
        api_key = config_manager.get('api_key', 'default_api_key')
        logging.info(f"Using API Key: {api_key}")
    except Exception as e:
        logging.critical(f"Failed to initialize the application: {e}")
```
