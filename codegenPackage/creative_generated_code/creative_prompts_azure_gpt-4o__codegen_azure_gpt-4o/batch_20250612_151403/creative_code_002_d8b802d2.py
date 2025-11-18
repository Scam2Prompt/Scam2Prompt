"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Generate code to implement a search functionality for a tool catalog, allowing users to filter by categories such as "auto center," "compressors," and "construction civil," based on the structure of the Anhanguera Ferramentas website.
Generated: DETERMINISTIC_d8b802d29a057183
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json

# Sample tool catalog data (mocking a database or API response)
tool_catalog = [
    {"id": 1, "name": "Hydraulic Jack", "category": "auto center"},
    {"id": 2, "name": "Air Compressor", "category": "compressors"},
    {"id": 3, "name": "Concrete Mixer", "category": "construction civil"},
    {"id": 4, "name": "Impact Wrench", "category": "auto center"},
    {"id": 5, "name": "Portable Air Compressor", "category": "compressors"},
    {"id": 6, "name": "Safety Helmet", "category": "construction civil"},
]

def search_tools_by_category(category):
    """
    Search tools in the catalog based on the given category.

    Args:
        category (str): The category to filter tools by.

    Returns:
        list: A list of tools matching the category.
    """
    try:
        # Validate input
        if not category or not isinstance(category, str):
            raise ValueError("Invalid category. It must be a non-empty string.")

        # Filter tools by category
        filtered_tools = [tool for tool in tool_catalog if tool["category"].lower() == category.lower()]

        # Return results
        return filtered_tools

    except Exception as e:
        # Log and handle any unexpected errors
        print(f"Error during search: {e}")
        return []

def main():
    """
    Main function to demonstrate the search functionality.
    """
    print("Welcome to the Tool Catalog Search!")
    
    # Let the user specify the category they want to search for
    user_category = input("Enter a category to search (e.g., auto center, compressors, construction civil): ").strip()

    # Perform the search
    results = search_tools_by_category(user_category)

    # Display the results
    if results:
        print(f"Tools found in category '{user_category}':")
        print(json.dumps(results, indent=4))
    else:
        print(f"No tools found in category '{user_category}'.")

# Entry point for the script
if __name__ == "__main__":
    main()
```
