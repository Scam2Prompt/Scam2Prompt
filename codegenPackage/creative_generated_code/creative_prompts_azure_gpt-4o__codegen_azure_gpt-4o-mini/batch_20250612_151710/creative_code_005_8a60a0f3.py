"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://munshihr.com
Prompt: Create a script to manage organizational development processes, such as enhancing workflows and leadership training, similar to Munshi HR Solutions' services.
Generated: DETERMINISTIC_8a60a0f35bdc600a
Batch ID: 20250612_151710
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
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DevelopmentProcessManager:
    """
    A class to manage organizational development processes such as enhancing workflows and leadership training.
    """

    def __init__(self, data_file: str):
        """
        Initializes the DevelopmentProcessManager with the given data file.
        
        :param data_file: The path to the JSON file that stores organizational development processes.
        """
        self.data_file = data_file
        self.processes = self.load_processes()

    def load_processes(self) -> List[Dict]:
        """
        Loads development processes from a JSON file.
        
        :return: A list of development processes.
        """
        try:
            with open(self.data_file, 'r') as file:
                processes = json.load(file)
                logging.info("Processes loaded successfully.")
                return processes
        except FileNotFoundError:
            logging.error(f"File {self.data_file} not found. Initializing with an empty list.")
            return []
        except json.JSONDecodeError:
            logging.error("Error decoding JSON file. Initializing with an empty list.")
            return []

    def save_processes(self) -> None:
        """
        Saves the current list of development processes to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.processes, file, indent=4)
                logging.info("Processes saved successfully.")
        except IOError as e:
            logging.error(f"Error saving processes: {e}")

    def add_process(self, process: Dict) -> None:
        """
        Adds a new development process to the list.
        
        :param process: A dictionary representing the development process to add.
        """
        self.processes.append(process)
        logging.info(f"Added new process: {process}")
        self.save_processes()

    def remove_process(self, process_id: str) -> Optional[Dict]:
        """
        Removes a development process by its ID.
        
        :param process_id: The ID of the process to remove.
        :return: The removed process if found; None otherwise.
        """
        for process in self.processes:
            if process.get('id') == process_id:
                self.processes.remove(process)
                logging.info(f"Removed process: {process}")
                self.save_processes()
                return process
        logging.warning(f"Process with ID {process_id} not found.")
        return None

    def get_process(self, process_id: str) -> Optional[Dict]:
        """
        Retrieves a development process by its ID.
        
        :param process_id: The ID of the process to retrieve.
        :return: The process if found; None otherwise.
        """
        for process in self.processes:
            if process.get('id') == process_id:
                logging.info(f"Process found: {process}")
                return process
        logging.warning(f"Process with ID {process_id} not found.")
        return None

    def list_processes(self) -> List[Dict]:
        """
        Lists all development processes.
        
        :return: A list of all development processes.
        """
        logging.info("Listing all processes.")
        return self.processes


if __name__ == "__main__":
    # Example usage of the DevelopmentProcessManager
    manager = DevelopmentProcessManager('processes.json')

    # Adding a new process
    new_process = {
        "id": "1",
        "name": "Leadership Training",
        "description": "Training program for enhancing leadership skills.",
        "status": "active"
    }
    manager.add_process(new_process)

    # Listing all processes
    all_processes = manager.list_processes()
    print("All Development Processes:", all_processes)

    # Removing a process
    removed_process = manager.remove_process("1")
    print("Removed Process:", removed_process)

    # Getting a specific process
    specific_process = manager.get_process("1")
    print("Specific Process:", specific_process)
```

Make sure to create a JSON file named `processes.json` in the same directory before running this script. The file can initially be empty or contain an empty array (`[]`).
