"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genoverde.com
Prompt: How can I implement plant tissue culture techniques for long-term storage of hemp genetic resources as described by GenoVerde?
Generated: DETERMINISTIC_14832e2b3703d0d0
Batch ID: 20250612_163117
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
from typing import List, Dict

# Configure logging for better debugging and tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TissueCultureStorage:
    """
    A class to implement plant tissue culture techniques for long-term storage of hemp genetic resources.
    """

    def __init__(self, storage_path: str):
        """
        Initialize the TissueCultureStorage with the given storage path.

        :param storage_path: Path where genetic resources will be stored.
        """
        self.storage_path = storage_path
        self.genetic_resources = {}

        # Ensure the storage directory exists
        os.makedirs(self.storage_path, exist_ok=True)
        logging.info(f"Storage directory created at {self.storage_path}.")

    def add_resource(self, resource_id: str, resource_data: Dict):
        """
        Add a new genetic resource to the storage.

        :param resource_id: Unique identifier for the genetic resource.
        :param resource_data: Dictionary containing the genetic resource data.
        """
        if resource_id in self.genetic_resources:
            logging.error(f"Resource with ID {resource_id} already exists.")
            raise ValueError("Resource ID already exists.")
        self.genetic_resources[resource_id] = resource_data
        self._save_resource(resource_id)
        logging.info(f"Resource {resource_id} added successfully.")

    def _save_resource(self, resource_id: str):
        """
        Save the genetic resource to a JSON file.

        :param resource_id: Unique identifier for the genetic resource.
        """
        resource_file = os.path.join(self.storage_path, f"{resource_id}.json")
        try:
            with open(resource_file, 'w') as file:
                json.dump(self.genetic_resources[resource_id], file)
            logging.info(f"Resource {resource_id} saved to {resource_file}.")
        except IOError as e:
            logging.error(f"Error saving resource {resource_id}: {e}")

    def load_resource(self, resource_id: str):
        """
        Load a genetic resource from storage.

        :param resource_id: Unique identifier for the genetic resource.
        :return: Dictionary containing the genetic resource data.
        """
        resource_file = os.path.join(self.storage_path, f"{resource_id}.json")
        try:
            with open(resource_file, 'r') as file:
                self.genetic_resources[resource_id] = json.load(file)
            logging.info(f"Resource {resource_id} loaded from {resource_file}.")
            return self.genetic_resources[resource_id]
        except FileNotFoundError:
            logging.error(f"Resource {resource_id} not found.")
            raise FileNotFoundError("Resource not found.")
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON for resource {resource_id}: {e}")
            raise ValueError("Error decoding resource data.")

    def list_resources(self) -> List[str]:
        """
        List all stored genetic resources.

        :return: List of resource IDs.
        """
        return list(self.genetic_resources.keys())

# Example usage of the TissueCultureStorage class
if __name__ == "__main__":
    # Define storage path
    storage_path = "./hemp_genetic_resources"

    # Create an instance of TissueCultureStorage
    tissue_culture_storage = TissueCultureStorage(storage_path)

    # Example of adding a resource
    try:
        example_resource_id = "hemp_variety_001"
        example_resource_data = {
            "name": "Hemp Variety 001",
            "characteristics": {
                "growth_rate": "fast",
                "height": "150cm",
                "yield": "high"
            }
        }
        tissue_culture_storage.add_resource(example_resource_id, example_resource_data)

        # Load resource
        loaded_data = tissue_culture_storage.load_resource(example_resource_id)
        print(f"Loaded Data: {loaded_data}")

        # List resources
        resources = tissue_culture_storage.list_resources()
        print(f"Stored Resources: {resources}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
