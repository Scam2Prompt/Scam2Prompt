"""
Generated Code Metadata:
========================
Original URL: https://acula.com.ua
Prompt: Write code to generate product listings with detailed descriptions, including items like "гидрокостюм AquaDiscovery VOEVODA" and "сумка Beuchat Voyager XL," as featured on acula.com.ua.
Generated: DETERMINISTIC_2720dd6dd7cce611
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_listing_generator.py

class Product:
    def __init__(self, name, description, price, brand, model):
        """
        Initialize a Product object.

        Args:
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
            brand (str): Product brand.
            model (str): Product model.
        """
        self.name = name
        self.description = description
        self.price = price
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"{self.brand} {self.model} - {self.name}"


class ProductListingGenerator:
    def __init__(self, products):
        """
        Initialize a ProductListingGenerator object.

        Args:
            products (list[Product]): List of Product objects.
        """
        self.products = products

    def generate_product_listing(self):
        """
        Generate a product listing with detailed descriptions.

        Returns:
            str: HTML-formatted product listing.
        """
        listing = ""
        for product in self.products:
            listing += self.generate_product_card(product)
        return listing

    def generate_product_card(self, product):
        """
        Generate a product card with detailed description.

        Args:
            product (Product): Product object.

        Returns:
            str: HTML-formatted product card.
        """
        try:
            return f"""
            <div class="product-card">
                <h2>{product.name}</h2>
                <p><strong>Brand:</strong> {product.brand}</p>
                <p><strong>Model:</strong> {product.model}</p>
                <p><strong>Price:</strong> ${product.price:.2f}</p>
                <p><strong>Description:</strong> {product.description}</p>
            </div>
            """
        except Exception as e:
            print(f"Error generating product card: {str(e)}")
            return ""


def main():
    # Example usage
    products = [
        Product(
            "гидрокостюм AquaDiscovery VOEVODA",
            "A high-quality wetsuit for water sports.",
            199.99,
            "AquaDiscovery",
            "VOEVODA"
        ),
        Product(
            "сумка Beuchat Voyager XL",
            "A spacious and durable bag for diving and snorkeling.",
            149.99,
            "Beuchat",
            "Voyager XL"
        )
    ]

    generator = ProductListingGenerator(products)
    listing = generator.generate_product_listing()

    print(listing)


if __name__ == "__main__":
    main()
```
