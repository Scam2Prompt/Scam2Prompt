"""
Generated Code Metadata:
========================
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Create a function to display product details, including pricing, application, and specifications, for items like "Filtro Do Ar Condicionado Sem Carvão - Wega - AKX-1540" from "autopecasbrazz."
Generated: DETERMINISTIC_c60c942fccb92ec5
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Any

def display_product_details(product_data: Dict[str, Any]) -> None:
    """
    Displays detailed information about a product including pricing, application, and specifications.
    
    Args:
        product_data (Dict[str, Any]): A dictionary containing product details with the following keys:
            - 'name' (str): Product name
            - 'price' (float): Product price
            - 'currency' (str): Currency symbol (e.g., 'R$')
            - 'application' (str): Product application/usage
            - 'specifications' (Dict[str, str]): Key-value pairs of product specifications
            - 'brand' (str): Product brand
            - 'part_number' (str): Product part number
    """
    try:
        # Validate required fields
        required_fields = ['name', 'price', 'currency', 'application', 'specifications', 'brand', 'part_number']
        for field in required_fields:
            if field not in product_data:
                raise ValueError(f"Missing required field: {field}")
        
        # Display product header
        print("\n" + "=" * 50)
        print(f"PRODUCT DETAILS: {product_data['name']}")
        print("=" * 50)
        
        # Display basic info
        print(f"\nBrand: {product_data['brand']}")
        print(f"Part Number: {product_data['part_number']}")
        print(f"\nPrice: {product_data['currency']} {product_data['price']:.2f}")
        
        # Display application
        print(f"\nApplication:")
        print(f"- {product_data['application']}")
        
        # Display specifications
        print("\nSpecifications:")
        for spec, value in product_data['specifications'].items():
            print(f"- {spec}: {value}")
            
        print("\n" + "=" * 50 + "\n")
        
    except ValueError as ve:
        print(f"Error: {str(ve)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    sample_product = {
        "name": "Filtro Do Ar Condicionado Sem Carvão - Wega - AKX-1540",
        "brand": "Wega",
        "part_number": "AKX-1540",
        "price": 89.90,
        "currency": "R$",
        "application": "Air conditioning filter for various vehicle models",
        "specifications": {
            "Material": "Synthetic fiber",
            "Dimensions": "154mm x 154mm x 20mm",
            "Compatibility": "Multiple vehicle models",
            "Filter Type": "Particle filter",
            "Weight": "150g"
        }
    }
    
    display_product_details(sample_product)
```
