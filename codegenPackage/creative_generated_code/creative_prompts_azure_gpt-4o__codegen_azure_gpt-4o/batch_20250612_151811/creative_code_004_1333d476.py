"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myrmp.org
Prompt: Write a program to categorize and search risk management resources, inspired by the "Resurslar" section of the RMP website.
Generated: DETERMINISTIC_1333d4767082b916
Batch ID: 20250612_151811
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/risk-assessment-guide": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/compliance-checklist": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here’s a production-ready Python program for categorizing and searching risk management resources:

```python
import json

class ResourceManager:
    """
    Class to manage risk management resources.
    Allows categorization, addition, and searching of resources.
    """

    def __init__(self):
        """
        Initialize the resource manager with an empty resource collection.
        """
        self.resources = {}

    def add_resource(self, category, resource_name, description, url):
        """
        Add a new resource under a specific category.

        :param category: The category under which the resource will be added.
        :param resource_name: The name of the resource.
        :param description: A brief description of the resource.
        :param url: A URL link to the resource.
        """
        if category not in self.resources:
            self.resources[category] = []

        self.resources[category].append({
            "name": resource_name,
            "description": description,
            "url": url
        })

    def search_resources(self, keyword):
        """
        Search for resources containing the keyword in their name or description.

        :param keyword: The keyword to search for.
        :return: A list of matching resources.
        """
        keyword = keyword.lower()
        results = []
        for category, resources in self.resources.items():
            for resource in resources:
                if (keyword in resource["name"].lower() or 
                    keyword in resource["description"].lower()):
                    results.append({
                        "category": category,
                        **resource
                    })
        return results

    def list_categories(self):
        """
        List all available categories.

        :return: A list of category names.
        """
        return list(self.resources.keys())

    def save_to_file(self, filename):
        """
        Save resources to a JSON file.

        :param filename: The name of the file to save the resources.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.resources, file, indent=4)
            print(f"Resources successfully saved to {filename}.")
        except IOError as e:
            print(f"Error saving resources to file: {e}")

    def load_from_file(self, filename):
        """
        Load resources from a JSON file.

        :param filename: The name of the file to load the resources.
        """
        try:
            with open(filename, 'r') as file:
                self.resources = json.load(file)
            print(f"Resources successfully loaded from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty resource collection.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON file: {e}")


# Example Usage
if __name__ == "__main__":
    # Initialize the ResourceManager
    manager = ResourceManager()

    # Add resources
    manager.add_resource(
        "Risk Assessment",
        "Risk Assessment Guide",
        "Comprehensive guide on assessing risks in projects.",
        "https://example.com/risk-assessment-guide"
    )
    manager.add_resource(
        "Compliance",
        "Compliance Checklist",
        "Checklist for ensuring compliance with regulations.",
        "https://example.com/compliance-checklist"
    )

    # Search resources
    print("Search results for 'guide':")
    search_results = manager.search_resources("guide")
    for result in search_results:
        print(result)

    # List categories
    print("\nAvailable Categories:")
    print(manager.list_categories())

    # Save resources to file
    manager.save_to_file("resources.json")

    # Load resources from file
    manager.load_from_file("resources.json")
```

This program is complete, satisfies the requirements, and can be directly run in a Python environment. It includes error handling, comments, and adheres to best practices.
