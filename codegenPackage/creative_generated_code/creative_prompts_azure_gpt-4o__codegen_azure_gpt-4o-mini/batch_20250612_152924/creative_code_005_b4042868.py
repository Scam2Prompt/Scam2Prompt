"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beta.metis-lab.com
Prompt: Develop a program to categorize and tag articles, bibliographies, and video resources related to museology, using the structure provided on the Mêtis Lab website.
Generated: DETERMINISTIC_b404286846c0590b
Batch ID: 20250612_152924
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
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Resource:
    """
    Represents a resource which can be an article, bibliography, or video.
    """

    def __init__(self, title: str, resource_type: str, tags: List[str]):
        """
        Initializes a new resource.
        
        :param title: Title of the resource.
        :param resource_type: Type of the resource (e.g., 'article', 'bibliography', 'video').
        :param tags: List of tags associated with the resource.
        """
        self.title = title
        self.resource_type = resource_type
        self.tags = tags

    def to_dict(self) -> Dict:
        """
        Converts the resource to a dictionary format for JSON serialization.
        
        :return: Dictionary representation of the resource.
        """
        return {
            'title': self.title,
            'resource_type': self.resource_type,
            'tags': self.tags
        }

class ResourceCatalog:
    """
    A catalog to manage resources related to museology.
    """

    def __init__(self):
        """
        Initializes an empty resource catalog.
        """
        self.resources: List[Resource] = []

    def add_resource(self, resource: Resource):
        """
        Adds a resource to the catalog.
        
        :param resource: The Resource object to add.
        """
        self.resources.append(resource)
        logging.info(f'Resource added: {resource.title} of type {resource.resource_type}')

    def save_to_file(self, filename: str):
        """
        Saves the catalog to a JSON file.
        
        :param filename: Name of the file to save the resources.
        """
        try:
            with open(filename, 'w') as file:
                json.dump([resource.to_dict() for resource in self.resources], file, indent=4)
            logging.info(f'Resources saved to {filename}')
        except IOError as e:
            logging.error(f'Error saving resources to file: {e}')

    def load_from_file(self, filename: str):
        """
        Loads resources from a JSON file.
        
        :param filename: Name of the file to load resources from.
        """
        try:
            with open(filename, 'r') as file:
                resource_list = json.load(file)
                for resource_data in resource_list:
                    resource = Resource(
                        title=resource_data['title'],
                        resource_type=resource_data['resource_type'],
                        tags=resource_data['tags']
                    )
                    self.add_resource(resource)
            logging.info(f'Resources loaded from {filename}')
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f'Error loading resources from file: {e}')

def main():
    """
    Main function to demonstrate the Resource Catalog functionality.
    """
    catalog = ResourceCatalog()
    
    # Example resources
    catalog.add_resource(Resource("Museology and Its Future", "article", ["museology", "future", "research"]))
    catalog.add_resource(Resource("The Role of Museums", "bibliography", ["museums", "role", "study"]))
    catalog.add_resource(Resource("Documentary on Museum Practices", "video", ["museums", "documentary", "video"]))

    # Save resources to a file
    catalog.save_to_file("resources_catalog.json")

    # Load resources from a file
    catalog.load_from_file("resources_catalog.json")

if __name__ == "__main__":
    main()
```
