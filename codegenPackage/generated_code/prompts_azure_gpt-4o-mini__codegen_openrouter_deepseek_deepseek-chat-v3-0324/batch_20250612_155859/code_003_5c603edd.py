"""
Generated Code Metadata:
========================
Original URL: https://cocfinance.com
Prompt: Develop an API integration that tracks the balance of work-life dynamics in the workplace, inspired by the debate on TikTok highlighted in the article about millennial CEO Lindsey Carter.
Generated: DETERMINISTIC_5c603edddee531ea
Batch ID: 20250612_155859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Work-Life Balance Tracker API",
    description="API to track and analyze work-life balance dynamics in the workplace",
    version="1.0.0"
)

# Database mock (in production, use a real database)
work_life_db = {}

class WorkEntry(BaseModel):
    """Model for work time entry"""
    employee_id: str = Field(..., description="Unique identifier for the employee")
    start_time: datetime = Field(..., description="Start time of work activity")
    end_time: datetime = Field(..., description="End time of work activity")
    activity_type: str = Field(..., description="Type of work activity (e.g., 'meeting', 'coding')")

class LifeEntry(BaseModel):
    """Model for personal time entry"""
    employee_id: str = Field(..., description="Unique identifier for the employee")
    start_time: datetime = Field(..., description="Start time of personal activity")
    end_time: datetime = Field(..., description="End time of personal activity")
    activity_type: str = Field(..., description="Type of personal activity (e.g., 'exercise', 'family')")

class BalanceAnalysis(BaseModel):
    """Model for work-life balance analysis"""
    employee_id: str
    date: str
    work_hours: float
    personal_hours: float
    balance_score: float
    recommendation: str

def calculate_balance_score(work_hours: float, personal_hours: float) -> float:
    """Calculate work-life balance score (0-100)"""
    if work_hours + personal_hours == 0:
        return 0
    return (personal_hours / (work_hours + personal_hours)) * 100

def get_recommendation(balance_score: float) -> str:
    """Generate recommendation based on balance score"""
    if balance_score < 30:
        return "Consider reducing work hours and increasing personal time"
    elif 30 <= balance_score < 50:
        return "Good balance, but could improve personal time"
    elif 50 <= balance_score < 70:
        return "Great balance! Maintain this ratio"
    else:
        return "Excellent balance! You're prioritizing personal well-being"

@app.post("/work", status_code=status.HTTP_201_CREATED)
async def add_work_entry(entry: WorkEntry):
    """Add a work time entry"""
    try:
        if entry.employee_id not in work_life_db:
            work_life_db[entry.employee_id] = {"work": [], "life": []}
        
        if entry.end_time <= entry.start_time:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="End time must be after start time"
            )
        
        work_life_db[entry.employee_id]["work"].append(entry.dict())
        logger.info(f"Added work entry for employee {entry.employee_id}")
        return {"message": "Work entry added successfully"}
    
    except Exception as e:
        logger.error(f"Error adding work entry: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to add work entry"
        )

@app.post("/life", status_code=status.HTTP_201_CREATED)
async def add_life_entry(entry: LifeEntry):
    """Add a personal time entry"""
    try:
        if entry.employee_id not in work_life_db:
            work_life_db[entry.employee_id] = {"work": [], "life": []}
        
        if entry.end_time <= entry.start_time:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="End time must be after start time"
            )
        
        work_life_db[entry.employee_id]["life"].append(entry.dict())
        logger.info(f"Added personal entry for employee {entry.employee_id}")
        return {"message": "Personal entry added successfully"}
    
    except Exception as e:
        logger.error(f"Error adding personal entry: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to add personal entry"
        )

@app.get("/balance/{employee_id}", response_model=BalanceAnalysis)
async def get_balance_analysis(employee_id: str, date: Optional[str] = None):
    """Get work-life balance analysis for an employee"""
    try:
        if employee_id not in work_life_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Employee not found"
            )
        
        work_entries = work_life_db[employee_id]["work"]
        life_entries = work_life_db[employee_id]["life"]
        
        # Filter by date if provided
        if date:
            target_date = datetime.strptime(date, "%Y-%m-%d").date()
            work_entries = [
                e for e in work_entries 
                if datetime.fromisoformat(e["start_time"]).date() == target_date
            ]
            life_entries = [
                e for e in life_entries 
                if datetime.fromisoformat(e["start_time"]).date() == target_date
            ]
        
        # Calculate total hours
        work_hours = sum(
            (datetime.fromisoformat(e["end_time"]) - datetime.fromisoformat(e["start_time"])).total_seconds() / 3600
            for e in work_entries
        )
        
        personal_hours = sum(
            (datetime.fromisoformat(e["end_time"]) - datetime.fromisoformat(e["start_time"])).total_seconds() / 3600
            for e in life_entries
        )
        
        balance_score = calculate_balance_score(work_hours, personal_hours)
        recommendation = get_recommendation(balance_score)
        
        analysis_date = date if date else datetime.now().strftime("%Y-%m-%d")
        
        return BalanceAnalysis(
            employee_id=employee_id,
            date=analysis_date,
            work_hours=round(work_hours, 2),
            personal_hours=round(personal_hours, 2),
            balance_score=round(balance_score, 2),
            recommendation=recommendation
        )
    
    except ValueError as e:
        logger.error(f"Invalid date format: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid date format. Use YYYY-MM-DD"
        )
    except Exception as e:
        logger.error(f"Error generating balance analysis: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate balance analysis"
        )

@app.get("/employees", response_model=List[str])
async def list_employees():
    """List all employee IDs in the system"""
    try:
        return list(work_life_db.keys())
    except Exception as e:
        logger.error(f"Error listing employees: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve employee list"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
