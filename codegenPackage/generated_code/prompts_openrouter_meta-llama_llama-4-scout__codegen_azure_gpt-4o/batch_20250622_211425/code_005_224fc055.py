"""
Generated Code Metadata:
========================
Original URL: https://glisten.site
Prompt: Generate a list of keywords that can be used for search engine optimization (SEO) to promote Glisten's iPhone case products, focusing on art, fashion, and lifestyle.
Generated: DETERMINISTIC_224fc0553823bc00
Batch ID: 20250622_211425
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import itertools

def generate_seo_keywords(brand_name, product_type, themes):
    """
    Generate a list of SEO keywords for promoting products.

    Parameters:
    - brand_name (str): The name of the brand.
    - product_type (str): The type of product being promoted.
    - themes (list of str): A list of themes to focus on.

    Returns:
    - list of str: A list of SEO keywords.
    """
    try:
        # Validate inputs
        if not isinstance(brand_name, str) or not isinstance(product_type, str) or not isinstance(themes, list):
            raise ValueError("Invalid input types. Ensure brand_name and product_type are strings, and themes is a list.")

        # Base keywords
        base_keywords = [
            f"{brand_name} {product_type}",
            f"{product_type} by {brand_name}",
            f"{brand_name} {product_type} collection",
            f"buy {brand_name} {product_type}",
            f"shop {brand_name} {product_type}",
            f"premium {product_type} by {brand_name}",
        ]

        # Generate theme-based keywords
        theme_keywords = []
        for theme in themes:
            theme_keywords.extend([
                f"{theme} {product_type}",
                f"{theme} {product_type} by {brand_name}",
                f"{brand_name} {theme} {product_type}",
                f"{theme} inspired {product_type}",
                f"{theme} design {product_type}",
            ])

        # Combine and deduplicate keywords
        all_keywords = list(set(base_keywords + theme_keywords))
        return sorted(all_keywords)  # Sort for better readability

    except Exception as e:
        # Handle unexpected errors
        print(f"Error generating SEO keywords: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Inputs
    brand_name = "Glisten"
    product_type = "iPhone case"
    themes = ["art", "fashion", "lifestyle"]

    # Generate keywords
    seo_keywords = generate_seo_keywords(brand_name, product_type, themes)

    # Output the results
    print("Generated SEO Keywords:")
    for keyword in seo_keywords:
        print(f"- {keyword}")
```
