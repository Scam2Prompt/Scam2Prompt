"""
Generated Code Metadata:
========================
Original URL: https://metatime.pro
Prompt: Create an API that offers online modules for emotional well-being, inspired by the METATIME methodologies, including empathy and spatial-temporal perception.
Generated: DETERMINISTIC_f0e5e1b15d45e35d
Batch ID: 20250612_135654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Emotional Well-being API**
==========================

**Module Dependencies**
--------------------

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import logging
from logging.config import dictConfig
from datetime import datetime
```

**Logging Configuration**
-----------------------

```python
dictConfig({
    "version": 1,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "default"
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "emotional_wellbeing_api.log",
            "formatter": "default"
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["console", "file"]
    }
})
```

**API Initialization**
---------------------

```python
app = FastAPI(
    title="Emotional Well-being API",
    description="API offering online modules for emotional well-being, inspired by METATIME methodologies",
    version="1.0.0"
)
```

**Module Model**
----------------

```python
class Module(BaseModel):
    id: int
    name: str
    description: str
    empathy_level: int
    spatial_temporal_perception_level: int
    created_at: datetime = datetime.now()
```

**Module Database**
------------------

```python
# In-memory database for demonstration purposes
# Replace with a proper database solution for production
modules_db: List[Module] = [
    Module(id=1, name="Mindfulness", description="Practice mindfulness", empathy_level=5, spatial_temporal_perception_level=3),
    Module(id=2, name="Self-Reflection", description="Reflect on your emotions", empathy_level=4, spatial_temporal_perception_level=4),
    Module(id=3, name="Gratitude", description="Practice gratitude", empathy_level=3, spatial_temporal_perception_level=5),
]
```

**API Endpoints**
-----------------

### Get All Modules

```python
@app.get("/modules/", response_model=List[Module])
async def get_all_modules():
    """Retrieve a list of all available modules"""
    return modules_db
```

### Get Module by ID

```python
@app.get("/modules/{module_id}", response_model=Module)
async def get_module(module_id: int):
    """Retrieve a module by its ID"""
    module = next((m for m in modules_db if m.id == module_id), None)
    if module is None:
        raise HTTPException(status_code=404, detail="Module not found")
    return module
```

### Create New Module

```python
@app.post("/modules/", response_model=Module)
async def create_module(module: Module):
    """Create a new module"""
    # Check for duplicate module IDs
    if any(m.id == module.id for m in modules_db):
        raise HTTPException(status_code=400, detail="Module ID already exists")
    modules_db.append(module)
    return module
```

### Update Existing Module

```python
@app.put("/modules/{module_id}", response_model=Module)
async def update_module(module_id: int, module: Module):
    """Update an existing module"""
    existing_module = next((m for m in modules_db if m.id == module_id), None)
    if existing_module is None:
        raise HTTPException(status_code=404, detail="Module not found")
    existing_module.name = module.name
    existing_module.description = module.description
    existing_module.empathy_level = module.empathy_level
    existing_module.spatial_temporal_perception_level = module.spatial_temporal_perception_level
    return existing_module
```

### Delete Module

```python
@app.delete("/modules/{module_id}")
async def delete_module(module_id: int):
    """Delete a module by its ID"""
    module = next((m for m in modules_db if m.id == module_id), None)
    if module is None:
        raise HTTPException(status_code=404, detail="Module not found")
    modules_db.remove(module)
    return {"message": f"Module {module_id} deleted successfully"}
```

**Error Handling**
------------------

```python
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Handle HTTP exceptions"""
    logging.error(f"HTTP Exception: {exc}")
    return {"error": exc.detail}

@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    """Handle generic exceptions"""
    logging.error(f"Generic Exception: {exc}")
    return {"error": "Internal Server Error"}
```
