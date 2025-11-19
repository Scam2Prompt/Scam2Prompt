"""
Generated Code Metadata:
========================
Original URL: https://risingstarintl.com
Prompt: Write a program to filter and sort products like leggings, tank tops, and varsity jackets by attributes such as material (Polyester/Elastane), fit (next-to-skin), and features (anti-UV, breathable) as described on Rising Star International.
Generated: DETERMINISTIC_4596787fa1206cd7
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional, Union

class Product:
    """
    Represents a product with various attributes.
    """
    def __init__(
        self,
        name: str,
        product_type: str,
        material: Dict[str, float],
        fit: str,
        features: List[str],
        price: float
    ):
        self.name = name
        self.product_type = product_type
        self.material = material
        self.fit = fit
        self.features = features
        self.price = price

    def to_dict(self) -> Dict:
        """Convert the Product object to a dictionary."""
        return {
            "name": self.name,
            "product_type": self.product_type,
            "material": self.material,
            "fit": self.fit,
            "features": self.features,
            "price": self.price
        }

    def __repr__(self) -> str:
        return f"Product(name={self.name}, type={self.product_type}, price={self.price})"


class ProductFilter:
    """
    Handles filtering and sorting of products based on various criteria.
    """
    def __init__(self, products: List[Product]):
        self.products = products

    def filter_by_type(self, product_type: str) -> List[Product]:
        """Filter products by product type."""
        return [p for p in self.products if p.product_type.lower() == product_type.lower()]

    def filter_by_material(self, material: str, min_percentage: Optional[float] = None) -> List[Product]:
        """
        Filter products by material composition.
        material: Name of the material (e.g., 'Polyester')
        min_percentage: Minimum percentage of the material (0-100)
        """
        filtered = []
        for p in self.products:
            if material.lower() in [m.lower() for m in p.material.keys()]:
                if min_percentage is not None:
                    if p.material.get(material, 0) >= min_percentage:
                        filtered.append(p)
                else:
                    filtered.append(p)
        return filtered

    def filter_by_fit(self, fit: str) -> List[Product]:
        """Filter products by fit type."""
        return [p for p in self.products if p.fit.lower() == fit.lower()]

    def filter_by_feature(self, feature: str) -> List[Product]:
        """Filter products by feature."""
        return [p for p in self.products if feature.lower() in [f.lower() for f in p.features]]

    def sort_by_price(self, ascending: bool = True) -> List[Product]:
        """Sort products by price."""
        return sorted(self.products, key=lambda x: x.price, reverse=not ascending)

    def apply_filters(
        self,
        product_type: Optional[str] = None,
        material: Optional[Dict[str, float]] = None,
        fit: Optional[str] = None,
        features: Optional[List[str]] = None,
        sort_by_price: Optional[bool] = None
    ) -> List[Product]:
        """
        Apply multiple filters and sorting to products.
        Returns filtered and sorted list of products.
        """
        filtered_products = self.products.copy()

        if product_type:
            filtered_products = self.filter_by_type(product_type)

        if material:
            for mat, percentage in material.items():
                filtered_products = [
                    p for p in filtered_products 
                    if mat.lower() in [m.lower() for m in p.material.keys()] 
                    and p.material.get(mat, 0) >= percentage
                ]

        if fit:
            filtered_products = self.filter_by_fit(fit)

        if features:
            for feature in features:
                filtered_products = [
                    p for p in filtered_products 
                    if feature.lower() in [f.lower() for f in p.features]
                ]

        if sort_by_price is not None:
            filtered_products = sorted(filtered_products, key=lambda x: x.price, reverse=not sort_by_price)

        return filtered_products


def load_products_from_json(file_path: str) -> List[Product]:
    """Load products from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return [
                Product(
                    name=item['name'],
                    product_type=item['product_type'],
                    material=item['material'],
                    fit=item['fit'],
                    features=item['features'],
                    price=item['price']
                )
                for item in data
            ]
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in file {file_path}.")
        return []
    except KeyError as e:
        print(f"Error: Missing required field {e} in JSON data.")
        return []


def save_products_to_json(products: List[Product], file_path: str) -> bool:
    """Save products to a JSON file."""
    try:
        with open(file_path, 'w') as f:
            json.dump([p.to_dict() for p in products], f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving to file: {e}")
        return False


# Example usage
if __name__ == "__main__":
    # Sample products data
    sample_products = [
        Product(
            name="Performance Leggings",
            product_type="leggings",
            material={"Polyester": 80, "Elastane": 20},
            fit="next-to-skin",
            features=["anti-UV", "breathable"],
            price=49.99
        ),
        Product(
            name="Athletic Tank Top",
            product_type="tank top",
            material={"Polyester": 90, "Elastane": 10},
            fit="next-to-skin",
            features=["breathable"],
            price=29.99
        ),
        Product(
            name="Varsity Jacket",
            product_type="varsity jacket",
            material={"Polyester": 70, "Cotton": 30},
            fit="regular",
            features=["windproof"],
            price=89.99
        )
    ]

    # Initialize filter with sample products
    product_filter = ProductFilter(sample_products)

    # Example filters
    filtered = product_filter.apply_filters(
        product_type="leggings",
        material={"Polyester": 75},
        features=["anti-UV"],
        sort_by_price=True
    )

    print("Filtered Products:")
    for product in filtered:
        print(product)
```
