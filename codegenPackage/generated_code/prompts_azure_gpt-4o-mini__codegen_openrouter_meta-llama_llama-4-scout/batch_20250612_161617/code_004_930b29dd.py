"""
Generated Code Metadata:
========================
Original URL: https://atakoynakliyat.gen.tr
Prompt: Design a RESTful API that provides information about the various services offered by Ataköy Nakliyat, including office relocation and storage options.
Generated: DETERMINISTIC_930b29ddf63f79dd
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**atakoy_nakliyat_api.py**
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Ataköy Nakliyat API",
    description="Provides information about services offered by Ataköy Nakliyat",
    version="1.0.0"
)

# Define a model for services
class Service(BaseModel):
    id: int
    name: str
    description: str

# Define a model for office relocation services
class OfficeRelocationService(Service):
    services_offered: List[str]

# Define a model for storage options
class StorageOption(Service):
    capacity: str
    duration: str

# In-memory data store for demonstration purposes
services: List[Service] = [
    OfficeRelocationService(
        id=1,
        name="Office Relocation",
        description="Professional office relocation services",
        services_offered=["Packing", "Loading", "Transportation", "Unloading"]
    ),
    StorageOption(
        id=2,
        name="Short-term Storage",
        description="Secure storage options for short-term needs",
        capacity="10 sqm",
        duration="1-30 days"
    ),
    StorageOption(
        id=3,
        name="Long-term Storage",
        description="Secure storage options for long-term needs",
        capacity="50 sqm",
        duration="30+ days"
    )
]

# GET /
@app.get("/")
def read_root():
    return {"message": "Ataköy Nakliyat API"}

# GET /services
@app.get("/services/", response_model=List[Service])
def read_services():
    return services

# GET /services/{service_id}
@app.get("/services/{service_id}", response_model=Service)
def read_service(service_id: int):
    service = next((s for s in services if s.id == service_id), None)
    if service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return service

# GET /office-relocation
@app.get("/office-relocation/", response_model=List[OfficeRelocationService])
def read_office_relocation_services():
    return [s for s in services if isinstance(s, OfficeRelocationService)]

# GET /storage-options
@app.get("/storage-options/", response_model=List[StorageOption])
def read_storage_options():
    return [s for s in services if isinstance(s, StorageOption)]

# Error handler for 404
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"error": exc.detail}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

**requirements.txt**
```
fastapi
pydantic
uvicorn
```

**Dockerfile**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "atakoy_nakliyat_api:app", "--host", "0.0.0.0", "--port", "8000"]
```

**docker-compose.yml**
```yml
version: "3"

services:
  api:
    build: .
    ports:
      - "8000:8000"
    restart: always
```
