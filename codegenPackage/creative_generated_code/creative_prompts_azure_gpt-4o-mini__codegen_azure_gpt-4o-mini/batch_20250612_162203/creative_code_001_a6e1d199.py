"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://educarcomitan.mx
Prompt: How can I implement a library management system for an educational institution that provides resources for admission exam preparation, similar to the "Biblioteca de estudio en casa" mentioned on Educar Comitán?
Generated: DETERMINISTIC_a6e1d199418e6da6
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any, Optional

class LibraryResource:
    """Class to represent a library resource."""
    
    def __init__(self, title: str, author: str, resource_type: str, available: bool = True):
        self.title = title
        self.author = author
        self.resource_type = resource_type
        self.available = available

    def to_dict(self) -> Dict[str, Any]:
        """Convert resource to dictionary for easy JSON serialization."""
        return {
            'title': self.title,
            'author': self.author,
            'resource_type': self.resource_type,
            'available': self.available
        }

class Library:
    """Class to manage a library of resources."""
    
    def __init__(self):
        self.resources: List[LibraryResource] = []

    def add_resource(self, resource: LibraryResource) -> None:
        """Add a new resource to the library."""
        self.resources.append(resource)

    def find_resource(self, title: str) -> Optional[LibraryResource]:
        """Find a resource by title."""
        for resource in self.resources:
            if resource.title.lower() == title.lower():
                return resource
        return None

    def borrow_resource(self, title: str) -> bool:
        """Borrow a resource from the library."""
        resource = self.find_resource(title)
        if resource and resource.available:
            resource.available = False
            return True
        return False

    def return_resource(self, title: str) -> bool:
        """Return a borrowed resource to the library."""
        resource = self.find_resource(title)
        if resource and not resource.available:
            resource.available = True
            return True
        return False

    def list_resources(self) -> List[Dict[str, Any]]:
        """List all resources in the library."""
        return [resource.to_dict() for resource in self.resources]

    def save_to_file(self, filepath: str) -> None:
        """Save the library resources to a file in JSON format."""
        try:
            with open(filepath, 'w') as f:
                json.dump(self.list_resources(), f, indent=4)
        except IOError as e:
            print(f"Error saving to file {filepath}: {e}")

    def load_from_file(self, filepath: str) -> None:
        """Load library resources from a file in JSON format."""
        try:
            with open(filepath, 'r') as f:
                resources_data = json.load(f)
                for data in resources_data:
                    resource = LibraryResource(**data)
                    self.add_resource(resource)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file {filepath}: {e}")

# Example usage
if __name__ == "__main__":
    library = Library()
    library.add_resource(LibraryResource("Python Programming", "John Doe", "Book"))
    library.add_resource(LibraryResource("Data Structures", "Jane Smith", "E-book"))
    
    print("Available resources:")
    print(library.list_resources())

    title_to_borrow = "Python Programming"
    if library.borrow_resource(title_to_borrow):
        print(f"Successfully borrowed '{title_to_borrow}'")
    else:
        print(f"'{title_to_borrow}' is not available for borrowing")

    library.save_to_file("library_resources.json")
    
    new_library = Library()
    new_library.load_from_file("library_resources.json")
    print("Loaded resources:")
    print(new_library.list_resources())
```
