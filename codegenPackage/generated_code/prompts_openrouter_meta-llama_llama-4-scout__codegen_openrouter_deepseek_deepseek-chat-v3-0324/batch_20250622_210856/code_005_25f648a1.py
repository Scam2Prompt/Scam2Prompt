"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Write a short program to determine the optimal storage and transportation conditions for cosmetic products, based on Fabricare Cosmeticos' logistics and quality control procedures.
Generated: DETERMINISTIC_25f648a1329bb591
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List, Optional

class ProductType(Enum):
    """Enumeration of cosmetic product types."""
    CREAM = auto()
    LIQUID = auto()
    POWDER = auto()
    GEL = auto()
    OIL = auto()

class StorageCondition(Enum):
    """Enumeration of storage conditions."""
    ROOM_TEMP = "Room temperature (15-25°C)"
    REFRIGERATED = "Refrigerated (2-8°C)"
    COOL = "Cool (8-15°C)"
    DRY = "Dry environment (<40% humidity)"

class TransportCondition(Enum):
    """Enumeration of transport conditions."""
    AMBIENT = "Ambient temperature"
    TEMPERATURE_CONTROLLED = "Temperature controlled (2-25°C)"
    REFRIGERATED = "Refrigerated (2-8°C)"

@dataclass
class CosmeticProduct:
    """Data class representing a cosmetic product."""
    name: str
    product_type: ProductType
    optimal_storage: StorageCondition
    optimal_transport: TransportCondition
    shelf_life_months: int
    sensitive_to_light: bool = False
    sensitive_to_humidity: bool = False

class CosmeticStorageOptimizer:
    """Determines optimal storage and transport conditions for cosmetic products."""
    
    def __init__(self):
        self.product_db: Dict[str, CosmeticProduct] = {}
        self._load_default_products()
    
    def _load_default_products(self) -> None:
        """Load default product database."""
        default_products = [
            CosmeticProduct(
                name="Moisturizing Cream",
                product_type=ProductType.CREAM,
                optimal_storage=StorageCondition.ROOM_TEMP,
                optimal_transport=TransportCondition.AMBIENT,
                shelf_life_months=24,
                sensitive_to_humidity=True
            ),
            CosmeticProduct(
                name="Vitamin C Serum",
                product_type=ProductType.LIQUID,
                optimal_storage=StorageCondition.REFRIGERATED,
                optimal_transport=TransportCondition.REFRIGERATED,
                shelf_life_months=12,
                sensitive_to_light=True
            ),
            CosmeticProduct(
                name="Mineral Powder",
                product_type=ProductType.POWDER,
                optimal_storage=StorageCondition.DRY,
                optimal_transport=TransportCondition.AMBIENT,
                shelf_life_months=36,
                sensitive_to_humidity=True
            )
        ]
        for product in default_products:
            self.product_db[product.name] = product
    
    def add_product(self, product: CosmeticProduct) -> None:
        """Add a new product to the database."""
        if product.name in self.product_db:
            raise ValueError(f"Product '{product.name}' already exists in database")
        self.product_db[product.name] = product
    
    def get_product(self, product_name: str) -> Optional[CosmeticProduct]:
        """Retrieve product information by name."""
        return self.product_db.get(product_name)
    
    def get_all_products(self) -> List[CosmeticProduct]:
        """Retrieve all products in the database."""
        return list(self.product_db.values())
    
    def export_to_json(self, file_path: str) -> None:
        """Export product database to JSON file."""
        try:
            with open(file_path, 'w') as f:
                products_data = [{
                    'name': product.name,
                    'product_type': product.product_type.name,
                    'optimal_storage': product.optimal_storage.value,
                    'optimal_transport': product.optimal_transport.value,
                    'shelf_life_months': product.shelf_life_months,
                    'sensitive_to_light': product.sensitive_to_light,
                    'sensitive_to_humidity': product.sensitive_to_humidity
                } for product in self.product_db.values()]
                json.dump(products_data, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to export to JSON: {str(e)}")
    
    def import_from_json(self, file_path: str) -> None:
        """Import product database from JSON file."""
        try:
            with open(file_path, 'r') as f:
                products_data = json.load(f)
                for product_data in products_data:
                    product = CosmeticProduct(
                        name=product_data['name'],
                        product_type=ProductType[product_data['product_type']],
                        optimal_storage=StorageCondition(product_data['optimal_storage']),
                        optimal_transport=TransportCondition(product_data['optimal_transport']),
                        shelf_life_months=product_data['shelf_life_months'],
                        sensitive_to_light=product_data.get('sensitive_to_light', False),
                        sensitive_to_humidity=product_data.get('sensitive_to_humidity', False)
                    )
                    self.product_db[product.name] = product
        except (IOError, json.JSONDecodeError, KeyError, ValueError) as e:
            raise ValueError(f"Failed to import from JSON: {str(e)}")

def main():
    """Example usage of the CosmeticStorageOptimizer."""
    optimizer = CosmeticStorageOptimizer()
    
    # Add a new product
    try:
        new_product = CosmeticProduct(
            name="Hyaluronic Acid Gel",
            product_type=ProductType.GEL,
            optimal_storage=StorageCondition.REFRIGERATED,
            optimal_transport=TransportCondition.TEMPERATURE_CONTROLLED,
            shelf_life_months=18,
            sensitive_to_light=True
        )
        optimizer.add_product(new_product)
    except ValueError as e:
        print(f"Error adding product: {e}")
    
    # Query product information
    product_name = "Vitamin C Serum"
    product = optimizer.get_product(product_name)
    if product:
        print(f"\nOptimal conditions for {product_name}:")
        print(f"- Storage: {product.optimal_storage.value}")
        print(f"- Transport: {product.optimal_transport.value}")
        print(f"- Shelf life: {product.shelf_life_months} months")
        if product.sensitive_to_light:
            print("- Note: Sensitive to light")
        if product.sensitive_to_humidity:
            print("- Note: Sensitive to humidity")
    
    # Export database to JSON
    try:
        optimizer.export_to_json("cosmetic_products.json")
        print("\nProduct database exported successfully.")
    except IOError as e:
        print(f"\nExport failed: {e}")

if __name__ == "__main__":
    main()
```
