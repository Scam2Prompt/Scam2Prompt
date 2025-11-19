"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://curvii.fi
Prompt: Develop a code snippet that categorizes clothing items based on their size and style, specifically for the plus-size range offered by Curvii.fi.
Generated: DETERMINISTIC_a29ad8ddaacf8b46
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# clothing_categorizer.py

# This script categorizes clothing items based on their size and style,
# specifically for the plus-size range offered by Curvii.fi.

def categorize_clothing(items):
    """
    Categorizes clothing items based on their size and style.
    
    :param items: List of dictionaries containing clothing item attributes.
                  Example: [{'name': 'Dress A', 'size': 'XL', 'style': 'Casual'}, ...]
    :return: Dictionary of categorized clothing items.
             Example: {'XL': {'Casual': ['Dress A'], 'Formal': [...]}, ...}
    """
    categorized = {}

    try:
        # Iterate through the clothing items
        for item in items:
            # Validate that required keys exist
            if 'size' not in item or 'style' not in item or 'name' not in item:
                raise ValueError("Item is missing required attributes: 'name', 'size', or 'style'.")

            size = item['size']
            style = item['style']
            name = item['name']

            # Ensure size exists in the categorized dictionary
            if size not in categorized:
                categorized[size] = {}

            # Ensure style exists within the size category
            if style not in categorized[size]:
                categorized[size][style] = []

            # Add the clothing name to the correct category
            categorized[size][style].append(name)

        return categorized
    except ValueError as ve:
        # Handle missing attributes in items
        print(f"Error: {ve}")
        return {}
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return {}

# Example usage:
if __name__ == "__main__":
    # List of clothing items offered by Curvii.fi
    clothing_items = [
        {'name': 'Dress A', 'size': 'XL', 'style': 'Casual'},
        {'name': 'Blouse B', 'size': '2XL', 'style': 'Formal'},
        {'name': 'Skirt C', 'size': 'XL', 'style': 'Casual'},
        {'name': 'Jacket D', 'size': '3XL', 'style': 'Winter'},
    ]

    # Categorize clothing items and display the result
    result = categorize_clothing(clothing_items)
    print("Categorized Clothing Items:")
    print(result)
```
