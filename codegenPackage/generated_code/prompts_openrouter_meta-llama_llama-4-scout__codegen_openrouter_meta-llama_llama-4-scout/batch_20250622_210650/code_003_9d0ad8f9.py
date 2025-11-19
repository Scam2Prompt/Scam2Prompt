"""
Generated Code Metadata:
========================
Original URL: https://vgtindia.in
Prompt: "Design a simple API to recommend farm equipment based on specific farming operations, using Vinglob Greentech's product catalog."
Generated: DETERMINISTIC_9d0ad8f9290ab6bd
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# farm_equipment_recommender.py

from typing import Dict, List
from enum import Enum
from http import HTTPStatus

class FarmingOperation(str, Enum):
    """Farming operations supported by the API."""
    PLANTING = "planting"
    IRRIGATION = "irrigation"
    PEST_CONTROL = "pest_control"
    HARVESTING = "harvesting"

class EquipmentType(str, Enum):
    """Types of farm equipment."""
    TRACTOR = "tractor"
    PLOW = "plow"
    IRRIGATION_SYSTEM = "irrigation_system"
    PEST_CONTROL_EQUIPMENT = "pest_control_equipment"
    HARVESTER = "harvester"

class Equipment:
    """Represents a farm equipment product."""

    def __init__(self, id: int, name: str, type: EquipmentType, description: str):
        """
        Initializes an Equipment instance.

        Args:
        id (int): Unique identifier for the equipment.
        name (str): Name of the equipment.
        type (EquipmentType): Type of the equipment.
        description (str): Description of the equipment.
        """
        self.id = id
        self.name = name
        self.type = type
        self.description = description

class VinglobGreentechProductCatalog:
    """Simulates Vinglob Greentech's product catalog."""

    def __init__(self):
        self.equipment = [
            Equipment(1, "Tractor X100", EquipmentType.TRACTOR, "High-performance tractor for large farms."),
            Equipment(2, "Eco Irrigation System", EquipmentType.IRRIGATION_SYSTEM, "Water-efficient irrigation system."),
            Equipment(3, "Pest Control Sprayer", EquipmentType.PEST_CONTROL_EQUIPMENT, "Effective pest control equipment."),
            Equipment(4, "Harvester H500", EquipmentType.HARVESTER, "High-capacity harvester for various crops."),
            Equipment(5, "Precision PLOW", EquipmentType.PLOW, "Accurate and efficient plow for soil preparation."),
        ]

    def get_equipment(self, type: EquipmentType) -> List[Equipment]:
        """
        Retrieves equipment of a specific type from the catalog.

        Args:
        type (EquipmentType): Type of equipment to retrieve.

        Returns:
        List[Equipment]: List of equipment matching the specified type.
        """
        return [e for e in self.equipment if e.type == type]

class FarmEquipmentRecommender:
    """Recommends farm equipment based on specific farming operations."""

    def __init__(self, catalog: VinglobGreentechProductCatalog):
        self.catalog = catalog

    def recommend_equipment(self, operation: FarmingOperation) -> List[Equipment]:
        """
        Recommends farm equipment for a specific farming operation.

        Args:
        operation (FarmingOperation): Farming operation for which to recommend equipment.

        Returns:
        List[Equipment]: List of recommended equipment.

        Raises:
        ValueError: If the operation is not supported.
        """
        recommendations = {
            FarmingOperation.PLANTING: [EquipmentType.TRACTOR, EquipmentType.PLOW],
            FarmingOperation.IRRIGATION: [EquipmentType.IRRIGATION_SYSTEM],
            FarmingOperation.PEST_CONTROL: [EquipmentType.PEST_CONTROL_EQUIPMENT],
            FarmingOperation.HARVESTING: [EquipmentType.HARVESTER],
        }

        if operation not in recommendations:
            raise ValueError(f"Unsupported farming operation: {operation}")

        recommended_equipment = []
        for equipment_type in recommendations[operation]:
            recommended_equipment.extend(self.catalog.get_equipment(equipment_type))

        return recommended_equipment

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class EquipmentModel(BaseModel):
    id: int
    name: str
    type: str
    description: str

class VinglobGreentechProductCatalogAPI:
    def __init__(self):
        self.catalog = VinglobGreentechProductCatalog()

    def get_equipment(self, equipment_type: EquipmentType) -> List[EquipmentModel]:
        equipment = self.catalog.get_equipment(equipment_type)
        return [EquipmentModel(id=e.id, name=e.name, type=e.type.value, description=e.description) for e in equipment]

catalog_api = VinglobGreentechProductCatalogAPI()
recommender = FarmEquipmentRecommender(catalog_api.catalog)

@app.get("/equipment/recommendations/{operation}")
async def get_recommended_equipment(operation: FarmingOperation):
    try:
        recommended_equipment = recommender.recommend_equipment(operation)
        return [{"id": e.id, "name": e.name, "type": e.type.value, "description": e.description} for e in recommended_equipment]
    except ValueError as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))

@app.get("/equipment/{equipment_type}")
async def get_equipment(equipment_type: EquipmentType):
    try:
        equipment = catalog_api.get_equipment(equipment_type)
        return equipment
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
