"""
Generated Code Metadata:
========================
Original URL: https://setingenieria.cl
Prompt: Provide a step-by-step guide to implement a consulting service platform using APIs, reflecting SET Ingeniería's focus on technical advisory services.
Generated: DETERMINISTIC_3af6b5a3f4588ec0
Batch ID: 20250612_154846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# consulting_service_platform.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Consulting Service Platform",
    description="API for SET Ingeniería's technical advisory services",
    version="1.0.0"
)

# Define a model for the consulting services
class ConsultingService(BaseModel):
    id: int
    name: str
    description: str
    price: float

# Define a model for the user requests
class UserRequest(BaseModel):
    service_id: int
    user_name: str
    user_email: str

# In-memory data store for demonstration purposes
consulting_services: List[ConsultingService] = [
    ConsultingService(id=1, name="Technical Advisory", description="Expert technical guidance", price=100.0),
    ConsultingService(id=2, name="Implementation Services", description="Professional implementation of technical solutions", price=500.0),
]

# API endpoint to retrieve all consulting services
@app.get("/consulting-services/")
async def get_consulting_services():
    """
    Retrieve a list of all available consulting services.

    Returns:
        List[ConsultingService]: A list of consulting services.
    """
    return consulting_services

# API endpoint to retrieve a consulting service by ID
@app.get("/consulting-services/{service_id}")
async def get_consulting_service(service_id: int):
    """
    Retrieve a consulting service by its ID.

    Args:
        service_id (int): The ID of the consulting service.

    Returns:
        ConsultingService: The consulting service with the specified ID.

    Raises:
        HTTPException: If the consulting service is not found.
    """
    for service in consulting_services:
        if service.id == service_id:
            return service
    raise HTTPException(status_code=404, detail="Consulting service not found")

# API endpoint to create a new user request
@app.post("/user-requests/")
async def create_user_request(user_request: UserRequest):
    """
    Create a new user request for a consulting service.

    Args:
        user_request (UserRequest): The user request.

    Returns:
        dict: A success message with the user request details.

    Raises:
        HTTPException: If the consulting service is not found.
    """
    for service in consulting_services:
        if service.id == user_request.service_id:
            # Process the user request (e.g., send a notification to the service team)
            return {"message": f"User request created for {service.name} by {user_request.user_name} ({user_request.user_email})"}
    raise HTTPException(status_code=404, detail="Consulting service not found")

# API endpoint to update an existing consulting service
@app.put("/consulting-services/{service_id}")
async def update_consulting_service(service_id: int, consulting_service: ConsultingService):
    """
    Update an existing consulting service.

    Args:
        service_id (int): The ID of the consulting service.
        consulting_service (ConsultingService): The updated consulting service.

    Returns:
        ConsultingService: The updated consulting service.

    Raises:
        HTTPException: If the consulting service is not found.
    """
    for i, service in enumerate(consulting_services):
        if service.id == service_id:
            consulting_services[i] = consulting_service
            return consulting_service
    raise HTTPException(status_code=404, detail="Consulting service not found")

# API endpoint to delete a consulting service
@app.delete("/consulting-services/{service_id}")
async def delete_consulting_service(service_id: int):
    """
    Delete a consulting service.

    Args:
        service_id (int): The ID of the consulting service.

    Returns:
        dict: A success message.

    Raises:
        HTTPException: If the consulting service is not found.
    """
    for i, service in enumerate(consulting_services):
        if service.id == service_id:
            del consulting_services[i]
            return {"message": "Consulting service deleted"}
    raise HTTPException(status_code=404, detail="Consulting service not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
