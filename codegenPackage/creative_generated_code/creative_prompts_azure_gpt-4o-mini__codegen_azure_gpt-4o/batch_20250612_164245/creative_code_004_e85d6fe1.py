"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://villagepetbrazz.blogspot.com
Prompt: Design a library function that formats product details for display on a pet supply website, inspired by the offerings on villagepetbrazz.
Generated: DETERMINISTIC_e85d6fe1b3fd1548
Batch ID: 20250612_164245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# pet_product_formatter.py

def format_product_details(product):
    """
    Formats product details for display on a pet supply website.

    Args:
        product (dict): A dictionary containing product details. Expected keys:
            - 'name' (str): The name of the product.
            - 'brand' (str): The brand of the product.
            - 'price' (float): The price of the product.
            - 'description' (str, Optional): A brief description of the product.
            - 'availability' (bool): Whether the product is in stock.

    Returns:
        str: A formatted string representing the product details.
    
    Raises:
        ValueError: If any required key is missing or contains invalid data.
    """
    # Validate input
    required_keys = ['name', 'brand', 'price', 'availability']
    for key in required_keys:
        if key not in product:
            raise ValueError(f"Missing required key: '{key}' in product data.")
        if key == 'price' and not isinstance(product[key], (int, float)):
            raise ValueError(f"Invalid price value: '{product[key]}'. Must be a number.")
        if key == 'availability' and not isinstance(product[key], bool):
            raise ValueError(f"Invalid availability value: '{product[key]}'. Must be a boolean.")
    
    # Optional key validation
    if 'description' in product and not isinstance(product['description'], str):
        raise ValueError(f"Invalid description value: '{product['description']}'. Must be a string.")
    
    # Format product details
    availability_status = "In Stock" if product['availability'] else "Out of Stock"
    description = product.get('description', "No description provided.")
    
    formatted_details = (
        f"Product Name: {product['name']}\n"
        f"Brand: {product['brand']}\n"
        f"Price: ${product['price']:.2f}\n"
        f"Availability: {availability_status}\n"
        f"Description: {description}\n"
    )
    
    return formatted_details


# Example usage
if __name__ == "__main__":
    try:
        example_product = {
            "name": "Organic Cat Food",
            "brand": "Nature's Best",
            "price": 24.99,
            "description": "A nutritious blend of organic ingredients for your cat.",
            "availability": True
        }
        
        print(format_product_details(example_product))
    except ValueError as e:
        print(f"Error: {e}")
```
