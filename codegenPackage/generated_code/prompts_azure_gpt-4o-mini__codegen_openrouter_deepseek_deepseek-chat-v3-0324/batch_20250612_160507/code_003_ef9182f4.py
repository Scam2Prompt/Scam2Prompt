"""
Generated Code Metadata:
========================
Original URL: https://skutersite.pl
Prompt: Develop an API recommendation for a system that protects car paint with ceramic coatings, inspired by the article's discussion on spring maintenance tips.
Generated: DETERMINISTIC_ef9182f424741ae1
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from enum import Enum

app = FastAPI(
    title="Ceramic Coating Protection API",
    description="API for recommending ceramic coating protection for car paint",
    version="1.0.0"
)

class CarType(str, Enum):
    SEDAN = "sedan"
    SUV = "suv"
    TRUCK = "truck"
    SPORTS = "sports"
    LUXURY = "luxury"

class CoatingType(str, Enum):
    BASIC = "basic"
    STANDARD = "standard"
    PREMIUM = "premium"
    PROFESSIONAL = "professional"

class EnvironmentFactor(str, Enum):
    MILD = "mild"
    MODERATE = "moderate"
    HARSH = "harsh"
    EXTREME = "extreme"

class RecommendationRequest(BaseModel):
    car_type: CarType
    environment: EnvironmentFactor
    budget: float
    desired_durability_months: Optional[int] = 24

class RecommendationResponse(BaseModel):
    recommended_coating: CoatingType
    estimated_cost: float
    expected_durability_months: int
    maintenance_tips: list[str]

COATING_DATA = {
    CoatingType.BASIC: {
        "cost": 500.00,
        "durability": 12,
        "suitable_for": [CarType.SEDAN, CarType.SUV],
        "environment": [EnvironmentFactor.MILD]
    },
    CoatingType.STANDARD: {
        "cost": 800.00,
        "durability": 24,
        "suitable_for": [CarType.SEDAN, CarType.SUV, CarType.TRUCK],
        "environment": [EnvironmentFactor.MILD, EnvironmentFactor.MODERATE]
    },
    CoatingType.PREMIUM: {
        "cost": 1200.00,
        "durability": 36,
        "suitable_for": [CarType.SEDAN, CarType.SUV, CarType.TRUCK, CarType.SPORTS],
        "environment": [EnvironmentFactor.MODERATE, EnvironmentFactor.HARSH]
    },
    CoatingType.PROFESSIONAL: {
        "cost": 2000.00,
        "durability": 48,
        "suitable_for": [CarType.SEDAN, CarType.SUV, CarType.TRUCK, CarType.SPORTS, CarType.LUXURY],
        "environment": [EnvironmentFactor.HARSH, EnvironmentFactor.EXTREME]
    }
}

MAINTENANCE_TIPS = [
    "Wash your car regularly with pH-neutral shampoo",
    "Avoid automatic car washes with brushes",
    "Apply ceramic coating booster every 6 months",
    "Remove bird droppings and tree sap immediately",
    "Park in shaded areas when possible",
    "Use microfiber towels for drying and cleaning"
]

@app.post("/recommend-coating", response_model=RecommendationResponse)
async def recommend_coating(request: RecommendationRequest):
    """
    Recommends the best ceramic coating based on car type, environment, and budget.
    """
    suitable_coatings = []
    
    for coating_type, data in COATING_DATA.items():
        if (request.car_type in data["suitable_for"] and 
            request.environment in data["environment"] and 
            data["cost"] <= request.budget and 
            data["durability"] >= request.desired_durability_months):
            suitable_coatings.append((coating_type, data))
    
    if not suitable_coatings:
        raise HTTPException(
            status_code=404,
            detail="No suitable coating found for the given parameters"
        )
    
    # Select the coating with highest durability that fits the budget
    best_coating = max(suitable_coatings, key=lambda x: x[1]["durability"])
    
    return RecommendationResponse(
        recommended_coating=best_coating[0],
        estimated_cost=best_coating[1]["cost"],
        expected_durability_months=best_coating[1]["durability"],
        maintenance_tips=MAINTENANCE_TIPS
    )

@app.get("/coating-types", response_model=list[CoatingType])
async def get_coating_types():
    """
    Returns all available ceramic coating types.
    """
    return list(CoatingType)

@app.get("/maintenance-tips", response_model=list[str])
async def get_maintenance_tips():
    """
    Returns general maintenance tips for ceramic coated vehicles.
    """
    return MAINTENANCE_TIPS
```
