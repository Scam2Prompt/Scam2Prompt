"""
Generated Code Metadata:
========================
Original URL: https://beboldproperties.com
Prompt: Design an API for a property management system that integrates with financial planners, mortgage brokers, accountants, and solicitors, similar to Bebold Properties' network of trusted experts.
Generated: DETERMINISTIC_c10b66eb564f7240
Batch ID: 20250622_211816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# property_management_system.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Property Management System API",
    description="API for integrating with financial planners, mortgage brokers, accountants, and solicitors",
    version="1.0.0"
)

# Define a base model for professionals
class Professional(BaseModel):
    id: int
    name: str
    profession: str
    contact_info: str

# Define a base model for properties
class Property(BaseModel):
    id: int
    address: str
    type: str
    price: float

# Define a model for client requests
class ClientRequest(BaseModel):
    client_name: str
    property_id: int
    professional_type: str

# In-memory storage for demonstration purposes
professionals: List[Professional] = [
    Professional(id=1, name="John Doe", profession="Financial Planner", contact_info="john.doe@example.com"),
    Professional(id=2, name="Jane Smith", profession="Mortgage Broker", contact_info="jane.smith@example.com"),
    Professional(id=3, name="Bob Johnson", profession="Accountant", contact_info="bob.johnson@example.com"),
    Professional(id=4, name="Alice Williams", profession="Solicitor", contact_info="alice.williams@example.com")
]

properties: List[Property] = [
    Property(id=1, address="123 Main St", type="Residential", price=500000.0),
    Property(id=2, address="456 Elm St", type="Commercial", price=1000000.0)
]

# API Endpoints
@app.get("/professionals/")
async def get_professionals():
    """Retrieve a list of all professionals in the network"""
    return professionals

@app.get("/professionals/{professional_id}")
async def get_professional(professional_id: int):
    """Retrieve a professional by ID"""
    professional = next((p for p in professionals if p.id == professional_id), None)
    if professional is None:
        raise HTTPException(status_code=404, detail="Professional not found")
    return professional

@app.get("/properties/")
async def get_properties():
    """Retrieve a list of all properties"""
    return properties

@app.get("/properties/{property_id}")
async def get_property(property_id: int):
    """Retrieve a property by ID"""
    property = next((p for p in properties if p.id == property_id), None)
    if property is None:
        raise HTTPException(status_code=404, detail="Property not found")
    return property

@app.post("/requests/")
async def create_request(client_request: ClientRequest):
    """Create a new client request"""
    property = next((p for p in properties if p.id == client_request.property_id), None)
    if property is None:
        raise HTTPException(status_code=404, detail="Property not found")
    
    professional = next((p for p in professionals if p.profession.lower() == client_request.professional_type.lower()), None)
    if professional is None:
        raise HTTPException(status_code=404, detail="Professional not found")
    
    # Simulate sending a request to the professional
    print(f"Sending request to {professional.name} for {client_request.client_name} and property {property.address}")
    return {"message": "Request sent successfully"}

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"error": exc.detail}, exc.status_code

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
uvicorn
pydantic
```

```bash
# Run with: uvicorn property_management_system:app --host 0.0.0.0 --port 8000
```
