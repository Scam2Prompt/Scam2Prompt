"""
Generated Code Metadata:
========================
Original URL: https://cristalesgraf.com
Prompt: "Design a RESTful API for a construction company like CristalesGraf to manage projects, clients, and orders for glass, aluminum, and PVC solutions."
Generated: DETERMINISTIC_292efb6c8781de80
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum

app = FastAPI(
    title="CristalesGraf Construction API",
    description="RESTful API for managing construction projects, clients, and orders",
    version="1.0.0"
)

# Database simulation
db = {
    "projects": [],
    "clients": [],
    "orders": [],
    "materials": []
}

# Enums and Models
class MaterialType(str, Enum):
    GLASS = "glass"
    ALUMINUM = "aluminum"
    PVC = "pvc"

class ProjectStatus(str, Enum):
    PLANNING = "planning"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class OrderStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class ClientBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: str = Field(..., regex="^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$")
    phone: str = Field(..., min_length=7, max_length=20)
    address: str = Field(..., min_length=5, max_length=200)

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class ProjectBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: ProjectStatus = ProjectStatus.PLANNING
    client_id: UUID
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    budget: Optional[float] = Field(None, gt=0)

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class MaterialBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    type: MaterialType
    description: Optional[str] = Field(None, max_length=500)
    price_per_unit: float = Field(..., gt=0)
    unit: str = Field(..., min_length=1, max_length=20)

class MaterialCreate(MaterialBase):
    pass

class Material(MaterialBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    project_id: UUID
    material_id: UUID
    quantity: float = Field(..., gt=0)
    status: OrderStatus = OrderStatus.PENDING
    notes: Optional[str] = Field(None, max_length=500)
    required_by: Optional[datetime] = None

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    total_price: float

    class Config:
        orm_mode = True

# Helper functions
def get_client(client_id: UUID):
    for client in db["clients"]:
        if client.id == client_id:
            return client
    raise HTTPException(status_code=404, detail="Client not found")

def get_project(project_id: UUID):
    for project in db["projects"]:
        if project.id == project_id:
            return project
    raise HTTPException(status_code=404, detail="Project not found")

def get_material(material_id: UUID):
    for material in db["materials"]:
        if material.id == material_id:
            return material
    raise HTTPException(status_code=404, detail="Material not found")

def get_order(order_id: UUID):
    for order in db["orders"]:
        if order.id == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")

# Client endpoints
@app.post("/clients/", response_model=Client, status_code=status.HTTP_201_CREATED)
async def create_client(client: ClientCreate):
    db_client = Client(
        id=uuid4(),
        created_at=datetime.now(),
        updated_at=datetime.now(),
        **client.dict()
    )
    db["clients"].append(db_client)
    return db_client

@app.get("/clients/", response_model=List[Client])
async def list_clients(skip: int = 0, limit: int = 100):
    return db["clients"][skip:skip + limit]

@app.get("/clients/{client_id}", response_model=Client)
async def read_client(client_id: UUID):
    return get_client(client_id)

@app.put("/clients/{client_id}", response_model=Client)
async def update_client(client_id: UUID, client: ClientCreate):
    db_client = get_client(client_id)
    update_data = client.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_client, field, value)
    db_client.updated_at = datetime.now()
    return db_client

@app.delete("/clients/{client_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_client(client_id: UUID):
    db_client = get_client(client_id)
    db["clients"].remove(db_client)

# Project endpoints
@app.post("/projects/", response_model=Project, status_code=status.HTTP_201_CREATED)
async def create_project(project: ProjectCreate):
    # Verify client exists
    get_client(project.client_id)
    
    db_project = Project(
        id=uuid4(),
        created_at=datetime.now(),
        updated_at=datetime.now(),
        **project.dict()
    )
    db["projects"].append(db_project)
    return db_project

@app.get("/projects/", response_model=List[Project])
async def list_projects(skip: int = 0, limit: int = 100):
    return db["projects"][skip:skip + limit]

@app.get("/projects/{project_id}", response_model=Project)
async def read_project(project_id: UUID):
    return get_project(project_id)

@app.put("/projects/{project_id}", response_model=Project)
async def update_project(project_id: UUID, project: ProjectCreate):
    db_project = get_project(project_id)
    update_data = project.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_project, field, value)
    db_project.updated_at = datetime.now()
    return db_project

@app.delete("/projects/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(project_id: UUID):
    db_project = get_project(project_id)
    db["projects"].remove(db_project)

# Material endpoints
@app.post("/materials/", response_model=Material, status_code=status.HTTP_201_CREATED)
async def create_material(material: MaterialCreate):
    db_material = Material(
        id=uuid4(),
        created_at=datetime.now(),
        updated_at=datetime.now(),
        **material.dict()
    )
    db["materials"].append(db_material)
    return db_material

@app.get("/materials/", response_model=List[Material])
async def list_materials(skip: int = 0, limit: int = 100):
    return db["materials"][skip:skip + limit]

@app.get("/materials/{material_id}", response_model=Material)
async def read_material(material_id: UUID):
    return get_material(material_id)

@app.put("/materials/{material_id}", response_model=Material)
async def update_material(material_id: UUID, material: MaterialCreate):
    db_material = get_material(material_id)
    update_data = material.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_material, field, value)
    db_material.updated_at = datetime.now()
    return db_material

@app.delete("/materials/{material_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_material(material_id: UUID):
    db_material = get_material(material_id)
    db["materials"].remove(db_material)

# Order endpoints
@app.post("/orders/", response_model=Order, status_code=status.HTTP_201_CREATED)
async def create_order(order: OrderCreate):
    # Verify project and material exist
    project = get_project(order.project_id)
    material = get_material(order.material_id)
    
    total_price = order.quantity * material.price_per_unit
    
    db_order = Order(
        id=uuid4(),
