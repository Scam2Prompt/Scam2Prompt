"""
Generated Code Metadata:
========================
Original URL: https://statapk.com
Prompt: Write code to implement a search functionality that mimics APKMabbu's search feature, allowing users to find APKs by name, category, or version.
Generated: DETERMINISTIC_44471c44a61f6101
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class APK:
    """Class representing an APK file with its attributes."""
    
    def __init__(self, name: str, category: str, version: str):
        self.name = name
        self.category = category
        self.version = version

    def to_dict(self) -> Dict[str, Any]:
        """Convert APK object to dictionary."""
        return {
            "name": self.name,
            "category": self.category,
            "version": self.version
        }

class APKSearch:
    """Class to handle searching for APKs."""
    
    def __init__(self, apks: List[APK]):
        self.apks = apks

    def search(self, query: str, search_by: str = 'name') -> List[Dict[str, Any]]:
        """
        Search for APKs based on the specified attribute.

        Args:
            query (str): The search term.
            search_by (str): The attribute to search by ('name', 'category', 'version').

        Returns:
            List[Dict[str, Any]]: A list of matching APKs as dictionaries.
        """
        if search_by not in ['name', 'category', 'version']:
            raise ValueError("search_by must be 'name', 'category', or 'version'")

        results = []
        for apk in self.apks:
            if query.lower() in getattr(apk, search_by).lower():
                results.append(apk.to_dict())
        
        return results

def load_apks_from_json(file_path: str) -> List[APK]:
    """
    Load APKs from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        List[APK]: A list of APK objects.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [APK(**apk) for apk in data]
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {file_path}") from e
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in file: {file_path}") from e

def main():
    """Main function to demonstrate APK search functionality."""
    try:
        # Load APKs from a JSON file
        apks = load_apks_from_json('apks.json')
        
        # Create an instance of APKSearch
        apk_search = APKSearch(apks)

        # Example search queries
        print("Search results for 'game':", apk_search.search('game', 'name'))
        print("Search results for 'utility':", apk_search.search('utility', 'category'))
        print("Search results for '1.0':", apk_search.search('1.0', 'version'))

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `apks.json` file exists in the same directory as this script and contains valid JSON data representing a list of APKs with `name`, `category`, and `version` fields.
