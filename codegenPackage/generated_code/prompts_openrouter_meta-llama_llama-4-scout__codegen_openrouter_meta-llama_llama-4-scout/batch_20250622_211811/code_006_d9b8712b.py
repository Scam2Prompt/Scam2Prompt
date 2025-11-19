"""
Generated Code Metadata:
========================
Original URL: https://daplatform.one
Prompt: "Create a RESTful API endpoint to retrieve specific data sets from a data platform."
Generated: DETERMINISTIC_d9b8712bd6a570e1
Batch ID: 20250622_211811
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
import uvicorn
from datetime import datetime

# Initialize FastAPI application
app = FastAPI(
    title="Data Platform API",
    description="API to retrieve specific data sets from a data platform",
    version="1.0.0"
)

# Define data model for data set
class DataSet(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime

# Mock data store (replace with actual database connection)
data_sets = [
    DataSet(id=1, name="Data Set 1", description="This is data set 1", created_at=datetime(2022, 1, 1)),
    DataSet(id=2, name="Data Set 2", description="This is data set 2", created_at=datetime(2022, 1, 15)),
    DataSet(id=3, name="Data Set 3", description="This is data set 3", created_at=datetime(2022, 2, 1)),
]

# Define API endpoint to retrieve all data sets
@app.get("/data-sets/", response_model=List[DataSet])
async def get_data_sets():
    """Retrieve all data sets"""
    return data_sets

# Define API endpoint to retrieve specific data set by ID
@app.get("/data-sets/{data_set_id}", response_model=DataSet)
async def get_data_set(data_set_id: int):
    """Retrieve data set by ID"""
    data_set = next((ds for ds in data_sets if ds.id == data_set_id), None)
    if data_set is None:
        raise HTTPException(status_code=404, detail="Data set not found")
    return data_set

# Define API endpoint to create new data set
@app.post("/data-sets/", response_model=DataSet)
async def create_data_set(data_set: DataSet):
    """Create new data set"""
    data_sets.append(data_set)
    return data_set

# Define API endpoint to update existing data set
@app.put("/data-sets/{data_set_id}", response_model=DataSet)
async def update_data_set(data_set_id: int, data_set: DataSet):
    """Update existing data set"""
    existing_data_set = next((ds for ds in data_sets if ds.id == data_set_id), None)
    if existing_data_set is None:
        raise HTTPException(status_code=404, detail="Data set not found")
    existing_data_set.name = data_set.name
    existing_data_set.description = data_set.description
    return existing_data_set

# Define API endpoint to delete data set
@app.delete("/data-sets/{data_set_id}")
async def delete_data_set(data_set_id: int):
    """Delete data set"""
    global data_sets
    data_sets = [ds for ds in data_sets if ds.id != data_set_id]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run with: uvicorn app:app --host 0.0.0.0 --port 8000
```
