"""
Generated Code Metadata:
========================
Original URL: https://pspamelaslocum.com
Prompt: Generate a slogan for a new product using a down-to-earth and spirited approach, inspired by PS Pamela Slocum's writing style.
Generated: DETERMINISTIC_df4ac6320e0746a6
Batch ID: 20250622_204729
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_slogan(product_name):
    """
    Generates a spirited, down-to-earth slogan for a product.
    
    Args:
        product_name (str): Name of the product to feature in the slogan
        
    Returns:
        str: A catchy slogan in PS Pamela Slocum's style
    """
    
    # List of spirited, down-to-earth phrases inspired by PS Pamela Slocum's style
    slogans = [
        f"{product_name} - It's not fancy, but it gets the job done right!",
        f"Honest {product_name} for real folks who need real results",
        f"{product_name}: Simple. Solid. Works like a charm.",
        f"No frills, just {product_name} - the way good things oughta be",
        f"{product_name} - Because sometimes the best things come without the hype",
        f"Straight-shooting {product_name} for folks who value substance over style",
        f"{product_name} - The sensible choice for people with things to do",
        f"Tried-and-true {product_name} - because newfangled isn't always better"
    ]
    
    # Select a random slogan
    import random
    return random.choice(slogans)

# Example usage
if __name__ == "__main__":
    product = "Widget"
    print(f"Generated slogan: {generate_slogan(product)}")
```
