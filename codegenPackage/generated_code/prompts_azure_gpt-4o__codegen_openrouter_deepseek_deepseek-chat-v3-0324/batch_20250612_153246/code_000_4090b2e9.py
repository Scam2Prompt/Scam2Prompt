"""
Generated Code Metadata:
========================
Original URL: https://nodoitalia.com
Prompt: Write a Python script to generate a catalog of outdoor furniture collections, including details like product names, materials (e.g., Olyna), and categories (e.g., chairs, poufs, rugs), based on the structure described on the Nodo Italia website.
Generated: DETERMINISTIC_4090b2e9de8825c6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, asdict
from typing import List, Optional
from enum import Enum, auto
import random
from faker import Faker

# Initialize Faker for generating fake data
fake = Faker()

class Material(Enum):
    OLYNA = "Olyna"
    TEKA = "Teka"
    RESIN = "Resin"
    ALUMINUM = "Aluminum"
    STEEL = "Steel"
    WOOD = "Wood"
    RATTAN = "Rattan"
    FABRIC = "Fabric"

class Category(Enum):
    CHAIRS = "Chairs"
    POUFS = "Poufs"
    RUGS = "Rugs"
    TABLES = "Tables"
    SOFAS = "Sofas"
    SUNBEDS = "Sunbeds"
    UMBRELLAS = "Umbrellas"
    ACCESSORIES = "Accessories"

@dataclass
class Product:
    id: str
    name: str
    description: str
    material: Material
    category: Category
    dimensions: str
    weight: float
    price: float
    colors: List[str]
    in_stock: bool

    def to_dict(self):
        return asdict(self)

class OutdoorFurnitureCatalog:
    def __init__(self):
        self.products = []
        self._generate_products()

    def _generate_dimensions(self, category: Category) -> str:
        if category == Category.CHAIRS:
            return f"{random.randint(50, 80)}x{random.randint(50, 80)}x{random.randint(70, 100)} cm"
        elif category == Category.POUFS:
            return f"{random.randint(30, 50)}x{random.randint(30, 50)}x{random.randint(30, 50)} cm"
        elif category == Category.RUGS:
            return f"{random.randint(120, 200)}x{random.randint(80, 180)} cm"
        elif category == Category.TABLES:
            return f"{random.randint(60, 120)}x{random.randint(60, 120)}x{random.randint(40, 80)} cm"
        else:
            return f"{random.randint(50, 200)}x{random.randint(50, 200)}x{random.randint(50, 100)} cm"

    def _generate_material(self, category: Category) -> Material:
        if category == Category.RUGS:
            return random.choice([Material.OLYNA, Material.FABRIC])
        elif category in [Category.CHAIRS, Category.SOFAS, Category.SUNBEDS]:
            return random.choice([Material.TEKA, Material.RESIN, Material.ALUMINUM, Material.RATTAN])
        elif category == Category.TABLES:
            return random.choice([Material.TEKA, Material.WOOD, Material.ALUMINUM])
        else:
            return random.choice(list(Material))

    def _generate_colors(self) -> List[str]:
        colors = ["Black", "White", "Beige", "Gray", "Brown", "Blue", "Green"]
        return random.sample(colors, k=random.randint(1, 3))

    def _generate_product_name(self, category: Category) -> str:
        prefixes = {
            Category.CHAIRS: ["Lounge", "Patio", "Outdoor", "Garden", "Relax"],
            Category.POUFS: ["Comfort", "Soft", "Round", "Square", "Modern"],
            Category.RUGS: ["Elegant", "Textured", "Patterned", "Outdoor", "Decorative"],
            Category.TABLES: ["Dining", "Coffee", "Side", "Outdoor", "Garden"],
            Category.SOFAS: ["Sectional", "Modular", "Outdoor", "Lounge", "Comfort"],
            Category.SUNBEDS: ["Relax", "Poolside", "Adjustable", "Luxury", "Outdoor"],
            Category.UMBRELLAS: ["Patio", "Market", "Cantilever", "Garden", "Outdoor"],
            Category.ACCESSORIES: ["Decorative", "Functional", "Outdoor", "Garden", "Modern"]
        }
        suffixes = {
            Category.CHAIRS: ["Chair", "Seat", "Armchair", "Recliner"],
            Category.POUFS: ["Pouf", "Ottoman", "Footrest"],
            Category.RUGS: ["Rug", "Mat", "Carpet"],
            Category.TABLES: ["Table", "Desk", "Stand"],
            Category.SOFAS: ["Sofa", "Couch", "Daybed"],
            Category.SUNBEDS: ["Sunbed", "Lounger", "Chaise"],
            Category.UMBRELLAS: ["Umbrella", "Shade", "Canopy"],
            Category.ACCESSORIES: ["Pillow", "Cushion", "Tray", "Light"]
        }
        prefix = random.choice(prefixes[category])
        suffix = random.choice(suffixes[category])
        return f"{prefix} {suffix}"

    def _generate_products(self):
        for i in range(1, 51):
            category = random.choice(list(Category))
            material = self._generate_material(category)
            product = Product(
                id=f"PROD-{i:03d}",
                name=self._generate_product_name(category),
                description=fake.sentence(nb_words=10),
                material=material,
                category=category,
                dimensions=self._generate_dimensions(category),
                weight=round(random.uniform(2.0, 25.0), 1),
                price=round(random.uniform(50.0, 2000.0), 2),
                colors=self._generate_colors(),
                in_stock=random.choice([True, False])
            )
            self.products.append(product)

    def get_catalog(self) -> List[dict]:
        return [product.to_dict() for product in self.products]

    def save_to_json(self, filename: str = "outdoor_furniture_catalog.json"):
        try:
            with open(filename, 'w') as f:
                json.dump(self.get_catalog(), f, indent=4, default=str)
            print(f"Catalog successfully saved to {filename}")
        except Exception as e:
            print(f"Error saving catalog: {e}")

    def filter_by_category(self, category: Category) -> List[dict]:
        return [product.to_dict() for product in self.products if product.category == category]

    def filter_by_material(self, material: Material) -> List[dict]:
        return [product.to_dict() for product in self.products if product.material == material]

if __name__ == "__main__":
    catalog = OutdoorFurnitureCatalog()
    catalog.save_to_json()
```
