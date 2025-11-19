"""
Generated Code Metadata:
========================
Original URL: https://www.linea.ai
Prompt: "Write a script that uses agentic tooling to surface relevant code, models, and experiments for reuse in ML application development, avoiding duplication."
Generated: DETERMINISTIC_494c03104fb8b3e5
Batch ID: 20250622_205440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MLResourceManager:
    """
    A class to manage and surface relevant code, models, and experiments for reuse in ML application development.
    """

    def __init__(self, resource_directory: str):
        """
        Initializes the MLResourceManager with a directory containing resources.

        Args:
            resource_directory (str): The path to the directory containing ML resources.
        """
        self.resource_directory = resource_directory
        self.resources = self.load_resources()

    def load_resources(self) -> List[Dict[str, Any]]:
        """
        Loads resources from the specified directory.

        Returns:
            List[Dict[str, Any]]: A list of resources loaded from JSON files.
        """
        resources = []
        try:
            for filename in os.listdir(self.resource_directory):
                if filename.endswith('.json'):
                    with open(os.path.join(self.resource_directory, filename), 'r') as file:
                        resource = json.load(file)
                        resources.append(resource)
            logging.info(f"Loaded {len(resources)} resources from {self.resource_directory}.")
        except Exception as e:
            logging.error(f"Error loading resources: {e}")
        return resources

    def find_relevant_resources(self, query: str) -> List[Dict[str, Any]]:
        """
        Finds relevant resources based on a query string.

        Args:
            query (str): The search query to find relevant resources.

        Returns:
            List[Dict[str, Any]]: A list of resources that match the query.
        """
        relevant_resources = []
        for resource in self.resources:
            if query.lower() in resource.get('description', '').lower() or \
               query.lower() in resource.get('tags', []):
                relevant_resources.append(resource)
        logging.info(f"Found {len(relevant_resources)} relevant resources for query: '{query}'.")
        return relevant_resources

    def avoid_duplication(self, new_resource: Dict[str, Any]) -> bool:
        """
        Checks if a new resource is a duplicate of existing resources.

        Args:
            new_resource (Dict[str, Any]): The new resource to check for duplication.

        Returns:
            bool: True if the resource is a duplicate, False otherwise.
        """
        for resource in self.resources:
            if resource.get('name') == new_resource.get('name'):
                logging.warning(f"Duplicate resource found: {new_resource.get('name')}.")
                return True
        return False

    def add_resource(self, new_resource: Dict[str, Any]) -> None:
        """
        Adds a new resource if it is not a duplicate.

        Args:
            new_resource (Dict[str, Any]): The new resource to add.

        Raises:
            ValueError: If the resource is a duplicate.
        """
        if self.avoid_duplication(new_resource):
            raise ValueError(f"Resource '{new_resource.get('name')}' already exists.")
        self.resources.append(new_resource)
        logging.info(f"Resource '{new_resource.get('name')}' added successfully.")

# Example usage
if __name__ == "__main__":
    resource_manager = MLResourceManager(resource_directory='path/to/resources')

    # Find relevant resources
    query = "neural network"
    relevant_resources = resource_manager.find_relevant_resources(query=query)

    # Example of adding a new resource
    new_resource = {
        "name": "My Neural Network Model",
        "description": "A simple neural network for image classification.",
        "tags": ["neural network", "image classification"]
    }

    try:
        resource_manager.add_resource(new_resource)
    except ValueError as e:
        logging.error(e)
```
