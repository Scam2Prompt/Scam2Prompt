"""
Generated Code Metadata:
========================
Original URL: https://somoscorujasbraz.blogspot.com
Prompt: Write a Python code snippet to create an e-commerce product catalog for baby clothing and accessories, including product names, prices, and descriptions, similar to the ones listed on Somos Corujas.
Generated: DETERMINISTIC_6e390d6182ad20bb
Batch ID: 20250622_212549
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
    Represents a product in the baby clothing and accessories catalog.
    """
    def __init__(
        self,
        id: str,
        name: str,
        price: float,
        description: str,
        category: str,
        sizes: Optional[List[str]] = None,
        colors: Optional[List[str]] = None,
        in_stock: bool = True
    ):
        """
        Initialize a product with its attributes.
        
        Args:
            id: Unique identifier for the product
            name: Name of the product
            price: Price of the product
            description: Description of the product
            category: Category of the product (e.g., 'clothing', 'accessories')
            sizes: Available sizes (optional)
            colors: Available colors (optional)
            in_stock: Whether the product is in stock (default: True)
        """
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.category = category
        self.sizes = sizes if sizes else []
        self.colors = colors if colors else []
        self.in_stock = in_stock

    def to_dict(self) -> Dict:
        """
        Convert the product to a dictionary for serialization.
        
        Returns:
            Dictionary representation of the product
        """
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'category': self.category,
            'sizes': self.sizes,
            'colors': self.colors,
            'in_stock': self.in_stock
        }

class ProductCatalog:
    """
    Manages a collection of baby clothing and accessory products.
    """
    def __init__(self):
        self.products: Dict[str, Product] = {}

    def add_product(self, product: Product) -> None:
        """
        Add a product to the catalog.
        
        Args:
            product: Product to add
        """
        if product.id in self.products:
            raise ValueError(f"Product with ID {product.id} already exists")
        self.products[product.id] = product

    def remove_product(self, product_id: str) -> None:
        """
        Remove a product from the catalog.
        
        Args:
            product_id: ID of the product to remove
        """
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        del self.products[product_id]

    def get_product(self, product_id: str) -> Product:
        """
        Retrieve a product by its ID.
        
        Args:
            product_id: ID of the product to retrieve
            
        Returns:
            The requested product
        """
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        return self.products[product_id]

    def get_all_products(self) -> List[Product]:
        """
        Retrieve all products in the catalog.
        
        Returns:
            List of all products
        """
        return list(self.products.values())

    def save_to_file(self, filename: str) -> None:
        """
        Save the catalog to a JSON file.
        
        Args:
            filename: Name of the file to save to
        """
        products_data = [product.to_dict() for product in self.products.values()]
        with open(filename, 'w') as f:
            json.dump(products_data, f, indent=4)

    def load_from_file(self, filename: str) -> None:
        """
        Load the catalog from a JSON file.
        
        Args:
            filename: Name of the file to load from
        """
        with open(filename, 'r') as f:
            products_data = json.load(f)
        
        self.products = {}
        for product_data in products_data:
            product = Product(
                id=product_data['id'],
                name=product_data['name'],
                price=product_data['price'],
                description=product_data['description'],
                category=product_data['category'],
                sizes=product_data.get('sizes', []),
                colors=product_data.get('colors', []),
                in_stock=product_data.get('in_stock', True)
            )
            self.products[product.id] = product

def create_sample_catalog() -> ProductCatalog:
    """
    Create a sample catalog with baby clothing and accessories.
    
    Returns:
        ProductCatalog with sample products
    """
    catalog = ProductCatalog()
    
    # Add sample products
    catalog.add_product(Product(
        id="bc001",
        name="Organic Cotton Baby Bodysuit",
        price=24.99,
        description="Soft 100% organic cotton bodysuit with snap buttons",
        category="clothing",
        sizes=["0-3M", "3-6M", "6-12M"],
        colors=["White", "Pink", "Blue"],
        in_stock=True
    ))
    
    catalog.add_product(Product(
        id="bc002",
        name="Baby Knitted Hat",
        price=18.50,
        description="Warm knitted hat with cute animal ears",
        category="accessories",
        sizes["Newborn", "0-6M", "6-12M"],
        colors=["Gray", "Pink", "Blue"],
        in_stock=True
    ))
    
    catalog.add_product(Product(
        id="bc003",
        name="Baby Leggings",
        price=22.99,
        description="Stretchy comfortable leggings with fun prints",
        category="clothing",
        sizes=["0-3M", "3-6M", "6-12M"],
        colors=["Black", "Gray", "Multicolor"],
        in_stock=True
    ))
    
    catalog.add_product(Product(
        id="bc004",
        name="Muslin Swaddle Blanket",
        price=29.99,
        description="Large breathable muslin blanket for swaddling",
        category="accessories",
        sizes=["Large"],
        colors=["White", "Pink", "Blue"],
        in_stock=True
    ))
    
    catalog.add_product(Product(
        id="bc005",
        name="Baby Denim Jacket",
        price=34.99,
        description="Stylish denim jacket with snap buttons",
        category="clothing",
        sizes=["0-3M", "3-6M", "6-12M"],
        colors=["Blue", "Black"],
        in_stock=False
    ))
    
    return catalog

# Example usage
if __name__ == "__main__":
    catalog = create_sample_catalog()
    
    # Save catalog to file
    catalog.save_to_file("baby_catalog.json")
    
    # Load catalog from file
    new_catalog = ProductCatalog()
    new_catalog.load_from_file("baby_catalog.json")
    
    # Print all products
    for product in new_catalog.get_all_products():
        print(f"{product.name}: ${product.price:.2f}")
```
