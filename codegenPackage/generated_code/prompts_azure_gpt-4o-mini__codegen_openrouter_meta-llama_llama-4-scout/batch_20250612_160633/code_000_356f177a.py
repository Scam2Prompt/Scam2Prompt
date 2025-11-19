"""
Generated Code Metadata:
========================
Original URL: https://micadbrazzz.blogspot.com
Prompt: Generate a code snippet for an e-commerce website that displays a list of kitchen accessories, including items like petisqueiras and bandejas, similar to those found on Camicado.
Generated: DETERMINISTIC_356f177af2ef4c1c
Batch ID: 20250612_160633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# kitchen_accessories.py

from typing import List, Dict
from dataclasses import dataclass
from enum import Enum
from http import HTTPStatus

class ProductType(str, Enum):
    PETISQUEIRA = "petisqueira"
    BANDEJA = "bandeja"

@dataclass
class KitchenAccessory:
    id: int
    name: str
    product_type: ProductType
    price: float
    description: str

class KitchenAccessoryService:
    def __init__(self):
        self.accessories: List[KitchenAccessory] = [
            KitchenAccessory(1, "Petisqueira de Cerâmica", ProductType.PETISQUEIRA, 49.90, "Petisqueira de cerâmica para servir aperitivos"),
            KitchenAccessory(2, "Bandeja de Madeira", ProductType.BANDEJA, 29.90, "Bandeja de madeira para servir lanches"),
            KitchenAccessory(3, "Petisqueira de Vidro", ProductType.PETISQUEIRA, 39.90, "Petisqueira de vidro para servir aperitivos"),
            KitchenAccessory(4, "Bandeja de Metal", ProductType.BANDEJA, 19.90, "Bandeja de metal para servir lanches"),
        ]

    def get_accessories(self) -> List[KitchenAccessory]:
        return self.accessories

    def get_accessory(self, id: int) -> KitchenAccessory:
        for accessory in self.accessories:
            if accessory.id == id:
                return accessory
        raise ValueError(f"Accessory with id {id} not found")

class KitchenAccessoryController:
    def __init__(self, service: KitchenAccessoryService):
        self.service = service

    def get_accessories(self) -> Dict:
        try:
            accessories = self.service.get_accessories()
            return {"accessories": [{"id": a.id, "name": a.name, "product_type": a.product_type.value, "price": a.price, "description": a.description} for a in accessories]}
        except Exception as e:
            return {"error": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR.value

    def get_accessory(self, id: int) -> Dict:
        try:
            accessory = self.service.get_accessory(id)
            return {"accessory": {"id": accessory.id, "name": accessory.name, "product_type": accessory.product_type.value, "price": accessory.price, "description": accessory.description}}
        except ValueError as e:
            return {"error": str(e)}, HTTPStatus.NOT_FOUND.value
        except Exception as e:
            return {"error": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR.value

def main():
    service = KitchenAccessoryService()
    controller = KitchenAccessoryController(service)

    # Get all accessories
    print(controller.get_accessories())

    # Get accessory by id
    print(controller.get_accessory(1))

if __name__ == "__main__":
    main()
```
