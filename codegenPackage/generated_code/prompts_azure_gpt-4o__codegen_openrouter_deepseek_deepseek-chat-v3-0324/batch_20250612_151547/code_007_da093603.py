"""
Generated Code Metadata:
========================
Original URL: https://www.brothernz.com
Prompt: Develop a REST API for managing product categories like "Combination Machines" and "Overlock and Coverstitch Machines" on an e-commerce site similar to Brother NZ.
Generated: DETERMINISTIC_da093603c8313270
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4, UUID
from fastapi.middleware.cors import CORSMiddleware
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="E-commerce Product Categories API",
    description="API for managing product categories on an e-commerce site",
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

# In-memory database simulation
categories_db = []

# Models
class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None
    parent_id: Optional[UUID] = None

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: UUID
    children: List['Category'] = []

    class Config:
        orm_mode = True

Category.update_forward_refs()

# Helper functions
def find_category(category_id: UUID) -> Optional[Category]:
    for category in categories_db:
        if category.id == category_id:
            return category
    return None

def find_category_index(category_id: UUID) -> Optional[int]:
    for index, category in enumerate(categories_db):
        if category.id == category_id:
            return index
    return None

# API Endpoints
@app.post("/categories/", response_model=Category, status_code=status.HTTP_201_CREATED)
async def create_category(category: CategoryCreate):
    """Create a new product category"""
    try:
        db_category = Category(
            id=uuid4(),
            name=category.name,
            description=category.description,
            parent_id=category.parent_id,
            children=[]
        )
        
        if category.parent_id:
            parent = find_category(category.parent_id)
            if not parent:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Parent category not found"
                )
            parent.children.append(db_category)
        
        categories_db.append(db_category)
        logger.info(f"Created new category: {db_category.name}")
        return db_category
    except Exception as e:
        logger.error(f"Error creating category: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error creating category"
        )

@app.get("/categories/", response_model=List[Category])
async def list_categories():
    """List all top-level product categories"""
    try:
        top_level_categories = [cat for cat in categories_db if cat.parent_id is None]
        return top_level_categories
    except Exception as e:
        logger.error(f"Error listing categories: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error listing categories"
        )

@app.get("/categories/{category_id}", response_model=Category)
async def get_category(category_id: UUID):
    """Get details of a specific category"""
    try:
        category = find_category(category_id)
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found"
            )
        return category
    except Exception as e:
        logger.error(f"Error getting category {category_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error getting category"
        )

@app.put("/categories/{category_id}", response_model=Category)
async def update_category(category_id: UUID, updated_category: CategoryCreate):
    """Update an existing category"""
    try:
        category_index = find_category_index(category_id)
        if category_index is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found"
            )
        
        # Check if parent exists if provided
        if updated_category.parent_id:
            parent = find_category(updated_category.parent_id)
            if not parent:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Parent category not found"
                )
        
        # Update the category
        current_category = categories_db[category_index]
        updated_data = updated_category.dict(exclude_unset=True)
        for key, value in updated_data.items():
            setattr(current_category, key, value)
        
        logger.info(f"Updated category {category_id}")
        return current_category
    except Exception as e:
        logger.error(f"Error updating category {category_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error updating category"
        )

@app.delete("/categories/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(category_id: UUID):
    """Delete a category"""
    try:
        category_index = find_category_index(category_id)
        if category_index is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found"
            )
        
        # Check if category has children
        category = categories_db[category_index]
        if category.children:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cannot delete category with children"
            )
        
        # Remove from parent's children if it has a parent
        if category.parent_id:
            parent = find_category(category.parent_id)
            if parent:
                parent.children = [child for child in parent.children if child.id != category_id]
        
        # Remove from database
        del categories_db[category_index]
        logger.info(f"Deleted category {category_id}")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting category {category_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error deleting category"
        )

# Sample data initialization
@app.on_event("startup")
async def startup_event():
    """Initialize with sample data"""
    try:
        combination_machines = Category(
            id=uuid4(),
            name="Combination Machines",
            description="Machines that combine multiple functions",
            parent_id=None,
            children=[]
        )
        
        overlock_machines = Category(
            id=uuid4(),
            name="Overlock and Coverstitch Machines",
            description="Professional finishing machines",
            parent_id=None,
            children=[]
        )
        
        categories_db.extend([combination_machines, overlock_machines])
        logger.info("Sample categories initialized")
    except Exception as e:
        logger.error(f"Error initializing sample data: {str(e)}")
```
