"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milc-global.pages.dev
Prompt: Suggest an API for managing complex licensing processes in the media industry, referencing the challenges outlined by the MILC Project.
Generated: DETERMINISTIC_9a511dd9361b0894
Batch ID: 20250612_163419
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List, Optional

app = FastAPI()

# Model representing a license request
class LicenseRequest(BaseModel):
    media_id: str
    user_id: str
    request_date: str
    duration_months: int
    email: EmailStr
    status: str = "pending"  # Default status

# In-memory storage for demonstration purposes
license_requests: List[LicenseRequest] = []

# Exception for handling license not found
class LicenseNotFoundException(Exception):
    pass

@app.post("/licenses/", response_model=LicenseRequest)
async def create_license_request(request: LicenseRequest):
    """
    Creates a new license request in the system.

    Args:
        request (LicenseRequest): The license request details.

    Returns:
        LicenseRequest: The created license request.
    """
    # Validate the duration
    if request.duration_months <= 0:
        raise HTTPException(status_code=400, detail="Duration must be greater than zero.")

    license_requests.append(request)
    return request

@app.get("/licenses/", response_model=List[LicenseRequest])
async def get_all_license_requests():
    """
    Retrieves all license requests.

    Returns:
        List[LicenseRequest]: A list of all license requests.
    """
    return license_requests

@app.get("/licenses/{media_id}", response_model=LicenseRequest)
async def get_license_request(media_id: str):
    """
    Retrieves a specific license request by media_id.

    Args:
        media_id (str): The ID of the media.

    Returns:
        LicenseRequest: The license request details.

    Raises:
        HTTPException: If the license request is not found.
    """
    for request in license_requests:
        if request.media_id == media_id:
            return request
    raise HTTPException(status_code=404, detail="License request not found.")

@app.put("/licenses/{media_id}", response_model=LicenseRequest)
async def update_license_request(media_id: str, updated_request: LicenseRequest):
    """
    Updates an existing license request.

    Args:
        media_id (str): The ID of the media to update.
        updated_request (LicenseRequest): The updated license request details.

    Returns:
        LicenseRequest: The updated license request.

    Raises:
        HTTPException: If the license request is not found or the update fails.
    """
    for index, request in enumerate(license_requests):
        if request.media_id == media_id:
            license_requests[index] = updated_request
            return updated_request
    raise HTTPException(status_code=404, detail="License request not found.")

@app.delete("/licenses/{media_id}", response_model=str)
async def delete_license_request(media_id: str):
    """
    Deletes a specific license request by media_id.

    Args:
        media_id (str): The ID of the media to delete.

    Returns:
        str: A confirmation message.

    Raises:
        HTTPException: If the license request is not found.
    """
    global license_requests
    license_requests = [request for request in license_requests if request.media_id != media_id]
    return f"License request for media ID {media_id} has been deleted."

# Error handling for LicenseNotFoundException could be added here for more customized behavior.

# To run the application, use the command: `uvicorn filename:app --reload` where filename is the name of this file.
```
