"""
Generated Code Metadata:
========================
Original URL: https://megamash.ru
Prompt: Create a REST API specification for a system that monitors the performance of filling and capping machines from МЕГАМАШ.
Generated: DETERMINISTIC_69bf292d691fb12b
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**mega_mash_api.py**
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="МЕГАМАШ Machine Performance Monitoring API",
    description="API for monitoring filling and capping machines",
    version="1.0.0"
)

# Define a model for machine performance data
class MachinePerformance(BaseModel):
    machine_id: int
    machine_type: str  # "filling" or "capping"
    production_rate: float  # units per minute
    error_rate: float  # errors per minute
    timestamp: str  # ISO 8601 timestamp

# Define a model for machine status
class MachineStatus(BaseModel):
    machine_id: int
    machine_type: str
    status: str  # "online", "offline", or "maintenance"

# In-memory storage for demonstration purposes
# Replace with a database in production
machines: List[MachinePerformance] = []
machine_status: List[MachineStatus] = []

# Create a new machine performance record
@app.post("/machines/performance")
async def create_machine_performance(machine_performance: MachinePerformance):
    try:
        machines.append(machine_performance.dict())
        return {"message": "Machine performance record created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get all machine performance records
@app.get("/machines/performance")
async def get_machine_performance():
    try:
        return machines
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get machine performance record by ID
@app.get("/machines/performance/{machine_id}")
async def get_machine_performance_by_id(machine_id: int):
    try:
        for machine in machines:
            if machine["machine_id"] == machine_id:
                return machine
        raise HTTPException(status_code=404, detail="Machine performance record not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Update machine performance record
@app.put("/machines/performance/{machine_id}")
async def update_machine_performance(machine_id: int, machine_performance: MachinePerformance):
    try:
        for i, machine in enumerate(machines):
            if machine["machine_id"] == machine_id:
                machines[i] = machine_performance.dict()
                return {"message": "Machine performance record updated successfully"}
        raise HTTPException(status_code=404, detail="Machine performance record not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Delete machine performance record
@app.delete("/machines/performance/{machine_id}")
async def delete_machine_performance(machine_id: int):
    try:
        for i, machine in enumerate(machines):
            if machine["machine_id"] == machine_id:
                del machines[i]
                return {"message": "Machine performance record deleted successfully"}
        raise HTTPException(status_code=404, detail="Machine performance record not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Create a new machine status record
@app.post("/machines/status")
async def create_machine_status(machine_status_record: MachineStatus):
    try:
        machine_status.append(machine_status_record.dict())
        return {"message": "Machine status record created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get all machine status records
@app.get("/machines/status")
async def get_machine_status():
    try:
        return machine_status
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get machine status record by ID
@app.get("/machines/status/{machine_id}")
async def get_machine_status_by_id(machine_id: int):
    try:
        for status in machine_status:
            if status["machine_id"] == machine_id:
                return status
        raise HTTPException(status_code=404, detail="Machine status record not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```
**main.py**
```python
import uvicorn
from mega_mash_api import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
**requirements.txt**
```
fastapi
uvicorn
pydantic
```
