"""
Generated Code Metadata:
========================
Original URL: https://shopmetlife.pk
Prompt: Write a Python code snippet to create a product catalog page for an e-commerce website selling hair care products, including product names, prices, and descriptions, similar to the ones listed on ShopMetlife.
Generated: DETERMINISTIC_24930e26508ea686
Batch ID: 20250622_212236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class Product:
    """
    Represents a hair care product with name, price, and description.
    """
    def __init__(self, name: str, price: float, description: str, sku: str, category: str):
        """
        Initialize a Product instance.
        
        Args:
            name (str): Name of the product
            price (float): Price of the product
            description (str): Description of the product
            sku (str): Stock Keeping Unit identifier
            category (str): Product category (e.g., 'Shampoo', 'Conditioner')
        """
        self.name = name
        self.price = price
        self.description = description
        self.sku = sku
        self.category = category

    def to_dict(self) -> Dict:
        """
        Convert the Product instance to a dictionary.
        
        Returns:
            Dict: Dictionary representation of the product
        """
        return {
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'sku': self.sku,
            'category': self.category
        }

class ProductCatalog:
    """
    Manages a collection of hair care products.
    """
    def __init__(self):
        """
        Initialize an empty product catalog.
        """
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        """
        Add a product to the catalog.
        
        Args:
            product (Product): Product to add
        """
        self.products.append(product)

    def get_products_by_category(self, category: str) -> List[Product]:
        """
        Retrieve all products in a specific category.
        
        Args:
            category (str): Category to filter by
            
        Returns:
            List[Product]: List of products in the category
        """
        return [p for p in self.products if p.category.lower() == category.lower()]

    def get_product_by_sku(self, sku: str) -> Optional[Product]:
        """
        Retrieve a product by its SKU.
        
        Args:
            sku (str): SKU to search for
            
        Returns:
            Optional[Product]: Product if found, None otherwise
        """
        for product in self.products:
            if product.sku == sku:
                return product
        return None

    def to_json(self) -> str:
        """
        Convert the catalog to a JSON string.
        
        Returns:
            str: JSON representation of the catalog
        """
        return json.dumps([p.to_dict() for p in self.products], indent=2)

def generate_sample_catalog() -> ProductCatalog:
    """
    Generate a sample product catalog with hair care products.
    
    Returns:
        ProductCatalog: Populated product catalog
    """
    catalog = ProductCatalog()
    
    # Add sample products
    catalog.add_product(Product(
        name="Hydrating Shampoo",
        price=12.99,
        description="Moisturizing shampoo for dry hair",
        sku="SH1001",
        category="Shampoo"
    ))
    
    catalog.add_product(Product(
        name="Volumizing Conditioner",
        price=14.99,
        description="Adds volume and body to fine hair",
        sku="CO2001",
        category="Conditioner"
    ))
    
    catalog.add_product(Product(
        name="Argan Oil Hair Mask",
        price=19.99,
        description="Deep conditioning treatment with argan oil",
        sku="TR3001",
        category="Treatment"
    ))
    
    catalog.add_product(Product(
        name="Heat Protectant Spray",
        price=9.99,
        description="Protects hair from heat damage up to 450°F",
        sku="ST4001",
        category="Styling"
    ))
    
    return catalog

def display_catalog(catalog: ProductCatalog) -> None:
    """
    Display the product catalog in a formatted way.
    
    Args:
        catalog (ProductCatalog): Catalog to display
    """
    print("\n=== HAIR CARE PRODUCT CATALOG ===\n")
    for product in catalog.products:
        print(f"Name: {product.name}")
        print(f"Price: ${product.price:.2f}")
        print(f"Category: {product.category}")
        print(f"Description: {product.description}")
        print(f"SKU: {product.sku}")
        print("-" * 40)

if __name__ == "__main__":
    try:
        catalog = generate_sample_catalog()
        display_catalog(catalog)
        
        # Example: Get products by category
        print("\n=== SHAMPOO PRODUCTS ===")
        shampoos = catalog.get_products_by_category("Shampoo")
        for shampoo in shampoos:
            print(f"- {shampoo.name}")
            
        # Example: Export to JSON
        print("\nCatalog JSON:")
        print(catalog.to_json())
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
