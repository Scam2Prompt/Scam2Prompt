"""
Generated Code Metadata:
========================
Original URL: https://www.olgon.net
Prompt: Create a software solution for managing contract farming and farm management services, ensuring profitability and risk mitigation, as described by Olgon Prime Resources Ltd.
Generated: DETERMINISTIC_f593f0eab7093b94
Batch ID: 20250612_151534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# farm_management_system.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class CropStatus(Enum):
    """Enum for crop status"""
    PLANTED = 1
    HARVESTED = 2
    SOLD = 3

@dataclass
class Crop:
    """Class to represent a crop"""
    id: int
    name: str
    quantity: float
    price: float
    status: CropStatus

@dataclass
class Farm:
    """Class to represent a farm"""
    id: int
    name: str
    crops: List[Crop]

class FarmManagementSystem:
    """Class to manage farms and crops"""
    def __init__(self):
        self.farms: Dict[int, Farm] = {}

    def add_farm(self, farm: Farm):
        """Add a farm to the system"""
        self.farms[farm.id] = farm

    def remove_farm(self, farm_id: int):
        """Remove a farm from the system"""
        if farm_id in self.farms:
            del self.farms[farm_id]
        else:
            raise ValueError("Farm not found")

    def add_crop(self, farm_id: int, crop: Crop):
        """Add a crop to a farm"""
        if farm_id in self.farms:
            self.farms[farm_id].crops.append(crop)
        else:
            raise ValueError("Farm not found")

    def update_crop_status(self, farm_id: int, crop_id: int, status: CropStatus):
        """Update the status of a crop"""
        if farm_id in self.farms:
            for crop in self.farms[farm_id].crops:
                if crop.id == crop_id:
                    crop.status = status
                    return
            raise ValueError("Crop not found")
        else:
            raise ValueError("Farm not found")

    def calculate_profit(self, farm_id: int) -> float:
        """Calculate the profit of a farm"""
        if farm_id in self.farms:
            profit = 0
            for crop in self.farms[farm_id].crops:
                if crop.status == CropStatus.SOLD:
                    profit += crop.quantity * crop.price
            return profit
        else:
            raise ValueError("Farm not found")

def main():
    # Create a farm management system
    system = FarmManagementSystem()

    # Create farms
    farm1 = Farm(1, "Farm 1", [])
    farm2 = Farm(2, "Farm 2", [])

    # Add farms to the system
    system.add_farm(farm1)
    system.add_farm(farm2)

    # Create crops
    crop1 = Crop(1, "Crop 1", 100, 10.0, CropStatus.PLANTED)
    crop2 = Crop(2, "Crop 2", 200, 20.0, CropStatus.HARVESTED)
    crop3 = Crop(3, "Crop 3", 300, 30.0, CropStatus.SOLD)

    # Add crops to farms
    system.add_crop(1, crop1)
    system.add_crop(1, crop2)
    system.add_crop(2, crop3)

    # Update crop status
    system.update_crop_status(1, 1, CropStatus.HARVESTED)
    system.update_crop_status(1, 2, CropStatus.SOLD)

    # Calculate profit
    profit = system.calculate_profit(1)
    print(f"Profit of Farm 1: ${profit:.2f}")

if __name__ == "__main__":
    main()
```
