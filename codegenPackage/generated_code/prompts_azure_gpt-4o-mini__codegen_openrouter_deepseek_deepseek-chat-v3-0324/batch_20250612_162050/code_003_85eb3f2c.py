"""
Generated Code Metadata:
========================
Original URL: https://tallhills.com
Prompt: Generate a sample API that integrates design thinking methodologies into a product development workflow, based on insights from TallHills.
Generated: DETERMINISTIC_85eb3f2cb23898e8
Batch ID: 20250612_162050
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
from typing import List, Optional
from enum import Enum
import uuid
from datetime import datetime

app = FastAPI(
    title="Design Thinking API",
    description="API for integrating design thinking methodologies into product development workflows",
    version="1.0.0"
)

# Data Models
class DesignPhase(str, Enum):
    EMPATHIZE = "empathize"
    DEFINE = "define"
    IDEATE = "ideate"
    PROTOTYPE = "prototype"
    TEST = "test"

class Insight(BaseModel):
    id: str
    text: str
    source: str
    created_at: datetime
    phase: DesignPhase
    tags: List[str] = []

class InsightCreate(BaseModel):
    text: str
    source: str
    phase: DesignPhase
    tags: List[str] = []

class ProductIdea(BaseModel):
    id: str
    title: str
    description: str
    insights: List[str]  # List of insight IDs
    created_at: datetime
    updated_at: datetime
    status: str = "draft"

class ProductIdeaCreate(BaseModel):
    title: str
    description: str
    insights: List[str]

# Database Simulation
db = {
    "insights": {},
    "product_ideas": {}
}

# Helper Functions
def generate_id():
    return str(uuid.uuid4())

def get_current_time():
    return datetime.utcnow()

# API Endpoints
@app.post("/insights/", response_model=Insight, status_code=status.HTTP_201_CREATED)
def create_insight(insight: InsightCreate):
    """Create a new design thinking insight"""
    insight_id = generate_id()
    new_insight = Insight(
        id=insight_id,
        text=insight.text,
        source=insight.source,
        created_at=get_current_time(),
        phase=insight.phase,
        tags=insight.tags
    )
    db["insights"][insight_id] = new_insight
    return new_insight

@app.get("/insights/", response_model=List[Insight])
def list_insights(phase: Optional[DesignPhase] = None, tag: Optional[str] = None):
    """List all insights, optionally filtered by phase or tag"""
    insights = list(db["insights"].values())
    
    if phase:
        insights = [i for i in insights if i.phase == phase]
    
    if tag:
        insights = [i for i in insights if tag in i.tags]
    
    return insights

@app.get("/insights/{insight_id}", response_model=Insight)
def get_insight(insight_id: str):
    """Get a specific insight by ID"""
    if insight_id not in db["insights"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Insight not found"
        )
    return db["insights"][insight_id]

@app.post("/product-ideas/", response_model=ProductIdea, status_code=status.HTTP_201_CREATED)
def create_product_idea(idea: ProductIdeaCreate):
    """Create a new product idea based on insights"""
    # Validate all insight IDs exist
    for insight_id in idea.insights:
        if insight_id not in db["insights"]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Insight with ID {insight_id} not found"
            )
    
    idea_id = generate_id()
    current_time = get_current_time()
    new_idea = ProductIdea(
        id=idea_id,
        title=idea.title,
        description=idea.description,
        insights=idea.insights,
        created_at=current_time,
        updated_at=current_time
    )
    db["product_ideas"][idea_id] = new_idea
    return new_idea

@app.get("/product-ideas/", response_model=List[ProductIdea])
def list_product_ideas():
    """List all product ideas"""
    return list(db["product_ideas"].values())

@app.get("/product-ideas/{idea_id}", response_model=ProductIdea)
def get_product_idea(idea_id: str):
    """Get a specific product idea by ID"""
    if idea_id not in db["product_ideas"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product idea not found"
        )
    return db["product_ideas"][idea_id]

@app.put("/product-ideas/{idea_id}", response_model=ProductIdea)
def update_product_idea(idea_id: str, idea_update: ProductIdeaCreate):
    """Update an existing product idea"""
    if idea_id not in db["product_ideas"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product idea not found"
        )
    
    # Validate all insight IDs exist
    for insight_id in idea_update.insights:
        if insight_id not in db["insights"]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Insight with ID {insight_id} not found"
            )
    
    existing_idea = db["product_ideas"][idea_id]
    updated_idea = ProductIdea(
        id=idea_id,
        title=idea_update.title,
        description=idea_update.description,
        insights=idea_update.insights,
        created_at=existing_idea.created_at,
        updated_at=get_current_time(),
        status=existing_idea.status
    )
    db["product_ideas"][idea_id] = updated_idea
    return updated_idea

@app.post("/product-ideas/{idea_id}/validate", response_model=ProductIdea)
def validate_product_idea(idea_id: str):
    """Mark a product idea as validated"""
    if idea_id not in db["product_ideas"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product idea not found"
        )
    
    idea = db["product_ideas"][idea_id]
    idea.status = "validated"
    idea.updated_at = get_current_time()
    return idea

@app.get("/phases/", response_model=List[str])
def list_design_phases():
    """List all available design thinking phases"""
    return [phase.value for phase in DesignPhase]
```
