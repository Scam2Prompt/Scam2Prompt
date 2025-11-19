"""
Generated Code Metadata:
========================
Original URL: https://ayb-sd.org
Prompt: Create an API that connects small business owners with resources for capacity building and skills training, reflecting the mission of جمعية علشانك يا بلدي.
Generated: DETERMINISTIC_32b7694abd1ae347
Batch ID: 20250612_162510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum
import uuid
from datetime import datetime
import logging
from fastapi.middleware.cors import CORSMiddleware

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Small Business Capacity Building API",
    description="API connecting small business owners with resources for capacity building and skills training",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Enums for resource types and categories
class ResourceType(str, Enum):
    COURSE = "course"
    WORKSHOP = "workshop"
    MENTORSHIP = "mentorship"
    FINANCIAL_AID = "financial_aid"
    NETWORKING = "networking"

class BusinessCategory(str, Enum):
    AGRICULTURE = "agriculture"
    HANDICRAFTS = "handicrafts"
    RETAIL = "retail"
    FOOD = "food"
    SERVICES = "services"
    TECHNOLOGY = "technology"
    OTHER = "other"

# Pydantic models
class Resource(BaseModel):
    id: str = str(uuid.uuid4())
    title: str
    description: str
    type: ResourceType
    categories: List[BusinessCategory]
    provider: str
    url: str
    location: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    is_free: bool = False
    language: str = "ar"

class BusinessOwner(BaseModel):
    id: str = str(uuid.uuid4())
    name: str
    email: str
    phone: str
    business_name: str
    business_category: BusinessCategory
    location: str
    needs: List[str]

class ResourceResponse(BaseModel):
    success: bool
    data: Resource

class BusinessOwnerResponse(BaseModel):
    success: bool
    data: BusinessOwner

class ResourceListResponse(BaseModel):
    success: bool
    data: List[Resource]

# Database simulation
resources_db = []
business_owners_db = []

# Helper functions
def find_resource(resource_id: str) -> Optional[Resource]:
    for resource in resources_db:
        if resource.id == resource_id:
            return resource
    return None

def find_business_owner(owner_id: str) -> Optional[BusinessOwner]:
    for owner in business_owners_db:
        if owner.id == owner_id:
            return owner
    return None

# API Endpoints
@app.post("/resources/", response_model=ResourceResponse, status_code=201)
async def create_resource(resource: Resource):
    """Create a new resource for small business owners"""
    try:
        resources_db.append(resource)
        logger.info(f"Created new resource: {resource.id}")
        return {"success": True, "data": resource}
    except Exception as e:
        logger.error(f"Error creating resource: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/resources/", response_model=ResourceListResponse)
async def get_resources(
    type: Optional[ResourceType] = None,
    category: Optional[BusinessCategory] = None,
    location: Optional[str] = None,
    is_free: Optional[bool] = None
):
    """Get all resources with optional filters"""
    try:
        filtered_resources = resources_db
        
        if type:
            filtered_resources = [r for r in filtered_resources if r.type == type]
        if category:
            filtered_resources = [r for r in filtered_resources if category in r.categories]
        if location:
            filtered_resources = [r for r in filtered_resources if r.location and location.lower() in r.location.lower()]
        if is_free is not None:
            filtered_resources = [r for r in filtered_resources if r.is_free == is_free]
            
        return {"success": True, "data": filtered_resources}
    except Exception as e:
        logger.error(f"Error fetching resources: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/resources/{resource_id}", response_model=ResourceResponse)
async def get_resource(resource_id: str):
    """Get a specific resource by ID"""
    resource = find_resource(resource_id)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    return {"success": True, "data": resource}

@app.post("/business-owners/", response_model=BusinessOwnerResponse, status_code=201)
async def register_business_owner(owner: BusinessOwner):
    """Register a new business owner"""
    try:
        # Check if email already exists
        if any(o.email == owner.email for o in business_owners_db):
            raise HTTPException(status_code=400, detail="Email already registered")
            
        business_owners_db.append(owner)
        logger.info(f"Registered new business owner: {owner.id}")
        return {"success": True, "data": owner}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error registering business owner: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/business-owners/{owner_id}", response_model=BusinessOwnerResponse)
async def get_business_owner(owner_id: str):
    """Get a specific business owner by ID"""
    owner = find_business_owner(owner_id)
    if not owner:
        raise HTTPException(status_code=404, detail="Business owner not found")
    return {"success": True, "data": owner}

@app.get("/business-owners/{owner_id}/recommendations", response_model=ResourceListResponse)
async def get_recommendations(owner_id: str):
    """Get recommended resources for a business owner based on their category and needs"""
    try:
        owner = find_business_owner(owner_id)
        if not owner:
            raise HTTPException(status_code=404, detail="Business owner not found")
            
        recommendations = []
        for resource in resources_db:
            # Match by business category
            if owner.business_category in resource.categories:
                recommendations.append(resource)
            # Match by needs (simple keyword matching)
            elif any(need.lower() in resource.description.lower() for need in owner.needs):
                recommendations.append(resource)
                
        return {"success": True, "data": recommendations}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error generating recommendations: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now()}
```
