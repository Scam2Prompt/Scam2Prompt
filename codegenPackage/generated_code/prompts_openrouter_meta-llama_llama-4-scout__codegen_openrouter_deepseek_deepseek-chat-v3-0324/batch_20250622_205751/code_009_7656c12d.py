"""
Generated Code Metadata:
========================
Original URL: https://novaforma.hr
Prompt: "Write a script to generate a catalog of products and services offered by a sign manufacturing company like Nova Forma d.o.o."
Generated: DETERMINISTIC_7656c12d1a57262c
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from dataclasses import dataclass, asdict
from typing import List, Optional
from enum import Enum, auto

class ProductCategory(Enum):
    SIGNS = auto()
    DIGITAL_PRINTING = auto()
    LIGHTING = auto()
    INSTALLATION = auto()
    MAINTENANCE = auto()

@dataclass
class Product:
    id: str
    name: str
    description: str
    category: ProductCategory
    price: float
    lead_time_days: int
    materials: List[str]
    available: bool = True
    customization_options: Optional[List[str]] = None

class CatalogGenerator:
    def __init__(self):
        self.materials = [
            "Acrylic", "Aluminum", "Stainless Steel", "PVC", 
            "Vinyl", "LED", "Neon", "Wood"
        ]
        self.customization_options = [
            "Size", "Color", "Font", "Logo", "Illumination", 
            "Mounting Type", "Finishing"
        ]
        
    def generate_product_id(self) -> str:
        return f"PRD-{random.randint(1000, 9999)}"
    
    def generate_product_name(self, category: ProductCategory) -> str:
        names = {
            ProductCategory.SIGNS: [
                "Illuminated Channel Letter", "Dimensional Letter", 
                "Pylon Sign", "Monument Sign", "Wayfinding Sign"
            ],
            ProductCategory.DIGITAL_PRINTING: [
                "Banner Printing", "Vehicle Wrap", 
                "Window Graphic", "Wall Mural"
            ],
            ProductCategory.LIGHTING: [
                "LED Lighting Kit", "Neon Sign", 
                "Backlit Sign", "Edge-lit Panel"
            ],
            ProductCategory.INSTALLATION: [
                "Sign Installation", "Electrical Hookup", 
                "Permit Assistance", "Site Survey"
            ],
            ProductCategory.MAINTENANCE: [
                "Sign Repair", "LED Replacement", 
                "Cleaning Service", "Annual Maintenance"
            ]
        }
        return random.choice(names[category])
    
    def generate_description(self, name: str) -> str:
        descriptions = {
            "Illuminated Channel Letter": "Custom fabricated channel letters with LED illumination for maximum visibility.",
            "Dimensional Letter": "Premium dimensional letters for a sophisticated look, available in various materials.",
            "Pylon Sign": "Tall freestanding signs perfect for retail locations and business parks.",
            "Monument Sign": "Ground-mounted signs that provide a professional appearance for businesses.",
            "Wayfinding Sign": "Directional signs to guide visitors through your facility.",
            "Banner Printing": "High-quality digitally printed banners for indoor and outdoor use.",
            "Vehicle Wrap": "Full or partial vehicle wraps to turn your car into a mobile advertisement.",
            "Window Graphic": "Perforated or opaque window graphics for branding and privacy.",
            "Wall Mural": "Large-scale wall graphics to transform any space.",
            "LED Lighting Kit": "Energy-efficient LED lighting solutions for signs and displays.",
            "Neon Sign": "Classic neon signs for a retro or modern look.",
            "Backlit Sign": "Signs with internal illumination for 24/7 visibility.",
            "Edge-lit Panel": "Sleek illuminated panels with edge lighting technology.",
            "Sign Installation": "Professional installation services for all types of signs.",
            "Electrical Hookup": "Certified electricians for sign power connections.",
            "Permit Assistance": "Help with obtaining necessary sign permits and approvals.",
            "Site Survey": "On-site evaluation for optimal sign placement and design.",
            "Sign Repair": "Expert repair services for damaged or malfunctioning signs.",
            "LED Replacement": "Replacement of LED modules and components.",
            "Cleaning Service": "Professional cleaning to maintain sign appearance.",
            "Annual Maintenance": "Comprehensive maintenance program to extend sign life."
        }
        return descriptions.get(name, "Professional sign product with custom options available.")
    
    def generate_product(self) -> Product:
        category = random.choice(list(ProductCategory))
        name = self.generate_product_name(category)
        materials = random.sample(
            self.materials, 
            k=random.randint(1, min(3, len(self.materials)))
        )
        customization = random.sample(
            self.customization_options, 
            k=random.randint(1, min(3, len(self.customization_options)))
        ) if random.random() > 0.3 else None
        
        return Product(
            id=self.generate_product_id(),
            name=name,
            description=self.generate_description(name),
            category=category,
            price=round(random.uniform(50, 5000), 2),
            lead_time_days=random.randint(1, 30),
            materials=materials,
            available=random.random() > 0.1,
            customization_options=customization
        )
    
    def generate_catalog(self, num_products: int = 20) -> List[Product]:
        return [self.generate_product() for _ in range(num_products)]
    
    def save_catalog_to_json(self, products: List[Product], filename: str = "sign_catalog.json"):
        with open(filename, 'w') as f:
            json.dump([asdict(product) for product in products], f, indent=2, default=str)

def main():
    try:
        generator = CatalogGenerator()
        catalog = generator.generate_catalog()
        generator.save_catalog_to_json(catalog)
        print(f"Successfully generated catalog with {len(catalog)} products.")
    except Exception as e:
        print(f"Error generating catalog: {e}")

if __name__ == "__main__":
    main()
```
