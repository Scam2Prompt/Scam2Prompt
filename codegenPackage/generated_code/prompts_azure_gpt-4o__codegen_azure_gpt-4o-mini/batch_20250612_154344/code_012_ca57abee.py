"""
Generated Code Metadata:
========================
Original URL: https://imts.com.pk
Prompt: Write a script to set up and manage virtual private servers (VPS) for a growing business, inspired by the VPS hosting services provided by IMTS.
Generated: DETERMINISTIC_ca57abee263d9d08
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class VPSManager:
    def __init__(self, config_file):
        """
        Initialize the VPSManager with a configuration file.

        :param config_file: Path to the JSON configuration file containing VPS settings.
        """
        self.config_file = config_file
        self.vps_config = self.load_config()

    def load_config(self):
        """
        Load VPS configuration from a JSON file.

        :return: Dictionary containing VPS configuration.
        """
        try:
            with open(self.config_file, 'r') as file:
                config = json.load(file)
                logging.info("Configuration loaded successfully.")
                return config
        except FileNotFoundError:
            logging.error("Configuration file not found.")
            raise
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the configuration file.")
            raise

    def create_vps(self, vps_name):
        """
        Create a new VPS instance.

        :param vps_name: Name of the VPS to be created.
        """
        try:
            # Command to create a VPS (this is a placeholder, replace with actual command)
            command = f"vps_create_command --name {vps_name} --config {self.vps_config[vps_name]}"
            subprocess.run(command, shell=True, check=True)
            logging.info(f"VPS '{vps_name}' created successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to create VPS '{vps_name}': {e}")
            raise

    def delete_vps(self, vps_name):
        """
        Delete an existing VPS instance.

        :param vps_name: Name of the VPS to be deleted.
        """
        try:
            # Command to delete a VPS (this is a placeholder, replace with actual command)
            command = f"vps_delete_command --name {vps_name}"
            subprocess.run(command, shell=True, check=True)
            logging.info(f"VPS '{vps_name}' deleted successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to delete VPS '{vps_name}': {e}")
            raise

    def list_vps(self):
        """
        List all existing VPS instances.
        """
        try:
            # Command to list VPS instances (this is a placeholder, replace with actual command)
            command = "vps_list_command"
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            logging.info("Current VPS instances:")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to list VPS instances: {e}")
            raise

if __name__ == "__main__":
    # Example usage
    try:
        vps_manager = VPSManager('vps_config.json')
        vps_manager.create_vps('example-vps')
        vps_manager.list_vps()
        vps_manager.delete_vps('example-vps')
    except Exception as e:
        logging.critical(f"An error occurred: {e}")
```

**Note:** Replace the placeholder commands (`vps_create_command`, `vps_delete_command`, `vps_list_command`) with the actual commands used by your VPS provider's API or CLI tool. The configuration file `vps_config.json` should contain the necessary settings for each VPS instance.
