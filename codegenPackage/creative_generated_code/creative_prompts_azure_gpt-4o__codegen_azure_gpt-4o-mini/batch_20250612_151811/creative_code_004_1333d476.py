"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myrmp.org
Prompt: Write a program to categorize and search risk management resources, inspired by the "Resurslar" section of the RMP website.
Generated: DETERMINISTIC_1333d4767082b916
Batch ID: 20250612_151811
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/risk-basics": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Optional

class Resource:
    """
    Class to represent a risk management resource.
    """

    def __init__(self, title: str, category: str, link: str):
        """
        Initializes a Resource instance.

        :param title: The title of the resource.
        :param category: The category of the resource.
        :param link: The URL link to the resource.
        """
        self.title = title
        self.category = category
        self.link = link

    def to_dict(self) -> Dict[str, str]:
        """
        Converts the resource to a dictionary format.

        :return: A dictionary representation of the resource.
        """
        return {
            "title": self.title,
            "category": self.category,
            "link": self.link
        }

class ResourceManager:
    """
    Class to manage a collection of resources.
    """

    def __init__(self):
        """
        Initializes the ResourceManager with an empty resource list.
        """
        self.resources: List[Resource] = []

    def add_resource(self, resource: Resource) -> None:
        """
        Adds a resource to the collection.

        :param resource: An instance of Resource to add.
        """
        self.resources.append(resource)

    def get_resources_by_category(self, category: str) -> List[Resource]:
        """
        Retrieves resources that belong to a specified category.

        :param category: The category to filter resources by.
        :return: A list of resources in the specified category.
        """
        return [resource for resource in self.resources if resource.category.lower() == category.lower()]

    def search_resources(self, keyword: str) -> List[Resource]:
        """
        Searches for resources containing the keyword in the title.

        :param keyword: The keyword to search for in resource titles.
        :return: A list of resources that match the search keyword.
        """
        return [resource for resource in self.resources if keyword.lower() in resource.title.lower()]

    def load_resources_from_json(self, file_path: str) -> None:
        """
        Loads resources from a JSON file.

        :param file_path: The file path to the JSON file containing resources.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                for item in data:
                    resource = Resource(title=item['title'], category=item['category'], link=item['link'])
                    self.add_resource(resource)
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except json.JSONDecodeError:
            print(f"Error: The file '{file_path}' contains invalid JSON.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def save_resources_to_json(self, file_path: str) -> None:
        """
        Saves resources to a JSON file.

        :param file_path: The file path to save the JSON file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump([resource.to_dict() for resource in self.resources], file, indent=4)
        except Exception as e:
            print(f"An unexpected error occurred while saving the file: {e}")

# Example usage
if __name__ == "__main__":
    manager = ResourceManager()
    
    # Load resources from a JSON file
    manager.load_resources_from_json('resources.json')

    # Add a resource manually
    manager.add_resource(Resource("Risk Management Basics", "Education", "https://example.com/risk-basics"))

    # Get resources by category
    education_resources = manager.get_resources_by_category("Education")
    print("Education Resources:")
    for resource in education_resources:
        print(resource.to_dict())

    # Search resources
    search_results = manager.search_resources("risk")
    print("\nSearch Results for 'risk':")
    for resource in search_results:
        print(resource.to_dict())

    # Save updated resources to a JSON file
    manager.save_resources_to_json('updated_resources.json')
```
