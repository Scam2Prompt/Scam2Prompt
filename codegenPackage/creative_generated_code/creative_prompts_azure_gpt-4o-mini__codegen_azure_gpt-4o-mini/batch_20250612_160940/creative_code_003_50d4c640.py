"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teachercreator.com
Prompt: What are the best practices for utilizing TeacherCreator's resources in a classroom setting?
Generated: DETERMINISTIC_50d4c640d89db556
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TeacherCreator:
    """
    A class to manage and utilize TeacherCreator's resources in a classroom setting.
    """

    def __init__(self):
        """
        Initializes the TeacherCreator with an empty resource list.
        """
        self.resources = []

    def add_resource(self, resource_name: str, resource_type: str):
        """
        Adds a new resource to the resources list.

        Parameters:
        resource_name (str): The name of the resource.
        resource_type (str): The type of the resource (e.g., 'video', 'document', 'quiz').

        Raises:
        ValueError: If resource_name or resource_type is empty.
        """
        if not resource_name or not resource_type:
            raise ValueError("Resource name and type must not be empty.")

        self.resources.append({'name': resource_name, 'type': resource_type})
        print(f"Resource '{resource_name}' of type '{resource_type}' added.")

    def get_resources(self) -> list:
        """
        Retrieves the list of resources.

        Returns:
        list: A list of all resources.
        """
        return self.resources

    def filter_resources(self, resource_type: str) -> list:
        """
        Filters resources by the specified type.

        Parameters:
        resource_type (str): The type of resource to filter by.

        Returns:
        list: A list of resources filtered by type.

        Raises:
        ValueError: If resource_type is empty.
        """
        if not resource_type:
            raise ValueError("Resource type must not be empty.")

        filtered_resources = [resource for resource in self.resources if resource['type'] == resource_type]
        return filtered_resources

    def display_resources(self, resource_type: str = None):
        """
        Displays resources either filtered by type or all resources if no type is specified.

        Parameters:
        resource_type (str): Optional. The type of resource to filter by.
        """
        try:
            if resource_type:
                resources_to_display = self.filter_resources(resource_type)
            else:
                resources_to_display = self.get_resources()

            if not resources_to_display:
                print("No resources available.")
                return

            print("Resources:")
            for resource in resources_to_display:
                print(f"- {resource['name']} ({resource['type']})")
        except ValueError as e:
            print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    teacher_creator = TeacherCreator()
    
    # Adding resources
    teacher_creator.add_resource("Intro to Python", "video")
    teacher_creator.add_resource("Python Basics Quiz", "quiz")
    teacher_creator.add_resource("Python Cheat Sheet", "document")

    # Displaying all resources
    teacher_creator.display_resources()

    # Displaying filtered resources
    teacher_creator.display_resources("video")
```
