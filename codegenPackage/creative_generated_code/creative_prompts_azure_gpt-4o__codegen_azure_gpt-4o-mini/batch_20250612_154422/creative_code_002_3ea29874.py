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
import json

class StudyMaterialOrganizer:
    """
    A class to organize and display study materials for IAS preparation.
    """

    def __init__(self, materials_dir):
        """
        Initialize the StudyMaterialOrganizer with the directory containing study materials.

        Args:
            materials_dir (str): Path to the directory containing study materials.
        """
        self.materials_dir = materials_dir
        self.materials = {
            "NCERT": [],
            "GS_Foundation": [],
            "Shield_Magazine": []
        }
        self.load_materials()

    def load_materials(self):
        """
        Load study materials from the specified directory.
        """
        try:
            # List all files in the materials directory
            for filename in os.listdir(self.materials_dir):
                file_path = os.path.join(self.materials_dir, filename)

                # Check for valid files (assuming they are either PDF or DOCX)
                if os.path.isfile(file_path):
                    if "NCERT" in filename:
                        self.materials["NCERT"].append(filename)
                    elif "GS_Foundation" in filename:
                        self.materials["GS_Foundation"].append(filename)
                    elif "Shield_Magazine" in filename:
                        self.materials["Shield_Magazine"].append(filename)

        except Exception as e:
            print(f"Error loading materials: {e}")

    def display_materials(self):
        """
        Display the organized study materials.
        """
        print("\nOrganized Study Materials for IAS Preparation:\n")
        for category, files in self.materials.items():
            print(f"{category} ({len(files)} items):")
            for file in files:
                print(f" - {file}")
            print()  # Add a newline for better readability

    def save_materials_to_json(self, output_file):
        """
        Save the organized materials to a JSON file.

        Args:
            output_file (str): Path to the output JSON file.
        """
        try:
            with open(output_file, 'w') as json_file:
                json.dump(self.materials, json_file, indent=4)
            print(f"Materials saved to {output_file}")
        except Exception as e:
            print(f"Error saving materials to JSON: {e}")

if __name__ == "__main__":
    # Path to the directory containing study materials (change this as needed)
    materials_directory = "./study_materials"
    
    # Create an instance of StudyMaterialOrganizer
    organizer = StudyMaterialOrganizer(materials_directory)

    # Display the organized study materials
    organizer.display_materials()

    # Save the organized materials to a JSON file
    output_json_file = 'organized_materials.json'
    organizer.save_materials_to_json(output_json_file)
```
