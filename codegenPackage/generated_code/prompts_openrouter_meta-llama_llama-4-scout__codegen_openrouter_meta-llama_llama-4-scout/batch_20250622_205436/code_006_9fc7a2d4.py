"""
Generated Code Metadata:
========================
Original URL: https://distribution-menuiserie.fr
Prompt: "Develop a Python program to analyze customer requests for custom menuiserie products, such as pergolas and fermetures bâtiment, and generate quotes based on product specifications and pricing rules."
Generated: DETERMINISTIC_9fc7a2d414631e11
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# menuiserie_quote_generator.py

class Product:
    """Represents a custom menuiserie product."""
    
    def __init__(self, name, description, price_per_unit):
        """
        Initializes a Product instance.

        Args:
            name (str): Product name.
            description (str): Product description.
            price_per_unit (float): Price per unit of the product.
        """
        self.name = name
        self.description = description
        self.price_per_unit = price_per_unit

class Pergola(Product):
    """Represents a pergola product."""
    
    def __init__(self, name, description, price_per_unit, size):
        """
        Initializes a Pergola instance.

        Args:
            name (str): Product name.
            description (str): Product description.
            price_per_unit (float): Price per unit of the product.
            size (float): Size of the pergola in square meters.
        """
        super().__init__(name, description, price_per_unit)
        self.size = size

class FermetureBatiment(Product):
    """Represents a fermeture bâtiment product."""
    
    def __init__(self, name, description, price_per_unit, length):
        """
        Initializes a FermetureBatiment instance.

        Args:
            name (str): Product name.
            description (str): Product description.
            price_per_unit (float): Price per unit of the product.
            length (float): Length of the fermeture bâtiment in meters.
        """
        super().__init__(name, description, price_per_unit)
        self.length = length

class Quote:
    """Represents a quote for a customer request."""
    
    def __init__(self, customer_name, products):
        """
        Initializes a Quote instance.

        Args:
            customer_name (str): Name of the customer.
            products (list[Product]): List of products in the quote.
        """
        self.customer_name = customer_name
        self.products = products

    def calculate_total(self):
        """
        Calculates the total cost of the quote.

        Returns:
            float: Total cost of the quote.
        """
        total = 0
        for product in self.products:
            if isinstance(product, Pergola):
                total += product.price_per_unit * product.size
            elif isinstance(product, FermetureBatiment):
                total += product.price_per_unit * product.length
        return total

def generate_quote(customer_name, products):
    """
    Generates a quote for a customer request.

    Args:
        customer_name (str): Name of the customer.
        products (list[dict]): List of product specifications.

    Returns:
        Quote: Quote instance for the customer request.

    Raises:
        ValueError: If an invalid product type is provided.
    """
    quote_products = []
    for product in products:
        product_type = product['type']
        if product_type == 'pergola':
            quote_products.append(Pergola(
                product['name'],
                product['description'],
                product['price_per_unit'],
                product['size']
            ))
        elif product_type == 'fermeture_batiment':
            quote_products.append(FermetureBatiment(
                product['name'],
                product['description'],
                product['price_per_unit'],
                product['length']
            ))
        else:
            raise ValueError(f"Invalid product type: {product_type}")
    return Quote(customer_name, quote_products)

def main():
    try:
        customer_name = "John Doe"
        products = [
            {
                'type': 'pergola',
                'name': 'Pergola 1',
                'description': 'Custom pergola',
                'price_per_unit': 100.0,
                'size': 10.0
            },
            {
                'type': 'fermeture_batiment',
                'name': 'Fermeture Batiment 1',
                'description': 'Custom fermeture bâtiment',
                'price_per_unit': 50.0,
                'length': 5.0
            }
        ]
        quote = generate_quote(customer_name, products)
        print(f"Quote for {quote.customer_name}:")
        for i, product in enumerate(quote.products):
            if isinstance(product, Pergola):
                print(f"Product {i+1}: {product.name} - {product.description} ({product.size} sqm) = ${product.price_per_unit * product.size:.2f}")
            elif isinstance(product, FermetureBatiment):
                print(f"Product {i+1}: {product.name} - {product.description} ({product.length} m) = ${product.price_per_unit * product.length:.2f}")
        print(f"Total: ${quote.calculate_total():.2f}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
