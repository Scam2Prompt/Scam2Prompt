"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blocprest.ro
Prompt: Write a script to categorize and assign cleaning tasks for residential blocks based on BlocPrest's cleaning services.
Generated: DETERMINISTIC_28f417e06c2952cb
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to categorize and assign cleaning tasks for residential blocks based on BlocPrest's cleaning services.
"""

import json

# Define cleaning categories and services offered by BlocPrest
CLEANING_SERVICES = {
    "basic": ["sweeping", "dusting", "mopping"],
    "deep": ["vacuuming", "window cleaning", "furniture polishing"],
    "exterior": ["garden maintenance", "pressure washing", "parking lot cleaning"]
}

# Sample residential blocks data (replace this with actual data source, e.g., database or API)
RESIDENTIAL_BLOCKS = [
    {"block_id": 1, "name": "Sunshine Apartments", "type": "basic"},
    {"block_id": 2, "name": "Maple Heights", "type": "deep"},
    {"block_id": 3, "name": "Oak Residencies", "type": "exterior"}
]

def categorize_cleaning_tasks(blocks, services):
    """
    Categorize and assign cleaning tasks for residential blocks.

    Args:
        blocks (list): List of residential blocks. Each block is a dictionary with 'block_id', 'name', and 'type'.
        services (dict): Dictionary of cleaning services categorized by type.

    Returns:
        dict: Dictionary containing block_id as keys and assigned services as values.
    """
    categorized_tasks = {}
    
    for block in blocks:
        block_id = block.get("block_id")
        block_type = block.get("type")
        
        # Validate block_type and assign services
        if block_type not in services:
            print(f"Warning: Block '{block.get('name')}' has an unrecognized cleaning type '{block_type}'. Skipping.")
            continue
        
        categorized_tasks[block_id] = {
            "block_name": block.get("name"),
            "assigned_tasks": services[block_type]
        }
    
    return categorized_tasks

def save_to_file(data, filename):
    """
    Save categorized tasks to a JSON file.

    Args:
        data (dict): Categorized tasks to save.
        filename (str): File path to save the JSON data.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Categorized tasks successfully saved to '{filename}'.")
    except Exception as e:
        print(f"Error saving tasks to file: {e}")

def main():
    """
    Main function to execute the script.
    """
    print("Categorizing cleaning tasks for residential blocks...")
    categorized_tasks = categorize_cleaning_tasks(RESIDENTIAL_BLOCKS, CLEANING_SERVICES)
    
    # Display categorized tasks
    print("Cleaning Tasks Categorized:")
    for block_id, tasks in categorized_tasks.items():
        print(f"Block ID {block_id}: {tasks}")
    
    # Save categorized tasks to a file
    save_to_file(categorized_tasks, "categorized_tasks.json")

if __name__ == "__main__":
    main()
```
