"""
Generated Code Metadata:
========================
Original URL: https://farmaciasantiagoapostol.com
Prompt: Write a Python script to manage an online pharmacy store's inventory, including sections for noticias (news), tienda (store), and contacto (contact).
Generated: DETERMINISTIC_43933456c7dcce5d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import Dict, List, Optional

class InventoryItem:
    """Class representing an inventory item in the pharmacy store."""
    def __init__(self, id: int, name: str, description: str, price: float, quantity: int):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def to_dict(self) -> Dict:
        """Convert the item to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'quantity': self.quantity
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'InventoryItem':
        """Create an InventoryItem from a dictionary."""
        return cls(
            id=data['id'],
            name=data['name'],
            description=data['description'],
            price=data['price'],
            quantity=data['quantity']
        )

class PharmacyStore:
    """Main class to manage the pharmacy store operations."""
    def __init__(self, inventory_file: str = 'inventory.json'):
        self.inventory_file = inventory_file
        self.inventory: List[InventoryItem] = []
        self.news: List[str] = []
        self.load_inventory()

    def load_inventory(self) -> None:
        """Load inventory from JSON file."""
        try:
            if os.path.exists(self.inventory_file):
                with open(self.inventory_file, 'r') as f:
                    data = json.load(f)
                    self.inventory = [InventoryItem.from_dict(item) for item in data]
        except Exception as e:
            print(f"Error loading inventory: {e}")
            self.inventory = []

    def save_inventory(self) -> None:
        """Save inventory to JSON file."""
        try:
            with open(self.inventory_file, 'w') as f:
                json.dump([item.to_dict() for item in self.inventory], f, indent=2)
        except Exception as e:
            print(f"Error saving inventory: {e}")

    def add_item(self, item: InventoryItem) -> None:
        """Add a new item to the inventory."""
        self.inventory.append(item)
        self.save_inventory()

    def update_item(self, item_id: int, **kwargs) -> bool:
        """Update an existing item in the inventory."""
        for item in self.inventory:
            if item.id == item_id:
                for key, value in kwargs.items():
                    if hasattr(item, key):
                        setattr(item, key, value)
                self.save_inventory()
                return True
        return False

    def remove_item(self, item_id: int) -> bool:
        """Remove an item from the inventory."""
        for i, item in enumerate(self.inventory):
            if item.id == item_id:
                del self.inventory[i]
                self.save_inventory()
                return True
        return False

    def get_item(self, item_id: int) -> Optional[InventoryItem]:
        """Get an item by its ID."""
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None

    def list_items(self) -> List[InventoryItem]:
        """List all items in the inventory."""
        return self.inventory

    def add_news(self, news_item: str) -> None:
        """Add a news item."""
        self.news.append(news_item)

    def list_news(self) -> List[str]:
        """List all news items."""
        return self.news

    def contact_info(self) -> Dict[str, str]:
        """Return contact information."""
        return {
            'email': 'contacto@farmaciaonline.com',
            'phone': '+1234567890',
            'address': '123 Calle Farmacia, Ciudad, País'
        }

def main():
    """Main function to demonstrate the pharmacy store functionality."""
    store = PharmacyStore()

    # Example usage
    store.add_item(InventoryItem(1, "Paracetamol", "Analgésico y antipirético", 5.99, 100))
    store.add_item(InventoryItem(2, "Ibuprofeno", "Antiinflamatorio", 7.50, 80))

    store.add_news("Nuevo lote de vacunas disponibles")
    store.add_news("Horario extendido durante festivos")

    print("=== Tienda ===")
    for item in store.list_items():
        print(f"{item.name}: ${item.price} - {item.quantity} unidades")

    print("\n=== Noticias ===")
    for news in store.list_news():
        print(f"- {news}")

    print("\n=== Contacto ===")
    contact = store.contact_info()
    print(f"Email: {contact['email']}")
    print(f"Teléfono: {contact['phone']}")
    print(f"Dirección: {contact['address']}")

if __name__ == "__main__":
    main()
```
