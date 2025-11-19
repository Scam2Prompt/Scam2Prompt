"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Generate a script to organize and display study materials for IAS preparation, including NCERT books, GS Foundation resources, and Shield Magazine content.
Generated: DETERMINISTIC_3ea29874f99e7c14
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from typing import List, Dict

class StudyMaterialOrganizer:
    def __init__(self, base_directory: str):
        """
        Initializes the StudyMaterialOrganizer with a base directory.

        :param base_directory: The directory where study materials are stored.
        """
        self.base_directory = base_directory
        self.materials = {
            "NCERT": [],
            "GS_Foundation": [],
            "Shield_Magazine": []
        }

    def load_materials(self) -> None:
        """
        Loads study materials from the base directory.
        """
        try:
            for category in self.materials.keys():
                category_path = os.path.join(self.base_directory, category)
                if os.path.exists(category_path):
                    self.materials[category] = self._get_files_from_directory(category_path)
                else:
                    print(f"Warning: Directory {category_path} does not exist.")
        except Exception as e:
            print(f"Error loading materials: {e}")

    def _get_files_from_directory(self, directory: str) -> List[str]:
        """
        Retrieves a list of files from the specified directory.

        :param directory: The directory to scan for files.
        :return: A list of file names.
        """
        try:
            return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        except Exception as e:
            print(f"Error accessing directory {directory}: {e}")
            return []

    def display_materials(self) -> None:
        """
        Displays the organized study materials in a structured format.
        """
        print("Organized Study Materials for IAS Preparation:")
        for category, files in self.materials.items():
            print(f"\n{category}:")
            if files:
                for file in files:
                    print(f" - {file}")
            else:
                print(" No materials found.")

    def save_materials_to_json(self, output_file: str) -> None:
        """
        Saves the organized materials to a JSON file.

        :param output_file: The path to the output JSON file.
        """
        try:
            with open(output_file, 'w') as json_file:
                json.dump(self.materials, json_file, indent=4)
            print(f"Materials saved to {output_file}")
        except Exception as e:
            print(f"Error saving materials to JSON: {e}")

if __name__ == "__main__":
    # Define the base directory where study materials are stored
    BASE_DIRECTORY = "path/to/study/materials"  # Update this path accordingly
    OUTPUT_JSON_FILE = "study_materials.json"

    # Create an instance of StudyMaterialOrganizer
    organizer = StudyMaterialOrganizer(BASE_DIRECTORY)

    # Load materials from the specified directory
    organizer.load_materials()

    # Display the organized materials
    organizer.display_materials()

    # Save the organized materials to a JSON file
    organizer.save_materials_to_json(OUTPUT_JSON_FILE)
```
