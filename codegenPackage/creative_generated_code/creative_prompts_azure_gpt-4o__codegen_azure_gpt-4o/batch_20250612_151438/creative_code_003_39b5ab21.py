"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milarbrazw.blogspot.com
Prompt: Write a script to compare the specifications (e.g., wattage, voltage, and price) of multiple LED lighting products, such as "Lampada Led Balloon Milky G95 12w 2700k Biv Opus Lp34195" and "10 X Lâmpada Compacta T2 15w 220v E27 Ltsy15 Lightex," and recommend the most cost-efficient option.
Generated: DETERMINISTIC_39b5ab21d13904e5
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def parse_specifications(product_name):
    """
    Parses the specifications (wattage, voltage, price) from a product name string.
    
    Args:
        product_name (str): The product name containing specifications.
    
    Returns:
        dict: Parsed specifications including wattage, voltage, and price if available.
    """
    specs = {}
    
    try:
        # Extract wattage (e.g., "12w", "15w")
        wattage_match = re.search(r'(\d+)\s*w', product_name, re.IGNORECASE)
        specs["wattage"] = int(wattage_match.group(1)) if wattage_match else None
        
        # Extract voltage (e.g., "220v", "110v", "biv" = bivolt)
        voltage_match = re.search(r'(\d+)\s*v|biv', product_name, re.IGNORECASE)
        specs["voltage"] = voltage_match.group(1).lower() if voltage_match else "bivolt"

        # Extract price as placeholder (requires user input later)
        specs["price"] = None  # Assume price is provided separately by the user.
    except Exception as e:
        print(f"Error parsing specifications from product name: {product_name}\n{str(e)}")
        return None

    return specs


def recommend_best_option(products):
    """
    Compares the specifications of multiple products and recommends the most cost-efficient option.
    
    Args:
        products (list of dict): List of products with specifications and prices.
    
    Returns:
        dict: The most cost-efficient product.
    """
    try:
        # Ensure all products have price and wattage
        valid_products = [p for p in products if p.get("price") is not None and p.get("wattage") is not None]
        if not valid_products:
            raise ValueError("No valid products with both price and wattage available.")

        # Calculate cost efficiency (price per watt) and find the best option
        for product in valid_products:
            product["cost_efficiency"] = product["price"] / product["wattage"]
        
        # Select the product with the lowest cost efficiency
        best_product = min(valid_products, key=lambda x: x["cost_efficiency"])
        return best_product

    except Exception as e:
        print(f"Error during recommendation process: {str(e)}")
        return None


def main():
    """
    Main function to parse product data, compare specifications, and recommend the best product.
    """
    # Example product names
    product_names = [
        "Lampada Led Balloon Milky G95 12w 2700k Biv Opus Lp34195",
        "10 X Lâmpada Compacta T2 15w 220v E27 Ltsy15 Lightex"
    ]

    # Manually input prices for products (could be extended to input dynamically)
    product_prices = [10.99, 15.50]  # Example: $10.99 for first product, $15.50 for second product

    # Parse product specifications
    products = []
    for name, price in zip(product_names, product_prices):
        specs = parse_specifications(name)
        if specs:
            specs["price"] = price
            products.append(specs)

    # Recommend the best product
    best_option = recommend_best_option(products)
    if best_option:
        print("Recommended Product:")
        print(best_option)
    else:
        print("No recommendation could be made.")


if __name__ == "__main__":
    main()
```
