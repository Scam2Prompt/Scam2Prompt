"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Develop a library function that filters sports equipment by type, such as "Acessórios" or "Fardamentos", as described on the sports blog page.
Generated: DETERMINISTIC_39caa56e3fdaa809
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# equipment_filter.py

from enum import Enum
from typing import List, Dict

class EquipmentType(str, Enum):
    """Enum for equipment types."""
    ACESSORIOS = "Acessórios"
    FARDAMENTOS = "Fardamentos"
    # Add more types as needed

class Equipment:
    """Represents a sports equipment."""
    def __init__(self, name: str, equipment_type: EquipmentType):
        """
        Initializes an Equipment object.

        Args:
        - name (str): The name of the equipment.
        - equipment_type (EquipmentType): The type of the equipment.
        """
        self.name = name
        self.equipment_type = equipment_type

def filter_equipment(equipment_list: List[Equipment], equipment_type: EquipmentType) -> List[Equipment]:
    """
    Filters a list of sports equipment by type.

    Args:
    - equipment_list (List[Equipment]): The list of equipment to filter.
    - equipment_type (EquipmentType): The type of equipment to filter by.

    Returns:
    - List[Equipment]: The filtered list of equipment.
    """
    return [equipment for equipment in equipment_list if equipment.equipment_type == equipment_type]

def main():
    # Example usage
    equipment_list: List[Equipment] = [
        Equipment("Ball", EquipmentType.ACESSORIOS),
        Equipment("Shirt", EquipmentType.FARDAMENTOS),
        Equipment("Shoes", EquipmentType.ACESSORIOS),
        Equipment("Pants", EquipmentType.FARDAMENTOS),
    ]

    try:
        filtered_equipment = filter_equipment(equipment_list, EquipmentType.ACESSORIOS)
        print("Filtered Equipment:")
        for equipment in filtered_equipment:
            print(f"- {equipment.name} ({equipment.equipment_type.value})")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
