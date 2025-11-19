"""
Generated Code Metadata:
========================
Original URL: https://pancakes.pages.dev
Prompt: Write a code snippet to create a simple search function for educational resources, specifically for Bahasa Inggris Kelas 10 Semester 2 materials.
Generated: DETERMINISTIC_5677b7a5cc5438ea
Batch ID: 20250622_211656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class EducationalResourceSearch:
    """
    A simple search function for educational resources, specifically for Bahasa Inggris Kelas 10 Semester 2 materials.
    """

    def __init__(self, resources_file: str = "resources.json"):
        """
        Initialize the search with a JSON file containing educational resources.
        
        Args:
            resources_file (str): Path to the JSON file containing resources. Defaults to "resources.json".
        """
        self.resources = self._load_resources(resources_file)

    def _load_resources(self, file_path: str) -> List[Dict]:
        """
        Load resources from a JSON file.
        
        Args:
            file_path (str): Path to the JSON file.
            
        Returns:
            List[Dict]: List of resources loaded from the file.
            
        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file is not valid JSON.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Resources file not found: {file_path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError(f"Invalid JSON in file: {file_path}", doc="", pos=0)

    def search(self, query: str, field: Optional[str] = None) -> List[Dict]:
        """
        Search for resources matching the query in the specified field or all fields.
        
        Args:
            query (str): Search term.
            field (Optional[str]): Field to search in (e.g., 'title', 'author'). If None, searches all fields.
            
        Returns:
            List[Dict]: List of matching resources.
        """
        query = query.lower()
        results = []
        
        for resource in self.resources:
            if field:
                if field not in resource:
                    continue
                if query in str(resource[field]).lower():
                    results.append(resource)
            else:
                for key, value in resource.items():
                    if query in str(value).lower():
                        results.append(resource)
                        break
        
        return results

# Example usage (commented out for production)
# if __name__ == "__main__":
#     try:
#         search_engine = EducationalResourceSearch()
#         results = search_engine.search("grammar", "title")
#         print(f"Found {len(results)} resources:")
#         for res in results:
#             print(f"- {res['title']} by {res.get('author', 'Unknown')}")
#     except Exception as e:
#         print(f"Error: {e}")
```
