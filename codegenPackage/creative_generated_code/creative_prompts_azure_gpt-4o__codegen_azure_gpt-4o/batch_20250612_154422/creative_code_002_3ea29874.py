"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shieldias.in
Prompt: Generate a script to organize and display study materials for IAS preparation, including NCERT books, GS Foundation resources, and Shield Magazine content.
Generated: DETERMINISTIC_3ea29874f99e7c14
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

class StudyMaterialOrganizer:
    """
    A class to organize and display study materials for IAS preparation.
    Includes categories such as NCERT books, GS Foundation resources, and Shield Magazine content.
    """
    
    def __init__(self, storage_directory):
        """
        Initializes the organizer with a storage directory.
        
        :param storage_directory: Path to the directory where study materials are stored.
        """
        self.storage_directory = storage_directory
        self.categories = {
            "NCERT Books": os.path.join(storage_directory, "NCERT"),
            "GS Foundation Resources": os.path.join(storage_directory, "GS_Foundation"),
            "Shield Magazine": os.path.join(storage_directory, "Shield_Magazine")
        }

        # Ensure directories exist
        self._create_directories()

    def _create_directories(self):
        """
        Creates directories for each category if they do not already exist.
        """
        for category, path in self.categories.items():
            if not os.path.exists(path):
                try:
                    os.makedirs(path)
                except OSError as e:
                    print(f"Error creating directory {path}: {e}")

    def add_material(self, category, filename, content):
        """
        Adds study material to the specified category.

        :param category: Category to add the material to (e.g., 'NCERT Books').
        :param filename: Name of the file to create.
        :param content: Content to write into the file.
        """
        if category not in self.categories:
            print(f"Invalid category: '{category}'. Available categories are: {list(self.categories.keys())}")
            return

        file_path = os.path.join(self.categories[category], filename)
        try:
            with open(file_path, 'w') as file:
                file.write(content)
            print(f"Material '{filename}' added to '{category}'")
        except OSError as e:
            print(f"Error writing to file {file_path}: {e}")

    def display_materials(self):
        """
        Displays the study materials organized under each category.
        """
        print("Study Materials:")
        for category, path in self.categories.items():
            print(f"\n{category}:")
            try:
                materials = os.listdir(path)
                if not materials:
                    print("  No materials found.")
                else:
                    for material in materials:
                        print(f"  - {material}")
            except OSError as e:
                print(f"Error reading directory {path}: {e}")


# Example Usage
if __name__ == "__main__":
    # Set up the organizer
    organizer = StudyMaterialOrganizer(storage_directory="StudyMaterials")

    # Add some materials (for demonstration purposes)
    organizer.add_material("NCERT Books", "History_Class_6.txt", "Content of History Class 6 NCERT.")
    organizer.add_material("GS Foundation Resources", "GS_Paper_I.txt", "Content of GS Paper I.")
    organizer.add_material("Shield Magazine", "Shield_2023_January.txt", "Content of Shield January 2023.")

    # Display organized materials
    organizer.display_materials()
```
