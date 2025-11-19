"""
Generated Code Metadata:
========================
Original URL: https://itscool.srv.br
Prompt: What are the key features of a school meal program that ensures quality and safety, as outlined by It's Cool Foods? Provide examples of how to integrate these features into an API.
Generated: DETERMINISTIC_ac380781af4baf5a
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid

app = FastAPI(
    title="School Meal Program API",
    description="API for managing school meal programs with quality and safety features",
    version="1.0.0"
)

# Data Models
class NutritionalInfo(BaseModel):
    calories: int = Field(..., gt=0, description="Calories per serving")
    protein_g: float = Field(..., gt=0, description="Protein in grams")
    carbs_g: float = Field(..., gt=0, description="Carbohydrates in grams")
    fat_g: float = Field(..., gt=0, description="Fat in grams")
    vitamins: List[str] = Field(..., description="List of vitamins present")

class MealItem(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Unique identifier")
    name: str = Field(..., min_length=1, description="Name of the meal item")
    description: str = Field(..., min_length=1, description="Description of the meal item")
    allergens: List[str] = Field(default=[], description="List of allergens present")
    nutritional_info: NutritionalInfo
    preparation_date: datetime = Field(..., description="When the item was prepared")
    expiry_date: datetime = Field(..., description="When the item expires")
    temperature_control: bool = Field(..., description="Whether temperature control is required")

class MealProgram(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Unique identifier")
    name: str = Field(..., min_length=1, description="Name of the meal program")
    description: str = Field(..., min_length=1, description="Description of the program")
    meals: List[MealItem] = Field(default=[], description="List of meal items")
    safety_certifications: List[str] = Field(default=[], description="List of safety certifications")
    last_inspection_date: Optional[datetime] = Field(None, description="Date of last inspection")
    is_active: bool = Field(default=True, description="Whether the program is currently active")

# In-memory database
db = {
    "programs": [],
    "meals": []
}

# Helper functions
def find_program(program_id: str) -> Optional[MealProgram]:
    for program in db["programs"]:
        if program.id == program_id:
            return program
    return None

def find_meal(meal_id: str) -> Optional[MealItem]:
    for meal in db["meals"]:
        if meal.id == meal_id:
            return meal
    return None

# API Endpoints
@app.post("/programs/", response_model=MealProgram, status_code=status.HTTP_201_CREATED)
def create_program(program: MealProgram):
    """Create a new meal program with quality and safety features"""
    db["programs"].append(program)
    return program

@app.get("/programs/", response_model=List[MealProgram])
def list_programs():
    """List all meal programs"""
    return db["programs"]

@app.get("/programs/{program_id}", response_model=MealProgram)
def get_program(program_id: str):
    """Get details of a specific meal program"""
    program = find_program(program_id)
    if not program:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Program not found"
        )
    return program

@app.post("/meals/", response_model=MealItem, status_code=status.HTTP_201_CREATED)
def create_meal(meal: MealItem):
    """Add a new meal item with nutritional and safety information"""
    if meal.expiry_date < datetime.now():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Expiry date must be in the future"
        )
    db["meals"].append(meal)
    return meal

@app.get("/meals/", response_model=List[MealItem])
def list_meals():
    """List all meal items"""
    return db["meals"]

@app.get("/meals/{meal_id}", response_model=MealItem)
def get_meal(meal_id: str):
    """Get details of a specific meal item"""
    meal = find_meal(meal_id)
    if not meal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Meal not found"
        )
    return meal

@app.get("/safety/expired-meals", response_model=List[MealItem])
def get_expired_meals():
    """Get list of expired meals for safety checks"""
    expired = [meal for meal in db["meals"] if meal.expiry_date < datetime.now()]
    return expired

@app.get("/nutrition/{program_id}", response_model=List[NutritionalInfo])
def get_program_nutrition(program_id: str):
    """Get nutritional information for all meals in a program"""
    program = find_program(program_id)
    if not program:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Program not found"
        )
    return [meal.nutritional_info for meal in program.meals]

@app.put("/programs/{program_id}/inspect", response_model=MealProgram)
def update_inspection(program_id: str):
    """Update inspection date for a program (mark as recently inspected)"""
    program = find_program(program_id)
    if not program:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Program not found"
        )
    program.last_inspection_date = datetime.now()
    return program
```
