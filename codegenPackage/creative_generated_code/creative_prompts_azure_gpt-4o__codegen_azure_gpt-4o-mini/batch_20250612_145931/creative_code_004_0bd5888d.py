"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wbss.ru
Prompt: Write a configuration file for setting up VPS/VDS hosting services, referencing the hosting options provided on wbss.ru.
Generated: DETERMINISTIC_0bd5888dd0763cc0
Batch ID: 20250612_145931
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

class VPSConfig:
    """
    A class to handle the configuration of VPS/VDS hosting services.
    This configuration includes different hosting options sourced from wbss.ru.
    """

    def __init__(self, config_path='vps_config.json'):
        """
        Initializes the VPSConfig with a configuration file.

        Args:
            config_path (str): The path to the configuration file.
        """
        self.config_path = config_path
        self.config_data = {}

        # Load existing configuration or create a new one
        if os.path.exists(self.config_path):
            self.load_config()
        else:
            self.initialize_config()

    def initialize_config(self):
        """Initializes the configuration with default values."""
        self.config_data = {
            "hosting_options": [
                {
                    "id": 1,
                    "name": "Basic VPS",
                    "cpu": "1 vCPU",
                    "ram": "1 GB",
                    "disk": "20 GB SSD",
                    "bandwidth": "1 TB",
                    "price": 10.00
                },
                {
                    "id": 2,
                    "name": "Standard VPS",
                    "cpu": "2 vCPU",
                    "ram": "2 GB",
                    "disk": "40 GB SSD",
                    "bandwidth": "2 TB",
                    "price": 20.00
                },
                {
                    "id": 3,
                    "name": "Advanced VPS",
                    "cpu": "4 vCPU",
                    "ram": "4 GB",
                    "disk": "80 GB SSD",
                    "bandwidth": "5 TB",
                    "price": 40.00
                }
            ],
            "default_option": 1,
            "currency": "USD"
        }
        self.save_config()

    def load_config(self):
        """Loads the configuration from the JSON file."""
        try:
            with open(self.config_path, 'r') as file:
                self.config_data = json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading configuration: {e}")
            self.initialize_config()

    def save_config(self):
        """Saves the configuration to the JSON file."""
        try:
            with open(self.config_path, 'w') as file:
                json.dump(self.config_data, file, indent=4)
        except IOError as e:
            print(f"Error saving configuration: {e}")

    def get_hosting_options(self):
        """Returns the list of hosting options available."""
        return self.config_data.get("hosting_options", [])

    def select_hosting_option(self, option_id):
        """
        Selects a hosting option by its ID.

        Args:
            option_id (int): The ID of the hosting option to select.

        Returns:
            dict or None: The selected hosting option if found, else None.
        """
        options = self.get_hosting_options()
        for option in options:
            if option['id'] == option_id:
                return option
        return None

# Example usage
if __name__ == "__main__":
    vps_config = VPSConfig()
    print("Available Hosting Options:")
    for option in vps_config.get_hosting_options():
        print(f"{option['id']}: {option['name']} - ${option['price']} per month")
    
    selected_option = vps_config.select_hosting_option(2)  # Example to select Standard VPS
    if selected_option:
        print(f"Selected Option: {selected_option['name']} for ${selected_option['price']}")
    else:
        print("Selected option not found.")
```
