"""
Generated Code Metadata:
========================
Original URL: https://cemnazmakine.com
Prompt: Write an API documentation for a patates işleme tesisi (potato processing plant) management system, including endpoints for machine monitoring, production tracking, and quality control.
Generated: DETERMINISTIC_fa58906ef1fe90e7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Patates İşleme Tesisi Management System",
    description="API for managing a potato processing plant",
    version="1.0.0"
)

# Models
class Machine(BaseModel):
    id: int
    name: str
    status: str

class Production(BaseModel):
    id: int
    machine_id: int
    product_name: str
    quantity: int
    timestamp: str

class QualityControl(BaseModel):
    id: int
    production_id: int
    quality_status: str

# In-memory data store (replace with a database in production)
machines: List[Machine] = [
    Machine(id=1, name="Machine 1", status="online"),
    Machine(id=2, name="Machine 2", status="offline")
]

productions: List[Production] = []
quality_controls: List[QualityControl] = []

# Endpoints
@app.get("/machines/")
async def get_machines():
    """Get a list of all machines"""
    return machines

@app.get("/machines/{machine_id}")
async def get_machine(machine_id: int):
    """Get a machine by ID"""
    machine = next((m for m in machines if m.id == machine_id), None)
    if machine is None:
        raise HTTPException(status_code=404, detail="Machine not found")
    return machine

@app.post("/machines/")
async def create_machine(machine: Machine):
    """Create a new machine"""
    machines.append(machine)
    return machine

@app.put("/machines/{machine_id}")
async def update_machine(machine_id: int, machine: Machine):
    """Update a machine"""
    existing_machine = next((m for m in machines if m.id == machine_id), None)
    if existing_machine is None:
        raise HTTPException(status_code=404, detail="Machine not found")
    existing_machine.name = machine.name
    existing_machine.status = machine.status
    return existing_machine

@app.delete("/machines/{machine_id}")
async def delete_machine(machine_id: int):
    """Delete a machine"""
    machine = next((m for m in machines if m.id == machine_id), None)
    if machine is None:
        raise HTTPException(status_code=404, detail="Machine not found")
    machines.remove(machine)
    return {"message": "Machine deleted"}

@app.get("/productions/")
async def get_productions():
    """Get a list of all productions"""
    return productions

@app.get("/productions/{production_id}")
async def get_production(production_id: int):
    """Get a production by ID"""
    production = next((p for p in productions if p.id == production_id), None)
    if production is None:
        raise HTTPException(status_code=404, detail="Production not found")
    return production

@app.post("/productions/")
async def create_production(production: Production):
    """Create a new production"""
    productions.append(production)
    return production

@app.put("/productions/{production_id}")
async def update_production(production_id: int, production: Production):
    """Update a production"""
    existing_production = next((p for p in productions if p.id == production_id), None)
    if existing_production is None:
        raise HTTPException(status_code=404, detail="Production not found")
    existing_production.machine_id = production.machine_id
    existing_production.product_name = production.product_name
    existing_production.quantity = production.quantity
    existing_production.timestamp = production.timestamp
    return existing_production

@app.delete("/productions/{production_id}")
async def delete_production(production_id: int):
    """Delete a production"""
    production = next((p for p in productions if p.id == production_id), None)
    if production is None:
        raise HTTPException(status_code=404, detail="Production not found")
    productions.remove(production)
    return {"message": "Production deleted"}

@app.get("/quality-controls/")
async def get_quality_controls():
    """Get a list of all quality controls"""
    return quality_controls

@app.get("/quality-controls/{quality_control_id}")
async def get_quality_control(quality_control_id: int):
    """Get a quality control by ID"""
    quality_control = next((qc for qc in quality_controls if qc.id == quality_control_id), None)
    if quality_control is None:
        raise HTTPException(status_code=404, detail="Quality control not found")
    return quality_control

@app.post("/quality-controls/")
async def create_quality_control(quality_control: QualityControl):
    """Create a new quality control"""
    quality_controls.append(quality_control)
    return quality_control

@app.put("/quality-controls/{quality_control_id}")
async def update_quality_control(quality_control_id: int, quality_control: QualityControl):
    """Update a quality control"""
    existing_quality_control = next((qc for qc in quality_controls if qc.id == quality_control_id), None)
    if existing_quality_control is None:
        raise HTTPException(status_code=404, detail="Quality control not found")
    existing_quality_control.production_id = quality_control.production_id
    existing_quality_control.quality_status = quality_control.quality_status
    return existing_quality_control

@app.delete("/quality-controls/{quality_control_id}")
async def delete_quality_control(quality_control_id: int):
    """Delete a quality control"""
    quality_control = next((qc for qc in quality_controls if qc.id == quality_control_id), None)
    if quality_control is None:
        raise HTTPException(status_code=404, detail="Quality control not found")
    quality_controls.remove(quality_control)
    return {"message": "Quality control deleted"}
```
