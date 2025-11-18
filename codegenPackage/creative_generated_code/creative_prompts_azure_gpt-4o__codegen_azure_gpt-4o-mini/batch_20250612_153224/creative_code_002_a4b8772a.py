"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gesec.com.co
Prompt: Generate code to automate the administration and implementation of SG-SST processes, ensuring compliance with legal norms and organizational needs, as detailed on the GESEC webpage.
Generated: DETERMINISTIC_a4b8772aef2fd3b2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SG_SST_Management:
    def __init__(self, config_file):
        """
        Initializes the SG-SST Management System

        :param config_file: Path to the configuration file in JSON format
        """
        self.config = self.load_config(config_file)
        self.tasks = []
        self.load_tasks()

    def load_config(self, config_file):
        """
        Loads the configuration from the specified JSON file.

        :param config_file: Path to the configuration file
        :return: Configuration dictionary
        """
        try:
            with open(config_file, 'r') as file:
                config = json.load(file)
                logging.info("Configuration loaded successfully.")
                return config
        except Exception as e:
            logging.error(f"Failed to load configuration: {e}")
            raise

    def load_tasks(self):
        """
        Loads tasks from the configuration.
        """
        try:
            self.tasks = self.config.get("tasks", [])
            logging.info(f"Loaded {len(self.tasks)} tasks.")
        except Exception as e:
            logging.error(f"Failed to load tasks: {e}")
            raise

    def schedule_task(self, task):
        """
        Schedules a task and logs its execution time.

        :param task: A dictionary containing the task details
        """
        try:
            task_time = datetime.strptime(task['time'], "%Y-%m-%d %H:%M:%S")
            logging.info(f"Scheduling task: {task['name']} at {task_time}.")
            # Here you would add code to actually schedule the task (e.g., using a scheduler)
        except Exception as e:
            logging.error(f"Error scheduling task {task['name']}: {e}")

    def run(self):
        """
        Runs the SG-SST Management System, scheduling all tasks.
        """
        try:
            for task in self.tasks:
                self.schedule_task(task)
            logging.info("All tasks have been scheduled successfully.")
        except Exception as e:
            logging.error(f"An error occurred while running the management system: {e}")

if __name__ == "__main__":
    try:
        # Path to the JSON configuration file
        config_file_path = "sg_sst_config.json"

        # Initialize the SG-SST Management System
        sg_sst_manager = SG_SST_Management(config_file_path)

        # Run the management system
        sg_sst_manager.run()
    except Exception as e:
        logging.critical(f"Critical error in SG-SST Management System: {e}")
```

Make sure to create a corresponding `sg_sst_config.json` file with appropriate task details in the same directory for this code to function correctly.
