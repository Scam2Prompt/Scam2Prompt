"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Write a Python script to filter tire products by width, height, and rim size, as described on the "Dal Cortivo Pneus" website, and display the filtered results.
Generated: DETERMINISTIC_1e7e0fdeeee3bb8e
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def filter_tires(products, width=None, height=None, rim_size=None):
    """
    Filters tire products based on width, height, and rim size criteria.

    :param products: List of tire products (dicts) to filter.
    :param width: Desired width of the tire, e.g., "205". Default is None.
    :param height: Desired height of the tire, e.g., "55". Default is None.
    :param rim_size: Desired rim size of the tire, e.g., "16". Default is None.
    :return: List of filtered tire products matching the criteria.
    """
    try:
        # Apply filtering based on provided criteria
        filtered_products = [
            product for product in products
            if (width is None or product.get("width") == width)
            and (height is None or product.get("height") == height)
            and (rim_size is None or product.get("rim_size") == rim_size)
        ]
        return filtered_products
    except Exception as e:
        print(f"Error during filtering: {e}")
        return []

def load_products(file_path):
    """
    Loads tire product data from a JSON file.

    :param file_path: Path to the JSON file containing tire product data.
    :return: List of tire products (dicts) if successful, otherwise empty list.
    """
    try:
        with open(file_path, "r") as file:
            products = json.load(file)
        return products
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON file: {file_path}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return []

def display_products(products):
    """
    Displays a list of tire products in a user-friendly format.

    :param products: List of tire products (dicts) to display.
    """
    if not products:
        print("No products found.")
        return

    print("Filtered Tire Products:")
    for product in products:
        print(f"- Brand: {product.get('brand', 'Unknown')}")
        print(f"  Model: {product.get('model', 'Unknown')}")
        print(f"  Width: {product.get('width', 'Unknown')}")
        print(f"  Height: {product.get('height', 'Unknown')}")
        print(f"  Rim Size: {product.get('rim_size', 'Unknown')}")
        print(f"  Price: {product.get('price', 'Unknown')}")
        print("-" * 40)

def main():
    """
    Main function to load, filter, and display tire products.
    """
    # Path to the JSON file containing tire products data (replace with actual path)
    file_path = "tire_products.json"

    # Load tire products from the JSON file
    products = load_products(file_path)

    # Define filtering criteria
    width = input("Enter tire width (e.g., 205) or press Enter to skip: ").strip() or None
    height = input("Enter tire height (e.g., 55) or press Enter to skip: ").strip() or None
    rim_size = input("Enter tire rim size (e.g., 16) or press Enter to skip: ").strip() or None

    # Filter products
    filtered_products = filter_tires(products, width, height, rim_size)

    # Display filtered products
    display_products(filtered_products)

if __name__ == "__main__":
    main()
```
