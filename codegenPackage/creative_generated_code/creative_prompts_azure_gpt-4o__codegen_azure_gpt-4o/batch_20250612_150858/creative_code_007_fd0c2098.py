"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vansoltravel.com
Prompt: Write a program to extract and categorize Vansol Travel's tour packages by activity type, such as adventure tours or pilgrimage tours.
Generated: DETERMINISTIC_fd0c20986427203c
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Sample tour package data (this would typically come from a database or API)
tour_packages = [
    {"id": 1, "name": "Mountain Adventure", "type": "adventure", "price": 1200},
    {"id": 2, "name": "Beach Relaxation", "type": "leisure", "price": 800},
    {"id": 3, "name": "Historical Pilgrimage", "type": "pilgrimage", "price": 1500},
    {"id": 4, "name": "Rainforest Expedition", "type": "adventure", "price": 1000},
    {"id": 5, "name": "City Exploration", "type": "leisure", "price": 450},
    {"id": 6, "name": "Sacred Temple Tour", "type": "pilgrimage", "price": 1350},
]

def categorize_tour_packages(packages):
    """
    Categorizes a list of tour packages by their activity type.

    Args:
        packages (list): A list of dictionaries where each dictionary represents a tour package.

    Returns:
        dict: A dictionary where the keys are activity types, and the values are lists of packages.
    """
    categorized_packages = {}
    for package in packages:
        activity_type = package.get("type")
        if not activity_type:
            continue  # Skip packages without a type

        if activity_type not in categorized_packages:
            categorized_packages[activity_type] = []  # Initialize the category if it doesn't exist

        categorized_packages[activity_type].append(package)  # Add the package to the appropriate category

    return categorized_packages

def save_to_file(data, filename):
    """
    Saves the categorized tour packages to a JSON file.

    Args:
        data (dict): Categorized tour packages.
        filename (str): The name of the file to save the data to.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

def main():
    """
    Main function to extract and categorize Vansol Travel's tour packages.
    """
    print("Categorizing tour packages...")
    categorized_packages = categorize_tour_packages(tour_packages)
    
    # Display categorized packages
    print("Categorized Packages:")
    for category, packages in categorized_packages.items():
        print(f"Category: {category}")
        for package in packages:
            print(f"  - {package['name']} (${package['price']})")

    # Save categorized packages to a JSON file
    save_to_file(categorized_packages, "categorized_tour_packages.json")

if __name__ == "__main__":
    main()
```
