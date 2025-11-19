"""
Generated Code Metadata:
========================
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Suggest an API for managing and displaying testimonials on a community-focused website like "The Faces Of Sedona and the Verde Valley."
Generated: DETERMINISTIC_b524fcdd7454c73e
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from uuid import uuid4
from fastapi.security import OAuth2PasswordBearer
import motor.motor_asyncio
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI(
    title="Testimonials API",
    description="API for managing and displaying testimonials for community-focused websites",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database configuration
DATABASE_URL = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)
db = client.testimonials_db
testimonials_collection = db.testimonials

# Security configuration
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class TestimonialBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    role: Optional[str] = Field(None, max_length=50)
    content: str = Field(..., min_length=10, max_length=500)
    image_url: Optional[str] = None
    featured: bool = False

class TestimonialCreate(TestimonialBase):
    pass

class Testimonial(TestimonialBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        json_encoders = {ObjectId: str}

class TestimonialUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=50)
    role: Optional[str] = Field(None, max_length=50)
    content: Optional[str] = Field(None, min_length=10, max_length=500)
    image_url: Optional[str] = None
    featured: Optional[bool] = None

# Helper functions
async def get_testimonial_or_404(id: str):
    testimonial = await testimonials_collection.find_one({"_id": ObjectId(id)})
    if not testimonial:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Testimonial not found")
    return testimonial

# API Endpoints
@app.post("/testimonials/", response_model=Testimonial, status_code=status.HTTP_201_CREATED)
async def create_testimonial(testimonial: TestimonialCreate, token: str = Depends(oauth2_scheme)):
    """Create a new testimonial"""
    testimonial_data = testimonial.dict()
    testimonial_data["_id"] = ObjectId()
    testimonial_data["created_at"] = testimonial_data["updated_at"] = datetime.utcnow()
    
    await testimonials_collection.insert_one(testimonial_data)
    return {**testimonial_data, "id": str(testimonial_data["_id"])}

@app.get("/testimonials/", response_model=List[Testimonial])
async def get_testimonials(featured: bool = None, limit: int = 10, skip: int = 0):
    """Get all testimonials, optionally filtered by featured status"""
    query = {}
    if featured is not None:
        query["featured"] = featured
    
    testimonials = []
    async for testimonial in testimonials_collection.find(query).skip(skip).limit(limit):
        testimonials.append({**testimonial, "id": str(testimonial["_id"])})
    return testimonials

@app.get("/testimonials/{id}", response_model=Testimonial)
async def get_testimonial(id: str):
    """Get a specific testimonial by ID"""
    testimonial = await get_testimonial_or_404(id)
    return {**testimonial, "id": str(testimonial["_id"])}

@app.put("/testimonials/{id}", response_model=Testimonial)
async def update_testimonial(id: str, testimonial_update: TestimonialUpdate, token: str = Depends(oauth2_scheme)):
    """Update a testimonial"""
    existing_testimonial = await get_testimonial_or_404(id)
    
    update_data = testimonial_update.dict(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No data provided for update")
    
    update_data["updated_at"] = datetime.utcnow()
    await testimonials_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": update_data}
    )
    
    updated_testimonial = await get_testimonial_or_404(id)
    return {**updated_testimonial, "id": str(updated_testimonial["_id"])}

@app.delete("/testimonials/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_testimonial(id: str, token: str = Depends(oauth2_scheme)):
    """Delete a testimonial"""
    testimonial = await get_testimonial_or_404(id)
    await testimonials_collection.delete_one({"_id": ObjectId(id)})
    return None

@app.get("/testimonials/random", response_model=Testimonial)
async def get_random_testimonial():
    """Get a random testimonial"""
    count = await testimonials_collection.count_documents({})
    if count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No testimonials found")
    
    random_skip = random.randint(0, count - 1)
    testimonial = await testimonials_collection.find_one(skip=random_skip)
    return {**testimonial, "id": str(testimonial["_id"])}
```
