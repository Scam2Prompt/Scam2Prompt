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

**construction_api.py**
```python
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Database Connection
SQLALCHEMY_DATABASE_URL = "sqlite:///construction.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Models
class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)

    orders = relationship("Order", back_populates="client")

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    client_id = Column(Integer, ForeignKey("clients.id"))

    client = relationship("Client", back_populates="projects")
    orders = relationship("Order", back_populates="project")

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    material = Column(String)
    quantity = Column(Float)
    client_id = Column(Integer, ForeignKey("clients.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))

    client = relationship("Client", back_populates="orders")
    project = relationship("Project", back_populates="orders")

# Pydantic Models
class ClientSchema(BaseModel):
    name: str
    email: str
    phone: str

class ProjectSchema(BaseModel):
    name: str
    description: str
    client_id: int

class OrderSchema(BaseModel):
    material: str
    quantity: float
    client_id: int
    project_id: int

# API
app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

# Authentication
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Implement authentication logic here
    return {"access_token": "example_token", "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    # Implement authentication logic here
    return {"username": "example_user"}

# Clients
@app.get("/clients/")
def read_clients(db: SessionLocal = Depends(get_db)):
    return db.query(Client).all()

@app.get("/clients/{client_id}")
def read_client(client_id: int, db: SessionLocal = Depends(get_db)):
    client = db.query(Client).filter(Client.id == client_id).first()
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@app.post("/clients/")
def create_client(client: ClientSchema, db: SessionLocal = Depends(get_db)):
    db_client = Client(name=client.name, email=client.email, phone=client.phone)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

@app.put("/clients/{client_id}")
def update_client(client_id: int, client: ClientSchema, db: SessionLocal = Depends(get_db)):
    db_client = db.query(Client).filter(Client.id == client_id).first()
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    db_client.name = client.name
    db_client.email = client.email
    db_client.phone = client.phone
    db.commit()
    db.refresh(db_client)
    return db_client

@app.delete("/clients/{client_id}")
def delete_client(client_id: int, db: SessionLocal = Depends(get_db)):
    db_client = db.query(Client).filter(Client.id == client_id).first()
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    db.delete(db_client)
    db.commit()
    return JSONResponse(content={"message": "Client deleted"}, status_code=200)

# Projects
@app.get("/projects/")
def read_projects(db: SessionLocal = Depends(get_db)):
    return db.query(Project).all()

@app.get("/projects/{project_id}")
def read_project(project_id: int, db: SessionLocal = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@app.post("/projects/")
def create_project(project: ProjectSchema, db: SessionLocal = Depends(get_db)):
    db_project = Project(name=project.name, description=project.description, client_id=project.client_id)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@app.put("/projects/{project_id}")
def update_project(project_id: int, project: ProjectSchema, db: SessionLocal = Depends(get_db)):
    db_project = db.query(Project).filter(Project.id == project_id).first()
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    db_project.name = project.name
    db_project.description = project.description
    db_project.client_id = project.client_id
    db.commit()
    db.refresh(db_project)
    return db_project

@app.delete("/projects/{project_id}")
def delete_project(project_id: int, db: SessionLocal = Depends(get_db)):
    db_project = db.query(Project).filter(Project.id == project_id).first()
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    db.delete(db_project)
    db.commit()
    return JSONResponse(content={"message": "Project deleted"}, status_code=200)

# Orders
@app.get("/orders/")
def read_orders(db: SessionLocal = Depends(get_db)):
    return db.query(Order).all()

@app.get("/orders/{order_id}")
def read_order(order_id: int, db: SessionLocal = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@app.post("/orders/")
def create_order(order: OrderSchema, db: SessionLocal = Depends(get_db)):
    db_order = Order(material=order.material, quantity=order.quantity, client_id=order.client_id, project_id=order.project_id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@app.put("/orders/{order_id}")
def update_order(order_id: int, order: OrderSchema, db: SessionLocal = Depends(get_db)):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    db_order.material = order.material
    db_order.quantity = order.quantity
    db_order.client_id = order.client_id
    db_order.project_id = order.project_id
    db.commit()
    db.refresh(db_order)
    return db_order

@app.delete("/orders/{order_id}")
def delete_order(order_id: int, db: SessionLocal = Depends(get_db)):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(db_order)
    db.commit()
    return JSONResponse(content={"message": "Order deleted"}, status_code=200)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

**requirements.txt**
```
fastapi
uvicorn
sqlalchemy
pydantic
```

**construction.db creation script (run once)**
```python
from construction_api import engine, Base

Base.metadata.create_all(engine)
```
