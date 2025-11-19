"""
Generated Code Metadata:
========================
Original URL: https://pancakes.pages.dev
Prompt: Generate a Python script to categorize and organize educational resources, such as Materi Bahasa Inggris Kelas 7 Bab 1 Kurikulum 2013, into a structured folder system.
Generated: DETERMINISTIC_bd3984439af3429a
Batch ID: 20250622_211656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import shutil

class ResourceOrganizer:
    def __init__(self, base_directory):
        """
        Initializes the ResourceOrganizer with a base directory.
        
        :param base_directory: The root directory where resources will be organized.
        """
        self.base_directory = base_directory
        self.create_base_directory()

    def create_base_directory(self):
        """Creates the base directory if it does not exist."""
        try:
            os.makedirs(self.base_directory, exist_ok=True)
            print(f"Base directory '{self.base_directory}' is ready.")
        except Exception as e:
            print(f"Error creating base directory: {e}")

    def categorize_resource(self, resource_name):
        """
        Categorizes a resource based on its name and organizes it into a structured folder system.
        
        :param resource_name: The name of the resource to categorize.
        """
        try:
            # Example: Extracting subject, grade, and chapter from the resource name
            parts = resource_name.split(" ")
            subject = parts[0]  # e.g., 'Materi'
            grade = parts[2]    # e.g., 'Kelas'
            chapter = parts[4]  # e.g., 'Bab'

            # Create a structured path
            resource_path = os.path.join(self.base_directory, subject, grade, chapter)
            os.makedirs(resource_path, exist_ok=True)

            # Simulate moving the resource file (for demonstration purposes)
            # In a real scenario, you would move an actual file here
            resource_file = f"{resource_name}.pdf"  # Example file name
            self.move_resource(resource_file, resource_path)

        except Exception as e:
            print(f"Error categorizing resource '{resource_name}': {e}")

    def move_resource(self, resource_file, destination):
        """
        Moves a resource file to the specified destination.
        
        :param resource_file: The name of the resource file to move.
        :param destination: The destination directory where the file should be moved.
        """
        try:
            # Simulate moving the file (this is just a placeholder)
            # In a real scenario, you would use shutil.move() to move an actual file
            print(f"Moving '{resource_file}' to '{destination}'")
            # shutil.move(resource_file, destination)  # Uncomment this line in production
        except Exception as e:
            print(f"Error moving resource file '{resource_file}': {e}")

if __name__ == "__main__":
    # Example usage
    base_dir = "Educational_Resources"
    organizer = ResourceOrganizer(base_dir)

    # List of resources to categorize
    resources = [
        "Materi Bahasa Inggris Kelas 7 Bab 1 Kurikulum 2013",
        "Materi Matematika Kelas 7 Bab 2 Kurikulum 2013",
        "Materi IPA Kelas 7 Bab 3 Kurikulum 2013"
    ]

    for resource in resources:
        organizer.categorize_resource(resource)
```
