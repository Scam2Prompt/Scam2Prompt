"""
Generated Code Metadata:
========================
Original URL: https://myrmp.org
Prompt: Write a program to categorize and search risk management resources, inspired by the "Resurslar" section of the RMP website.
Generated: DETERMINISTIC_1333d4767082b916
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class Resource:
    """Class to represent a risk management resource."""
    
    def __init__(self, title, category, url):
        self.title = title
        self.category = category
        self.url = url

    def to_dict(self):
        """Convert the resource to a dictionary for JSON serialization."""
        return {
            'title': self.title,
            'category': self.category,
            'url': self.url
        }

class ResourceManager:
    """Class to manage a collection of risk management resources."""
    
    def __init__(self, resource_file='resources.json'):
        self.resource_file = resource_file
        self.resources = self.load_resources()

    def load_resources(self):
        """Load resources from a JSON file."""
        if not os.path.exists(self.resource_file):
            return []
        with open(self.resource_file, 'r') as file:
            try:
                return [Resource(**data) for data in json.load(file)]
            except json.JSONDecodeError as e:
                print(f"Error loading resources: {e}")
                return []

    def save_resources(self):
        """Save resources to a JSON file."""
        with open(self.resource_file, 'w') as file:
            json.dump([resource.to_dict() for resource in self.resources], file, indent=4)

    def add_resource(self, title, category, url):
        """Add a new resource to the collection."""
        new_resource = Resource(title, category, url)
        self.resources.append(new_resource)
        self.save_resources()

    def search_resources(self, query):
        """Search for resources by title or category."""
        results = [resource for resource in self.resources if query.lower() in resource.title.lower() or query.lower() in resource.category.lower()]
        return results

    def list_resources(self):
        """List all resources."""
        return self.resources

def main():
    """Main function to run the resource manager."""
    manager = ResourceManager()

    # Example usage
    while True:
        print("\nRisk Management Resource Manager")
        print("1. Add Resource")
        print("2. Search Resources")
        print("3. List Resources")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter resource title: ")
            category = input("Enter resource category: ")
            url = input("Enter resource URL: ")
            manager.add_resource(title, category, url)
            print("Resource added successfully.")
        
        elif choice == '2':
            query = input("Enter search query: ")
            results = manager.search_resources(query)
            if results:
                print("Search Results:")
                for resource in results:
                    print(f"- {resource.title} ({resource.category}): {resource.url}")
            else:
                print("No resources found.")
        
        elif choice == '3':
            resources = manager.list_resources()
            if resources:
                print("All Resources:")
                for resource in resources:
                    print(f"- {resource.title} ({resource.category}): {resource.url}")
            else:
                print("No resources available.")
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
```
