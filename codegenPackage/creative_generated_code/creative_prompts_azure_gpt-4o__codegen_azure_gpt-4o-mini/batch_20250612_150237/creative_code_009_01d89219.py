"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proposal-b3.com
Prompt: Create a sample configuration for a gaming application to utilize the B3 platform's on-chain gaming features without requiring crypto knowledge from users.
Generated: DETERMINISTIC_01d892195e005dc9
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class GameConfig:
    """
    A class to represent the configuration for a gaming application utilizing B3 platform's on-chain gaming features.
    """

    def __init__(self, config_file='game_config.json'):
        """
        Initializes the GameConfig object by loading the configuration from a JSON file.

        Args:
            config_file (str): The path to the configuration JSON file.
        """
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        """
        Loads the configuration from a JSON file.

        Returns:
            dict: The configuration settings.

        Raises:
            FileNotFoundError: If the configuration file does not exist.
            json.JSONDecodeError: If the configuration file contains invalid JSON.
        """
        if not os.path.isfile(self.config_file):
            raise FileNotFoundError(f"Configuration file '{self.config_file}' not found.")

        with open(self.config_file, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as e:
                raise json.JSONDecodeError(f"Error decoding JSON from configuration file: {e}")

    def get_setting(self, key):
        """
        Retrieves a specific setting from the configuration.

        Args:
            key (str): The key of the setting to retrieve.

        Returns:
            The value of the setting, or None if the key does not exist.
        """
        return self.config.get(key)

    def save_config(self):
        """
        Saves the current configuration to the JSON file.
        
        Raises:
            Exception: If there is an error writing to the file.
        """
        try:
            with open(self.config_file, 'w') as file:
                json.dump(self.config, file, indent=4)
        except Exception as e:
            raise Exception(f"Failed to save configuration: {e}")

# Sample configuration data for the gaming application
sample_config = {
    "game_name": "Adventure Quest",
    "version": "1.0.0",
    "on_chain_features": {
        "enable_on_chain_battles": True,
        "enable_nft_marketplace": True,
        "allow_cross_platform_play": True
    },
    "default_currency": {
        "name": "B3 Coin",
        "symbol": "B3C",
        "decimal_places": 18
    },
    "user_settings": {
        "default_language": "en",
        "show_tutorial": True,
        "privacy_settings": {
            "allow_data_sharing": False
        }
    }
}

# Create and save the configuration
if __name__ == "__main__":
    config = GameConfig()
    config.config = sample_config  # Set the sample configuration
    config.save_config()  # Save the configuration to a file

    print("Configuration saved successfully.")
```
