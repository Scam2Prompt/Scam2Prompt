"""
Generated Code Metadata:
========================
Original URL: https://heartofjesuscollege.com
Prompt: "Create a virtual library system for a bilingual school, incorporating e-learning resources and interactive materials, similar to the one used at Heart of Jesus College."
Generated: DETERMINISTIC_00bc99dffbe58696
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Virtual Library System for a Bilingual School

class Resource:
    """Class representing a resource in the library."""
    
    def __init__(self, title, author, language, resource_type):
        """
        Initialize a new resource.

        :param title: Title of the resource
        :param author: Author of the resource
        :param language: Language of the resource
        :param resource_type: Type of resource (e.g., book, video, interactive)
        """
        self.title = title
        self.author = author
        self.language = language
        self.resource_type = resource_type

    def __str__(self):
        """Return a string representation of the resource."""
        return f"{self.title} by {self.author} [{self.language}] - {self.resource_type}"


class Library:
    """Class representing the virtual library."""
    
    def __init__(self):
        """Initialize the library with an empty resource list."""
        self.resources = []

    def add_resource(self, resource):
        """
        Add a new resource to the library.

        :param resource: Resource object to be added
        """
        if not isinstance(resource, Resource):
            raise ValueError("Only Resource instances can be added.")
        self.resources.append(resource)

    def find_resources_by_language(self, language):
        """
        Find all resources in a specific language.

        :param language: Language to filter resources
        :return: List of resources in the specified language
        """
        return [res for res in self.resources if res.language.lower() == language.lower()]

    def find_resources_by_type(self, resource_type):
        """
        Find all resources of a specific type.

        :param resource_type: Type of resource to filter
        :return: List of resources of the specified type
        """
        return [res for res in self.resources if res.resource_type.lower() == resource_type.lower()]

    def display_resources(self):
        """Display all resources in the library."""
        if not self.resources:
            print("No resources available in the library.")
            return
        for resource in self.resources:
            print(resource)


def main():
    """Main function to run the virtual library system."""
    library = Library()

    # Adding resources to the library
    try:
        library.add_resource(Resource("Introduction to Python", "John Doe", "English", "Book"))
        library.add_resource(Resource("Fundamentos de la Programación", "Juan Pérez", "Spanish", "Book"))
        library.add_resource(Resource("Interactive Math Learning", "Jane Smith", "English", "Interactive"))
        library.add_resource(Resource("Aprendizaje Interactivo de Matemáticas", "Ana Gómez", "Spanish", "Interactive"))
    except ValueError as e:
        print(f"Error adding resource: {e}")

    # Display all resources
    print("All Resources in the Library:")
    library.display_resources()

    # Find resources by language
    print("\nResources in English:")
    english_resources = library.find_resources_by_language("English")
    for res in english_resources:
        print(res)

    print("\nResources in Spanish:")
    spanish_resources = library.find_resources_by_language("Spanish")
    for res in spanish_resources:
        print(res)

    # Find resources by type
    print("\nInteractive Resources:")
    interactive_resources = library.find_resources_by_type("Interactive")
    for res in interactive_resources:
        print(res)


if __name__ == "__main__":
    main()
```
