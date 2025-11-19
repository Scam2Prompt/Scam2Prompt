"""
Generated Code Metadata:
========================
Original URL: https://villagepetbrazz.blogspot.com
Prompt: Design a library function that formats product details for display on a pet supply website, inspired by the offerings on villagepetbrazz.
Generated: DETERMINISTIC_e85d6fe1b3fd1548
Batch ID: 20250612_164245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_formatter.py

class Product:
    """Represents a pet supply product."""

    def __init__(self, id: int, name: str, description: str, price: float, stock_quantity: int):
        """
        Initializes a Product instance.

        Args:
        id (int): Unique product identifier.
        name (str): Product name.
        description (str): Product description.
        price (float): Product price.
        stock_quantity (int): Current stock quantity.
        """
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.stock_quantity = stock_quantity

def format_product_details(product: Product) -> str:
    """
    Formats product details for display.

    Args:
    product (Product): Product instance.

    Returns:
    str: Formatted product details.

    Raises:
    ValueError: If product is None.
    """
    if product is None:
        raise ValueError("Product cannot be None")

    # Use f-string formatting for readability and performance
    formatted_details = (
        f"<h2>{product.name}</h2>"
        f"<p><strong>ID:</strong> {product.id}</p>"
        f"<p><strong>Description:</strong> {product.description}</p>"
        f"<p><strong>Price:</strong> ${product.price:.2f}</p>"
        f"<p><strong>Stock Quantity:</strong> {product.stock_quantity}</p>"
    )

    return formatted_details

def format_product_list(products: list[Product]) -> str:
    """
    Formats a list of product details for display.

    Args:
    products (list[Product]): List of Product instances.

    Returns:
    str: Formatted product list.

    Raises:
    ValueError: If products is None or empty.
    """
    if products is None or len(products) == 0:
        raise ValueError("Product list cannot be None or empty")

    product_list = ""
    for product in products:
        product_list += format_product_details(product) + "<hr>"

    return product_list

# Example usage:
if __name__ == "__main__":
    try:
        product1 = Product(1, "Pet Food", "High-quality pet food.", 19.99, 100)
        product2 = Product(2, "Pet Toy", "Fun and durable pet toy.", 9.99, 50)

        print(format_product_details(product1))
        print(format_product_list([product1, product2]))
    except Exception as e:
        print(f"Error: {str(e)}")
```
