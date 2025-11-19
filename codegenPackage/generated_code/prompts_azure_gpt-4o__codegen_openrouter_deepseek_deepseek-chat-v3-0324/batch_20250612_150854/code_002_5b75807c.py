"""
Generated Code Metadata:
========================
Original URL: https://immediate-xzen.com
Prompt: Generate code to create a system that matches users with investment education firms based on their submitted information, following the Immediate ZenX workflow.
Generated: DETERMINISTIC_5b75807c46049eee
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from enum import Enum
import logging
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, validator, ValidationError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class InvestmentExperience(str, Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"

class InvestmentGoal(str, Enum):
    RETIREMENT = "retirement"
    WEALTH_BUILDING = "wealth_building"
    EDUCATION = "education"
    OTHER = "other"

class UserProfile(BaseModel):
    name: str
    email: str
    age: int
    income: float
    investment_experience: InvestmentExperience
    investment_goals: List[InvestmentGoal]
    risk_tolerance: int  # Scale of 1-10
    preferred_contact_method: str

    @validator('age')
    def age_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Age must be positive')
        return v

    @validator('risk_tolerance')
    def risk_tolerance_within_range(cls, v):
        if v < 1 or v > 10:
            raise ValueError('Risk tolerance must be between 1 and 10')
        return v

@dataclass
class EducationFirm:
    id: str
    name: str
    description: str
    min_age: int
    min_income: float
    target_experience: List[InvestmentExperience]
    target_goals: List[InvestmentGoal]
    risk_tolerance_range: tuple  # (min, max)
    contact_methods: List[str]
    match_score: float = 0.0

class MatchingEngine:
    def __init__(self, firms_data: List[Dict]):
        self.firms = [EducationFirm(**firm) for firm in firms_data]
    
    def calculate_match_score(self, user: UserProfile, firm: EducationFirm) -> float:
        score = 0.0
        
        # Age match
        if user.age >= firm.min_age:
            score += 0.2
        
        # Income match
        if user.income >= firm.min_income:
            score += 0.2
        
        # Experience match
        if user.investment_experience in firm.target_experience:
            score += 0.15
        
        # Goals match
        common_goals = set(user.investment_goals) & set(firm.target_goals)
        score += 0.15 * (len(common_goals) / len(user.investment_goals))
        
        # Risk tolerance match
        if firm.risk_tolerance_range[0] <= user.risk_tolerance <= firm.risk_tolerance_range[1]:
            score += 0.2
        
        # Contact method match
        if user.preferred_contact_method in firm.contact_methods:
            score += 0.1
        
        return round(score, 2)
    
    def find_best_matches(self, user: UserProfile, top_n: int = 3) -> List[EducationFirm]:
        for firm in self.firms:
            firm.match_score = self.calculate_match_score(user, firm)
        
        # Filter firms with at least 0.5 match score
        eligible_firms = [f for f in self.firms if f.match_score >= 0.5]
        
        # Sort by match score descending
        eligible_firms.sort(key=lambda x: x.match_score, reverse=True)
        
        return eligible_firms[:top_n]

# Load firms data from JSON file
def load_firms_data(file_path: str) -> List[Dict]:
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logger.error(f"Firms data file not found: {file_path}")
        raise
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in firms data file: {file_path}")
        raise

# Initialize FastAPI app
app = FastAPI(
    title="Investment Education Firm Matching System",
    description="Matches users with investment education firms based on their profile",
    version="1.0.0"
)

# Load firms data at startup
@app.on_event("startup")
async def startup_event():
    try:
        firms_data = load_firms_data("firms_data.json")
        app.state.matching_engine = MatchingEngine(firms_data)
        logger.info("Successfully loaded firms data and initialized matching engine")
    except Exception as e:
        logger.critical(f"Failed to initialize matching engine: {str(e)}")
        raise

# Exception handlers
@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": exc.errors()},
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {str(exc)}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "An internal server error occurred"},
    )

# API endpoints
@app.post("/match", response_model=List[Dict], status_code=status.HTTP_200_OK)
async def match_user_with_firms(user_profile: UserProfile):
    """
    Match a user with investment education firms based on their profile.
    Returns top 3 matching firms with their match scores.
    """
    try:
        matching_engine = app.state.matching_engine
        matches = matching_engine.find_best_matches(user_profile)
        
        # Convert matches to dictionaries including match_score
        result = []
        for match in matches:
            match_dict = asdict(match)
            match_dict["match_score"] = match.match_score
            result.append(match_dict)
        
        return result
    except Exception as e:
        logger.error(f"Error during matching: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error processing your request"
        )

@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

# Sample firms data (would normally be in a separate JSON file)
sample_firms_data = [
    {
        "id": "firm1",
        "name": "Wealth Builders Academy",
        "description": "Specializes in retirement and wealth building strategies",
        "min_age": 25,
        "min_income": 50000,
        "target_experience": ["beginner", "intermediate"],
        "target_goals": ["retirement", "wealth_building"],
        "risk_tolerance_range": [3, 7],
        "contact_methods": ["email", "phone"]
    },
    {
        "id": "firm2",
        "name": "Advanced Investment Strategies",
        "description": "For experienced investors looking to maximize returns",
        "min_age": 30,
        "min_income": 100000,
        "target_experience": ["intermediate", "advanced"],
        "target_goals": ["wealth_building", "education"],
        "risk_tolerance_range": [6, 10],
        "contact_methods": ["phone", "video_call"]
    },
    {
        "id": "firm3",
        "name": "Financial Foundations",
        "description": "Beginner-friendly investment education",
        "min_age": 18,
        "min_income": 30000,
        "target_experience": ["beginner"],
        "target_goals": ["retirement", "education", "other"],
        "risk_tolerance_range": [1, 5],
        "contact_methods": ["email", "chat"]
    }
]

# For testing purposes - save sample data to JSON file
if __name__ == "__main__":
    import os
    if not os.path.exists("firms_data.json"):
        with open("firms_data.json", "w") as f:
            json.dump(sample_firms_data, f, indent=2)
    
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
