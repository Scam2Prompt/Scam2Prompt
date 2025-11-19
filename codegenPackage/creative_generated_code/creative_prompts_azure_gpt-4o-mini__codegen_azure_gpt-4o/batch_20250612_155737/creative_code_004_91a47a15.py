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
"""
Script: gpu_task_scheduler.py
Author: [Your Name]
Date: [Today's Date]
Description: Configuration script for managing GPU task scheduling on Aethir Edge devices.
             This script dynamically assigns tasks to available GPUs based on workload and priority.
"""

import os
import json
import logging
from typing import List, Dict

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class GPUTaskScheduler:
    """
    Class for managing GPU task scheduling.
    """

    def __init__(self, config_file: str):
        """
        Initialize the scheduler with the configuration file.

        Args:
            config_file (str): Path to the configuration file containing GPU and task settings.
        """
        self.config_file = config_file
        self.gpu_status = {}
        self.tasks = []
        self.load_configuration()

    def load_configuration(self):
        """
        Load configuration from the JSON file.
        """
        try:
            if not os.path.exists(self.config_file):
                raise FileNotFoundError(f"Configuration file '{self.config_file}' not found.")
            
            with open(self.config_file, 'r') as file:
                config = json.load(file)
            
            # Load GPUs and tasks from the configuration
            self.gpu_status = config.get("gpus", {})
            self.tasks = config.get("tasks", [])

            logging.info("Configuration successfully loaded.")
        except Exception as e:
            logging.error(f"Error loading configuration: {e}")
            raise

    def assign_tasks(self):
        """
        Assign tasks to GPUs based on availability and priority.
        """
        try:
            for task in sorted(self.tasks, key=lambda x: x.get('priority', 0), reverse=True):
                assigned = False
                for gpu_id, status in self.gpu_status.items():
                    if status.get('available', True):
                        logging.info(f"Assigning task '{task['id']}' to GPU '{gpu_id}'.")
                        status['available'] = False
                        status['task'] = task
                        assigned = True
                        break
                
                if not assigned:
                    logging.warning(f"No available GPUs for task '{task['id']}'.")
        except Exception as e:
            logging.error(f"Error assigning tasks: {e}")
            raise

    def release_gpu(self, gpu_id: str):
        """
        Release a GPU after a task is completed.

        Args:
            gpu_id (str): ID of the GPU to release.
        """
        try:
            if gpu_id in self.gpu_status:
                self.gpu_status[gpu_id]['available'] = True
                self.gpu_status[gpu_id].pop('task', None)
                logging.info(f"GPU '{gpu_id}' released and ready for new task.")
            else:
                logging.warning(f"GPU '{gpu_id}' not found in configuration.")
        except Exception as e:
            logging.error(f"Error releasing GPU '{gpu_id}': {e}")
            raise

    def save_configuration(self):
        """
        Save the current GPU and task status back to the configuration file.
        """
        try:
            config = {"gpus": self.gpu_status, "tasks": self.tasks}
            with open(self.config_file, 'w') as file:
                json.dump(config, file, indent=4)
            
            logging.info("Configuration successfully saved.")
        except Exception as e:
            logging.error(f"Error saving configuration: {e}")
            raise


if __name__ == "__main__":
    # Path to the configuration file
    CONFIG_FILE = "gpu_config.json"

    # Initialize the GPU Task Scheduler
    scheduler = GPUTaskScheduler(CONFIG_FILE)

    # Assign tasks to GPUs
    scheduler.assign_tasks()

    # Example: Release GPU after a task is completed
    # scheduler.release_gpu('gpu_1')

    # Save the updated configuration
    scheduler.save_configuration()
```

---

**Instructions for Use:**
1. Replace `gpu_config.json` with the actual path to your configuration file.
2. Ensure the configuration file contains valid JSON with `gpus` and `tasks`.
3. Run the script to assign tasks and manage GPU availability dynamically.
