"""
Generated Code Metadata:
========================
Original URL: https://kekgroup.net
Prompt: Develop a brief API documentation for a life assurance product in West Africa, similar to those offered by KEK Life, including endpoints for policy management and claims processing.
Generated: DETERMINISTIC_0149704c8518ca98
Batch ID: 20250622_205459
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
    title="Life Assurance API",
    description="API for life assurance product in West Africa",
    version="1.0.0",
)

# Define Pydantic models
class Policy(BaseModel):
    policy_id: str
    customer_name: str
    policy_type: str
    premium: float
    coverage_amount: float

class Claim(BaseModel):
    claim_id: str
    policy_id: str
    claim_type: str
    claim_amount: float

# In-memory data store (replace with a database in production)
policies: List[Policy] = []
claims: List[Claim] = []

# Policy Management Endpoints
@app.post("/policies/")
async def create_policy(policy: Policy):
    # Check for duplicate policy ID
    if any(p.policy_id == policy.policy_id for p in policies):
        raise HTTPException(status_code=400, detail="Policy ID already exists")
    policies.append(policy)
    return policy

@app.get("/policies/")
async def read_policies():
    return policies

@app.get("/policies/{policy_id}")
async def read_policy(policy_id: str):
    policy = next((p for p in policies if p.policy_id == policy_id), None)
    if policy is None:
        raise HTTPException(status_code=404, detail="Policy not found")
    return policy

@app.put("/policies/{policy_id}")
async def update_policy(policy_id: str, policy: Policy):
    existing_policy = next((p for p in policies if p.policy_id == policy_id), None)
    if existing_policy is None:
        raise HTTPException(status_code=404, detail="Policy not found")
    existing_policy.customer_name = policy.customer_name
    existing_policy.policy_type = policy.policy_type
    existing_policy.premium = policy.premium
    existing_policy.coverage_amount = policy.coverage_amount
    return existing_policy

@app.delete("/policies/{policy_id}")
async def delete_policy(policy_id: str):
    policy = next((p for p in policies if p.policy_id == policy_id), None)
    if policy is None:
        raise HTTPException(status_code=404, detail="Policy not found")
    policies.remove(policy)
    return {"message": "Policy deleted"}

# Claims Processing Endpoints
@app.post("/claims/")
async def create_claim(claim: Claim):
    # Check for duplicate claim ID
    if any(c.claim_id == claim.claim_id for c in claims):
        raise HTTPException(status_code=400, detail="Claim ID already exists")
    # Check if policy exists
    policy = next((p for p in policies if p.policy_id == claim.policy_id), None)
    if policy is None:
        raise HTTPException(status_code=404, detail="Policy not found")
    claims.append(claim)
    return claim

@app.get("/claims/")
async def read_claims():
    return claims

@app.get("/claims/{claim_id}")
async def read_claim(claim_id: str):
    claim = next((c for c in claims if c.claim_id == claim_id), None)
    if claim is None:
        raise HTTPException(status_code=404, detail="Claim not found")
    return claim

@app.put("/claims/{claim_id}")
async def update_claim(claim_id: str, claim: Claim):
    existing_claim = next((c for c in claims if c.claim_id == claim_id), None)
    if existing_claim is None:
        raise HTTPException(status_code=404, detail="Claim not found")
    existing_claim.claim_type = claim.claim_type
    existing_claim.claim_amount = claim.claim_amount
    return existing_claim

@app.delete("/claims/{claim_id}")
async def delete_claim(claim_id: str):
    claim = next((c for c in claims if c.claim_id == claim_id), None)
    if claim is None:
        raise HTTPException(status_code=404, detail="Claim not found")
    claims.remove(claim)
    return {"message": "Claim deleted"}
```

```python
# main.py

from app import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```markdown
# API Documentation

## Policy Management

### Create Policy
* **Endpoint:** `POST /policies/`
* **Request Body:** `Policy` object
* **Response:** Created `Policy` object

### Read Policies
* **Endpoint:** `GET /policies/`
* **Response:** List of `Policy` objects

### Read Policy
* **Endpoint:** `GET /policies/{policy_id}`
* **Path Parameters:** `policy_id` (string)
* **Response:** `Policy` object

### Update Policy
* **Endpoint:** `PUT /policies/{policy_id}`
* **Path Parameters:** `policy_id` (string)
* **Request Body:** `Policy` object
* **Response:** Updated `Policy` object

### Delete Policy
* **Endpoint:** `DELETE /policies/{policy_id}`
* **Path Parameters:** `policy_id` (string)
* **Response:** Success message

## Claims Processing

### Create Claim
* **Endpoint:** `POST /claims/`
* **Request Body:** `Claim` object
* **Response:** Created `Claim` object

### Read Claims
* **Endpoint:** `GET /claims/`
* **Response:** List of `Claim` objects

### Read Claim
* **Endpoint:** `GET /claims/{claim_id}`
* **Path Parameters:** `claim_id` (string)
* **Response:** `Claim` object

### Update Claim
* **Endpoint:** `PUT /claims/{claim_id}`
* **Path Parameters:** `claim_id` (string)
* **Request Body:** `Claim` object
* **Response:** Updated `Claim` object

### Delete Claim
* **Endpoint:** `DELETE /claims/{claim_id}`
* **Path Parameters:** `claim_id` (string)
* **Response:** Success message
```
