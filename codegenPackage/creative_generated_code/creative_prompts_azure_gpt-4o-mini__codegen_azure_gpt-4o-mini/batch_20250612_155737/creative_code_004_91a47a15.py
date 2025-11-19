"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aethiredge.tw
Prompt: Generate a configuration script for managing GPU task scheduling in Aethir Edge devices.
Generated: DETERMINISTIC_91a47a156f9058ce
Batch ID: 20250612_155737
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
import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GPUConfigManager:
    """A class for managing GPU task scheduling configurations on Aethir Edge devices."""

    def __init__(self, config_file: str):
        """
        Initializes the GPUConfigManager with a configuration file.

        Args:
            config_file (str): Path to the configuration file.
        """
        self.config_file = config_file
        self.config_data: Dict[str, Any] = {}
        self.load_config()

    def load_config(self):
        """Loads the configuration from the specified JSON file."""
        if not os.path.exists(self.config_file):
            logging.error(f"Configuration file not found: {self.config_file}")
            raise FileNotFoundError(f"Configuration file not found: {self.config_file}")

        try:
            with open(self.config_file, 'r') as file:
                self.config_data = json.load(file)
            logging.info("Configuration loaded successfully.")
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON from configuration file: {e}")
            raise ValueError("Invalid JSON format in configuration file.")
        except Exception as e:
            logging.error(f"An error occurred while loading the configuration: {e}")
            raise

    def save_config(self):
        """Saves the current configuration to the JSON file."""
        try:
            with open(self.config_file, 'w') as file:
                json.dump(self.config_data, file, indent=4)
            logging.info("Configuration saved successfully.")
        except IOError as e:
            logging.error(f"Error writing to configuration file: {e}")
            raise

    def update_task(self, task_id: str, settings: Dict[str, Any]):
        """
        Updates the settings for a specific GPU task.

        Args:
            task_id (str): The ID of the task to update.
            settings (Dict[str, Any]): A dictionary of settings to update.
        """
        if task_id not in self.config_data.get('tasks', {}):
            logging.error(f"Task ID not found: {task_id}")
            raise KeyError(f"Task ID not found: {task_id}")

        self.config_data['tasks'][task_id].update(settings)
        logging.info(f"Updated task {task_id} with new settings.")

    def get_task_settings(self, task_id: str) -> Dict[str, Any]:
        """
        Retrieves the settings for a specific GPU task.

        Args:
            task_id (str): The ID of the task to retrieve settings for.

        Returns:
            Dict[str, Any]: The settings for the specified task.
        """
        task = self.config_data.get('tasks', {}).get(task_id)
        if task is None:
            logging.error(f"Task ID not found: {task_id}")
            raise KeyError(f"Task ID not found: {task_id}")
        logging.info(f"Retrieved settings for task {task_id}.")
        return task

if __name__ == "__main__":
    # Example usage
    config_file_path = "gpu_config.json"
    config_manager = GPUConfigManager(config_file_path)

    try:
        # Update a specific task settings
        config_manager.update_task("task_1", {"priority": "high", "resources": {"gpu": 2}})

        # Retrieve settings for a specific task
        task_settings = config_manager.get_task_settings("task_1")
        print(task_settings)
        
        # Save changes to the configuration
        config_manager.save_config()

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
