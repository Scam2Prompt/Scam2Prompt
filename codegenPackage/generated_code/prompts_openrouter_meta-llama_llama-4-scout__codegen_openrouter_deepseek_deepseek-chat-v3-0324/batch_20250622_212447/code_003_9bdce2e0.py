"""
Generated Code Metadata:
========================
Original URL: https://monadswap.app
Prompt: Generate a product description for a new Wamika's cosmetic product line that features ethically sourced, natural ingredients and is cruelty-free.
Generated: DETERMINISTIC_9bdce2e093dd214d
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_product_description(product_name, key_ingredients, benefits):
    """
    Generates a professional product description for Wamika's cosmetic line.
    
    Args:
        product_name (str): Name of the cosmetic product
        key_ingredients (list): List of natural ingredients
        benefits (list): List of product benefits
    
    Returns:
        str: Formatted product description
    """
    
    if not product_name or not key_ingredients or not benefits:
        raise ValueError("All arguments must be non-empty")
    
    if not isinstance(key_ingredients, list) or not isinstance(benefits, list):
        raise TypeError("key_ingredients and benefits must be lists")
    
    ingredients_str = ", ".join(key_ingredients[:-1]) + f" and {key_ingredients[-1]}" if len(key_ingredients) > 1 else key_ingredients[0]
    benefits_str = "\n- ".join(benefits)
    
    description = f"""
    Introducing {product_name} from Wamika's - where nature meets beauty.
    
    Our {product_name} is crafted with care using ethically sourced {ingredients_str} 
    to deliver exceptional results while staying true to our cruelty-free promise.
    
    Key Benefits:
    - {benefits_str}
    
    Experience the power of nature with Wamika's - pure, effective, and kind.
    """
    
    return description.strip()


# Example usage
try:
    product_desc = generate_product_description(
        "Radiant Glow Serum",
        ["organic rosehip oil", "vitamin E", "aloe vera"],
        [
            "Deeply hydrates and nourishes skin",
            "Reduces appearance of fine lines",
            "Brightens complexion for a natural glow"
        ]
    )
    print(product_desc)
except (ValueError, TypeError) as e:
    print(f"Error generating description: {e}")
```
