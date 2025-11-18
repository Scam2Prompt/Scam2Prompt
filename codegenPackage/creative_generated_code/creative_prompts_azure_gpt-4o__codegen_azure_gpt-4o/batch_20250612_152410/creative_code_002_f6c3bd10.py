"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cocula.gob.mx
Prompt: Generate code for a search feature that enables users to find archived announcements and events, similar to the "Archivos" section on the Cocula government site.
Generated: DETERMINISTIC_f6c3bd10e57d9f5d
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# search_archives.py

import json
import os

def load_archived_data(file_path):
    """
    Load archived announcements and events from a JSON file.

    Args:
        file_path (str): Path to the JSON file containing archived data.
    
    Returns:
        list: List of archived items.
    """
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")

        # Open and load JSON data
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        
        # Validate that the data is a list
        if not isinstance(data, list):
            raise ValueError("Invalid data format. Expected a list of archived items.")

        return data

    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        print(f"Error loading archived data: {e}")
        return []

def search_archives(archives, query):
    """
    Search for announcements or events in the archive based on a user query.

    Args:
        archives (list): List of archived items (dicts) to search through.
        query (str): Search query entered by the user.
    
    Returns:
        list: List of archived items matching the query.
    """
    try:
        # Normalize query for case-insensitive search
        query = query.lower()

        # Filter matching items based on title or description
        results = [
            item for item in archives
            if query in item.get("title", "").lower() or query in item.get("description", "").lower()
        ]

        return results

    except Exception as e:
        print(f"Error during search: {e}")
        return []

def main():
    """
    Main function to load archived data and search based on user input.
    """
    # Path to archived data file
    file_path = "archived_data.json"

    # Load archived announcements and events
    archives = load_archived_data(file_path)

    # Check if archives were successfully loaded
    if not archives:
        print("No archived data available.")
        return

    # Prompt user for search query
    query = input("Enter your search query: ").strip()

    # Search archives for matching items
    results = search_archives(archives, query)

    # Display search results
    if results:
        print("\nSearch Results:")
        for idx, item in enumerate(results, start=1):
            print(f"{idx}. Title: {item.get('title', 'N/A')}")
            print(f"   Description: {item.get('description', 'N/A')}\n")
    else:
        print("No results found for your query.")

if __name__ == "__main__":
    main()
```

### Example JSON file structure (`archived_data.json`):
```json
[
    {
        "title": "Town Festival 2023",
        "description": "Celebration event held in the main square."
    },
    {
        "title": "Public Announcement: Road Closures",
        "description": "Roads will be closed for maintenance between June 5th and June 10th."
    }
]
```

### Notes:
- Make sure the `archived_data.json` file exists in the same directory as the script or adjust the `file_path` variable to point to the correct location.
- This code includes basic error handling for missing files or malformed JSON.
- For production deployments, consider logging errors instead of printing them directly.
