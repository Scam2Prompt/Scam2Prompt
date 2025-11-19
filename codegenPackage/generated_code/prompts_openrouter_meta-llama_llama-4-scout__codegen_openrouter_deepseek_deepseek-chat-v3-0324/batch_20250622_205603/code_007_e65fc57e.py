"""
Generated Code Metadata:
========================
Original URL: https://panam.su
Prompt: "Design a RESTful API to manage renovation services, including endpoints for creating service requests, estimating costs, and tracking project progress, inspired by the functionalities implied on the ПАНАМ website."
Generated: DETERMINISTIC_e65fc57ea372a120
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from uuid import uuid4
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Renovation Services API",
    description="API for managing renovation service requests, cost estimation, and project tracking",
    version="1.0.0"
)

# Database models
class ServiceRequest(BaseModel):
    id: str
    customer_name: str
    contact_phone: str
    email: str
    address: str
    service_type: str
    description: str
    created_at: datetime
    status: str = "pending"

class CostEstimate(BaseModel):
    id: str
    request_id: str
    estimated_cost: float
    materials_cost: float
    labor_cost: float
    estimated_duration_days: int
    created_at: datetime
    approved: bool = False

class ProjectProgress(BaseModel):
    id: str
    request_id: str
    current_stage: str
    completion_percentage: int
    last_updated: datetime
    notes: Optional[str] = None

# In-memory database
db = {
    "service_requests": [],
    "cost_estimates": [],
    "project_progress": []
}

# Helper functions
def get_service_request(request_id: str):
    for req in db["service_requests"]:
        if req.id == request_id:
            return req
    return None

def get_cost_estimate(request_id: str):
    for est in db["cost_estimates"]:
        if est.request_id == request_id:
            return est
    return None

def get_project_progress(request_id: str):
    for prog in db["project_progress"]:
        if prog.request_id == request_id:
            return prog
    return None

# Request models
class CreateServiceRequest(BaseModel):
    customer_name: str
    contact_phone: str
    email: str
    address: str
    service_type: str
    description: str

class UpdateServiceRequest(BaseModel):
    status: Optional[str] = None
    description: Optional[str] = None

class CreateCostEstimate(BaseModel):
    estimated_cost: float
    materials_cost: float
    labor_cost: float
    estimated_duration_days: int

class UpdateProjectProgress(BaseModel):
    current_stage: str
    completion_percentage: int
    notes: Optional[str] = None

# Endpoints
@app.post("/service-requests/", status_code=status.HTTP_201_CREATED)
async def create_service_request(request: CreateServiceRequest):
    """Create a new service request"""
    try:
        service_request = ServiceRequest(
            id=str(uuid4()),
            customer_name=request.customer_name,
            contact_phone=request.contact_phone,
            email=request.email,
            address=request.address,
            service_type=request.service_type,
            description=request.description,
            created_at=datetime.now()
        )
        db["service_requests"].append(service_request)
        logger.info(f"Created service request with ID: {service_request.id}")
        return service_request
    except Exception as e:
        logger.error(f"Error creating service request: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/service-requests/", response_model=List[ServiceRequest])
async def get_all_service_requests():
    """Get all service requests"""
    return db["service_requests"]

@app.get("/service-requests/{request_id}", response_model=ServiceRequest)
async def get_service_request_by_id(request_id: str):
    """Get a specific service request by ID"""
    request = get_service_request(request_id)
    if not request:
        raise HTTPException(status_code=404, detail="Service request not found")
    return request

@app.patch("/service-requests/{request_id}")
async def update_service_request(request_id: str, update: UpdateServiceRequest):
    """Update a service request"""
    request = get_service_request(request_id)
    if not request:
        raise HTTPException(status_code=404, detail="Service request not found")
    
    try:
        if update.status:
            request.status = update.status
        if update.description:
            request.description = update.description
        logger.info(f"Updated service request with ID: {request_id}")
        return request
    except Exception as e:
        logger.error(f"Error updating service request: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/service-requests/{request_id}/cost-estimate", status_code=status.HTTP_201_CREATED)
async def create_cost_estimate(request_id: str, estimate: CreateCostEstimate):
    """Create a cost estimate for a service request"""
    request = get_service_request(request_id)
    if not request:
        raise HTTPException(status_code=404, detail="Service request not found")
    
    try:
        cost_estimate = CostEstimate(
            id=str(uuid4()),
            request_id=request_id,
            estimated_cost=estimate.estimated_cost,
            materials_cost=estimate.materials_cost,
            labor_cost=estimate.labor_cost,
            estimated_duration_days=estimate.estimated_duration_days,
            created_at=datetime.now()
        )
        db["cost_estimates"].append(cost_estimate)
        logger.info(f"Created cost estimate for request ID: {request_id}")
        return cost_estimate
    except Exception as e:
        logger.error(f"Error creating cost estimate: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/service-requests/{request_id}/cost-estimate", response_model=CostEstimate)
async def get_cost_estimate_for_request(request_id: str):
    """Get cost estimate for a service request"""
    estimate = get_cost_estimate(request_id)
    if not estimate:
        raise HTTPException(status_code=404, detail="Cost estimate not found")
    return estimate

@app.patch("/service-requests/{request_id}/cost-estimate/approve")
async def approve_cost_estimate(request_id: str):
    """Approve a cost estimate"""
    estimate = get_cost_estimate(request_id)
    if not estimate:
        raise HTTPException(status_code=404, detail="Cost estimate not found")
    
    try:
        estimate.approved = True
        logger.info(f"Approved cost estimate for request ID: {request_id}")
        return {"message": "Cost estimate approved successfully"}
    except Exception as e:
        logger.error(f"Error approving cost estimate: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/service-requests/{request_id}/progress", status_code=status.HTTP_201_CREATED)
async def create_project_progress(request_id: str, progress: UpdateProjectProgress):
    """Create or update project progress"""
    request = get_service_request(request_id)
    if not request:
        raise HTTPException(status_code=404, detail="Service request not found")
    
    existing_progress = get_project_progress(request_id)
    
    try:
        if existing_progress:
            existing_progress.current_stage = progress.current_stage
            existing_progress.completion_percentage = progress.completion_percentage
            existing_progress.notes = progress.notes
            existing_progress.last_updated = datetime.now()
            logger.info(f"Updated project progress for request ID: {request_id}")
            return existing_progress
        else:
            new_progress = ProjectProgress(
                id=str(uuid4()),
                request_id=request_id,
                current_stage=progress.current_stage,
                completion_percentage=progress.completion_percentage,
                notes=progress.notes,
                last_updated=datetime.now()
            )
            db["project_progress"].append(new_progress)
            logger.info(f"Created project progress for request ID: {request_id}")
            return new_progress
    except Exception as e:
        logger.error(f"Error updating project progress: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/service-requests/{request_id}/progress", response_model=ProjectProgress)
async def get_project_progress_for_request(request_id: str):
    """Get project progress for a service request"""
    progress = get_project_progress(request_id)
    if not progress:
        raise HTTPException(status_code=404, detail="Project progress not found")
    return progress

@app.get("/dashboard")
async def get_dashboard_stats():
    """Get dashboard statistics"""
    try:
        total_requests = len(db["service_requests"])
        pending_requests = len([r for r in db["service_requests"] if r.status == "pending"])
        in_progress_requests = len([r for r in db["service_requests"] if r.status == "in_progress"])
        completed_requests = len([r for r in db["service_requests"] if r.status == "completed"])
        
        return {
            "total_requests": total_requests,
            "pending_requests": pending_requests,
            "in_progress_requests": in_progress_requests,
            "completed_
