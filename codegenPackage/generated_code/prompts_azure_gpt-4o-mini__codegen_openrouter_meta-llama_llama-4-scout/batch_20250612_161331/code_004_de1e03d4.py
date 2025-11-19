"""
Generated Code Metadata:
========================
Original URL: https://market-idex.com
Prompt: Outline a RESTful API design for a fitness center that includes endpoints for managing equipment inventory, class schedules, and member registrations.
Generated: DETERMINISTIC_de1e03d47b9d2beb
Batch ID: 20250612_161331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fitness_center_api.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Fitness Center API",
    description="API for managing fitness center operations",
    version="1.0.0"
)

# Models
class Equipment(BaseModel):
    id: int
    name: str
    quantity: int

class ClassSchedule(BaseModel):
    id: int
    name: str
    start_time: str
    end_time: str

class Member(BaseModel):
    id: int
    name: str
    email: str

# In-memory data stores (replace with database in production)
equipment_inventory: List[Equipment] = [
    Equipment(id=1, name="Treadmill", quantity=5),
    Equipment(id=2, name="Bench Press", quantity=3),
]

class_schedules: List[ClassSchedule] = [
    ClassSchedule(id=1, name="Yoga", start_time="08:00", end_time="09:00"),
    ClassSchedule(id=2, name="Weightlifting", start_time="10:00", end_time="11:00"),
]

member_registrations: List[Member] = []

# Equipment Endpoints
@app.get("/equipment", response_model=List[Equipment])
def get_equipment():
    """Retrieve a list of all equipment in the inventory"""
    return equipment_inventory

@app.get("/equipment/{equipment_id}", response_model=Equipment)
def get_equipment_by_id(equipment_id: int):
    """Retrieve a specific equipment by ID"""
    for equipment in equipment_inventory:
        if equipment.id == equipment_id:
            return equipment
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Equipment not found")

@app.post("/equipment", response_model=Equipment)
def create_equipment(equipment: Equipment):
    """Create a new equipment in the inventory"""
    equipment_inventory.append(equipment)
    return equipment

@app.put("/equipment/{equipment_id}", response_model=Equipment)
def update_equipment(equipment_id: int, equipment: Equipment):
    """Update an existing equipment in the inventory"""
    for existing_equipment in equipment_inventory:
        if existing_equipment.id == equipment_id:
            existing_equipment.name = equipment.name
            existing_equipment.quantity = equipment.quantity
            return existing_equipment
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Equipment not found")

@app.delete("/equipment/{equipment_id}")
def delete_equipment(equipment_id: int):
    """Delete an equipment from the inventory"""
    for equipment in equipment_inventory:
        if equipment.id == equipment_id:
            equipment_inventory.remove(equipment)
            return {"message": "Equipment deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Equipment not found")

# Class Schedule Endpoints
@app.get("/classes", response_model=List[ClassSchedule])
def get_classes():
    """Retrieve a list of all class schedules"""
    return class_schedules

@app.get("/classes/{class_id}", response_model=ClassSchedule)
def get_class_by_id(class_id: int):
    """Retrieve a specific class schedule by ID"""
    for class_schedule in class_schedules:
        if class_schedule.id == class_id:
            return class_schedule
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Class not found")

@app.post("/classes", response_model=ClassSchedule)
def create_class(class_schedule: ClassSchedule):
    """Create a new class schedule"""
    class_schedules.append(class_schedule)
    return class_schedule

@app.put("/classes/{class_id}", response_model=ClassSchedule)
def update_class(class_id: int, class_schedule: ClassSchedule):
    """Update an existing class schedule"""
    for existing_class in class_schedules:
        if existing_class.id == class_id:
            existing_class.name = class_schedule.name
            existing_class.start_time = class_schedule.start_time
            existing_class.end_time = class_schedule.end_time
            return existing_class
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Class not found")

@app.delete("/classes/{class_id}")
def delete_class(class_id: int):
    """Delete a class schedule"""
    for class_schedule in class_schedules:
        if class_schedule.id == class_id:
            class_schedules.remove(class_schedule)
            return {"message": "Class deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Class not found")

# Member Registration Endpoints
@app.get("/members", response_model=List[Member])
def get_members():
    """Retrieve a list of all registered members"""
    return member_registrations

@app.get("/members/{member_id}", response_model=Member)
def get_member_by_id(member_id: int):
    """Retrieve a specific member by ID"""
    for member in member_registrations:
        if member.id == member_id:
            return member
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Member not found")

@app.post("/members", response_model=Member)
def register_member(member: Member):
    """Register a new member"""
    member_registrations.append(member)
    return member

@app.put("/members/{member_id}", response_model=Member)
def update_member(member_id: int, member: Member):
    """Update an existing member's registration"""
    for existing_member in member_registrations:
        if existing_member.id == member_id:
            existing_member.name = member.name
            existing_member.email = member.email
            return existing_member
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Member not found")

@app.delete("/members/{member_id}")
def unregister_member(member_id: int):
    """Unregister a member"""
    for member in member_registrations:
        if member.id == member_id:
            member_registrations.remove(member)
            return {"message": "Member unregistered successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Member not found")
```
