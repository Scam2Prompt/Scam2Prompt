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
from typing import List, Dict, Optional
from enum import Enum

class EquipmentType(Enum):
    """Enum representing different types of sports equipment."""
    ACCESSORIES = "Acessórios"
    UNIFORMS = "Fardamentos"
    FOOTWEAR = "Calçados"
    EQUIPMENT = "Equipamentos"

class SportsEquipment:
    """Class representing a sports equipment item."""
    def __init__(self, name: str, equipment_type: EquipmentType, price: float):
        self.name = name
        self.type = equipment_type
        self.price = price

def filter_equipment_by_type(
    equipment_list: List[SportsEquipment], 
    filter_type: Optional[EquipmentType] = None
) -> List[SportsEquipment]:
    """
    Filters a list of sports equipment by the specified type.
    
    Args:
        equipment_list: List of SportsEquipment objects to filter.
        filter_type: EquipmentType to filter by. If None, returns all items.
    
    Returns:
        List of SportsEquipment objects that match the filter type.
    
    Raises:
        TypeError: If equipment_list contains non-SportsEquipment objects.
    """
    if not all(isinstance(item, SportsEquipment) for item in equipment_list):
        raise TypeError("All items in equipment_list must be SportsEquipment instances.")
    
    if filter_type is None:
        return equipment_list
    
    return [item for item in equipment_list if item.type == filter_type]

# Example usage
if __name__ == "__main__":
    # Sample equipment list
    equipment = [
        SportsEquipment("Basketball", EquipmentType.EQUIPMENT, 29.99),
        SportsEquipment("Jersey", EquipmentType.UNIFORMS, 49.99),
        SportsEquipment("Running Shoes", EquipmentType.FOOTWEAR, 89.99),
        SportsEquipment("Water Bottle", EquipmentType.ACCESSORIES, 12.99),
    ]
    
    # Filter by type
    accessories = filter_equipment_by_type(equipment, EquipmentType.ACCESSORIES)
    print("Accessories:")
    for item in accessories:
        print(f"- {item.name}: ${item.price}")
```
