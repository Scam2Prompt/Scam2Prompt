"""
Generated Code Metadata:
========================
Original URL: https://artpelbrazz.blogspot.com
Prompt: Generate a list of product recommendations for a customer who buys a "Caderno Inteligente Felicity By Alexity A5" and a "Caneta Crown Metal Belíssima Esferográfica Prata", considering related products from the Art Pel catalog.
Generated: DETERMINISTIC_07880956b1b9d388
Batch ID: 20250622_212633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_recommender.py

class Product:
    """Represents a product with its id, name, and category."""

    def __init__(self, id, name, category):
        """
        Initializes a Product instance.

        Args:
            id (int): Unique product identifier.
            name (str): Product name.
            category (str): Product category.
        """
        self.id = id
        self.name = name
        self.category = category

class ProductRecommender:
    """Provides product recommendations based on purchased items."""

    def __init__(self, catalog):
        """
        Initializes a ProductRecommender instance.

        Args:
            catalog (list): List of Product instances.
        """
        self.catalog = catalog

    def get_recommendations(self, purchased_products):
        """
        Generates a list of product recommendations.

        Args:
            purchased_products (list): List of purchased Product instances.

        Returns:
            list: List of recommended Product instances.
        """
        # Get categories of purchased products
        purchased_categories = set(product.category for product in purchased_products)

        # Filter catalog to get related products
        related_products = [product for product in self.catalog 
                            if product.category in purchased_categories 
                            and product not in purchased_products]

        # Remove duplicates and prioritize products from the same category
        recommended_products = []
        for category in purchased_categories:
            category_products = [product for product in related_products if product.category == category]
            recommended_products.extend(category_products)

        # Limit recommendations to 5 products
        return recommended_products[:5]

def main():
    # Define Art Pel catalog
    catalog = [
        Product(1, "Caderno Inteligente Felicity By Alexity A5", "Cadernos"),
        Product(2, "Caneta Crown Metal Belíssima Esferográfica Prata", "Canetas"),
        Product(3, "Caderno de Anotações A4", "Cadernos"),
        Product(4, "Caneta Esferográfica Azul", "Canetas"),
        Product(5, "Lápis de Cor 12 Cores", "Lápis e Canetas de Cor"),
        Product(6, "Caderno de Desenho A3", "Cadernos"),
        Product(7, "Caneta Marcadora de Tinta", "Canetas"),
        Product(8, "Borracha de Borracha", "Material Escolar"),
    ]

    # Create a ProductRecommender instance
    recommender = ProductRecommender(catalog)

    # Define purchased products
    purchased_products = [
        Product(1, "Caderno Inteligente Felicity By Alexity A5", "Cadernos"),
        Product(2, "Caneta Crown Metal Belíssima Esferográfica Prata", "Canetas"),
    ]

    try:
        # Get product recommendations
        recommendations = recommender.get_recommendations(purchased_products)

        # Print recommendations
        print("Recomendações de produtos:")
        for i, product in enumerate(recommendations, start=1):
            print(f"{i}. {product.name} ({product.category})")

    except Exception as e:
        print(f"Erro: {str(e)}")

if __name__ == "__main__":
    main()
```
