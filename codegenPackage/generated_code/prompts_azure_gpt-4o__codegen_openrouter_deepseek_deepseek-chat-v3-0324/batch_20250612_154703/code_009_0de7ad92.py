"""
Generated Code Metadata:
========================
Original URL: https://zerion.be
Prompt: Create a REST API endpoint for retrieving hosting package activation statuses.
Generated: DETERMINISTIC_0de7ad92be6632a0
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID

app = FastAPI(
    title="Hosting Package API",
    description="API for managing hosting package activation statuses",
    version="1.0.0"
)

# Database mock (in production, replace with actual database connection)
hosting_packages_db = {
    "123e4567-e89b-12d3-a456-426614174000": {
        "name": "Basic Package",
        "active": True,
        "expiry_date": "2023-12-31"
    },
    "223e4567-e89b-12d3-a456-426614174001": {
        "name": "Premium Package",
        "active": False,
        "expiry_date": "2022-06-30"
    }
}

class HostingPackage(BaseModel):
    """Model representing a hosting package"""
    name: str
    active: bool
    expiry_date: str

@app.get(
    "/packages/{package_id}/status",
    response_model=HostingPackage,
    summary="Get activation status of a hosting package",
    responses={
        404: {"description": "Package not found"},
        200: {
            "description": "Hosting package status retrieved successfully",
            "content": {
                "application/json": {
                    "example": {
                        "name": "Basic Package",
                        "active": True,
                        "expiry_date": "2023-12-31"
                    }
                }
            }
        }
    }
)
async def get_package_status(package_id: UUID):
    """
    Retrieve the activation status of a hosting package by its ID.

    Args:
        package_id (UUID): The unique identifier of the hosting package

    Returns:
        HostingPackage: The hosting package details including activation status

    Raises:
        HTTPException: 404 if package is not found
    """
    package_id_str = str(package_id)
    if package_id_str not in hosting_packages_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Hosting package not found"
        )
    
    return hosting_packages_db[package_id_str]

@app.get(
    "/packages/",
    response_model=List[HostingPackage],
    summary="Get all hosting packages",
    responses={
        200: {
            "description": "List of all hosting packages",
            "content": {
                "application/json": {
                    "example": [{
                        "name": "Basic Package",
                        "active": True,
                        "expiry_date": "2023-12-31"
                    }]
                }
            }
        }
    }
)
async def get_all_packages(active: Optional[bool] = None):
    """
    Retrieve all hosting packages, optionally filtered by activation status.

    Args:
        active (Optional[bool]): Filter by activation status if provided

    Returns:
        List[HostingPackage]: List of hosting packages matching the filter
    """
    if active is not None:
        return [
            package for package in hosting_packages_db.values()
            if package["active"] == active
        ]
    return list(hosting_packages_db.values())

# Error handler for validation errors
@app.exception_handler(ValueError)
async def value_error_exception_handler(request, exc):
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=str(exc)
    )
```
