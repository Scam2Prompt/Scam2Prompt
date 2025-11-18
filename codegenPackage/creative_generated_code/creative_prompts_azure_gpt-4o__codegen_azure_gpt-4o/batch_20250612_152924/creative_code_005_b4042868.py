"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beta.metis-lab.com
Prompt: Develop a program to categorize and tag articles, bibliographies, and video resources related to museology, using the structure provided on the Mêtis Lab website.
Generated: DETERMINISTIC_b404286846c0590b
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Union

# Define a type alias for resource data
Resource = Dict[str, Union[str, List[str]]]

class ResourceCategorizer:
    """
    ResourceCategorizer class to categorize and tag resources such as articles,
    bibliographies, and videos related to museology.
    """
    
    def __init__(self):
        # Initialize dictionaries for categories and tags
        self.categories = {
            "articles": [],
            "bibliographies": [],
            "videos": []
        }
        self.tags = {}

    def add_resource(self, resource_type: str, resource_data: Resource):
        """
        Add a resource to a specific category.

        Args:
            resource_type (str): Type of the resource ('articles', 'bibliographies', 'videos').
            resource_data (Resource): Resource data containing title, description, and tags.

        Raises:
            ValueError: If resource_type is invalid or required fields are missing.
        """
        # Validate resource type
        if resource_type not in self.categories:
            raise ValueError(f"Invalid resource type: {resource_type}")
        
        # Validate required fields
        if "title" not in resource_data or "tags" not in resource_data:
            raise ValueError("Resource must include 'title' and 'tags'.")
        
        # Add resource to the appropriate category
        self.categories[resource_type].append(resource_data)
        self._update_tags(resource_data["tags"])

    def _update_tags(self, tags: List[str]):
        """
        Update the global tag index with the given tags.

        Args:
            tags (List[str]): List of tags to update.
        """
        for tag in tags:
            if tag in self.tags:
                self.tags[tag] += 1
            else:
                self.tags[tag] = 1

    def search_by_tag(self, tag: str) -> Dict[str, List[Resource]]:
        """
        Search for resources by a specific tag.

        Args:
            tag (str): Tag to search for.

        Returns:
            Dict[str, List[Resource]]: Resources that match the given tag, grouped by category.
        """
        result = {category: [] for category in self.categories}

        for category, resources in self.categories.items():
            for resource in resources:
                if tag in resource.get("tags", []):
                    result[category].append(resource)
        
        return result

    def save_to_json(self, filepath: str):
        """
        Save the categorized resources and tags to a JSON file.

        Args:
            filepath (str): Path to the output JSON file.
        """
        data = {
            "categories": self.categories,
            "tags": self.tags
        }
        try:
            with open(filepath, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_json(self, filepath: str):
        """
        Load categorized resources and tags from a JSON file.

        Args:
            filepath (str): Path to the input JSON file.

        Raises:
            IOError: If there's an issue reading the file.
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.categories = data.get("categories", {})
                self.tags = data.get("tags", {})
        except IOError as e:
            print(f"Error loading from file: {e}")


# Example usage
if __name__ == "__main__":
    categorizer = ResourceCategorizer()

    # Adding resources
    try:
        categorizer.add_resource(
            "articles",
            {
                "title": "The Role of Museums in Modern Society",
                "description": "An in-depth analysis of museums in contemporary culture.",
                "tags": ["museology", "culture", "society"]
            }
        )

        categorizer.add_resource(
            "videos",
            {
                "title": "Museum Exhibition Design",
                "description": "A video tutorial on designing engaging museum exhibits.",
                "tags": ["design", "exhibitions", "museology"]
            }
        )

        # Search by tag
        search_results = categorizer.search_by_tag("museology")
        print("Search Results for tag 'museology':", json.dumps(search_results, indent=4))

        # Save to JSON
        categorizer.save_to_json("resources.json")

        # Load from JSON
        categorizer.load_from_json("resources.json")
        print("Resources loaded from file:", json.dumps(categorizer.categories, indent=4))

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
```
