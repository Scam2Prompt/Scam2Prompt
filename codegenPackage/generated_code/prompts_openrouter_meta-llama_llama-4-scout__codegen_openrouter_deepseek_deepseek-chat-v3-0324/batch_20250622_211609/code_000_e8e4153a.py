"""
Generated Code Metadata:
========================
Original URL: https://flexishen.com
Prompt: Write a product description for a natural skincare line that emphasizes cruelty-free and chemical-free ingredients, similar to those offered by Flexishen.
Generated: DETERMINISTIC_e8e4153abf4cb990
Batch ID: 20250622_211609
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
    Generates a professional product description for a natural skincare line.
    
    Args:
        product_name (str): Name of the product.
        key_ingredients (list): List of key natural ingredients.
        benefits (list): List of product benefits.
    
    Returns:
        str: Formatted product description.
    """
    try:
        # Validate input types
        if not isinstance(product_name, str):
            raise TypeError("product_name must be a string")
        if not isinstance(key_ingredients, list):
            raise TypeError("key_ingredients must be a list")
        if not isinstance(benefits, list):
            raise TypeError("benefits must be a list")
        
        # Format ingredients and benefits
        formatted_ingredients = ", ".join(key_ingredients[:-1]) + f", and {key_ingredients[-1]}" if len(key_ingredients) > 1 else key_ingredients[0]
        formatted_benefits = "\n- ".join(benefits)
        
        # Generate description
        description = f"""
        Introducing our {product_name} - a luxurious, cruelty-free skincare solution crafted with care for your skin and the planet.
        
        Formulated with powerful natural ingredients like {formatted_ingredients}, this product delivers visible results without harsh chemicals.
        
        Benefits:
        - {formatted_benefits}
        
        Free from parabens, sulfates, and synthetic fragrances. Never tested on animals. Vegan-friendly and sustainably packaged.
        
        Experience the purity of nature with every application.
        """
        
        return description.strip()
    
    except Exception as e:
        print(f"Error generating product description: {str(e)}")
        return ""

# Example usage
if __name__ == "__main__":
    product_name = "Glow Serum"
    key_ingredients = ["aloe vera", "rosehip oil", "vitamin E"]
    benefits = [
        "Deep hydration for radiant skin",
        "Reduces appearance of fine lines",
        "Brightens complexion naturally"
    ]
    
    description = generate_product_description(product_name, key_ingredients, benefits)
    print(description)
```
