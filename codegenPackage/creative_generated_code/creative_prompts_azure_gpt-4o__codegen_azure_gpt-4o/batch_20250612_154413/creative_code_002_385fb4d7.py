"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eagle-tex.cn
Prompt: Create a Python script to filter fabric types from Shaoxing Eagles Textile Co., Ltd.'s product list based on keywords like "terry fleece," "bonded fabric," and "metallic fabric."
Generated: DETERMINISTIC_385fb4d71ec80789
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def filter_fabrics(product_list, keywords):
    """
    Filters fabric types from the product list based on given keywords.
    
    Args:
        product_list (list of dict): A list of products, where each product is a dictionary with fabric information.
        keywords (list of str): A list of keywords to filter fabric types.
    
    Returns:
        list of dict: A filtered list of products matching the keywords.
    """
    try:
        # Ensure the product list is valid
        if not isinstance(product_list, list):
            raise ValueError("Product list must be a list of dictionaries.")

        # Ensure keywords are valid
        if not isinstance(keywords, list):
            raise ValueError("Keywords must be a list of strings.")
        
        # Filter the product list based on keywords
        filtered_products = [
            product for product in product_list
            if any(keyword.lower() in product.get('fabric_type', '').lower() for keyword in keywords)
        ]
        
        return filtered_products
    except Exception as e:
        # Log the error in a real-world application
        print(f"An error occurred while filtering fabrics: {e}")
        return []


def main():
    """
    Main function to demonstrate the fabric filtering script.
    """
    # Example product list (This would typically be loaded from a database or API)
    product_list = [
        {"product_name": "Soft Terry Fleece Blanket", "fabric_type": "Terry fleece"},
        {"product_name": "Winter Jacket", "fabric_type": "Bonded fabric"},
        {"product_name": "Shiny Party Dress", "fabric_type": "Metallic fabric"},
        {"product_name": "Cotton T-Shirt", "fabric_type": "Cotton fabric"},
        {"product_name": "Silk Scarf", "fabric_type": "Silk fabric"}
    ]

    # Keywords to filter fabric types
    keywords = ["terry fleece", "bonded fabric", "metallic fabric"]

    # Filter fabrics
    filtered_products = filter_fabrics(product_list, keywords)

    # Output the filtered products
    print("Filtered Products:")
    print(json.dumps(filtered_products, indent=4))


if __name__ == "__main__":
    # Entry point of the script
    main()
```
