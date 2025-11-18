"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millymally.pl
Prompt: Write a Python function to categorize products into groups like "akcesoria niemowlęce" and "meble dla dzieci," based on the Milly Mally website structure.
Generated: DETERMINISTIC_90186d74f683c59a
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def categorize_product(product_name: str) -> str:
    """
    Categorizes a product into predefined groups based on the Milly Mally website structure.

    Args:
        product_name (str): The name of the product to be categorized.

    Returns:
        str: The category name if matched, or 'Uncategorized' if no match is found.
    """
    # Define category patterns with regular expressions
    categories = {
        "akcesoria niemowlęce": [
            r"fotelik", 
            r"wózek", 
            r"nosidełko", 
            r"mata edukacyjna", 
            r"śpiworek"
        ],
        "meble dla dzieci": [
            r"łóżeczko", 
            r"krzesełko", 
            r"stolik", 
            r"komoda", 
            r"szafa"
        ]
    }
    
    # Normalize the product name to lower case for case-insensitive matching
    normalized_name = product_name.lower()
    
    # Match the product name against the category patterns
    for category, patterns in categories.items():
        for pattern in patterns:
            if re.search(pattern, normalized_name):
                return category

    # Return 'Uncategorized' if no category matches
    return "Uncategorized"

# Example usage
if __name__ == "__main__":
    try:
        product = "Wózek spacerowy Milly Mally"
        category = categorize_product(product)
        print(f"Product: {product}")
        print(f"Category: {category}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
