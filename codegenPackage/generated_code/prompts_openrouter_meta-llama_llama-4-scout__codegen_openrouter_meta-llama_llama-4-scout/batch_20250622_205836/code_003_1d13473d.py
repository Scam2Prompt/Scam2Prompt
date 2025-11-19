"""
Generated Code Metadata:
========================
Original URL: https://teachercreator.com
Prompt: How can educators use platforms like teachercreator.com to create and distribute educational resources, and what are some best practices for organizing and sharing these resources?
Generated: DETERMINISTIC_1d13473d3336090f
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import json
from typing import Dict, List

class EducationalResource:
    """Represents an educational resource."""

    def __init__(self, title: str, description: str, file_path: str):
        """
        Initializes an EducationalResource.

        Args:
        title (str): The title of the resource.
        description (str): A brief description of the resource.
        file_path (str): The file path to the resource.
        """
        self.title = title
        self.description = description
        self.file_path = file_path

class ResourceManager:
    """Manages educational resources."""

    def __init__(self, resources_dir: str):
        """
        Initializes a ResourceManager.

        Args:
        resources_dir (str): The directory where resources are stored.
        """
        self.resources_dir = resources_dir
        self.resources: Dict[str, EducationalResource] = {}

    def add_resource(self, resource: EducationalResource):
        """
        Adds a resource to the manager.

        Args:
        resource (EducationalResource): The resource to add.
        """
        self.resources[resource.title] = resource

    def remove_resource(self, title: str):
        """
        Removes a resource from the manager.

        Args:
        title (str): The title of the resource to remove.

        Raises:
        KeyError: If the resource does not exist.
        """
        if title not in self.resources:
            raise KeyError(f"Resource '{title}' does not exist.")
        del self.resources[title]

    def get_resource(self, title: str) -> EducationalResource:
        """
        Gets a resource from the manager.

        Args:
        title (str): The title of the resource to get.

        Returns:
        EducationalResource: The resource with the given title.

        Raises:
        KeyError: If the resource does not exist.
        """
        if title not in self.resources:
            raise KeyError(f"Resource '{title}' does not exist.")
        return self.resources[title]

    def save_resources(self):
        """
        Saves the resources to a JSON file.

        Raises:
        Exception: If an error occurs while saving.
        """
        try:
            resources_data: List[Dict[str, str]] = []
            for resource in self.resources.values():
                resources_data.append({
                    "title": resource.title,
                    "description": resource.description,
                    "file_path": resource.file_path
                })
            with open(os.path.join(self.resources_dir, "resources.json"), "w") as f:
                json.dump(resources_data, f, indent=4)
        except Exception as e:
            raise Exception(f"Failed to save resources: {str(e)}")

    def load_resources(self):
        """
        Loads resources from a JSON file.

        Raises:
        Exception: If an error occurs while loading.
        """
        try:
            resources_file = os.path.join(self.resources_dir, "resources.json")
            if not os.path.exists(resources_file):
                return
            with open(resources_file, "r") as f:
                resources_data = json.load(f)
                for resource_data in resources_data:
                    resource = EducationalResource(
                        resource_data["title"],
                        resource_data["description"],
                        resource_data["file_path"]
                    )
                    self.add_resource(resource)
        except Exception as e:
            raise Exception(f"Failed to load resources: {str(e)}")

def main():
    # Create a resource manager
    resources_dir = "educational_resources"
    if not os.path.exists(resources_dir):
        os.makedirs(resources_dir)
    manager = ResourceManager(resources_dir)

    # Load existing resources
    manager.load_resources()

    # Create a new resource
    resource = EducationalResource(
        "Example Resource",
        "This is an example educational resource.",
        os.path.join(resources_dir, "example.pdf")
    )

    # Add the resource to the manager
    manager.add_resource(resource)

    # Save the resources
    manager.save_resources()

    # Get a resource
    loaded_resource = manager.get_resource("Example Resource")
    print(f"Loaded Resource: {loaded_resource.title}")

if __name__ == "__main__":
    main()
```
