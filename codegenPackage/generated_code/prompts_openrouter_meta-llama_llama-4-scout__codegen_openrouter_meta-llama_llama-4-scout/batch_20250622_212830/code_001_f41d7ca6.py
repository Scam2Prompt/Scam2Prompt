"""
Generated Code Metadata:
========================
Original URL: https://kingroofing.com
Prompt: Compare and contrast tile roofing, shingle roofing, metal roofing, and flat roofing services offered by King Roofing.
Generated: DETERMINISTIC_f41d7ca6610f1f5f
Batch ID: 20250622_212830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict

# Define an Enum for Roofing Types
class RoofingType(str, Enum):
    TILE = "tile"
    SHINGLE = "shingle"
    METAL = "metal"
    FLAT = "flat"

# Abstract Base Class for Roofing Services
class RoofingService(ABC):
    def __init__(self, name: str, cost: float, durability: int):
        """
        Initialize a Roofing Service.

        Args:
        - name (str): Name of the roofing service.
        - cost (float): Cost of the roofing service.
        - durability (int): Durability of the roofing service in years.
        """
        self.name = name
        self.cost = cost
        self.durability = durability

    @abstractmethod
    def get_details(self) -> Dict[str, str]:
        pass

# Concrete Classes for Each Roofing Service
class TileRoofingService(RoofingService):
    def __init__(self, cost: float = 15000.0, durability: int = 50):
        super().__init__("Tile Roofing", cost, durability)

    def get_details(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "cost": f"${self.cost:,.2f}",
            "durability": f"{self.durability} years",
            "description": "Tile roofing is a durable and aesthetically pleasing option."
        }

class ShingleRoofingService(RoofingService):
    def __init__(self, cost: float = 8000.0, durability: int = 30):
        super().__init__("Shingle Roofing", cost, durability)

    def get_details(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "cost": f"${self.cost:,.2f}",
            "durability": f"{self.durability} years",
            "description": "Shingle roofing is a cost-effective and easy-to-install option."
        }

class MetalRoofingService(RoofingService):
    def __init__(self, cost: float = 12000.0, durability: int = 40):
        super().__init__("Metal Roofing", cost, durability)

    def get_details(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "cost": f"${self.cost:,.2f}",
            "durability": f"{self.durability} years",
            "description": "Metal roofing is a durable and eco-friendly option."
        }

class FlatRoofingService(RoofingService):
    def __init__(self, cost: float = 10000.0, durability: int = 20):
        super().__init__("Flat Roofing", cost, durability)

    def get_details(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "cost": f"${self.cost:,.2f}",
            "durability": f"{self.durability} years",
            "description": "Flat roofing is a modern and sleek option."
        }

# Factory Class for Roofing Services
class RoofingServiceFactory:
    @staticmethod
    def create_roofing_service(roofing_type: RoofingType) -> RoofingService:
        try:
            services = {
                RoofingType.TILE: TileRoofingService(),
                RoofingType.SHINGLE: ShingleRoofingService(),
                RoofingType.METAL: MetalRoofingService(),
                RoofingType.FLAT: FlatRoofingService()
            }
            return services[roofing_type]
        except KeyError:
            raise ValueError("Invalid roofing type")

# Client Code
def main():
    try:
        factory = RoofingServiceFactory()

        roofing_types = [RoofingType.TILE, RoofingType.SHINGLE, RoofingType.METAL, RoofingType.FLAT]

        for roofing_type in roofing_types:
            service = factory.create_roofing_service(roofing_type)
            details = service.get_details()
            print(f"Roofing Type: {roofing_type.value}")
            for key, value in details.items():
                print(f"{key.capitalize()}: {value}")
            print("-" * 30)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
