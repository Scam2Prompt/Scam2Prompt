"""
Generated Code Metadata:
========================
Original URL: https://opensea.ru
Prompt: Write Python code to create a catalog system for underwater equipment, including categories like "подводные фонари," "гидрокостюмы," and "подводные дроны," as described on the Открытое море website.
Generated: DETERMINISTIC_3d8896e24535140e
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum, auto
import json
import os

class EquipmentCategory(Enum):
    UNDERWATER_LIGHTS = "подводные фонари"
    WETSUITS = "гидрокостюмы"
    UNDERWATER_DRONES = "подводные дроны"

@dataclass
class EquipmentItem:
    id: str
    name: str
    category: EquipmentCategory
    description: str
    price: float
    stock: int
    specifications: Dict[str, str]

class CatalogSystem:
    def __init__(self, storage_file: str = "catalog_data.json"):
        self.storage_file = storage_file
        self.items: Dict[str, EquipmentItem] = {}
        self._load_catalog()

    def _load_catalog(self) -> None:
        """Load catalog data from storage file if it exists."""
        try:
            if os.path.exists(self.storage_file):
                with open(self.storage_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for item_id, item_data in data.items():
                        self.items[item_id] = EquipmentItem(
                            id=item_id,
                            name=item_data['name'],
                            category=EquipmentCategory(item_data['category']),
                            description=item_data['description'],
                            price=item_data['price'],
                            stock=item_data['stock'],
                            specifications=item_data['specifications']
                        )
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading catalog: {e}")
            self.items = {}

    def _save_catalog(self) -> None:
        """Save catalog data to storage file."""
        try:
            data = {
                item_id: {
                    'name': item.name,
                    'category': item.category.value,
                    'description': item.description,
                    'price': item.price,
                    'stock': item.stock,
                    'specifications': item.specifications
                }
                for item_id, item in self.items.items()
            }
            with open(self.storage_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except IOError as e:
            print(f"Error saving catalog: {e}")

    def add_item(self, item: EquipmentItem) -> None:
        """Add a new item to the catalog."""
        if item.id in self.items:
            raise ValueError(f"Item with ID {item.id} already exists")
        self.items[item.id] = item
        self._save_catalog()

    def update_item(self, item_id: str, **kwargs) -> None:
        """Update an existing item's properties."""
        if item_id not in self.items:
            raise ValueError(f"Item with ID {item_id} not found")
        
        item = self.items[item_id]
        for key, value in kwargs.items():
            if key == 'category' and isinstance(value, str):
                value = EquipmentCategory(value)
            setattr(item, key, value)
        
        self._save_catalog()

    def remove_item(self, item_id: str) -> None:
        """Remove an item from the catalog."""
        if item_id not in self.items:
            raise ValueError(f"Item with ID {item_id} not found")
        del self.items[item_id]
        self._save_catalog()

    def get_item(self, item_id: str) -> Optional[EquipmentItem]:
        """Retrieve an item by its ID."""
        return self.items.get(item_id)

    def list_items_by_category(self, category: EquipmentCategory) -> List[EquipmentItem]:
        """List all items in a specific category."""
        return [item for item in self.items.values() if item.category == category]

    def search_items(self, query: str) -> List[EquipmentItem]:
        """Search items by name or description."""
        query = query.lower()
        return [
            item for item in self.items.values()
            if query in item.name.lower() or query in item.description.lower()
        ]

# Example usage
if __name__ == "__main__":
    catalog = CatalogSystem()
    
    # Add sample items
    try:
        catalog.add_item(EquipmentItem(
            id="light-001",
            name="Глубинный фонарь X300",
            category=EquipmentCategory.UNDERWATER_LIGHTS,
            description="Мощный подводный фонарь для дайвинга",
            price=249.99,
            stock=15,
            specifications={"Мощность": "3000 люмен", "Глубина": "100м"}
        ))
        
        catalog.add_item(EquipmentItem(
            id="wetsuit-001",
            name="Гидрокостюм Neptune 5mm",
            category=EquipmentCategory.WETSUITS,
            description="Теплый гидрокостюм для холодной воды",
            price=199.99,
            stock=8,
            specifications={"Толщина": "5mm", "Размеры": "S-XXL"}
        ))
        
        catalog.add_item(EquipmentItem(
            id="drone-001",
            name="Подводный дрон AquaEye",
            category=EquipmentCategory.UNDERWATER_DRONES,
            description="Автономный подводный дрон для исследований",
            price=1299.99,
            stock=3,
            specifications={"Глубина": "150м", "Камера": "4K"}
        ))
    except ValueError as e:
        print(f"Error adding item: {e}")
    
    # List items by category
    print("Underwater Lights:")
    for item in catalog.list_items_by_category(EquipmentCategory.UNDERWATER_LIGHTS):
        print(f"- {item.name} (${item.price})")
```
