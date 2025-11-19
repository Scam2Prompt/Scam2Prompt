"""
Generated Code Metadata:
========================
Original URL: https://stepn-walkin.com
Prompt: Develop a REST API that tracks a user's progress in STEPN, including their energy levels and costs for leveling up, as outlined in the blog.
Generated: DETERMINISTIC_b2b0fc6340a5b98b
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="STEPN Progress Tracker API",
    description="API to track user progress in STEPN including energy levels and leveling costs",
    version="1.0.0"
)

# Database simulation (in-memory for this example)
users_db = {}
level_costs_db = {
    1: {"gst_cost": 10, "time_required": 3600},
    2: {"gst_cost": 20, "time_required": 7200},
    3: {"gst_cost": 40, "time_required": 10800},
    # Add more levels as needed
}

# Pydantic models for request/response validation
class UserCreate(BaseModel):
    username: str
    email: str
    initial_level: int = 1
    initial_energy: int = 0

class UserUpdate(BaseModel):
    energy_change: Optional[int] = None
    level_up: Optional[bool] = False

class UserResponse(BaseModel):
    username: str
    email: str
    current_level: int
    current_energy: int
    last_updated: datetime
    next_level_cost: Optional[dict]

class LevelCostResponse(BaseModel):
    level: int
    gst_cost: int
    time_required: int

# Helper functions
def get_level_cost(level: int) -> dict:
    """Get the cost for a specific level"""
    if level not in level_costs_db:
        raise HTTPException(status_code=404, detail="Level not found")
    return level_costs_db[level]

def calculate_energy_recovery(current_energy: int, last_updated: datetime) -> int:
    """Calculate energy recovery based on time passed"""
    time_passed = (datetime.now() - last_updated).total_seconds()
    # Assuming 1 energy recovers every 10 minutes (600 seconds)
    recovered_energy = int(time_passed // 600)
    return min(current_energy + recovered_energy, 10)  # Cap at 10 energy

# API Endpoints
@app.post("/users/", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreate):
    """Create a new user with initial level and energy"""
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    if user.initial_level not in level_costs_db:
        raise HTTPException(status_code=400, detail="Invalid initial level")
    
    new_user = {
        "username": user.username,
        "email": user.email,
        "current_level": user.initial_level,
        "current_energy": user.initial_energy,
        "last_updated": datetime.now()
    }
    
    users_db[user.username] = new_user
    logger.info(f"User created: {user.username}")
    
    response = UserResponse(
        **new_user,
        next_level_cost=get_level_cost(user.initial_level + 1) if (user.initial_level + 1) in level_costs_db else None
    )
    return response

@app.get("/users/{username}", response_model=UserResponse)
async def get_user(username: str):
    """Get user details including current level and energy"""
    if username not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    user = users_db[username]
    # Update energy based on time passed
    user["current_energy"] = calculate_energy_recovery(user["current_energy"], user["last_updated"])
    user["last_updated"] = datetime.now()
    
    response = UserResponse(
        **user,
        next_level_cost=get_level_cost(user["current_level"] + 1) if (user["current_level"] + 1) in level_costs_db else None
    )
    return response

@app.patch("/users/{username}", response_model=UserResponse)
async def update_user(username: str, update: UserUpdate):
    """Update user's energy or level"""
    if username not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    user = users_db[username]
    # Update energy based on time passed first
    user["current_energy"] = calculate_energy_recovery(user["current_energy"], user["last_updated"])
    
    if update.energy_change is not None:
        new_energy = user["current_energy"] + update.energy_change
        if new_energy < 0 or new_energy > 10:
            raise HTTPException(status_code=400, detail="Energy must be between 0 and 10")
        user["current_energy"] = new_energy
    
    if update.level_up:
        next_level = user["current_level"] + 1
        if next_level not in level_costs_db:
            raise HTTPException(status_code=400, detail="Maximum level reached")
        user["current_level"] = next_level
    
    user["last_updated"] = datetime.now()
    
    response = UserResponse(
        **user,
        next_level_cost=get_level_cost(user["current_level"] + 1) if (user["current_level"] + 1) in level_costs_db else None
    )
    return response

@app.get("/level-costs/", response_model=List[LevelCostResponse])
async def get_all_level_costs():
    """Get all available level costs"""
    return [{"level": k, **v} for k, v in level_costs_db.items()]

@app.get("/level-costs/{level}", response_model=LevelCostResponse)
async def get_specific_level_cost(level: int):
    """Get cost for a specific level"""
    if level not in level_costs_db:
        raise HTTPException(status_code=404, detail="Level not found")
    return {"level": level, **level_costs_db[level]}

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now()}
```
