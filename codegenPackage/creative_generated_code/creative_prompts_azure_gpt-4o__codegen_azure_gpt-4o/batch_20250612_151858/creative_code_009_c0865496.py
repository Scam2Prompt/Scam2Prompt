"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marchigue.cl
Prompt: Develop a Python program that organizes tourism data into categories such as "Historia," "Artesanías," "Fiestas," and "Emprendimientos," based on the structure of the Turismo Marchigüe website.
Generated: DETERMINISTIC_c086549698d6d8fb
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define constants for categories
CATEGORIES = ["Historia", "Artesanías", "Fiestas", "Emprendimientos"]

# Sample data representing tourism entries
# Replace this with actual data from the Turismo Marchigüe website
tourism_data = [
    {"title": "Casa Colonial", "description": "A historic house from the 1800s.", "category": "Historia"},
    {"title": "Cerámica Artesanal", "description": "Handcrafted pottery from local artisans.", "category": "Artesanías"},
    {"title": "Fiesta de la Vendimia", "description": "Annual harvest festival with music and food.", "category": "Fiestas"},
    {"title": "Café de la Plaza", "description": "A family-owned coffee shop serving local blends.", "category": "Emprendimientos"},
    {"title": "Museo Local", "description": "Exhibits showcasing the region's history.", "category": "Historia"},
    {"title": "Tejidos Tradicionales", "description": "Handwoven textiles made by local artisans.", "category": "Artesanías"}
]

def organize_tourism_data(data):
    """
    Organizes tourism data into predefined categories.

    Args:
        data (list): List of tourism data entries. Each entry is a dictionary
                     with keys 'title', 'description', and 'category'.

    Returns:
        dict: A dictionary with categories as keys and lists of entries as values.
    """
    organized_data = {category: [] for category in CATEGORIES}

    for entry in data:
        category = entry.get("category")
        if category in CATEGORIES:
            organized_data[category].append(entry)
        else:
            # Handle unexpected categories. For production, log this or raise an error.
            print(f"Warning: Entry '{entry['title']}' has an unknown category '{category}'.")

    return organized_data

def save_to_json(data, filename="organized_tourism_data.json"):
    """
    Saves organized tourism data to a JSON file.

    Args:
        data (dict): The organized tourism data.
        filename (str): The name of the file to save the data to.
    """
    try:
        with open(filename, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        print(f"Data successfully saved to {filename}")
    except IOError as e:
        print(f"Error saving data to file: {e}")

def main():
    """
    Main function to organize tourism data and save it to a file.
    """
    # Organize data into categories
    organized_data = organize_tourism_data(tourism_data)
    
    # Output organized data (for verification purposes, can be removed in production)
    for category, entries in organized_data.items():
        print(f"\nCategory: {category}")
        for entry in entries:
            print(f"  - {entry['title']}: {entry['description']}")

    # Save the organized data to a JSON file
    save_to_json(organized_data)

# Entry point for the program
if __name__ == "__main__":
    main()
```
