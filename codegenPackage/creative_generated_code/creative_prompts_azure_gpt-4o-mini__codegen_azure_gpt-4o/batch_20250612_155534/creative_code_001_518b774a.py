"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reward-beamtoken.net
Prompt: Write a Python script that organizes a garage space using IKEA's storage ideas as a guideline.
Generated: DETERMINISTIC_518b774ace23a3dd
Batch ID: 20250612_155534
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

# Define the storage categories based on IKEA's guidelines
STORAGE_CATEGORIES = {
    "tools": ["hammer", "screwdriver", "wrench", "drill"],
    "sports_equipment": ["bicycle", "soccer ball", "tennis racket", "helmet"],
    "cleaning_supplies": ["broom", "mop", "detergent", "sponges"],
    "seasonal_items": ["holiday decorations", "snow shovel", "beach umbrella"],
    "miscellaneous": []  # Catch-all category
}

# Define the garage space layout
GARAGE_LAYOUT = {
    "wall_shelves": [],
    "floor_bins": [],
    "ceiling_hooks": [],
    "storage_cabinets": [],
    "miscellaneous": []  # For items that don't fit other storage solutions
}

def load_items(file_path):
    """
    Load items from a JSON file. Each item should have a name and category.
    :param file_path: Path to the JSON file containing garage items.
    :return: List of items.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    
    with open(file_path, 'r') as file:
        try:
            items = json.load(file)
            if not isinstance(items, list):
                raise ValueError("The JSON file must contain a list of items.")
            return items
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON: {str(e)}")

def organize_items(items):
    """
    Organize items into the garage layout based on their category.
    :param items: List of items to be organized.
    :return: Updated garage layout.
    """
    for item in items:
        name = item.get("name")
        category = item.get("category")
        
        if not name or not category:
            print(f"Skipping item with missing name or category: {item}")
            continue
        
        # Place items in appropriate storage category
        if category in STORAGE_CATEGORIES:
            GARAGE_LAYOUT["wall_shelves"].append(name) if category == "tools" else None
            GARAGE_LAYOUT["floor_bins"].append(name) if category == "sports_equipment" else None
        #....
