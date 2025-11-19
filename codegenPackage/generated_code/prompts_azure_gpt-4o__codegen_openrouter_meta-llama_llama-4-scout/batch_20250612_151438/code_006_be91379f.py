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
# lighting_products.py

class LightingProduct:
    """Represents a lighting product."""

    def __init__(self, name, category, has_free_shipping):
        """
        Initializes a LightingProduct.

        Args:
            name (str): Product name.
            category (str): Product category.
            has_free_shipping (bool): Whether the product has free shipping.
        """
        self.name = name
        self.category = category
        self.has_free_shipping = has_free_shipping

    def __repr__(self):
        return f"LightingProduct(name='{self.name}', category='{self.category}', has_free_shipping={self.has_free_shipping})"


def filter_lighting_products(products, category=None, has_free_shipping=False):
    """
    Filters lighting products by category and/or free shipping.

    Args:
        products (list[LightingProduct]): List of lighting products.
        category (str, optional): Category to filter by. Defaults to None.
        has_free_shipping (bool, optional): Whether to filter by free shipping. Defaults to False.

    Returns:
        list[LightingProduct]: Filtered list of lighting products.
    """
    try:
        filtered_products = products.copy()

        if category:
            filtered_products = [product for product in filtered_products if product.category == category]

        if has_free_shipping:
            filtered_products = [product for product in filtered_products if product.has_free_shipping]

        return filtered_products

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []


# Example usage:
if __name__ == "__main__":
    products = [
        LightingProduct("Sensor Presença Sobrepor C/ Fotocel Qualitronix Qa26m", "Casa, Móveis e Decoração", True),
        LightingProduct("Lampada LED", "Construção", False),
        LightingProduct("Chandelier", "Casa, Móveis e Decoração", False),
        LightingProduct("Street Light", "Construção", True),
    ]

    filtered_products = filter_lighting_products(products, category="Casa, Móveis e Decoração", has_free_shipping=True)

    print("Filtered Products:")
    for product in filtered_products:
        print(product)
```
