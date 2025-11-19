"""
Generated Code Metadata:
========================
Original URL: https://micadbrazzz.blogspot.com
Prompt: Write a function that filters a list of dining products based on categories such as "Mesa Posta" and "Acessórios para servir," inspired by the offerings on the Camicado website.
Generated: DETERMINISTIC_a9141955e0dca26e
Batch ID: 20250612_160633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def filter_dining_products(products, categories):
    """
    Filters a list of dining products based on specified categories.

    Args:
        products (list of dict): List of product dictionaries, each containing at least a 'category' key.
        categories (list of str): List of category names to filter by.

    Returns:
        list of dict: Filtered list of products that match any of the specified categories.
    """
    if not isinstance(products, list) or not isinstance(categories, list):
        raise TypeError("Both 'products' and 'categories' must be lists.")
    
    if not products or not categories:
        return []
    
    filtered_products = []
    for product in products:
        try:
            if product.get('category') in categories:
                filtered_products.append(product)
        except AttributeError:
            continue
    
    return filtered_products


# Example usage:
if __name__ == "__main__":
    sample_products = [
        {"name": "Prato de Porcelana", "category": "Mesa Posta", "price": 49.90},
        {"name": "Jogo de Talheres", "category": "Mesa Posta", "price": 89.90},
        {"name": "Jarra de Vidro", "category": "Acessórios para servir", "price": 39.90},
        {"name": "Cesta de Pão", "category": "Acessórios para servir", "price": 59.90},
        {"name": "Toalha de Mesa", "category": "Têxteis", "price": 29.90},
    ]
    
    filtered = filter_dining_products(
        sample_products,
        ["Mesa Posta", "Acessórios para servir"]
    )
    print(filtered)
```
