"""
Generated Code Metadata:
========================
Original URL: https://poocoinmod.blogspot.com
Prompt: Generate a list of shoe products for kids, including chuteira infantil and tenis de esporte.
Generated: DETERMINISTIC_79c141da5c0f0e5c
Batch ID: 20250622_205440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import json

# Define a function to generate a list of shoe products for kids
def generate_kids_shoe_products():
    """
    Generates a list of shoe products for kids, including 'chuteira infantil' and 'tenis de esporte'.
    
    Returns:
        list: A list of dictionaries representing shoe products.
    """
    try:
        # List of shoe products
        shoe_products = [
            {"id": 1, "name": "Chuteira Infantil Nike", "category": "chuteira infantil", "price": 120.00, "size_range": [28, 29, 30, 31, 32]},
            {"id": 2, "name": "Chuteira Infantil Adidas", "category": "chuteira infantil", "price": 110.00, "size_range": [28, 29, 30, 31, 32]},
            {"id": 3, "name": "Tenis de Esporte Puma", "category": "tenis de esporte", "price": 90.00, "size_range": [28, 29, 30, 31, 32]},
            {"id": 4, "name": "Tenis de Esporte Reebok", "category": "tenis de esporte", "price": 85.00, "size_range": [28, 29, 30, 31, 32]},
        ]
        
        # Return the list of products
        return shoe_products
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while generating the shoe products: {e}")
        return []

# Main execution block
if __name__ == "__main__":
    # Generate the list of kids' shoe products
    kids_shoe_products = generate_kids_shoe_products()
    
    # Print the products in JSON format for better readability
    print(json.dumps(kids_shoe_products, indent=4, ensure_ascii=False))
```
