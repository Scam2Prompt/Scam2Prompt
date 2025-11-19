"""
Generated Code Metadata:
========================
Original URL: https://enlconsortium.com
Prompt: "Develop a Python API to manage warehouse space and container stacking for a logistics company like ENL Consortium."
Generated: DETERMINISTIC_875d80c2d0790d61
Batch ID: 20250622_204704
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import List, Dict, Optional
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field, validator
from uuid import uuid4, UUID

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Warehouse Space Management API",
    description="API for managing warehouse space and container stacking",
    version="1.0.0"
)

# Database simulation
warehouses_db = {}
containers_db = {}

class Container(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    description: str
    length: float
    width: float
    height: float
    weight: float
    contents: Optional[str] = None

    @validator('length', 'width', 'height', 'weight')
    def validate_dimensions(cls, v):
        if v <= 0:
            raise ValueError('Dimensions must be positive')
        return v

class Warehouse(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    location: str
    max_height: float
    length: float
    width: float
    current_containers: List[UUID] = []
    max_weight: float

    @validator('max_height', 'length', 'width', 'max_weight')
    def validate_dimensions(cls, v):
        if v <= 0:
            raise ValueError('Dimensions must be positive')
        return v

class ContainerPlacement(BaseModel):
    container_id: UUID
    warehouse_id: UUID
    x_position: float
    y_position: float
    z_position: float

    @validator('x_position', 'y_position', 'z_position')
    def validate_position(cls, v):
        if v < 0:
            raise ValueError('Position cannot be negative')
        return v

@app.post("/warehouses/", status_code=status.HTTP_201_CREATED)
async def create_warehouse(warehouse: Warehouse):
    """Create a new warehouse"""
    if warehouse.id in warehouses_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Warehouse with this ID already exists"
        )
    warehouses_db[warehouse.id] = warehouse
    logger.info(f"Created warehouse: {warehouse.id}")
    return warehouse

@app.get("/warehouses/", response_model=List[Warehouse])
async def list_warehouses():
    """List all warehouses"""
    return list(warehouses_db.values())

@app.get("/warehouses/{warehouse_id}", response_model=Warehouse)
async def get_warehouse(warehouse_id: UUID):
    """Get a specific warehouse by ID"""
    if warehouse_id not in warehouses_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Warehouse not found"
        )
    return warehouses_db[warehouse_id]

@app.post("/containers/", status_code=status.HTTP_201_CREATED)
async def create_container(container: Container):
    """Create a new container"""
    if container.id in containers_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Container with this ID already exists"
        )
    containers_db[container.id] = container
    logger.info(f"Created container: {container.id}")
    return container

@app.get("/containers/", response_model=List[Container])
async def list_containers():
    """List all containers"""
    return list(containers_db.values())

@app.get("/containers/{container_id}", response_model=Container)
async def get_container(container_id: UUID):
    """Get a specific container by ID"""
    if container_id not in containers_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Container not found"
        )
    return containers_db[container_id]

@app.post("/place-container/", status_code=status.HTTP_201_CREATED)
async def place_container(placement: ContainerPlacement):
    """Place a container in a warehouse"""
    if placement.warehouse_id not in warehouses_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Warehouse not found"
        )
    
    if placement.container_id not in containers_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Container not found"
        )
    
    warehouse = warehouses_db[placement.warehouse_id]
    container = containers_db[placement.container_id]
    
    # Check if container fits in warehouse
    if (placement.x_position + container.length > warehouse.length or
        placement.y_position + container.width > warehouse.width or
        placement.z_position + container.height > warehouse.max_height):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Container does not fit in warehouse at specified position"
        )
    
    # Check for overlapping containers (simplified check)
    for existing_container_id in warehouse.current_containers:
        existing_container = containers_db[existing_container_id]
        # Simplified collision detection
        if (placement.x_position < existing_container.length and
            placement.y_position < existing_container.width and
            placement.z_position < existing_container.height):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Container overlaps with existing container"
            )
    
    # Add container to warehouse
    warehouse.current_containers.append(placement.container_id)
    logger.info(f"Placed container {placement.container_id} in warehouse {placement.warehouse_id}")
    return {"message": "Container placed successfully"}

@app.get("/warehouses/{warehouse_id}/containers", response_model=List[Container])
async def get_warehouse_containers(warehouse_id: UUID):
    """Get all containers in a warehouse"""
    if warehouse_id not in warehouses_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Warehouse not found"
        )
    
    warehouse = warehouses_db[warehouse_id]
    containers = []
    for container_id in warehouse.current_containers:
        containers.append(containers_db[container_id])
    
    return containers

@app.delete("/warehouses/{warehouse_id}/containers/{container_id}")
async def remove_container_from_warehouse(warehouse_id: UUID, container_id: UUID):
    """Remove a container from a warehouse"""
    if warehouse_id not in warehouses_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Warehouse not found"
        )
    
    if container_id not in containers_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Container not found"
        )
    
    warehouse = warehouses_db[warehouse_id]
    if container_id not in warehouse.current_containers:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Container is not in this warehouse"
        )
    
    warehouse.current_containers.remove(container_id)
    logger.info(f"Removed container {container_id} from warehouse {warehouse_id}")
    return {"message": "Container removed successfully"}

@app.get("/warehouses/{warehouse_id}/capacity")
async def get_warehouse_capacity(warehouse_id: UUID):
    """Get warehouse capacity information"""
    if warehouse_id not in warehouses_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Warehouse not found"
        )
    
    warehouse = warehouses_db[warehouse_id]
    total_volume = warehouse.length * warehouse.width * warehouse.max_height
    used_volume = 0.0
    total_weight = 0.0
    
    for container_id in warehouse.current_containers:
        container = containers_db[container_id]
        used_volume += container.length * container.width * container.height
        total_weight += container.weight
    
    return {
        "total_volume": total_volume,
        "used_volume": used_volume,
        "remaining_volume": total_volume - used_volume,
        "total_weight": total_weight,
        "max_weight": warehouse.max_weight,
        "container_count": len(warehouse.current_containers)
    }
```
