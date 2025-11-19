"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koveindustrial.com
Prompt: Create a function that filters products from KOVE INDUSTRIAL based on specific industries like mining, pharmaceuticals, and textiles, focusing on their unique offerings.
Generated: DETERMINISTIC_6cfe57fa53821cef
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Dict

# Define the function to filter products by industry
def filter_products_by_industry(products: List[Dict], industries: List[str]) -> List[Dict]:
    """
    Filters products based on specific industries.

    Args:
        products (List[Dict]): A list of product dictionaries. Each dictionary should have 
                               keys like 'name', 'industry', and 'unique_offering'.
        industries (List[str]): A list of industries to filter by (e.g., 'mining', 
                                'pharmaceuticals', 'textiles').

    Returns:
        List[Dict]: A filtered list of product dictionaries matching the specified industries.
    """
    # Validate input parameters
    if not isinstance(products, list) or not all(isinstance(p, dict) for p in products):
        raise ValueError("Products must be a list of dictionaries.")
    if not isinstance(industries, list) or not all(isinstance(i, str) for i in industries):
        raise ValueError("Industries must be a list of strings.")

    # Perform the filtering based on the industries
    filtered_products = [
        product for product in products
        if product.get('industry') in industries and 'unique_offering' in product
    ]

    return filtered_products


# Example usage (this would typically be in a separate file or testing framework)
if __name__ == "__main__":
    # Sample product data
    product_data = [
        {"name": "Excavator X1", "industry": "mining", "unique_offering": "High durability"},
        {"name": "Pharma Cleanroom System", "industry": "pharmaceuticals", "unique_offering": "Sterile environment"},
        {"name": "Textile Dye Machine", "industry": "textiles", "unique_offering": "Eco-friendly dyeing"},
        {"name": "Generic Machine", "industry": "manufacturing"},
    ]
    
    # Industries to filter
    target_industries = ["mining", "pharmaceuticals", "textiles"]
    
    # Calling the function and printing the result
    try:
        filtered = filter_products_by_industry(product_data, target_industries)
        print("Filtered Products:", filtered)
    except ValueError as e:
        print("Error:", str(e))
```
