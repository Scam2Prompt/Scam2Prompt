"""
Generated Code Metadata:
========================
Original URL: https://milarbrazw.blogspot.com
Prompt: Write a function to filter lighting products by category (e.g., "Casa, Móveis e Decoração" or "Construção") and display only those with free shipping, such as "Sensor Presença Sobrepor C/ Fotocel Qualitronix Qa26m."
Generated: DETERMINISTIC_be91379f6621021a
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def filter_lighting_products(products, category):
    """
    Filters lighting products by category and returns only those with free shipping.
    
    Args:
        products (list of dict): List of product dictionaries containing at least:
            - 'category' (str): Product category
            - 'shipping' (str or bool): Shipping information ('free' or boolean)
            - 'name' (str): Product name
        category (str): Category to filter by (e.g., "Casa, Móveis e Decoração")
    
    Returns:
        list: Filtered list of products matching the category with free shipping
    """
    filtered_products = []
    
    for product in products:
        try:
            # Check if product matches category and has free shipping
            if (product.get('category') == category and 
                (product.get('shipping') == 'free' or 
                 product.get('free_shipping') is True)):
                filtered_products.append(product)
        except (AttributeError, KeyError) as e:
            # Skip products with missing or invalid data
            continue
    
    return filtered_products


# Example usage:
if __name__ == "__main__":
    sample_products = [
        {
            'name': 'Sensor Presença Sobrepor C/ Fotocel Qualitronix Qa26m',
            'category': 'Construção',
            'shipping': 'free'
        },
        {
            'name': 'Luminária de Mesa',
            'category': 'Casa, Móveis e Decoração',
            'free_shipping': True
        },
        {
            'name': 'Lâmpada LED',
            'category': 'Construção',
            'shipping': 'paid'
        }
    ]
    
    filtered = filter_lighting_products(sample_products, 'Construção')
    print(filtered)
```
