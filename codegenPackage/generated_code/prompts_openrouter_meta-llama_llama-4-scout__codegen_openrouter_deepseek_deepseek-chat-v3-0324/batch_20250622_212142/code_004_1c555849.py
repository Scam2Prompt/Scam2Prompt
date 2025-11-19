"""
Generated Code Metadata:
========================
Original URL: https://gra-pro-canv.webflow.io
Prompt: "Develop an API for managing grants programs, including endpoints for creating, reading, updating, and deleting program data."
Generated: DETERMINISTIC_1c55584910473610
Batch ID: 20250622_212142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import uuid4, UUID
from datetime import datetime

# Initialize FastAPI app
app = FastAPI(
    title="Grants Program Management API",
    description="API for managing grants programs",
    version="1.0.0"
)

# Database simulation (in-memory storage)
grants_db = []

# Pydantic models for request/response validation
class GrantProgramBase(BaseModel):
    name: str = Field(..., example="Education Initiative", min_length=3)
    description: str = Field(..., example="Funding for educational projects")
    start_date: datetime = Field(..., example="2023-01-01T00:00:00")
    end_date: datetime = Field(..., example="2023-12-31T23:59:59")
    budget: float = Field(..., example=1000000.00, gt=0)
    active: bool = Field(default=True)

class GrantProgramCreate(GrantProgramBase):
    pass

class GrantProgram(GrantProgramBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# Helper functions
def get_grant_program(program_id: UUID):
    for program in grants_db:
        if program.id == program_id:
            return program
    return None

# API Endpoints
@app.post("/programs/", response_model=GrantProgram, status_code=status.HTTP_201_CREATED)
async def create_grant_program(program: GrantProgramCreate):
    """
    Create a new grants program.
    """
    program_data = program.dict()
    program_id = uuid4()
    now = datetime.now()
    
    db_program = {
        "id": program_id,
        "created_at": now,
        "updated_at": now,
        **program_data
    }
    
    grants_db.append(db_program)
    return db_program

@app.get("/programs/", response_model=List[GrantProgram])
async def read_grant_programs(active: Optional[bool] = None):
    """
    Get all grants programs, optionally filtered by active status.
    """
    if active is not None:
        return [program for program in grants_db if program["active"] == active]
    return grants_db

@app.get("/programs/{program_id}", response_model=GrantProgram)
async def read_grant_program(program_id: UUID):
    """
    Get a specific grants program by ID.
    """
    program = get_grant_program(program_id)
    if not program:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Grant program not found"
        )
    return program

@app.put("/programs/{program_id}", response_model=GrantProgram)
async def update_grant_program(program_id: UUID, program: GrantProgramCreate):
    """
    Update an existing grants program.
    """
    existing_program = get_grant_program(program_id)
    if not existing_program:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Grant program not found"
        )
    
    update_data = program.dict(exclude_unset=True)
    update_data["updated_at"] = datetime.now()
    
    for key, value in update_data.items():
        existing_program[key] = value
    
    return existing_program

@app.delete("/programs/{program_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_grant_program(program_id: UUID):
    """
    Delete a grants program.
    """
    program = get_grant_program(program_id)
    if not program:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Grant program not found"
        )
    
    grants_db.remove(program)
    return None

# Error handlers
@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=str(exc)
    )
```
