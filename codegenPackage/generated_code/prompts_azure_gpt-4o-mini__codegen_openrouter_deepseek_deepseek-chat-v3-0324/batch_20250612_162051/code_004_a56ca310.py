"""
Generated Code Metadata:
========================
Original URL: https://prgmea.pk
Prompt: How can I create a training program API that aligns with the objectives of the Pakistan Readymade Garments Technical Training Institute (PRGTTI)?
Generated: DETERMINISTIC_a56ca3108c04180a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
PRGTTI Training Program API
This API provides endpoints to manage training programs for the Pakistan Readymade Garments Technical Training Institute.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import date
import uuid
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="PRGTTI Training Program API",
    description="API for managing training programs at Pakistan Readymade Garments Technical Training Institute",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory database (replace with actual database in production)
training_programs_db = []

class TrainingProgram(BaseModel):
    """Model representing a training program"""
    id: str
    title: str
    description: str
    duration_weeks: int
    start_date: date
    end_date: date
    max_participants: int
    current_participants: int = 0
    instructor: str
    location: str
    program_type: str  # e.g., "Basic", "Advanced", "Specialized"
    is_active: bool = True

class CreateTrainingProgramRequest(BaseModel):
    """Request model for creating a new training program"""
    title: str
    description: str
    duration_weeks: int
    start_date: date
    end_date: date
    max_participants: int
    instructor: str
    location: str
    program_type: str

class UpdateTrainingProgramRequest(BaseModel):
    """Request model for updating a training program"""
    title: Optional[str] = None
    description: Optional[str] = None
    duration_weeks: Optional[int] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    max_participants: Optional[int] = None
    instructor: Optional[str] = None
    location: Optional[str] = None
    program_type: Optional[str] = None
    is_active: Optional[bool] = None

@app.get("/programs", response_model=List[TrainingProgram], tags=["Programs"])
def get_all_programs(active_only: bool = True):
    """Get all training programs, optionally filtered by active status"""
    if active_only:
        return [program for program in training_programs_db if program["is_active"]]
    return training_programs_db

@app.get("/programs/{program_id}", response_model=TrainingProgram, tags=["Programs"])
def get_program(program_id: str):
    """Get a specific training program by ID"""
    program = next((p for p in training_programs_db if p["id"] == program_id), None)
    if not program:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Program not found"
        )
    return program

@app.post("/programs", response_model=TrainingProgram, status_code=status.HTTP_201_CREATED, tags=["Programs"])
def create_program(program_data: CreateTrainingProgramRequest):
    """Create a new training program"""
    if program_data.start_date > program_data.end_date:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="End date must be after start date"
        )
    
    program_id = str(uuid.uuid4())
    new_program = TrainingProgram(
        id=program_id,
        **program_data.dict()
    )
    training_programs_db.append(new_program.dict())
    return new_program

@app.put("/programs/{program_id}", response_model=TrainingProgram, tags=["Programs"])
def update_program(program_id: str, update_data: UpdateTrainingProgramRequest):
    """Update an existing training program"""
    program = next((p for p in training_programs_db if p["id"] == program_id), None)
    if not program:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Program not found"
        )
    
    update_dict = update_data.dict(exclude_unset=True)
    
    # Validate dates if they're being updated
    if "start_date" in update_dict or "end_date" in update_dict:
        new_start = update_dict.get("start_date", program["start_date"])
        new_end = update_dict.get("end_date", program["end_date"])
        if new_start > new_end:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="End date must be after start date"
            )
    
    for key, value in update_dict.items():
        program[key] = value
    
    return program

@app.delete("/programs/{program_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Programs"])
def delete_program(program_id: str):
    """Delete a training program (soft delete by setting is_active=False)"""
    program = next((p for p in training_programs_db if p["id"] == program_id), None)
    if not program:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Program not found"
        )
    
    program["is_active"] = False
    return None

@app.post("/programs/{program_id}/enroll", response_model=TrainingProgram, tags=["Enrollment"])
def enroll_participant(program_id: str):
    """Enroll a participant in a training program"""
    program = next((p for p in training_programs_db if p["id"] == program_id), None)
    if not program:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Program not found"
        )
    
    if not program["is_active"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Program is not active"
        )
    
    if program["current_participants"] >= program["max_participants"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Program is full"
        )
    
    program["current_participants"] += 1
    return program

@app.post("/programs/{program_id}/withdraw", response_model=TrainingProgram, tags=["Enrollment"])
def withdraw_participant(program_id: str):
    """Withdraw a participant from a training program"""
    program = next((p for p in training_programs_db if p["id"] == program_id), None)
    if not program:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Program not found"
        )
    
    if program["current_participants"] <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No participants to withdraw"
        )
    
    program["current_participants"] -= 1
    return program

@app.get("/programs/types/{program_type}", response_model=List[TrainingProgram], tags=["Programs"])
def get_programs_by_type(program_type: str, active_only: bool = True):
    """Get training programs filtered by type"""
    programs = [p for p in training_programs_db if p["program_type"].lower() == program_type.lower()]
    if active_only:
        programs = [p for p in programs if p["is_active"]]
    return programs
```
