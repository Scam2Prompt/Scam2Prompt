"""
Generated Code Metadata:
========================
Original URL: https://harda-ke.org
Prompt: Develop a sample API documentation for a platform that facilitates funding and partnership management for NGOs like HARDA.
Generated: DETERMINISTIC_6b0eaa1a1b971941
Batch ID: 20250622_211610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Initialize FastAPI application
app = FastAPI(
    title="NGO Funding and Partnership Management API",
    description="API for managing funding and partnerships for NGOs",
    version="1.0.0",
)

# Define Pydantic models for request and response bodies
class NGO(BaseModel):
    """NGO details"""
    id: int
    name: str
    description: str

class FundingRequest(BaseModel):
    """Funding request details"""
    id: int
    ngo_id: int
    amount: float
    description: str

class PartnershipRequest(BaseModel):
    """Partnership request details"""
    id: int
    ngo_id: int
    partner_name: str
    description: str

class Funding(BaseModel):
    """Funding details"""
    id: int
    ngo_id: int
    amount: float
    status: str

class Partnership(BaseModel):
    """Partnership details"""
    id: int
    ngo_id: int
    partner_name: str
    status: str

# Sample in-memory data store (replace with a database in production)
ngos: List[NGO] = [
    NGO(id=1, name="HARDA", description="Helping Rural Development Association"),
]

funding_requests: List[FundingRequest] = []
partnership_requests: List[PartnershipRequest] = []
fundings: List[Funding] = []
partnerships: List[Partnership] = []

# API Endpoints
@app.get("/ngos/")
async def get_ngos():
    """Retrieve a list of all NGOs"""
    return ngos

@app.get("/ngos/{ngo_id}")
async def get_ngo(ngo_id: int):
    """Retrieve a specific NGO by ID"""
    ngo = next((ngo for ngo in ngos if ngo.id == ngo_id), None)
    if ngo is None:
        raise HTTPException(status_code=404, detail="NGO not found")
    return ngo

@app.post("/funding/requests/")
async def create_funding_request(funding_request: FundingRequest):
    """Create a new funding request"""
    funding_requests.append(funding_request)
    return funding_request

@app.get("/funding/requests/")
async def get_funding_requests():
    """Retrieve a list of all funding requests"""
    return funding_requests

@app.post("/partnership/requests/")
async def create_partnership_request(partnership_request: PartnershipRequest):
    """Create a new partnership request"""
    partnership_requests.append(partnership_request)
    return partnership_request

@app.get("/partnership/requests/")
async def get_partnership_requests():
    """Retrieve a list of all partnership requests"""
    return partnership_requests

@app.post("/funding/")
async def create_funding(funding: Funding):
    """Create a new funding"""
    fundings.append(funding)
    return funding

@app.get("/funding/")
async def get_funding():
    """Retrieve a list of all funding"""
    return fundings

@app.post("/partnerships/")
async def create_partnership(partnership: Partnership):
    """Create a new partnership"""
    partnerships.append(partnership)
    return partnership

@app.get("/partnerships/")
async def get_partnerships():
    """Retrieve a list of all partnerships"""
    return partnerships

@app.put("/funding/{funding_id}")
async def update_funding(funding_id: int, funding: Funding):
    """Update an existing funding"""
    existing_funding = next((f for f in fundings if f.id == funding_id), None)
    if existing_funding is None:
        raise HTTPException(status_code=404, detail="Funding not found")
    existing_funding.amount = funding.amount
    existing_funding.status = funding.status
    return existing_funding

@app.put("/partnerships/{partnership_id}")
async def update_partnership(partnership_id: int, partnership: Partnership):
    """Update an existing partnership"""
    existing_partnership = next((p for p in partnerships if p.id == partnership_id), None)
    if existing_partnership is None:
        raise HTTPException(status_code=404, detail="Partnership not found")
    existing_partnership.partner_name = partnership.partner_name
    existing_partnership.status = partnership.status
    return existing_partnership

@app.delete("/funding/{funding_id}")
async def delete_funding(funding_id: int):
    """Delete a funding"""
    global fundings
    fundings = [f for f in fundings if f.id != funding_id]
    return {"message": "Funding deleted successfully"}

@app.delete("/partnerships/{partnership_id}")
async def delete_partnership(partnership_id: int):
    """Delete a partnership"""
    global partnerships
    partnerships = [p for p in partnerships if p.id != partnership_id]
    return {"message": "Partnership deleted successfully"}
```
