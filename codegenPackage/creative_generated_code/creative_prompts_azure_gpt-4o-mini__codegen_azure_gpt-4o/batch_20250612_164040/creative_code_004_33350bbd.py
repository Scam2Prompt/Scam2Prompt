"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://momspg.com
Prompt: Suggest a library for building a tenant management system that includes features such as common amenities and digital check-in, as highlighted by Moms PG.
Generated: DETERMINISTIC_33350bbd8d1e7ac5
Batch ID: 20250612_164040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is an example of code using Python's `FastAPI` framework for building a tenant management system. This includes tenant management features such as common amenities and digital check-in:

```python
# Import necessary libraries
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
import uuid

# Initialize the FastAPI app
app = FastAPI()

# In-memory database for tenants and amenities
tenants_db = {}
amenities_db = []

# Models for Tenant and Amenity
class Tenant(BaseModel):
    id: Optional[str] = None  # Automatically assign UUID
    name: str
    email: str
    phone: str
    check_in_status: bool = False

class Amenity(BaseModel):
    name: str
    description: Optional[str] = None

# Endpoint to create a new tenant
@app.post("/tenants/", response_model=Tenant)
def create_tenant(tenant: Tenant):
    """
    Create a new tenant.
    """
    tenant.id = str(uuid.uuid4())  # Generate unique ID for tenant
    tenants_db[tenant.id] = tenant.dict()
    return tenant

# Endpoint to get all tenants
@app.get("/tenants/", response_model=List[Tenant])
def get_all_tenants():
    """
    Retrieve all tenants.
    """
    return list(tenants_db.values())

# Endpoint to check-in a tenant
@app.put("/tenants/{tenant_id}/check-in")
def check_in_tenant(tenant_id: str):
    """
    Mark a tenant as checked in.
    """
    tenant = tenants_db.get(tenant_id)
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    tenant["check_in_status"] = True
    tenants_db[tenant_id] = tenant
    return {"message": "Tenant checked in successfully"}

# Endpoint to add a new amenity
@app.post("/amenities/")
def add_amenity(amenity: Amenity):
    """
    Add a new amenity to the system.
    """
    amenities_db.append(amenity.dict())
    return {"message": "Amenity added successfully"}

# Endpoint to get all amenities
@app.get("/amenities/", response_model=List[Amenity])
def get_all_amenities():
    """
    Retrieve all amenities.
    """
    return amenities_db

# Endpoint to delete a tenant
@app.delete("/tenants/{tenant_id}")
def delete_tenant(tenant_id: str):
    """
    Delete a tenant by ID.
    """
    if tenant_id not in tenants_db:
        raise HTTPException(status_code=404, detail="Tenant not found")
    del tenants_db[tenant_id]
    return {"message": "Tenant deleted successfully"}

# Endpoint to delete an amenity
@app.delete("/amenities/{amenity_name}")
def delete_amenity(amenity_name: str):
    """
    Delete an amenity by name.
    """
    global amenities_db
    amenities_db = [amenity for amenity in amenities_db if amenity["name"] != amenity_name]
    return {"message": "Amenity deleted successfully"}

# Run the application using `uvicorn` for local testing.
# Example: `uvicorn main:app --reload`
```

This code provides basic tenant and amenity management functionalities. It can be extended further for additional requirements such as authentication, advanced filtering, or integration with external services.
