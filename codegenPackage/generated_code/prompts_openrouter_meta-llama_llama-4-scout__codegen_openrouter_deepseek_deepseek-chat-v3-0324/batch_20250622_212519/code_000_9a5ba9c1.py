"""
Generated Code Metadata:
========================
Original URL: https://myallora.com
Prompt: Write a product description for a women's clothing item, specifically a maxi dress, that is on sale with a discount of up to 80% off, similar to those found on Sophie's Boutique.
Generated: DETERMINISTIC_9a5ba9c1d66443b4
Batch ID: 20250622_212519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_product_description(product_name, original_price, discount_percentage, colors_available, sizes_available):
    """
    Generates a compelling product description for a women's maxi dress on sale.
    
    Args:
        product_name (str): Name of the maxi dress product
        original_price (float): Original price before discount
        discount_percentage (int): Discount percentage (0-100)
        colors_available (list): List of available colors
        sizes_available (list): List of available sizes
        
    Returns:
        str: Formatted product description
    """
    
    # Calculate sale price
    sale_price = original_price * (1 - discount_percentage/100)
    
    # Format prices to 2 decimal places
    original_price_str = f"${original_price:.2f}"
    sale_price_str = f"${sale_price:.2f}"
    
    # Create color options string
    colors_str = ", ".join(colors_available[:-1]) + f" and {colors_available[-1]}" if len(colors_available) > 1 else colors_available[0]
    
    # Create size options string
    sizes_str = ", ".join(sizes_available[:-1]) + f" and {sizes_available[-1]}" if len(sizes_available) > 1 else sizes_available[0]
    
    description = f"""
    {product_name} - Limited Time Sale!
    
    Elevate your wardrobe with this stunning maxi dress, now at an incredible {discount_percentage}% off!
    
    • Original Price: {original_price_str}
    • Sale Price: {sale_price_str} (Save {discount_percentage}%)
    • Available in beautiful {colors_str}
    • Sizes: {sizes_str}
    
    This flowy maxi dress features:
    - Flattering A-line silhouette
    - Soft, breathable fabric
    - Adjustable waist tie for perfect fit
    - Versatile design for any occasion
    
    Hurry - this deal won't last! Shop now before your size sells out.
    """
    
    return description.strip()

# Example usage
if __name__ == "__main__":
    description = generate_product_description(
        "Floral Summer Maxi Dress",
        89.99,
        60,
        ["navy blue", "rose pink", "ivory"],
        ["XS", "S", "M", "L", "XL"]
    )
    print(description)
```
