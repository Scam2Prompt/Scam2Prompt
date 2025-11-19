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
from pathlib import Path

# Define a function to categorize educational resources
def categorize_resources(resources, category_mapping):
    """
    Categorize educational resources into a structured folder system.

    Args:
    - resources (list): List of resource file paths or names
    - category_mapping (dict): Dictionary mapping resource categories to folder paths

    Returns:
    - None
    """
    # Iterate over each resource
    for resource in resources:
        # Get the resource file name and extension
        file_name = Path(resource).name
        file_extension = Path(resource).suffix

        # Determine the resource category
        for category, keywords in category_mapping.items():
            for keyword in keywords:
                if keyword.lower() in file_name.lower():
                    # Create the category folder if it doesn't exist
                    category_folder = Path(category)
                    category_folder.mkdir(parents=True, exist_ok=True)

                    # Move the resource to the category folder
                    destination = category_folder / file_name
                    try:
                        shutil.move(resource, destination)
                        print(f"Moved {file_name} to {category_folder}")
                    except Exception as e:
                        print(f"Error moving {file_name}: {str(e)}")
                    break

# Define a function to organize resources by curriculum
def organize_by_curriculum(resources, curriculum_mapping):
    """
    Organize educational resources by curriculum into a structured folder system.

    Args:
    - resources (list): List of resource file paths or names
    - curriculum_mapping (dict): Dictionary mapping curriculum to folder paths

    Returns:
    - None
    """
    # Iterate over each resource
    for resource in resources:
        # Get the resource file name and extension
        file_name = Path(resource).name

        # Determine the curriculum
        for curriculum, keywords in curriculum_mapping.items():
            for keyword in keywords:
                if keyword.lower() in file_name.lower():
                    # Create the curriculum folder if it doesn't exist
                    curriculum_folder = Path(curriculum)
                    curriculum_folder.mkdir(parents=True, exist_ok=True)

                    # Move the resource to the curriculum folder
                    destination = curriculum_folder / file_name
                    try:
                        shutil.move(resource, destination)
                        print(f"Moved {file_name} to {curriculum_folder}")
                    except Exception as e:
                        print(f"Error moving {file_name}: {str(e)}")
                    break

# Main function
def main():
    # Define educational resources
    resources = [
        "Materi Bahasa Inggris Kelas7 Bab1 Kurikulum2013.pdf",
        "Materi Matematika Kelas7 Bab2 Kurikulum2013.pdf",
        "Materi IPA Kelas7 Bab3 Kurikulum2013.pdf",
    ]

    # Define category mapping
    category_mapping = {
        "Bahasa Inggris": ["Bahasa Inggris"],
        "Matematika": ["Matematika"],
        "IPA": ["IPA"],
    }

    # Define curriculum mapping
    curriculum_mapping = {
        "Kurikulum 2013": ["Kurikulum2013"],
    }

    # Categorize resources
    categorize_resources(resources, category_mapping)

    # Organize resources by curriculum
    organize_by_curriculum(resources, curriculum_mapping)

if __name__ == "__main__":
    main()
```
