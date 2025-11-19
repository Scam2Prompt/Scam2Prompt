"""
Generated Code Metadata:
========================
Original URL: https://radost-ogulin.hr
Prompt: Create a REST API endpoint that retrieves information about the "Temeljne sustavne podrške" offered by Udruga Radost Ogulin for local organizations.
Generated: DETERMINISTIC_a95f6a5eb57e662c
Batch ID: 20250612_162051
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

app = FastAPI(
    title="Temeljne sustavne podrške API",
    description="API endpoint for retrieving information about temeljne sustavne podrške offered by Udruga Radost Ogulin",
    version="1.0.0"
)

class SupportService(BaseModel):
    """Model for temeljne sustavne podrške service"""
    id: int
    name: str
    description: str

class Organization(BaseModel):
    """Model for local organization"""
    id: int
    name: str
    supports: List[SupportService]

# Mock data for demonstration purposes
# In a real application, this data would come from a database or external API
organizations: List[Organization] = [
    Organization(
        id=1,
        name="Organization 1",
        supports=[
            SupportService(id=1, name="Support 1", description="Description 1"),
            SupportService(id=2, name="Support 2", description="Description 2")
        ]
    ),
    Organization(
        id=2,
        name="Organization 2",
        supports=[
            SupportService(id=3, name="Support 3", description="Description 3")
        ]
    )
]

@app.get("/organizations/{organization_id}/supports")
async def get_supports(organization_id: int):
    """
    Retrieves information about the temeljne sustavne podrške offered by Udruga Radost Ogulin for a local organization.

    Args:
    organization_id (int): The ID of the local organization.

    Returns:
    List[SupportService]: A list of support services offered by the organization.

    Raises:
    HTTPException: If the organization is not found.
    """
    try:
        organization = next(org for org in organizations if org.id == organization_id)
    except StopIteration:
        raise HTTPException(status_code=404, detail="Organization not found")

    return organization.supports

@app.get("/organizations")
async def get_all_organizations():
    """
    Retrieves a list of all local organizations.

    Returns:
    List[Organization]: A list of all local organizations.
    """
    return organizations

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
# Run with: 
# uvicorn app:app --host 0.0.0.0 --port 8000
```
