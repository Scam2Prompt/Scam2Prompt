"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mnswap.org
Prompt: Develop a script to organize and categorize regulatory resources for activity professionals, inspired by MN SWAP's regulatory resources section.
Generated: DETERMINISTIC_b9d37b4fa1d1c2a7
Batch ID: 20250612_142640
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
from pathlib import Path

# Constants
REGULATORY_RESOURCES_DIR = "regulatory_resources"
CATEGORIES_FILE = "categories.json"

def create_directory_structure(base_dir, categories):
    """
    Create a directory structure for categorizing regulatory resources.

    :param base_dir: The base directory where all categorized folders will be created.
    :param categories: A list of categories to create folders for.
    """
    try:
        for category in categories:
            category_path = Path(base_dir) / category
            category_path.mkdir(parents=True, exist_ok=True)
            print(f"Created/Checked folder: {category_path}")
    except Exception as e:
        print(f"Error creating directory structure: {e}")
        raise

def categorize_resources(base_dir, resources):
    """
    Organize regulatory resources into appropriate category folders.

    :param base_dir: The base directory where categorized folders exist.
    :param resources: A dictionary with resource names as keys and their categories as values.
    """
    try:
        for resource, category in resources.items():
            category_path = Path(base_dir) / category
            resource_path = Path(base_dir) / resource

            if category_path.exists() and resource_path.exists():
                # Move the resource to its category folder
                destination = category_path / resource
                resource_path.rename(destination)
                print(f"Moved {resource} to {destination}")
            else:
                print(f"Skipping {resource}: Either source file or category folder does not exist.")
    except Exception as e:
        print(f"Error categorizing resources: {e}")
        raise

def load_categories(file_path):
    """
    Load categories from a JSON file.

    :param file_path: Path to the categories JSON file.
    :return: A list of categories.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Categories file not found: {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding categories file: {file_path}")
        return []
    except Exception as e:
        print(f"Unexpected error loading categories file: {e}")
        raise

def main():
    """
    Main function to organize and categorize regulatory resources for activity professionals.
    """
    # Load categories
    categories = load_categories(CATEGORIES_FILE)
    if not categories:
        print("No categories found. Exiting.")
        return

    # Create directory structure
    create_directory_structure(REGULATORY_RESOURCES_DIR, categories)

    # Example resources for categorization (this would typically be dynamically loaded or input)
    resources_to_categorize = {
        "resource1.pdf": "Category1",
        "resource2.docx": "Category2",
        "resource3.txt": "Category1",
    }

    # Categorize resources
    categorize_resources(REGULATORY_RESOURCES_DIR, resources_to_categorize)

if __name__ == "__main__":
    # Create the base directory if it doesn't exist
    Path(REGULATORY_RESOURCES_DIR).mkdir(parents=True, exist_ok=True)
    
    main()
```
