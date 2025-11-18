"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chicatchi.com
Prompt: Generate a function to extract and display the customization options for branded stationery offered by Chicatchi, such as mugs and letterheads.
Generated: DETERMINISTIC_10840af4b5a56eb9
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def extract_customization_options(product_data, brand_name):
    """
    Extracts and displays the customization options for branded stationery offered by a specific brand.

    Parameters:
        product_data (str): JSON string containing product details.
        brand_name (str): Name of the brand (e.g., 'Chicatchi').

    Returns:
        dict: Dictionary of products with their customization options.
    """
    try:
        # Parse the JSON string into Python dictionary
        products = json.loads(product_data)
        
        # Validate the structure of input data
        if not isinstance(products, list):
            raise ValueError("Product data must be a list of dictionaries.")
        
        # Filter products for the specific brand and extract customization options
        customization_options = {}
        for product in products:
            if product.get("brand") == brand_name:
                product_name = product.get("name", "Unnamed Product")
                options = product.get("customization_options", {})
                customization_options[product_name] = options
        
        # Display the customization options
        print(f"Customization Options for {brand_name}:")
        for product, options in customization_options.items():
            print(f"Product: {product}")
            for option, details in options.items():
                print(f"  - {option}: {details}")
        
        return customization_options
    
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON data: {e}")
    except ValueError as e:
        print(f"Error validating product data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    product_data_json = """
    [
        {
            "name": "Mug",
            "brand": "Chicatchi",
            "customization_options": {
                "Color": "Red, Blue, Green",
                "Text": "Up to 20 characters"
            }
        },
        {
            "name": "Letterhead",
            "brand": "Chicatchi",
            "customization_options": {
                "Logo Placement": "Top, Bottom, Center",
                "Paper Quality": "Standard, Premium"
            }
        },
        {
            "name": "Notebook",
            "brand": "OtherBrand",
            "customization_options": {
                "Cover Color": "Black, White",
                "Size": "A4, A5"
            }
        }
    ]
    """
    
    extract_customization_options(product_data_json, "Chicatchi")
```
