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
# Import necessary modules
import json

def search_resources(query, resources):
    """
    Search for educational resources based on a query.

    Args:
        query (str): The search term provided by the user.
        resources (list): A list of dictionaries containing resource data.

    Returns:
        list: A list of resources that match the search query.
    """
    try:
        # Ensure the query is a string
        if not isinstance(query, str):
            raise ValueError("Query must be a string.")

        # Normalize query for case-insensitive search
        query = query.lower()

        # Filter resources based on the query
        matching_resources = [
            resource for resource in resources
            if query in resource.get('title', '').lower() or query in resource.get('description', '').lower()
        ]

        return matching_resources

    except Exception as e:
        # Log the error and return an empty list
        print(f"An error occurred during the search: {e}")
        return []

# Example resources data (normally this would come from a database or API)
resources_data = [
    {"id": 1, "title": "Bahasa Inggris Kelas 10 Semester 2 - Grammar Basics", "description": "Learn the fundamentals of English grammar."},
    {"id": 2, "title": "Bahasa Inggris Kelas 10 Semester 2 - Vocabulary Expansion", "description": "Expand your English vocabulary with practical examples."},
    {"id": 3, "title": "Bahasa Inggris Kelas 10 Semester 2 - Reading Comprehension", "description": "Improve your reading skills with engaging texts."},
    {"id": 4, "title": "Bahasa Inggris Kelas 10 Semester 1 - Writing Skills", "description": "Develop your writing skills effectively."}
]

# Example usage
if __name__ == "__main__":
    # User query
    user_query = "Semester 2"

    # Perform the search
    results = search_resources(user_query, resources_data)

    # Display the results
    if results:
        print("Search Results:")
        print(json.dumps(results, indent=4))
    else:
        print("No matching resources found.")
```
