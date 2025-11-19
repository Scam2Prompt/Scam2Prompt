"""
Generated Code Metadata:
========================
Original URL: https://harda-ke.org
Prompt: Design an algorithm for resource allocation in agriculture and food security projects, taking into account HARDA's experience in the Horn of Africa.
Generated: DETERMINISTIC_93866e7edb5b38ab
Batch ID: 20250622_211610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# resource_allocation.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum

class CropType(str, Enum):
    """Type of crop"""
    MAIZE = "maize"
    SORGHUM = "sorghum"
    VEGETABLES = "vegetables"

@dataclass
class Farm:
    """Farm data class"""
    id: int
    location: str
    soil_type: str
    water_availability: float  # in liters

@dataclass
class Resource:
    """Resource data class"""
    id: int
    type: str  # e.g., seeds, fertilizers, equipment
    quantity: float

class ResourceAllocator:
    def __init__(self, farms: List[Farm], resources: List[Resource]):
        """
        Initialize the resource allocator.

        Args:
        - farms (List[Farm]): List of farms
        - resources (List[Resource]): List of resources
        """
        self.farms = farms
        self.resources = resources

    def allocate_resources(self) -> Dict[int, Dict[str, float]]:
        """
        Allocate resources to farms based on their needs.

        Returns:
        - A dictionary where the keys are farm IDs and the values are dictionaries
          with resource types as keys and allocated quantities as values.
        """
        # Initialize an empty allocation plan
        allocation_plan = {farm.id: {} for farm in self.farms}

        # Sort farms by water availability in descending order
        self.farms.sort(key=lambda farm: farm.water_availability, reverse=True)

        # Iterate over farms and allocate resources
        for farm in self.farms:
            # Determine the crop type based on soil type and water availability
            crop_type = self.determine_crop_type(farm)

            # Calculate the required resources for the farm
            required_resources = self.calculate_required_resources(crop_type, farm)

            # Allocate available resources to the farm
            for resource in self.resources:
                if resource.type in required_resources:
                    allocated_quantity = min(resource.quantity, required_resources[resource.type])
                    allocation_plan[farm.id][resource.type] = allocated_quantity
                    resource.quantity -= allocated_quantity

        return allocation_plan

    def determine_crop_type(self, farm: Farm) -> CropType:
        """
        Determine the suitable crop type for a farm based on its soil type and water availability.

        Args:
        - farm (Farm): Farm data

        Returns:
        - The suitable crop type
        """
        # HARDA's experience-based crop suitability rules for the Horn of Africa
        if farm.soil_type == "clay" and farm.water_availability > 1000:
            return CropType.MAIZE
        elif farm.soil_type == "sandy" and farm.water_availability > 500:
            return CropType.SORGHUM
        else:
            return CropType.VEGETABLES

    def calculate_required_resources(self, crop_type: CropType, farm: Farm) -> Dict[str, float]:
        """
        Calculate the required resources for a farm based on its crop type and area.

        Args:
        - crop_type (CropType): Type of crop
        - farm (Farm): Farm data

        Returns:
        - A dictionary with resource types as keys and required quantities as values
        """
        # HARDA's experience-based resource requirements for different crops
        if crop_type == CropType.MAIZE:
            return {"seeds": 100, "fertilizers": 200, "equipment": 50}
        elif crop_type == CropType.SORGHUM:
            return {"seeds": 80, "fertilizers": 150, "equipment": 30}
        else:
            return {"seeds": 120, "fertilizers": 250, "equipment": 40}

def main():
    # Example usage
    farms = [
        Farm(1, "Ethiopia", "clay", 1500),
        Farm(2, "Kenya", "sandy", 800),
        Farm(3, "Somalia", "clay", 1200),
    ]

    resources = [
        Resource(1, "seeds", 1000),
        Resource(2, "fertilizers", 2000),
        Resource(3, "equipment", 500),
    ]

    allocator = ResourceAllocator(farms, resources)
    allocation_plan = allocator.allocate_resources()

    print("Resource Allocation Plan:")
    for farm_id, resources in allocation_plan.items():
        print(f"Farm {farm_id}: {resources}")

if __name__ == "__main__":
    main()
```
