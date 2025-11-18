"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.crediblebd.net
Prompt: Create a script to filter lighting products from Credible BD's catalog based on IP rating, wattage, and application type, such as outdoor lighting or commercial lighting.
Generated: DETERMINISTIC_bf4049abc61e9ffc
Batch ID: 20250612_154905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def filter_lighting_products(catalog, ip_rating=None, wattage_range=None, application_type=None):
    """
    Filters lighting products based on the specified criteria.

    Args:
        catalog (list): List of lighting product dictionaries.
        ip_rating (str, optional): Desired IP rating (e.g., "IP65"). Defaults to None.
        wattage_range (tuple, optional): Range of wattage in the format (min_wattage, max_wattage). Defaults to None.
        application_type (str, optional): Desired application type (e.g., "outdoor lighting"). Defaults to None.

    Returns:
        list: Filtered list of lighting products.
    """
    filtered_products = []

    for product in catalog:
        # Extract product attributes
        product_ip_rating = product.get("ip_rating")
        product_wattage = product.get("wattage")
        product_application_type = product.get("application_type")

        # Apply filters
        if ip_rating and product_ip_rating != ip_rating:
            continue
        if wattage_range and not (wattage_range[0] <= product_wattage <= wattage_range[1]):
            continue
        if application_type and product_application_type != application_type:
            continue

        filtered_products.append(product)

    return filtered_products

def load_catalog(file_path):
    """
    Loads the product catalog from a JSON file.

    Args:
        file_path (str): Path to the catalog JSON file.

    Returns:
        list: List of lighting product dictionaries.
    """
    try:
        with open(file_path, "r") as file:
            catalog = json.load(file)
            return catalog
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON data")
        return []

def main():
    """
    Main function to demonstrate filtering of lighting products.
    """
    # Load the catalog from a JSON file
    catalog_file = "credible_bd_catalog.json"
    catalog = load_catalog(catalog_file)

    if not catalog:
        print("No products to filter due to catalog loading error.")
        return

    # Define filter criteria
    ip_rating = "IP65"
    wattage_range = (10, 50)
    application_type = "outdoor lighting"

    # Filter products
    filtered_products = filter_lighting_products(
        catalog, ip_rating=ip_rating, wattage_range=wattage_range, application_type=application_type
    )

    # Output filtered products
    if filtered_products:
        print("Filtered Products:")
        for product in filtered_products:
            print(product)
    else:
        print("No products matched the given criteria.")

if __name__ == "__main__":
    main()
```
