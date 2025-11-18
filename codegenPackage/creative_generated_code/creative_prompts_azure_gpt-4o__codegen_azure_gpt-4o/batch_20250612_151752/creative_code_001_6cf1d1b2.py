"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bgmarkazi.com
Prompt: Generate a script to filter products by brand (e.g., Apple, Xiaomi, Huawei) and type (e.g., chargers, earphones, cases) based on the categories listed on the BG Markazi website.
Generated: DETERMINISTIC_6cf1d1b2f993654d
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def filter_products(products, brand=None, product_type=None):
    """
    Filters a list of products by brand and type.
    
    Args:
        products (list): List of product dictionaries.
        brand (str): Brand name to filter by (e.g., 'Apple', 'Xiaomi').
        product_type (str): Product type to filter by (e.g., 'chargers', 'earphones').
    
    Returns:
        list: Filtered list of products.
    """
    try:
        # Validate input
        if not isinstance(products, list):
            raise ValueError("Products should be a list of dictionaries.")
        
        # Apply filters based on the provided brand and product type
        filtered = [
            product for product in products
            if (brand is None or product.get('brand') == brand) and
               (product_type is None or product.get('type') == product_type)
        ]
        
        return filtered
    except Exception as e:
        print(f"An error occurred while filtering products: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Sample products data
    sample_data = """
    [
        {"id": 1, "name": "iPhone Charger", "brand": "Apple", "type": "chargers"},
        {"id": 2, "name": "AirPods Pro", "brand": "Apple", "type": "earphones"},
        {"id": 3, "name": "Mi Charger", "brand": "Xiaomi", "type": "chargers"},
        {"id": 4, "name": "Huawei Case", "brand": "Huawei", "type": "cases"},
        {"id": 5, "name": "Samsung Earphones", "brand": "Samsung", "type": "earphones"}
    ]
    """
    
    # Load sample data as a Python list
    products = json.loads(sample_data)
    
    # Filter products by brand and type
    apple_earphones = filter_products(products, brand="Apple", product_type="earphones")
    xiaomi_chargers = filter_products(products, brand="Xiaomi", product_type="chargers")
    all_cases = filter_products(products, product_type="cases")
    
    # Print filtered results
    print("Apple Earphones:", apple_earphones)
    print("Xiaomi Chargers:", xiaomi_chargers)
    print("All Cases:", all_cases)
```
