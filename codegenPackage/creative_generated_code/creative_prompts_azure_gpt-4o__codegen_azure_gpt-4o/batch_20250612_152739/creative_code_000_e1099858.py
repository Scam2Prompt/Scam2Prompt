"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activesport.cz
Prompt: Write a Python script to categorize sports equipment into "cycling," "camping," "skiing," and "hiking" based on product descriptions and tags, as seen on the ActiveSport.cz website.
Generated: DETERMINISTIC_e10998587011cfa4
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def categorize_sports_equipment(product_description, product_tags):
    """
    Categorize sports equipment based on product description and tags.

    Args:
        product_description (str): The product description text.
        product_tags (list): A list of tags associated with the product.

    Returns:
        str: The category of the product ("cycling", "camping", "skiing", "hiking", or "uncategorized").
    """
    # Define keywords for each category
    categories = {
        "cycling": ["bike", "cycling", "helmet", "bicycle", "chain", "pedal"],
        "camping": ["tent", "camping", "sleeping bag", "backpack", "campfire", "stove"],
        "skiing": ["ski", "skiing", "snowboard", "goggles", "boots", "poles"],
        "hiking": ["hiking", "trail", "boots", "trekking", "backpack", "map"]
    }

    # Combine product description and tags into a single searchable text
    searchable_text = product_description.lower() + " " + " ".join(tag.lower() for tag in product_tags)

    # Check for keywords in the text and categorize
    for category, keywords in categories.items():
        for keyword in keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', searchable_text):
                return category

    # Default to "uncategorized" if no keywords match
    return "uncategorized"


# Example usage
if __name__ == "__main__":
    # Sample product descriptions and tags
    products = [
        {"description": "A durable helmet for mountain biking.", "tags": ["cycling", "helmet", "biking"]},
        {"description": "Lightweight tent perfect for camping trips.", "tags": ["camping", "tent"]},
        {"description": "High-performance skis for professional skiers.", "tags": ["skiing", "skis"]},
        {"description": "Comfortable boots designed for long hiking trails.", "tags": ["boots", "hiking"]},
        {"description": "A strong and versatile rope.", "tags": ["rope", "utility"]}
    ]

    # Categorize each product
    for product in products:
        category = categorize_sports_equipment(product["description"], product["tags"])
        print(f'Product: "{product["description"]}"')
        print(f'Category: {category}')
        print()
```
