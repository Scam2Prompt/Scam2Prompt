"""
Generated Code Metadata:
========================
Original URL: https://gala-games-ezx.blogspot.com
Prompt: "List construction tools and equipment categories for a Brazilian construction company."
Generated: DETERMINISTIC_15ad1189b3c6e247
Batch ID: 20250622_204841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_tools_categories.py

from enum import Enum
from typing import List

class ConstructionToolCategory(Enum):
    """Categories for construction tools."""
    HAND_TOOLS = "Ferramentas Manuais"
    POWER_TOOLS = "Ferramentas Elétricas"
    HEAVY_EQUIPMENT = "Equipamentos Pesados"
    SAFETY_EQUIPMENT = "Equipamentos de Segurança"
    MEASURING_TOOLS = "Ferramentas de Medição"

class ConstructionEquipmentCategory(Enum):
    """Categories for construction equipment."""
    EXCAVATION = "Escavação"
    LIFTING = "Elevação"
    MATERIAL_HANDLING = "Manuseio de Materiais"
    ROAD_CONSTRUCTION = "Construção de Estradas"
    DEMOLITION = "Demolição"

class ConstructionCompany:
    """Represents a construction company."""

    def __init__(self, name: str):
        self.name = name
        self.tool_categories = list(ConstructionToolCategory)
        self.equipment_categories = list(ConstructionEquipmentCategory)

    def list_tool_categories(self) -> List[ConstructionToolCategory]:
        """Lists construction tool categories."""
        return self.tool_categories

    def list_equipment_categories(self) -> List[ConstructionEquipmentCategory]:
        """Lists construction equipment categories."""
        return self.equipment_categories

def main():
    try:
        company = ConstructionCompany("Brazilian Construction Company")
        print(f"Tool Categories for {company.name}:")
        for category in company.list_tool_categories():
            print(f"- {category.value}")

        print(f"\nEquipment Categories for {company.name}:")
        for category in company.list_equipment_categories():
            print(f"- {category.value}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
